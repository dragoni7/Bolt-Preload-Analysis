classdef Dataset < handle
properties (Access = public)
        setName % name of the dataset
        data % dataset table contents
        coefficients = [] % the solved coefficients for the dataset
        mdl cfit % solution for coefficients of dataset
end
methods       
    function obj = Dataset(file, path)
        if nargin == 2
            obj.data = readtable(fullfile(path, file));
            obj.setName = strrep(file, '_', '');
        end
    end

    % overload dictionary functions to ensure dataset works in dictionaries
    function h = keyHash(obj)
            h = keyHash(obj.setName);
    end

    function TF = keyMatch(objA,objB)
            tf = keyMatch(objA.setName,objB.setName);
    end
end
end