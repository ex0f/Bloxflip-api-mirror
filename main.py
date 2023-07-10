import os

os.system("pip install flask")
os.system("pip install fake_useragent")
os.system("pip install zenrows")
os.system("pip install requests")

from zenrows import ZenRowsClient
from fake_useragent import UserAgent
from flask import Flask, jsonify, request
import requests
 
ex = Flask(__name__)
 
crash = 'https://api.bloxflip.com/games/crash'
roulette = 'https://api.bloxflip.com/games/roulette'
zenrows_client = ZenRowsClient("YOU API KEY") #get your api key from https://www.zenrows.com/
 
@ex.route('/games/crash', methods=['GET'])
def crash_mirror():
    user_agent = UserAgent()
    headers = {'User-Agent': user_agent.random}
    response = zenrows_client.get(crash, headers=headers)
    json_data = response.json()
    css_style = 'background-color: black; color: white;'
    api_response = {
        'style': css_style,
        **json_data
    }
    response_string = jsonify(api_response)
    response_string.headers['Content-Type'] = 'application/json'
    return response_string
 
@ex.route('/games/roulette', methods=['GET'])
def roulette_mirror():
    user_agent = UserAgent()
    headers = {'User-Agent': user_agent.random}
    response = zenrows_client.get(roulette, headers=headers)
    json_data = response.json()
    css_style = 'background-color: black; color: white;'
    api_response = {
        'style': css_style,
        **json_data
    }
    response_string = jsonify(api_response)
    response_string.headers['Content-Type'] = 'application/json'
    return response_string
 
if __name__ == '__main__':
    ex.run(debug=True, host='0.0.0.0', port=8080)
