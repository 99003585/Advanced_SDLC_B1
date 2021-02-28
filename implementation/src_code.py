import os
import csv
import pandas as pd
from functools import reduce

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
filePath = os.path.join(desktop, "ScriptTestFolder", "InputFolder")
outfilePath = os.path.join(desktop, "ScriptTestFolder")

dfList = []

# Create a dataframe from csv
df = pd.read_csv('InputFolder/Module1.csv',)
# User list comprehension to create a list of lists from Dataframe rows
list_of_rows = [list(row) for row in df.values]
# print(df)
f = open("results/studentMarks.csv", "w")
f.write("studentID,studentNAME,studentEMAIL,Module1,Module2,Module3,Average\n")
for i in list_of_rows:
  # print(i)
  for j in i:
    # print(j)
    f.write(str(j).strip()+",")

  mod1= pd.read_csv('InputFolder/Module1.csv'', delimiter=',')  
  if i[0] in subPhy.values:
    temp_rows= [list(row) for row in mod1.values]
    for row in temp_rows:
      if i[0] in row:
        t=temp_rows.index(row)
        break
    f.write(str(mod1.values[t][3])+",")
  else: 
    f.write("NA,")

  subChe = pd.read_csv('dataset/Mod.csv', delimiter=',')  
  if i[0] in subChe.values:
    temp_rows= [list(row) for row in subChe.values]
    for row in temp_rows:
      if i[0] in row:
        t=temp_rows.index(row)
        break
    f.write(str(subChe.values[t][3])+",")
  else:
    f.write("NA,")

  subBio = pd.read_csv('dataset/Biology.csv', delimiter=',')  
  if i[0] in subBio.values:
    temp_rows= [list(row) for row in subBio.values]
    for row in temp_rows:
      if i[0] in row:
        t=temp_rows.index(row)
        break
    f.write(str(subBio.values[t][3])+",")
  else:
    f.write("NA,")
  
  subMat = pd.read_csv('dataset/Maths.csv', delimiter=',')  
  if i[0] in subMat.values:
    temp_rows= [list(row) for row in subMat.values]
    for row in temp_rows:
      if i[0] in row:
        t=temp_rows.index(row)
        break
    f.write(str(subMat.values[t][3])+",")
  else:
    f.write("NA,")


  subPy = pd.read_csv('dataset/Python.csv', delimiter=',')  
  if i[0] in subPy.values:
    temp_rows= [list(row) for row in subPy.values]
    for row in temp_rows:
      if i[0] in row:
        t=temp_rows.index(row)
        break
    f.write(str(subPy.values[t][3])+",")
  else:
    f.write("NA,")
    
  f.write("\n")
f.close()


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
