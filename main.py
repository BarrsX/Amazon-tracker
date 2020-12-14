import requests
import bs4
import pandas as pd

proxies = {
    "http": 'http://162.214.92.202:80',
    "https": 'http://162.214.92.202:80'
}

HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
offer = []


def tracker(url, TrackingPrice):
    res = requests.get(url, headers=HEADERS)
    soup = bs4.BeautifulSoup(res.content, features='lxml')

    try:
        title = soup.find(id="productTitle").get_text().strip()
        amount = float(soup.find(id='priceblock_ourprice').get_text().replace("₹", "").replace("$", "").strip())
        if amount <= TrackingPrice:
            offer.append("The {0} is available for {1}. Here's the link {2}".format(title, amount, url))
    except:
        offer.append("Price for {0} was not found.".format(title))


df = pd.read_csv(
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vTMjUgd1sofL4XxRvsbw8z0PbZ_-9m9bBM3nYwms3ZBrSYPVVI-NbJu2KMGo5BUwl5WYgISU2ao-4dK/pub?output=csv")
for i in range(0, len(df["URL"])):
    tracker(df["URL"][i], df["TrackingPrice"][i])
outputs["message"] = offer
