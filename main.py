from bs4 import BeautifulSoup
import requests

'''Function to get the URL for the prices
        1. make an empty url string
        2. check if the symbol/url is for apple because
            apple's url is different
        3. if its not apples url use the base url and pass the symbol as perameters
        4. Lastly return the url for use in other functions '''

def getURL(symbol):
    url = ""
    if symbol == "APPL":
        url = "https://www.cnbc.com/quotes/AAPL?qsearchterm="
    else:
        url = "https://www.cnbc.com/quotes/{}?qsearchterm={}".format(symbol, symbol)
    return url

'''Function to get the price for the given stock
        1. use our getURL function to make a url for the given stock
        2. load up our basic BeautifulSoup structure
        3. get the price using the class name and make a prices array
        4. check if its after hours
        5. if its after hours append the closed price and the after hours price to the prices array and 
            return it
        6. if its not after hours then just return the current price'''

def getPrice(symbol):
    url = getURL(symbol)
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    spanElms = soup.find_all("span")
    price = soup.find(class_='QuoteStrip-lastPrice').text
    prices = []
    if "After Hours:" in spanElms[52].text:
        price = soup.find(class_='QuoteStrip-lastPrice').text
        prices.append(price)
        prices.append(spanElms[58].text)
        return prices
    return price

'''Function to get the difference/the amount a stock went up or down
        1. get the url for the given stock using the getURL
        2. load up our basic BeautifulSoup structure
        3. get the difference using the tag name and make a differences array
        4. check if its after hours
        5. if its after hours append the closed difference and the after hours 
            differences to the differences array and return it
        6. if its not after hours then just return the current difference'''


def getDifference(symbol):
    url = getURL(symbol)
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    spanElms = soup.find_all("span")
    diff = spanElms[52].text
    diffs = []
    if "After Hours:" in diff:
        diff = spanElms[56].text
        diffs.append(diff)
        diffs.append(spanElms[60].text)
        return diffs
    else:
        diff = spanElms[52].text
        return diff

'''Function to get the percentage a stock went up or down
        1. get the url for the given stock using the getURL
        2. load up our basic BeautifulSoup structure
        3. get the percentage using the tag name and make a percentages array
        4. check if its after hours
        5. if its after hours append the closed percentage and the after hours 
            percentage to the percentages array and return it
        6. if its not after hours then just return the current percentage'''

def getPercentage(symbol):
    url = getURL(symbol)
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    spanElms = soup.find_all("span")
    percent = spanElms[53].text
    percents = []
    if "EST" in percent:
        percent = spanElms[57].text
        percents.append(percent)
        percents.append(spanElms[61].text)
        return percents
    else:
        percent = spanElms[53].text
        return percent