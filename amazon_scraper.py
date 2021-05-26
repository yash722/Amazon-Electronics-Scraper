from bs4 import BeautifulSoup
import requests

def get_name(soup):
    try:
        title = soup.find("span", attrs={"class":'a-size-medium a-color-base a-text-normal'}).string.strip()
    except AttributeError:
        title = ""   
    return title

def get_rating(soup):
    try:
        rating = soup.find("span", attrs={"class":'a-icon-alt'}).string.strip()
    except AttributeError:
        rating = "Rating not listed"   
    return rating

def get_price(soup):
    try:
        price = "Rs. "+soup.find("span", attrs={'class':'a-price-whole'}).string.strip()
    except AttributeError:
        price = "Price Not listed"  
    return price

def get_pic_url(soup):
    try:
        img_div = soup.find("div", attrs = {'class':"a-section aok-relative s-image-fixed-height"})
        img_str = img_div.img.get('src')
    except AttributeError:
        img_str = 'Image not available'
    return img_str


if __name__ == '__main__':
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})
    query = input("Enter product you want to search about(Electronics):- ")
    query = "+".join(query.split(" ")).lower()
    starting_url = f'https://www.amazon.in/s?k={query}&ref=nb_sb_noss_2'
    webpage = requests.get(starting_url, headers = HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    prods = []
    res = soup.find_all("div", attrs = {"data-component-type":"s-search-result"})
    print("\nSEARCH RESULTS FOR FIRST PAGE: - \n\n")
    for i in res:
        print("Product Name =", get_name(i))
        print("Product Selling Price =", get_price(i))
        print("Product Rating =", get_rating(i))
        print("Product Image =", get_pic_url(i))
        print("\n-----------------------------------------------------------------------------------------------\n")