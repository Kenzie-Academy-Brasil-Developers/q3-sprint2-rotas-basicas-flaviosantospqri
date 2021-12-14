from flask import Flask
from os import getenv
from datetime import datetime

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return {'data': 'Hello Flask!'}

@app.route('/current_datetime', methods=['GET'])
def current():
    datetimeHour = datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")
    hour = datetime.now().hour
    if int(hour) < 12:
        message = 'Bom dia!' 
    elif int(hour) > 12 and int(hour) < 18:
        message = 'Boa tarde!'
    else:
        message = 'Boa noite!'     
    return {"current_datetime": datetimeHour, "message": message}