import requests

# request_bbc_status = requests.get("http://www.bbc.co.uk")
# web_code = request_bbc_status.status_code

# if web_code == 200:
#     print("The BBC website is up and running")
# elif web_code == 404:
#     print("The BBC website is not available")
# elif web_code == 500:
#     print("The BBC website is down")
# else:
#     print("The BBC website is not available")

url = "https://api.postcodes.io/postcodes/"

postcode = "po20uj" 
#input("Please enter your postcode: ")

# request_postcode = requests.get(url + postcode)

# print(request_postcode.status_code)
# print(request_postcode.json()["result"]["postcode"])
# print(request_postcode.json()["result"]["longitude"])
# print(request_postcode.json()["result"]["latitude"])


def check_postcode(postcode):
    request_postcode = requests.get(url + postcode)
    if request_postcode.status_code == 200:
        return True
    else:
        return False


def getURL(postcode):
    if check_postcode(postcode):
        request_postcode = requests.get(url + postcode)
        return request_postcode
    else:
        return "The postcode is not valid"


def get_postcode_info(postcode):
    request_postcode = getURL(postcode)
    
    if request_postcode.status_code == 200:
        print(request_postcode.json()["result"]["postcode"])
        print(request_postcode.json()["result"]["longitude"])
        print(request_postcode.json()["result"]["latitude"])
        print(request_postcode.json()["result"]["region"])
    else:
        print("The postcode is not valid")
