% Add the data folder to the path for access
%addpath(".\data");

% Data Example:
% data_import

clear;
clc;
tdata = [1 2 3 4 5 6 7 8 9 10 11 12 13]; % time
force = [500 500 500 495 494 490 482 471 458 441 423 402 377 344]; %force
c2_guess = 50; % guess the coefficient
c2 = lsquarecurvefit(@(c2,t)FittingFunction(c2,t), c2_guess, tdata, force); %curve fit the coefficient

figure %plot the data as well as the fitted function
hold 'on'
plot(tdata, force, 'ko', 'DisplayName','data')
plot_times = linspace(0,max(tdata),100) ;
plot(plot_times, FittingFunction(c2,plot_times),'-r','DisplayName','fit') ;
xlabel('time'), ylabel('Force')

% create the ODE solution by using RK4 
function F = FittingFunction(c2,tdata)
tspan = tdata ;
InitConds = [0 0] ; %assume initial displacement and velocity are 0
[t_atTdata,y_atTdata] = ode45(@(t,y)ODEsystem(t,y,c2),tspan,InitConds) ;
F = y_atTdata(:,1) ; %return y only, not y and y'
end

function Y = ODEsystem(t,y,c2)

% assume that c1 (damping coefficeint) is 0 - all terms affect stiffness
% x''+c1*x'+c2*x=F  => x'' + 0*x' + c2*x = F => F = x'' + c2*x
% for homogenous solution: x'' + c2*x = 0 => x'' = -c2*x
% let x1' = x2 =>
% equation 1: x1' = x2
% equation 2: x2' = -c2*x1

end
