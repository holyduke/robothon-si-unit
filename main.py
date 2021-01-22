
from datareader.csvreader import Csvreader 

def main():
    csv_reader = Csvreader("data/")
    czc_eshop = csv_reader.parse_csv("czc.csv")
    print(czc_eshop.products[0])

if __name__ == '__main__':
    main()