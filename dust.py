import requests
from bs4 import BeautifulSoup

KEY = ''
url = f''

response = requests.get(url).text

response = requests.get(url).text
data = BeautifulSoup(response, 'xml')
item = data('item')[7]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)

if 150 < dust:
    status = '매우나쁨'
elif 80 < dust <= 150:
    status = '나쁨'
elif 30 < dust and dust <= 80:
    status = '보통'
else:
    status = '좋음'

print(f'{time} 기준 {station}의 미세먼지 농도는 {dust}')