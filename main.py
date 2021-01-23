
from datareader.csvreader import Csvreader 

def main():
    csv_reader = Csvreader("data/")
    czc = csv_reader.parse_csv("czc.csv")
    alza = csv_reader.parse_csv("alza.csv")
    mironet = csv_reader.parse_csv("mironet.csv")
    mall = csv_reader.parse_csv("mall.csv")

if __name__ == '__main__':
    main()