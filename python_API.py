import requests

request_bbc_status = requests.get("http://www.bbc.co.uk")
web_code = request_bbc_status.status_code

if web_code == 200:
    print("The BBC website is up and running")
elif web_code == 404:
    print("The BBC website is not available")
elif web_code == 500:
    print("The BBC website is down")
else:
    print("The BBC website is not available")
    