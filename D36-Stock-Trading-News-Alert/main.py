import requests
import os
import itertools
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

refined_news_data = []

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
alphavantage_token = os.environ.get("AVANTAGE_TOKEN")

# Daily data not free anymore, had to use a workaround
alphavantage_params = {
    'function': 'TIME_SERIES_INTRADAY',
    'symbol': STOCK_NAME,
    'interval': '60min',
    'apikey': alphavantage_token,
}
# Get stock info from Alphavantage
alphavantage_response = requests.get(STOCK_ENDPOINT, params=alphavantage_params)
alphavantage_response.raise_for_status()
raw_stock_data = alphavantage_response.json()

# Reduce stock info to only daily data at close
daily_info = {date_hour: price_info for (date_hour, price_info) in
              raw_stock_data['Time Series (60min)'].items() if "16:00:00" in date_hour}

# Reduce daily info set to only last two days
two_day_data = dict(itertools.islice(daily_info.items(), 2))

# Reduce last two days price data to only close price
two_day_close = {date_hour: price_data['4. close'] for (date_hour, price_data) in two_day_data.items()}
two_day_close_price = [price_data['4. close'] for (date_hour, price_data) in two_day_data.items()]
print(two_day_close_price)

# Mpte: Alternatively, can reduce raw data straight to list containing dictionaries of close data only (ie strip dates)

# Calculate  difference between close prices
price_delta = float(two_day_close_price[0]) - float(two_day_close_price[1])
up_down = None
if price_delta > 0:
    up_down = "📈"
else:
    up_down = "📉"

# Calculate percent difference
percent_diff = round((float(two_day_close_price[0])-float(two_day_close_price[1]))/float(two_day_close_price[0])*100)

get_news = False

if abs(percent_diff) > 5:
    get_news = True

# STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# Extract dates from stock info for news search
raw_dates = [raw_date for raw_date in two_day_data.keys()]
to_date = raw_dates[0]
to_date = to_date[0:10]
from_date = raw_dates[1]
from_date = from_date[0:10]

news_params = {
    'q': COMPANY_NAME,
    'from': from_date,
    'to': to_date,
    'language': 'en',
    'apiKey': os.environ.get('NEWS_TOKEN')
}

# Use the News API to get articles related to the COMPANY_NAME.
if get_news:
    raw_news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    raw_news_data = raw_news_response.json()

    # Reduce news info to first few entries
    raw_news_data_slice = raw_news_data['articles'][0:3]
    # Note: Can combine line 76 and line 73 but cant slice; need two lines to splice
    # Note: Could slice [:3] instead

    # Generate list with 3 articles and keep only relevant info
    refined_news_data = [f"{STOCK_NAME}: {up_down}{percent_diff}%\nHeadline: {article['title']}.\n"
                         f"Brief: {article['description']}\nURL: {article['url']}" for article in raw_news_data_slice]
    print(refined_news_data)

# STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

# Send info via Twilio
if get_news:
    account_sid = "AC58224f128a10772cb2d1591eba220c35"
    auth_token = os.environ.get("AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    for article_item in refined_news_data:
        message = client.messages \
            .create(
                body=article_item,
                from_='+18885944415',
                to='+17862901867'
            )
        print(message.status)

# Optional Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to 
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height 
of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to 
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height 
of the coronavirus market crash.
"""
