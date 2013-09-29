# -*- coding: utf-8 -*-
from session import Session


def is_logged(response):
    if response is None:
        return False
    url = response.geturl()
    return "studMain" in url


def get_users_count(conn):
    remote_page = 'remote.web?getOnlineCount'
    resp = conn.get_data(remote_page, {})
    if resp is not None:
        return resp.read()


def login(conn, login, password):
    login_page = 'login.web'
    credentials = {'licznik': 's', 'login': login, 'pass': password}
    print "Logowanie rozpoczęte.."
    resp = conn.post_data(login_page, credentials)
    return is_logged(resp)


def zapisz_na_zajecia(conn, idblok, idzajec):
    data = {'action': 'Zapisz na zajęcia', 'idBlok': idblok, 'idZajec': idzajec}
    zajecia_page = 'zajecia.web'
    print "Żadanie zostało wysłane.."
    return conn.post_data(zajecia_page, data)

#data = {'action': 'Zapisz na zajęcia', 'idBloku': '9197067', 'idZajec': '9599287'}
url = 'https://ps.ug.edu.pl/'

log = raw_input("Login: ")
password = raw_input("Password: ")
conn = Session(url)

if login(conn, log, password):
    print "Zalogowano pomyślnie."
else:
    print "Wystąpił błąd podczas logowania."

response = zapisz_na_zajecia(conn, '9197067', '9599287')
print response.getcode()