%Name: Terrell Watkins
%Lab: 5 - Optimization
%How to run program: Alls you need to do is click run and your surf 

steepDescent
%gradf()
hessf()
y= linspace(-1, 1,400); % generates 400 x points between -1 and 1
x= linspace(-1, 1,400); % genrates 400 y points betweem -1 and 1
[X,Y] = meshgrid(x, y);
Funct = @(x,y) (1-x).^2 + 100.*(y-x.^2).^2;
F = Funct(X,Y);
surf(X, Y, F) 
shading interp; % makes the colors more visible and brighter.

function Z = f(x)
    Z = (1 - x(1)).^2 + 100.*(x(2)-x(1).^2).^2;
end

function Z = gradf(x) 
    %syms x y
    %Funct = (1-x).^2 + 100.*(y-x.^2).^2;
    %Z = gradient(Funct, [x, y]);
    
    %gradient of the function
    Z = [2.*x(1) - 400.*x(1).*(- x(1).^2 + x(2)) - 2;
           - 200.*x(1).^2 + 200.*x(2)];
end

function Z = hessf(x)
    syms x y
    Funct = (1-x).^2 + 100.*(y-x.^2).^2;
    %I could not use the hessian function, so I decided to use the Jacobian
    %function over the gradient function which is equivalent to the hessain
    %function.
    Z = jacobian(gradient(Funct, [x, y]));
end

%I used the steepest descent algorithm, I realize this is not the best, 
%Newton's method is probably the best. However, for my own evaluation, I
%wanted to see how many iteration it would take for the function to
%converge using the steepest descent method, which was a huge number like
%9000+ iterations needed for it to converge.
function[xopt, fopt, nopt] = steepDescent(x0, tol)
    x0 = [-1 1]'; %initial guess
    x = x0;
    k = 0;
    tol = 10^-3; %tolerance
    
    while k < 50 %stop after 50 iterations
        g = - gradf(x);
        falpha = @(alpha) f(x + alpha*g);
        alpha = fminsearch(falpha, 0.1); 
        x = x + alpha*g;
        k = k + 1;
    end
    xopt = x; fopt = f(x); nopt = k; disp(nopt);
end