from flask import Flask
import requests
import json


# app = Flask(__name__)



# TODO
# 1. Прием сообщений
# 2. Отправка сообщений
URL = 'https://api.telegram.org/bot507654623:AAGyzs4Et1ImX9oaALZseb4UY_hhjci8_po/'

def write_json(data, filename='answer.json'):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=2, ensure_ascii=False)


def get_updates():
	url = URL + 'getUpdates'
	r = requests.get(url)
	# write_json(r.json())
	return r.json()


def send_message(chat_id, text='blalbya'):
	url = URL + 'sendMessage'
	answer = {'chat_id': chat_id, 'text': text}
	r = requests.post(url, json=answer)
	return r.json()



def main():
	# r =requests.get(URL + 'getMe')
	# write_json(r.json())
	r = get_updates()
	chat_id = r['result'][-1]['message']['chat']['id']
	send_message(chat_id)





if __name__ == '__main__':
	main()