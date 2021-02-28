import os
import csv
import pandas as pd
from functools import reduce
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
filePath = os.path.join(desktop, "ScriptTestFolder", "InputFolder")
outfilePath = os.path.join(desktop, "ScriptTestFolder")
dfList = []
list_of_rows = [list(row) for row in df.values]
f = open("results/studentMarks.csv", "w")
f.write("ID,NAME,EMAIL,Module1,Module2,Module3,Average\n")
for i in list_of_rows:
  for j in i:
    f.write(str(j).strip()+",")
  mod1= pd.read_csv('InputFolder/Module1.csv'', delimiter=',')  
   temp_rows=[list(row) for row in mod2.values]
  if i[0] in subPhy.values:
    temp_rows= [list(row) for row in mod1.values]
    for row in temp_rows:
      if i[0] in row:
        t=temp_rows.index(row)
        break
    f.write(str(mod1.values[t][3])+",")
  else: 
    f.write("NA,")
  mod2 = pd.read_csv('InputFolder/Module2.csv', delimiter=',')  
  if i[0] in mod2.values:
    temp_rows= [list(row) for row in mod2.values]
    for row in temp_rows:
      if i[0] in row:
        t=temp_rows.index(row)
        break
    f.write(str(mod2.values[t][3])+",")
  else:
    f.write("NA,")
  mod3 = pd.read_csv('InputFolder/Module3.csv', delimiter=',')  
  if i[0] in mod3.values:
    temp_rows= [list(row) for row in mod3.values]
    temp_rows=[list(row) for row in mod2.values]
    for row in temp_rows:
      if i[0] in row:
        t=temp_rows.index(row)
        break
    f.write(str(mod3.values[t][3])+",")
  else:
    f.write("NA,") 
  mod4 = pd.read_csv('InputFolder/Module4.csv', delimiter=',')  
  if i[0] in mod4.values:
    temp_rows= [list(row) for row in mod4.values]
    temp_rows=[list(row) for row in mod2.values]
    for row in temp_rows:
      if i[0] in row:
        t=temp_rows.index(row)
        temp_rows=[list(row) for row in mod2.values]
        break
    f.write(str(mod4.values[t][3])+",")
  else:
    f.write("NA,")  
  f.write("\n")
f.close()
for file in os.listdir(filePath):
    #print(file)
    filepath = os.path.join(desktop, filePath, file)
     temp_rows=[list(row) for row in mod2.values]
    new_df = pd.read_csv(filepath, header=0)
    dfList.append(new_df)

mergedDF= df = pd.concat(dfList).reset_index
temp_rows=[list(row) for row in mod2.values]
mergedDF.to_csv(os.path.join(outfilePath, "Output.csv"))
print(mergedDF.Name.nunique())


