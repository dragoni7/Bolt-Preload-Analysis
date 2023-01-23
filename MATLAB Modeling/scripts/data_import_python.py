import matlab
import numpy as np
import pandas as pd

path = str(__file__)
path = path.split("data_import_python.py")
path = path[0].replace('\\', '/')

csv = pd.read_csv(path + "/data/dummy.csv")
x = csv.to_numpy()