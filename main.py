import urllib.request
import json
import numpy
import datetime
import random
import string
import time
import os
import sys

os.system("title WARP-PLUS-CLOUDFLARE By ALIILAPRO")
os.system('cls' if os.name == 'nt' else 'clear')

referrer  = ['7d4d392f-104d-44ec-bce0-f40f7d0b8aa1','622737e8-05fa-4879-9e5c-3019d203af97']
def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run(index):
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer[index],
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
				"type": "Android",
				"locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		pass  

def run_buff():
  timeCount = 0
  g = numpy.zeros(len(referrer))
  b = numpy.zeros(len(referrer))
  rs = ["" for x in range(len(referrer))]
  
  while True:
   
    for index in range(len(referrer)) :
      result = run(index)
      timeCount = timeCount+1
      if result == 200:
        g[index] = g[index] + 1
      else:
        b[index] =  b[index] + 1  
      rs[index] = f"{g[index]} GB \n" + f"accountId = {referrer[index]}\n"
    if timeCount% (len(referrer)*10) == 0 :
      os.system('cls' if os.name == 'nt' else 'clear')
      print(f"count : {timeCount}")
      for i in rs :
        print(i)
run_buff()