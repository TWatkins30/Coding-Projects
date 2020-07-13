function num = Jacobi()
syms x 
f = (x.^2 - 1).*tan(x) - 2*(x);
fprime = diff(f);

x0 = 1.2;

while x0 > -0.01
    x0 = x0 - f(x0)./fprime(x0);
end
num = x0;
end