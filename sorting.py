import pandas as pd
import argparse as ap
from pathlib import Path

##Read file as mandatory argument, error if not given.
##Read output as optional with -o flag, "output.csv" is default
##Can get description of input by calling with -h
parser=ap.ArgumentParser()
parser.add_argument('file',help="CSV file of stilde values")
parser.add_argument('-o','--output',help='Sorted stilde output file, with extension',
                    default="output.csv")
args=parser.parse_args()

filename = args.file
output = args.output

##No issues (at least for me) when using the command prompt
print("WARNING: Admin rights may be required to write files at the end of this program")
print("If saving the file fails, try running the program as admin")

try:
    dataframe = pd.read_csv(filename)
except FileNotFoundError as err:
    print("Exception: {0}".format(err))
    exit()
print('\n')


###### Printing of dataframes for testing ######
#print("Sorted data by S-tilde\n")
#print(dataframe)
#print('\n')
#print("Sorted data by absolute value of S-tilde")
#print(dataframe)
#print('\n')
#################


dataframe['S'] = dataframe['S'].apply(abs)
dataframe.sort_values(by='S', axis=0, inplace=True, ascending = False)

newData = dataframe[list(dataframe.columns)].copy()

newData = newData[:30]
print("Top 30 s-tilde values")
print(newData)


##Path will automatically enter address compatible with Linux/Mac/Windows
outdir = Path('./SortedData')
if not Path.exists(outdir):
    Path.mkdir(outdir)
##Can extend Path objects with /
fullname = outdir / output


try:
    ##Removed row label
    newData.to_csv(fullname,index=False)
    print("New file saved successfully")
except OSError as err:
    print("Directory error: {0}".format(err))

#add magnitudes of vectors and cosine of angle
#add an option for number of s-tilde values
#include sign on absolute value of s-tilde
#visual representation of s-tilde
#print a relative number of s-tilde based on percent error/total sum of all values
