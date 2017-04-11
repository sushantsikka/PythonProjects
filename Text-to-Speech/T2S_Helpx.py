from flask import Flask,render_template,request
from bs4 import BeautifulSoup
# Import BeautifulSoup to scrape webpage
import speech
import requests


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def T2S():
  try:
        if request.method=='POST':
            url=request.form['url']
            r = requests.get(url)
            soup = BeautifulSoup(r.text)

            speech.say(soup.title.string)
            text_list = soup.find_all('p' or 'h1')
            for l in text_list:
                speech.say(l)

            return render_template('index.html',data=request.form['url'])
        if request.method=='GET':
            return render_template('index.html')
  except:
      return 'Sorry, there seems to be some error !'

if __name__ == '__main__':
    app.run(
       host="127.0.0.1",
       port=int("5005")
    )
