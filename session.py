# Filename: session.py
# -*- coding: utf-8 -*-
import cookielib
import urllib
import urllib2


class Session:
    def __init__(self, url):
        self._cookieJar = cookielib.CookieJar()
        self._opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self._cookieJar))
        self._opener.addheaders.append(('Connection', 'keep-alive'))
        self._opener.addheaders.append(('User-agent', 'Mozilla/4.0'))
        self._url = url

    def post_data(self, page, data):
        data = urllib.urlencode(data)
        destination = self._url + page
        try:
            response = self._opener.open(destination, data)
        except urllib2.URLError:
            print "Nie udało się."
            return None
        return response

    def get_data(self, page, data):
        data = urllib.urlencode(data)
        destination = self._url + page
        if len(data) != 0:
            destination += '?'+data
        try:
            response = self._opener.open(destination)
        except urllib2.URLError:
            print "Nie udało się."
            return None
        return response

    def set_url(self, url):
        self._url = url

    def get_url(self):
        return self._url

    def set_opener(self, opener):
        self._opener = opener

    def get_opener(self):
        return self._opener

    def set_cookie_jar(self, cookie_jar):
        self._cookieJar = cookie_jar

    def get_cookie_jar(self):
        return self._cookieJar
# End of session.py