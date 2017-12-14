from flask import Flask
from flask import request
from flask import jsonify
import requests
import json
import re

from flask_sslify import SSLify


app = Flask(__name__)
sslify = SSLify(app)


# TODO
# 1. Прием сообщений
# 2. Отправка сообщений
#
URL = 'https://api.telegram.org/bot/'

def write_json(data, filename='answer.json'):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=2, ensure_ascii=False)


def parse_text(text):
	pattern = r'/\w+'
	crypto = re.search(pattern, text).group()
	return crypto[1:]


def get_price(crypto):
	url = 'https://api.coinmarketcap.com/v1/ticker/{}'.format(crypto)
	r = requests.get(url).json()
	price = r[-1]['price_usd']
	# write_json(r.json(), filename='price.json')
	return price

# def get_updates():
# 	url = URL + 'getUpdates'
# 	r = requests.get(url)
# 	# write_json(r.json())
# 	return r.json()


def send_message(chat_id, text='blalbya'):
	url = URL + 'sendMessage'
	answer = {'chat_id': chat_id, 'text': text}
	r = requests.post(url, json=answer)
	return r.json()




@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		r = request.get_json()
		chat_id = r['message']['chat']['id']
		message = r['message']['text']

		pattern = r'/\w+'

		if re.search(pattern, message):
			price = get_price(parse_text(message))
			send_message(chat_id, text=price)

		# write_json(r)
		return jsonify(r)
	return '<h1>Bot welcomes you</h1>'



# def main():
# 	# r =requests.get(URL + 'getMe')
# 	# write_json(r.json())
# 	# r = get_updates()
# 	# chat_id = r['result'][-1]['message']['chat']['id']
# 	# send_message(chat_id)
# 	pass

if __name__ == '__main__':
	app.run()