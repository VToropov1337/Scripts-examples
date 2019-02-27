import requests
import misc
from yobit import get_btc
from time import sleep

token = misc.token
URL = 'https://api.telegram.org/bot' + token + '/'
proxies = {
    "https": "168.11.14.250:8009"
}


def get_updates():
    url = URL + 'getupdates'

    r = requests.get(url, proxies=proxies)
    return r.json()


def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']

    messages = {'chat_id': chat_id,
                'message': message_text}

    return messages


def send_message_to_bot(chat_id, text='Processing'):
    url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url, proxies=proxies)


def main():
    while True:

        answer = get_message()
        chat_id = answer['chat_id']
        text = answer['message']

        if text == '/btc':
            send_message_to_bot(chat_id, get_btc())

        sleep(3)

    # d = get_updates()
    # with open('updates.json','w') as file:
    #     json.dump(d,file,indent=2,ensure_ascii=False)


if __name__ == '__main__':
    main()
