clear;
clc;
tdata = [1 2 3 4 5 6 7 8 9 10 11 12 13, 14]; % xData, time
force = [500 500 500 495 494 490 482 471 458 441 423 402 377 344]; % yData, force
c2_guess = 50; % guess the coefficient
c2 = lsqcurvefit(@(c2,t)FittingFunction(c2,t), c2_guess, tdata(:), force(:)); % curve fit the coefficient

figure %plot the data as well as the fitted function
hold 'on'
plot(tdata, force, 'ko', 'DisplayName','data')
plot_times = linspace(0,max(tdata),14) ;
plot(plot_times, FittingFunction(c2,plot_times),'-r','DisplayName','fit');
xlabel('time'), ylabel('Force')

% create the ODE solution by using RK4 
function F = FittingFunction(c2, tdata)
tspan = [0 14];
InitConds = [0 0] ; % assume initial displacement and velocity are 0
[t_atTdata,y_atTdata] = ode45(@(t,y)ODEsystem(t,y,c2),tspan,InitConds);
f = y_atTdata(:,1); % return y only, not y and y'
F = f(1:14); % the length of this vector is longer than ydata, so trim it. Unknown if this is detrimental, therefore temp fix.
end

function Y = ODEsystem(t,y,c2)

% assume that c1 (damping coefficeint) is 0 - all terms affect stiffness
% x''+c1*x'+c2*x=F  => x'' + 0*x' + c2*x = F => F = x'' + c2*x
% for homogenous solution: x'' + c2*x = 0 => x'' = -c2*x
% let x1' = x2 =>
% equation 1: x1' = x2
% equation 2: x2' = -c2*x1
% X(1) = X(2)
% X(2) = -c2*X(1)
Y(1) = y(2);
Y(2) = -c2*y(1);
Y = [Y(1); Y(2)];
end