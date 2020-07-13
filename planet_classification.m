
net = planet_classifications(); %I called my neural network function that 
                                % I created below, to be able to use my
                                % neural netork on other examples. 

video = VideoReader('Planets.mp4'); % I am importing a video that 
                                    %demonnstrates the use of the neural
                                    %network. What I am doing with this
                                    %video is taking each frame from the
                                    %video, and resizing the frames to fit
                                    %the network's size and I am running
                                    %each frame in a for loop until it
                                    %reaches the end, which is basically
                                    %running all of the frames and
                                    %sppeeding it up, so it runs like a
                                    %video, but classifying each pixel of
                                    %the image data giving it the correct
                                    %planet classification. 

                                    %Starting the frame at 1100th frame in
                                    %the video.
for img = 1200:video.NumberOfFrames;
    video_frame = read(video, img);
    video_frame = imresize(video_frame, [227 227]);            

    %Now that we have the options created, we now to need to started training
    %our data for the neural network to work properly.
    [label,scores] = classify(net,video_frame);
   
    label_str = string(label) + ", " + num2str(100*scores(net.Layers(end).ClassNames == label),3) + "%";
    RGB = insertObjectAnnotation(video_frame, 'rectangle', [43 43 100 100], label_str); % this is my annotation
                                                                                        %that classifies the region its trying to classify.
    figure(2)
    imshow(RGB)
end

function tr = planet_classifications()
    layers1 = [
        imageInputLayer([227 227 3]) %1
        convolution2dLayer(11, 96, 'Stride', 4, 'Padding', 0, 'BiasLearnRateFactor', 2, 'WeightL2Factor', 1, 'WeightLearnRateFactor', 1) %2
        batchNormalizationLayer
        reluLayer() %3

        crossChannelNormalizationLayer(5, 'Alpha', 0.0001, 'Beta', 0.750, 'K', 1) %4
        maxPooling2dLayer(3, 'Stride', 2, 'Padding', 0) %5
        groupedConvolution2dLayer(5, 128, 2, 'Padding', 2, 'Stride', 1, 'BiasLearnRateFactor', 2, 'WeightL2Factor', 1, 'WeightLearnRateFactor', 1) %6
        batchNormalizationLayer
        reluLayer() %7

        crossChannelNormalizationLayer(5) %8
        maxPooling2dLayer(3, 'Stride', 2, 'Padding', 0) %9
        convolution2dLayer(3, 384, 'Stride', 1, 'Padding', 1, 'WeightL2Factor', 1, 'WeightLearnRateFactor', 1, 'BiasLearnRateFactor', 2, 'BiasL2Factor', 0) %10
        reluLayer() %11

        groupedConvolution2dLayer(3, 192, 2, 'Padding', 1, 'Stride', 1, 'BiasLearnRateFactor', 2, 'WeightL2Factor', 1, 'WeightLearnRateFactor',1) %12
        batchNormalizationLayer
        reluLayer() %13

        groupedConvolution2dLayer(3, 192, 2, 'Padding', 1, 'Stride', 1, 'BiasLearnRateFactor', 2, 'WeightL2Factor',1, 'WeightLearnRateFactor', 1)
        batchNormalizationLayer
        reluLayer()

        maxPooling2dLayer(3, 'Stride', 2, 'Padding', 0)
        fullyConnectedLayer(4096, 'BiasLearnRateFactor', 2)
        reluLayer()

        dropoutLayer(0.500)
        fullyConnectedLayer(4096, 'BiasLearnRateFactor', 10, 'WeightLearnRateFactor', 10)
        reluLayer()

        dropoutLayer(0.500)
        fullyConnectedLayer(4, 'BiasLearnRateFactor', 1, 'WeightLearnRateFactor', 1, 'WeightL2Factor', 1, 'BiasL2Factor', 1)
        softmaxLayer
        classificationLayer
    ];

    %I am importing the images from the file called 'Symbolic', which is
    %labels the planets accordingly.
    images = imageDatastore('Symbolic', 'IncludeSubFolders', true,... 
    'LabelSource', 'foldernames');
    [image_train, image_valid] = splitEachLabel(images, 0.72, 'randomized'); 

    %splitting the image datastorage into two knew data storages to handle the
    %labels of the images "Terrestrial Planets, Ice Giants, Dwarf Planets, and
    %Gas Giants goes into one and in the other the image validation just grabs
    %every other file that is not placed in the first data storage. I have the
    %number of files going to imds1 or image_Train set at 0.9 of the files and
    %the rest are going to data storage 2.

    %Now we need to resize all the images to give the same as specified in the
    %nueral network.

    image_size = augmentedImageDatastore([227 227], image_train);
    valid_size = augmentedImageDatastore([227 227], image_valid);

    %All of the images are of the same size that are stored inside of each data
    %storage, we can now move to the point of needing to specify the training
    %option of the neural network.
    options = trainingOptions('sgdm',...
    'MiniBatchSize', 10,...
    'MaxEpochs', 3,...
    'InitialLearnRate', 0.0001,...,
    'Shuffle', 'every-epoch',...,
    'ValidationData', valid_size,...,
    'ValidationFrequency', 30,...,
    'Verbose', false,...
    'Plots', 'training-progress');

    %Now that we have the options created, we now to need to started training
    %our data for the neural network to work properly.

    train_network = trainNetwork(image_size, layers1, options);
    tr = train_network;

end