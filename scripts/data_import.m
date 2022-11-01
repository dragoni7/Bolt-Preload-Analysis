% This is where we will import our data.
% If necessary, this is also where the data will be preprocessed if it's not in the format/units we need

% Add the data folder into the path
addpath(".\data");

% Example:
T = readtable('dummy.csv');
T % display the csv file