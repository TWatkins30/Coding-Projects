function maxima = golden_search(tol, xl, xu)
    tol = 10^-3; xl = -1; xu = 1;
    g = @(c) (2*c) / (4 + 0.8*c + c^2 + 0.2^c^3);
    error = zeros(xu, 1); iteration = 1;
    while abs(xu - xl) > tol
       ratio = (1/3)* (xu-xl);
       x2 = xl + ratio; x1 = xu - ratio;
       if g(x2) > g(x1)
          xu = x1; 
       else
           xl = x2;
       end
       true_minimum = fzero(g, x2);
       x2_old = x2;
       err = (true_minimum- g(x2));
       error(iteration) = err; iteration = iteration + 1;
    end
    maxima = g(xl);
    disp(xl)
    semilogx(error)
end