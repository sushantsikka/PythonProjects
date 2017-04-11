from flask import Flask,request
from flask_restful import reqparse
from bs4 import BeautifulSoup
import speech
import requests

app = Flask(__name__)

parser = reqparse.RequestParser() # We add a Request parser using library flask_restful
parser.add_argument('url', type=str)

@app.route('/<string:url>',methods=['GET'])
def call_api(url):
    r = requests.get('https://adobe.ly/'+url)
    soup = BeautifulSoup(r.text)

    speech.say(soup.title.string)
    text_list = soup.find_all('p' or 'h1')

    for l in text_list:
        speech.say(l)


if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=int("5000")
    )
