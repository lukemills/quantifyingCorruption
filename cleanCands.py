import pandas as pd
import os

names = ["year", "seat", "CID", "name", "party","district", "unknown",  "unknown1", "unknown2","unknown3","unknown4", "unknown5"]
    
for fileName in os.listdir(os.path.dirname(os.path.abspath(__file__))):
    if fileName.endswith(".txt"):
        print(fileName)

        #read the CSV, the delimiter in the file is |,|
        df = pd.read_csv(fileName, sep = '\|,\|', engine='python', names = names)
        
        #remove extra pipes
        df = df.replace({'\|':''}, regex=True)

    #drop unknown columns
        df = df.drop(["seat", "district","unknown", "unknown1","unknown2", "unknown3", "unknown4","unknown5"], axis=1)


        #Save cleaned data frame as a .csv
        newName=fileName.replace(".txt",".csv")
        df.to_csv(newName, sep=';', index=False)
