from containers.Session import *
import pandas as pd

csvFile = pd.read_csv("testw.csv")
print(csvFile['tcp.srcport'][0])
mySession = Session("42577","443","10.185.33.246","172.217.22.106",csvFile)

mySession.print_frame()

