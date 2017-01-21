# from urllib import request
import urllib as scrape

file_url = "https://raw.githubusercontent.com/okfn/datapipes/master/test/data/gla.csv"

def file_downloader(csv_url):
    result = scrape.urlopen(csv_url)
    result_str = str(result)
    lines = result_str.split("\n")
    dest_file = '/Users/Tuhin_Khare/Desktop/Codes/Python/companies.csv'
    # dest_file = r'companies.csv'
    fp = open(dest_file,"w")
    for line in lines:
        fp.write(line + "\n")
    fp.close()

if __name__ == '__main__':
    file_downloader(file_url)
