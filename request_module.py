import requests
# dic={'key1':'pramod','key2':'beti'}
# r=requests.get('https://in.search.yahoo.com/search?fr=mcafee&type=E211IN826G0&p=google.com',params=dic)
# print(r)
# print(r.url)
dic={'key1':'pramod','key2':'beti'}
r=requests.post('https://in.search.yahoo.com/search?fr=mcafee&type=E211IN826G0&p=google.com',data=dic)
print(r.text)
print(r.status_code)
