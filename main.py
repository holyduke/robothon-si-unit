
from datareader.csvreader import Csvreader 

def main():
    csv_reader = Csvreader("data/")
    alza_eshop = csv_reader.parse_csv("alza.csv")
    print(alza_eshop.products[0])

if __name__ == '__main__':
    main()