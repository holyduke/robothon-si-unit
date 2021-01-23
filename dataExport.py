import json

def dataExport(dataToExport):
  with open('data.json', 'w') as outfile:
    json.dump(dataToExport, outfile)