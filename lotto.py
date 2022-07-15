from nturl2path import url2pathname
import re
import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1021'

response = requests.get(url).json
# print(response)
print(response.get('drwtNo1'))
print(response.get('drwtNo2'))
print(response.get('drwtNo3'))
print(response.get('drwtNo4'))
print(response.get('drwtNo5'))
print(response.get('drwtNo6'))