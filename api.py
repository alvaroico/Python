# import requests

# resp = requests.get('https://api.github.com/users/alvaroico')
# if resp.status_code != 200:
#     # This means something went wrong.
#     raise print('GET /tasks/ {}'.format(resp.status_code))
# # dados = resp.json()
# # print(dados['login'])

#pip install Flask
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'