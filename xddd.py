import pandas as pd
import numpy as np


descriptors = pd.read_excel(r"C:\Users\marci\Downloads\Descriptors (1).xlsx", dtype = "float")

for label, content in descriptors.items():
    if label == "Unnamed: 0": #usun dodatkowa kolumne
        descriptors.drop(label, axis = 1, inplace = True)

    if "Nan" in content: #usun nan
        print(label, content)
        descriptors.drop(label, axis = 1, inplace = True)

    if content.var() == 0: #usun gdzie wariancja 0
        descriptors.drop(label, axis = 1, inplace = True)
obj = len(label)
df = descriptors

for label, content in df.items():
    if label != "Unnamed: 0":
        sr = np.mean(content)
        std = np.std(content)

        for x in range(len(content)):
            AS = (content[x] - sr)/std
            df.loc[x,label] = float(AS)

print(df)
obj, col = df.shape

dist_df = np.zeros((obj,obj))

# Nested loop to iterate through each element in the array
for i in range(len(df)):
    for j in range(len(df[i])):
        suma = 0
        # Add the square of each element to the sum_of_squares
        suma += df[i][j] ** 2
    dyst_euk = np.sqrt(suma)
