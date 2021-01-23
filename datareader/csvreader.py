import csv
import sys
import os
from .Eshop import Eshop

csv.field_size_limit(13107200)

class Csvreader:
  def __init__(self, path_to_csv):
    self.path_to_csv = path_to_csv

  def parse_csv(self, csv_name):
    path = self.path_to_csv + csv_name
    with open(path, encoding='utf-8') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      eshop = Eshop(csv_name.replace(".csv",""))
      # try:
      for row in csv_reader:
          if line_count == 0:
              print(f'Column names are {", ".join(row)}')
              line_count += 1
          else:
              eshop.addProduct(row)
              line_count += 1
      # except:
      #   print("hovno")
      print(f'Processed {line_count} lines.')

      return eshop