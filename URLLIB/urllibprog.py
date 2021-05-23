# from urllib.request import urlopen
# from urllib.request import Request
# import urllib.error
# r = urlopen("https://google.com")
# r = Request("https://google.com")
# r.add_header('Accept-Language', 'hi')
# encodings = 'deflate, gzip, identity'
# r.add_header("Accept-Encoding", encodings)
# res = urlopen(r);
# print(res.getheader('Content-Encoding'))
# print(r.header_items())
# print(r.url)
# print(r.readline())

from http.cookiejar import CookieJar

cookie_jar = CookieJar()
print(len(cookie_jar))

from urllib.request import build_opener, HTTPCookieProcessor

opener = build_opener(HTTPCookieProcessor(cookie_jar))
opener.open("https://google.com")
print(len(cookie_jar))

print(cookie_jar)
