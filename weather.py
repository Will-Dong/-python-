import requests
import itchat
import json
import datetime
import time

city = '宣城'
url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city

def get_weather():
	resp = requests.get(url)
	return json.loads(resp.text)

def send_data(data):
	friend = itchat.search_friends(name='董玮')
	username = friend[0].UserName
	if '雨' in data['type']:
		data = data['date'] + '  ' + data['type'] + '  ' + data['high'] + '  ' + data['low'] + '  ' + data['fengxiang'] + '  记得带伞哦！'
	else:
		data = data['date'] + '  ' + data['type'] + '  ' + data['high'] + '  ' + data['low'] + '  ' + data['fengxiang']
	itchat.send(data, toUserName=username)

if __name__ == '__main__':
	itchat.auto_login(enableCmdQR=2, hotReload=True)
	while True:
		time_now = datetime.datetime.now()
		if time_now.hour == 9 and time_now.minute == 41:
			data = get_weather()
			print(data)
			data = data['data']['forecast'][0]
			send_data(data)
		else:
			print('it is not time to send weather forecast, waiting')
		time.sleep(60)
		