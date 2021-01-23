import os
from os import path
from datareader.csvreader import Csvreader
import pickle


def loadDataSets(USE_PICKLE):
  if USE_PICKLE and path.exists("pickle-data/czc.obj") and path.exists("pickle-data/alza.obj") and path.exists("pickle-data/mall.obj") and path.exists("pickle-data/mironet.obj"):
    # Load pickle
    filehandler = open("pickle-data/czc.obj","rb")
    czc = pickle.load(filehandler)
    filehandler = open("pickle-data/alza.obj","rb")
    alza = pickle.load(filehandler)
    filehandler = open("pickle-data/mironet.obj","rb")
    mironet = pickle.load(filehandler)
    filehandler = open("pickle-data/mall.obj","rb")
    mall = pickle.load(filehandler)
  else:
    csv_reader = Csvreader("data/")
    czc = csv_reader.parse_csv("czc.csv")
    alza = csv_reader.parse_csv("alza.csv")
    mironet = csv_reader.parse_csv("mironet.csv")
    mall = csv_reader.parse_csv("mall.csv")
    # Dump pickle
    filepath = "./pickle-data"
    if not path.exists("pickle-data"):
      os.mkdir(filepath)
    filehandler = open(filepath+"/czc.obj","wb")
    pickle.dump(alza, filehandler)
    filehandler = open(filepath+"/alza.obj","wb")
    pickle.dump(alza, filehandler)
    filehandler.close()
    filehandler = open(filepath+"/mironet.obj","wb")
    pickle.dump(mironet, filehandler)
    filehandler = open(filepath+"/mall.obj","wb")
    pickle.dump(mall, filehandler)
    filehandler.close()
  
  return czc, alza, mironet, mall