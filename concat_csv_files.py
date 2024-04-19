import os
import pandas as pd
#read the path
cwd = os.path.abspath('')
#list all the files from the directory
file_list = os.listdir(cwd)
print(file_list)

csv_files = []

for f in file_list:
    if f[-4:] == '.csv':
        csv_files.append(f)

print(csv_files)

df_concat = pd.concat([pd.read_csv(f) for f in csv_files ], ignore_index=True)
print(df_concat)