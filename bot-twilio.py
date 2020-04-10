from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests #For getting URL
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    url = "https://www.worldometers.info/coronavirus/country/peru/"
    r = requests.get(url)
    s = BeautifulSoup(r.text, 'html.parser')
    data = s.find_all("div","maincounter-number")
    
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    if 'Peru' in msg:
        resp = MessagingResponse()
        imagen = Image.open()
        resp.message('Total cases: {}'.format(data[0].text.strip()))
        resp.message('Total deaths: {}'.format(data[1].text.strip()))
        resp.message('Total recovered: {}'.format(data[2].text.strip()))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)