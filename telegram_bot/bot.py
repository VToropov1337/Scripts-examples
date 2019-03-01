import requests
import misc
from yobit import get_btc
from time import sleep

token = misc.token
URL = 'https://api.telegram.org/bot' + token + '/'
proxies = {
    "https": "168.11.14.250:8009"
}

global last_update_id
last_update_id = 0


def get_updates():
    url = URL + 'getupdates'

    r = requests.get(url, proxies=proxies)
    return r.json()


def get_message():
    data = get_updates()
    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']

        messages = {'chat_id': chat_id,
                    'message': message_text}

        return messages
    return None


def send_message_to_bot(chat_id, text='Processing'):
    url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url, proxies=proxies)


def main():
    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['message']

            if text == '/btc':
                send_message_to_bot(chat_id, get_btc())

        else:
            continue

        sleep(3)


# d = get_message()
# with open('updates.json','w') as file:
#     json.dump(d,file,indent=2,ensure_ascii=False)


if __name__ == '__main__':
    main()
