#TODO To fix the spider's movement


import requests
from bs4 import BeautifulSoup

def my_spider(no_pages,url):
    page = 1
    while page <= no_pages:
        src = requests.get(url)
        #convert the source code in text format
        text = src.text
        mysoup = BeautifulSoup(text)

        #TODO Remember #Camel Case in the find function

        for link in mysoup.findAll("script","item-name"):
            ta = "My url is" + link.get('href')
            print(href)

        page += 1

if __name__ == "__main__":
    my_spider(1,"http://www.amazon.in/s/ref=s9_acss_bw_cg_UBSGenr_4a1_w?fst=as%3Aoff&rh=n%3A%2110892650031%2Cn%3A1318161031&bbn=10892650031&ie=UTF8&qid=1472092151&rnid=10892650031&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=0DEZ34D8WZYJ1RYRTQKT&pf_rd_t=101&pf_rd_p=75a867b4-2a5e-4164-9960-7d79228ad118&pf_rd_i=10892650031")
