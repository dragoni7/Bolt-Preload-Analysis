clear;
clc;

 

time = [0 2160 4320 6480 8640 10800 12960 15120 17280 19440 21600 23760]; % independent variable, sample # (270 second samples)
force = [100 97.8 97 96.7 96.6 96.55 96.50 96.45 96.40 96.35 96.30 96.25] ; % dependent variable, experimental data

 

mdl = fit(time', force', 'exp2');

 


plot(time,force,'ko');
hold on

 

plot(mdl)

 

legend('Data','Fitted exponential');
title('Data and Fitted Curve');
xlabel('cycles'); % 270 seconds
ylabel('%force');