import numpy as np
import urllib.request
import json

from flask import Flask, render_template


app = Flask(__name__)


def get_json_object(url):
    """
    Calls the urllib.request.urlopen function and return JSON.
    """

    # make a call to the specified url
    webURL = urllib.request.urlopen(url)

    # parse the data into a JSON object
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    msg = json.loads(data.decode(encoding))

    return msg


def price(url):
    """
    """
    return float(get_json_object(url)[0]['price_eur'])


@app.route('/')
@app.route('/index')
def main():

    # # links to the coinmarketcap.com API for the various coins
    # eth_url = 'https://api.coinmarketcap.com/v1/ticker/ethereum/?convert=EUR'

    # # user amount in each coin
    # eth = 1.00

    # urls = [eth_url]
    # amts = [eth]

    # prices = [price(x) for x in urls]

    # values = [prices[x]*amts[x] for x in range(len(amts))]

    # roi = sum([price(urls[x])*amts[x] for x in range(len(amts))])

    # returnstr = ('Crypto Price Summary \n\n\n' +
    #              'COIN:   ' + 'PRICE      ' + '  ' + 'VALUE      ' + '\n\n' +
    #              'ETH:    ' + str(prices[0]) + ' ' + str(values[0]) +
    #              '\n\n\nROI: ' + str(roi) + '\n\n\n')

    user = {'username': 'Miguel'}
    posts = [{
                'author': {'username': 'John'},
                'body': 'Beautiful day in Portland!'
            },
            {
                'author': {'username': 'Susan'},
                'body': 'The Avengers movie was so cool!'
            }]

    return render_template('index.html', title='This is the Title', user=user, posts=posts)


if __name__ == '__main__':
    app.run()
