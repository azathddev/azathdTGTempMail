import requests
import random
import string
import time
import os
from config import *

API = 'https://www.1secmail.com/api/v1/'
domain_list = ["1secmail.com", "1secmail.org", "1secmail.net"]
domain = random.choice(domain_list)


def generate_username():
    name = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(name) for i in range(10))

    return username


def check(mail=''):
    req_link = f'{API}?action=getMessages&login={mail.split("@")[0]}&domain={mail.split("@")[1]}'
    r = requests.get(req_link).json()
    length = len(r)

    if length == 0:
        return EMPTY_MAIL_MESSAGE, None
    else:
        id_list = []

        for i in r:
            for k, v in i.items():
                if k == 'id':
                    id_list.append(v)
        letters = []
        for i in id_list:
            read_msg = f'{API}?action=readMessage&login={mail.split("@")[0]}&domain={mail.split("@")[1]}&id={i}'
            r = requests.get(read_msg).json()
            print(r)

            sender = r.get('from')
            subject = r.get('subject')
            date = r.get('date')
            content = r.get('textBody')

            letters.append(f'Отправитель: {sender} \nДата: {date} \nТема: {subject} \nСодержание: {content}')

        return COUNT_MAIL_MESSAGE.replace('length', str(len(id_list))), letters


def delete(mail=''):
    url = 'https://www.1secmail.com/mailbox'

    data = {
        'action': 'deleteMailbox',
        'login': mail.split('@')[0],
        'domain': mail.split('@')[1]
    }

    r = requests.post(url, data=data)


def create() -> str:
    username = generate_username()
    mail = f'{username}@{domain}'
    requests.get(f'{API}?login={mail.split("@")[0]}&domain={mail.split("@")[1]}')
    return mail
