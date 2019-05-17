# -*- coding:utf-8 -*-
# 
"""
Created by hui at 2019/5/17

@author: hui
"""

import requests
import urllib.parse


token_url = 'https://openapi.baidu.com/oauth/2.0/token'
text2audio_url = 'http://tsn.baidu.com/text2audio'
client_id = 'your baidu API Key'
client_secret = 'your baidu	Secret Key'

text = '''你想转换的内容'''

'''
grant_type：必须参数，固定为“client_credentials”；
client_id：必须参数，应用的 API Key；
client_secret：必须参数，应用的 Secret Key;
'''


def text2audio():
	params = {
		'grant_type': 'client_credentials',
		'client_id': client_id,
		'client_secret': client_secret
	}
	response = requests.post(url=token_url, data=params)
	# print(response.json()['access_token'])
	'''
	tex	必填	合成的文本，使用UTF-8编码。小于2048个中文字或者英文数字。（文本在百度服务器内转换为GBK后，长度必须小于4096字节）
	tok	必填	开放平台获取到的开发者access_token（见上面的“鉴权认证机制”段落）
	cuid	必填	用户唯一标识，用来计算UV值。建议填写能区分用户的机器 MAC 地址或 IMEI 码，长度为60字符以内
	ctp	必填	客户端类型选择，web端填写固定值1
	lan	必填	固定值zh。语言选择,目前只有中英文混合模式，填写固定值zh
	spd	选填	语速，取值0-15，默认为5中语速
	pit	选填	音调，取值0-15，默认为5中语调
	vol	选填	音量，取值0-15，默认为5中音量
	per	选填	发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女声
	aue	选填	3为mp3格式(默认)； 4为pcm-16k；5为pcm-8k；6为wav（内容同pcm-16k）; 注意aue=4或者6是语音识别要求的格式，但是音频内容不是语音识别要求的自然人发音，所以识别效果会受影响。
	'''
	text2audio_data = {
		'tok': response.json()['access_token'],
		'cuid': 'chizhouhuipingtianhu',
		'ctp': 1,
		'lan': 'zh',
		'spd': 7,
		'pit': 8,
		'vol': 15,
		'per': 4,
		'aue': 3,
		'tex': urllib.parse.quote_plus(text)
	}
	# l1 = urllib.parse.quote(text)
	# print(l1)
	# l2 = urllib.parse.quote_plus(text)
	# print(l2)
	response = requests.post(url=text2audio_url, data=text2audio_data)
	# print(response.headers)
  
  # 将生成的MP3格式语音文件保存到当前目录的result.mp3
	with open('result.mp3', 'wb') as f:
		f.write(response.content)



def main():
	"""程序执行主入口"""
	text2audio()



if __name__ == '__main__':
	main()
