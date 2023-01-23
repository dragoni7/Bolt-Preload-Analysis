% This is where we will import our data.
% If necessary, this is also where the data will be preprocessed if it's not in the format/units we need

% Add the data folder into the path
addpath(".\data");

% Example:
T = readtable('dummy.csv');
tdata = table2array(T(1,:));
force = table2array(T(2,:));
% From here, tdata and force will be passed to the data analysis script.

disp(tdata) % display the first row, time
disp(force) % display the second row, force

% From Python:
data = py.importlib.import_module('data_import_python'); % If preprocessing is needed, data can be imported from python
py.importlib.reload(data);
x = py.numpy.array(py.data_import_python.x);
double(x)
plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14], double(x))