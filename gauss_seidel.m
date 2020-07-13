%How this function works: My function is title "gauss_seidel
% ... and this function takes in 4 arguments,
% ... "A" for your matrix, "b" as your solution, 
%... vi as your initial guess and your tolerance number

%However, I created the correct variables 
% for this lab inside of the function, so I you need
% to do is click "Run" and ot will print out the iterations as well as 
%the vector

function num = gauss_seidel(A, b, vi, tolerance)
    A = [-2 1 0 0 0 0;
         1 -2 1 0 0 0;
         0 1 -2 1 0 0;
         0 0 1 -2 1 0;
         0 0 0 1 -2 1;
         0 0 0 0 1 -2;]; %matrix
     
    b = [-2.01; -0.01; -0.01; -0.01; -0.01; -3.01]; %solution
    
    tolerance = 10^-5; vi = [0 0 0 0 0 0]'; iteration = 0; err = 1;
    vi_new = (vi);
    while err >= tolerance
        %need to created a nested for loop to handle the rows and
        %columns of the matrix.
        for i = 1:length(A) 
           sigma = 0;
           for j = 1:length(A)
               if j ~= i
                   sigma = sigma + A(i,j)*vi(j); 
               end
            vi_new(i) = (1 / A(i,i)) *(b(i)-sigma);
           end
        end
        err = (norm(vi_new - vi) / norm(vi_new));
        disp(err)
        vi = (vi_new);
        disp(vi)
        iteration = iteration + 1;
        disp(iteration)
    end
end