import os, requests; from flask import Flask, jsonify, request; from fake_useragent import UserAgent; from zenrows import ZenRowsClient

ex = Flask(__name__)

pip_packages = ["requests", "flask", "fake_useragent", "zenrows"]
for package in pip_packages:
    os.system(f"pip install {package}")

zenrows_client = ZenRowsClient("YOUR ZENROWS API KEY HERE") #get your api key from https://www.zenrows.com/

def exy(url):
    user_agent = UserAgent()
    headers = {'User-Agent': user_agent.random,
               'x-auth-token': request.headers.get('x-auth-token')}
    response = zenrows_client.get(url, headers=headers)
    json_data = response.json()
    css_style = 'background-color: black; color: white;'
    api_response = {'style': css_style, **json_data}
    response_string = jsonify(api_response)
    response_string.headers['Content-Type'] = 'application/json'
    return response_string

@ex.route('/games/crash', methods=['GET'])
def crash_mirror():
    return exy('https://api.bloxflip.com/games/crash')

@ex.route('/games/roulette', methods=['GET'])
def roulette_mirror():
    return exy('https://api.bloxflip.com/games/roulette')

@ex.route('/user', methods=['GET'])
def user_mirror():
    return exy('https://api.bloxflip.com/user')

@ex.route('/games/mines', methods=['GET', 'POST', 'PUT', 'DELETE'])
def games_mirror():
    headers = {'x-auth-token': request.headers.get('x-auth-token')}
    method = request.method
    if 'x-auth-token' not in request.headers:
        return {"success": False, "msg": "Authorization header is missing", "error": "Authorization header is missing"}, 401
    
    try:
        if method == 'GET':
            return exy('https://api.bloxflip.com/games/mines')
        elif method == 'POST':
            response = zenrows_client.post('https://api.bloxflip.com/games/mines', headers=headers, json=request.json)
        elif method == 'PUT':
            response = zenrows_client.put('https://api.bloxflip.com/games/mines', headers=headers, json=request.json)
        elif method == 'DELETE':
            response = zenrows_client.delete('https://api.bloxflip.com/games/mines', headers=headers)
        else:
            return {'error': 'Invalid HTTP method'}, 400
        response.raise_for_status()
        response_data = response.json()
        return jsonify(response_data)
    except requests.exceptions.HTTPError as err:
        if str(err).startswith('422 Client Error: Unprocessable Entity'):
            return {"success": False, "msg": "Authentication failed, please try to login again!", "error": "Authentication failed, please try to login again!"}, 401
        return {'error': str(err)}, err.response.status_code
    except requests.exceptions.RequestException as err:
        return {'error': str(err)}, 500
    except ValueError as err:
        return {'error': 'Invalid JSON response'}, 500

@ex.route('/games/mines/history', methods=['GET', 'POST', 'PUT', 'DELETE'])
def history():
    headers = dict(request.headers)
    method = request.method
    path = 'https://api.bloxflip.com/games/mines/history'
    if request.args:
        path += '?' + '&'.join([f"{key}={value}" for key, value in request.args.items()])
    if 'x-auth-token' not in request.headers:
        return {"success": False, "msg": "Authorization header is missing", "error": "Authorization header is missing"}, 401
    try:
        if method == 'GET':
            return exy(path)
        elif method == 'POST':
            response = zenrows_client.post(path, headers=headers, json=request.json)
        elif method == 'PUT':
            response = zenrows_client.put(path, headers=headers, json=request.json)
        elif method == 'DELETE':
            response = zenrows_client.delete(path, headers=headers)
        else:
            return {'error': 'Invalid HTTP method'}, 400

        response.raise_for_status()
        response_data = response.json()
        return jsonify(response_data)
    except requests.exceptions.HTTPError as err:
        if str(err).startswith('422 Client Error: Unprocessable Entity'):
            return {"success": False, "msg": "Authentication failed, please try to login again!", "error": "Authentication failed, please try to login again!"}, 401
        return {'error': str(err)}, err.response.status_code
    except requests.exceptions.RequestException as err:
        return {'error': str(err)}, 500
    except ValueError as err:
        return {'error': 'Invalid JSON response'}, 500

@ex.route('/chat/history', methods=['GET'])
def chat_mirror():
    return exy('https://api.bloxflip.com/chat/history')

if __name__ == '__main__':
    ex.run(debug=True, host='0.0.0.0', port=8080)
