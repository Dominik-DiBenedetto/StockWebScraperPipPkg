from bs4 import BeautifulSoup
import requests

def getURL(symbol):
    url = ""
    if symbol == "APPL":
        url = "https://www.cnbc.com/quotes/AAPL?qsearchterm="
    else:
        url = "https://www.cnbc.com/quotes/{}?qsearchterm={}".format(symbol, symbol)
    return url

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