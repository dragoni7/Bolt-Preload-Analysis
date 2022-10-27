% Example of importing csv data into matlab
% Add the data folder into the path
addpath(".\data");
T = readtable('dummy.csv');
T % display the csv file