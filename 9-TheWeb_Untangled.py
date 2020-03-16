import urllib.request as ur
#url = 'http://www.jbbank.co.kr'
url = 'http://google.com'
conn = ur.urlopen(url)
data = conn.read()
print(conn.status)
print(conn.getheader('Content-Type'))
#print(data)
for key, value in conn.getheaders():
    print('[Key, Value]', key, value)

import requests
url = 'http://google.com'
url = 'http://www.jbbank.co.kr'
resp = requests.get(url)
print(resp)
print(resp.text)


from bottle import route, run
@route('/')
def home():
    return "It isn't fancy, but it's my home page"

#run(host='localhost', port=9999)

from bottle import route, run, static_file

@route('/')
def main():
    return static_file('index.html', root='.')

#run(host='localhost', port=9999)


from bottle import route, run, static_file

@route('/')
def home():
    return static_file('index.html', root='.')

@route('/echo/<thing>')
def echo(thing):
    return "Say hello to my little friend: %s!" % thing
# run(host='localhost', port=9999)

import requests

resp = requests.get('http://localhost:9999/echo/Mothra')
if resp.status_code == 200 and resp.text == 'Say hello to my little friend: Mothra!':
    print('It worded! That almost never happens!')
else:
    print('Argh, got this:', resp.text)
