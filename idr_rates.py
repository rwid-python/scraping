import requests

sources = requests.get('http://www.floatrates.com/daily/idr.json')
json_data = sources.json()
# print(json_datas)

for data in json_data.values():
    print({data['code']})
    print({data['name']})
    print({data['date']})
    print({data['inverseRate']})
