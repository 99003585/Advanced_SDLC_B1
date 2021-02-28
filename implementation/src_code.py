import os
import csv
import pandas as pd
from functools import reduce

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
filePath = os.path.join(desktop, "ScriptTestFolder", "InputFolder")
outfilePath = os.path.join(desktop, "ScriptTestFolder")

dfList = []
for file in os.listdir(filePath):
    #print(file)
    filepath = os.path.join(desktop, filePath, file)
    new_df = pd.read_csv(filepath, header=0)
    dfList.append(new_df)
#
mergedDF= df = pd.concat(dfList).reset_index()
#
mergedDF.to_csv(os.path.join(outfilePath, "Output.csv"))

print(mergedDF.Name.nunique())


#THIS IS A CHANGE... A BORING CHANGE>> BUT A CHANGE
