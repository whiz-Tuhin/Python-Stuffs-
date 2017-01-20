import random
import urllib as scrape

def image_downloader(url):
    name = str(random.randrange(1,1000)) + ".jpg"
    scrape.urlretrieve(url,name)

if __name__ == '__main__':
    image_downloader("http://www.highreshdwallpapers.com/wp-content/uploads/2013/08/Neptune-Skies.jpg")