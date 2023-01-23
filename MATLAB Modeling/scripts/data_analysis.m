clear;
clc;

 

I = 0; %initial
S = 270; %step
N = 12; %number of values
Time_data = I+S*(0:N-1); % independent variable, # seconds
force = [ 100 ; 97.8 ; 97 ; 96.7 ; 96.6 ; 96.55 ; 96.50 ; 96.45 ; 96.40; 96.35; 96.30; 96.25] ; % dependent variable, experimental data
c_guess = [1; 100] ; %init guess for c1 and c2, the parameters to be fitted
c = lsqcurvefit(@(c,t)FittingFunction(c,t),c_guess,Time_data,force)

 


figure %plot the data as well as the fitted function
hold 'on'
plot(Time_data, force, 'ko', 'DisplayName','data')
plot_times = linspace(0,max(Time_data),100) ;
plot(plot_times, FittingFunction(c,plot_times),'-r','DisplayName','fit') ;
xlabel('time(sec)'), ylabel('Force(N)'), legend('Location','South');

 

function F = FittingFunction(c,Time_data)
tspan = Time_data ;
InitConds = [1;1]; % initially, no displacement or velocity
[~,y_atTdata] = ode45(@(t,y)SysOfDiffEqns(t,y,c),tspan,InitConds) ;
%F = y_atTdata(:,1) ; %return y only, not y and y'
displacement = y_atTdata(:,1) ;
velocity = y_atTdata(:,2);
%F=ma=-bv-ky
F = -c(2).*displacement-c(1).*velocity;
end

 

function Y = SysOfDiffEqns(~,y,c)
%sum of forces F=ma=-bv-ky, F=0 for fixed object
%divide by m, c1 = b/m and c2 = k/m
%y''+c1*y'+c2*y = 0
%y''=-c1*y'-c2*y
%y1 = y = displacement
%y2 = y'= velocity

 

% SUBSTITUTE: 
%Y(1) = y' = y2
%Y(2) = y2'= y''

Y = zeros(2,1);
Y(1) = y(2);
Y(2) = -c(1)*y(2)-c(2)*y(1);

end