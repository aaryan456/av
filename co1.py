import plotly.express as pl
import csv 
import numpy as np
def StoreData(datapath):
    icecreamsales = []
    coldrinksales = []
    with open(datapath) as file:
        csvreader = csv.DictReader(file)
        for i in csvreader:
            icecreamsales.append(float(row["Temperature"]))
            coldrinksales.append(float(row["IcecreamSales"]))
    return {"x":icecreamsales,"y":coldrinksales}    
def findcorelation(storedata):
    correlation = np.corrcoef(storedata["x"],storedata["y"])
    print(correlation[0,1])
def setup():
    datapath = "C:/Users/HOME/Downloads/Ice-Creamdata.csv"
    storedata = StoreData(datapath)
    findcorrelation(storedata)
setup()    