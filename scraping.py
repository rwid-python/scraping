import bs4
import requests

url = 'https://jadwalsholat.pkpu.or.id/?id=308'
contents = requests.get(url)
s_code = contents.status_code
print(s_code)

response = bs4.BeautifulSoup(contents.text,"html.parser")
#print(response)

if s_code == 200:
    data = response.find_all('tr', 'table_highlight')
    data = data[0]
    print(data)

    jadwal_sholat = {}
    i = 0
    for d in data:
        if i == 1:
            jadwal_sholat['subuh'] = d.get_text()
        elif i == 2:
            jadwal_sholat['zuhur'] = d.get_text()
        elif i == 3:
            jadwal_sholat['ashar'] = d.get_text()
        elif i == 4:
            jadwal_sholat['magrib'] = d.get_text()
        elif i == 5:
            jadwal_sholat['isya'] = d.get_text()
        i += 1
    print(jadwal_sholat)
    print(jadwal_sholat['magrib'])
else:
    print('error')
