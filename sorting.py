import numpy as np
import pandas as pd
import sys
import os


if(len(sys.argv) < 2):
    print("Incorrect usage: Program takes file name as command line argument, exiting...")
    exit()
filename = sys.argv[1]


print("WARNING: Admin rights may be required to write files at the end of this program")
print("If saving the file fails, try running the program as admin")

try:
    dataframe = pd.read_csv(filename)
except FileNotFoundError as err:
    print("Exception: {0}".format(err))
    exit()
print('\n')


dataframe.insert(3, 'Negative?', np.nan, False)
dataframe = dataframe.astype({'Negative?': str})




for i in range(len(dataframe.index)):
    if(dataframe.at[i, 'S'] < 0):
        dataframe.at[i, 'Negative?'] = 'Yes'
    else:
        dataframe.at[i, 'Negative?'] = 'No'


dataframe['S'] = dataframe['S'].apply(abs)
dataframe.sort_values(by='S', axis=0, inplace=True, ascending = False)
print(dataframe)


values = int(input("Enter the number of S-tilde values you'd like to have in the exported file\n"))

newData = dataframe[list(dataframe.columns)].copy()

newData = newData[:values]
print("Top ", values, " s-tilde values")
print(newData)

file = ""
file = input("Enter a filename for the sorted file to be saved as, including the file type\n")

outdir = './SortedData'
if not os.path.exists(outdir):
    os.mkdir(outdir)
fullname = os.path.join(outdir, file)


try:
    newData.to_csv(fullname)
    print("New file saved successfully")
except OSError as err:
    print("Directory error: {0}".format(err))

#add magnitudes of vectors and cosine of angle
#add an option for number of s-tilde values
#include sign on absolute value of s-tilde
#visual representation of s-tilde
#print a relative number of s-tilde based on percent error/total sum of all values
