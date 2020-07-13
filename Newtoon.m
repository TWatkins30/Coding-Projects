function num = Newtoon(x0)
    syms x 
    f = (x.^2 - 1).*tan(x) - 2.*x;
    fprime = diff(f);
    start = true;
    
    while start 
       xprev = x0;
       x0 = x0 - f(x0) ./ fprime(x0);
       if abs(xprev - x0) < 10^-3
          start = false;
       end
       disp(x0)
    end

end