import requests

class PostcodeDetails:
    def __init__(self, postcode):
        self.postcode = postcode
        self.url = "https://api.postcodes.io/postcodes/"
        self.newURL = self.url + self.postcode
        self.request_postcode = requests.get(self.url + self.postcode)
        self.status_code = self.request_postcode.status_code
        self.all = self.request_postcode.json()
        self.postcode = self.request_postcode.json()["result"]["postcode"]
        self.longitude = self.request_postcode.json()["result"]["longitude"]
        self.latitude = self.request_postcode.json()["result"]["latitude"]
        self.region = self.request_postcode.json()["result"]["region"]
        
    def check_postcode(self):
        if self.status_code == 200:
            return True
        else:
            return False
    
    def get_postcode(self):
        if self.check_postcode():
            return self.postcode
        else:
            print("The postcode is not valid")
    
    def get_latitude(self):
        if self.check_postcode():
            return self.latitude
        else:
            print("The postcode is not valid")
            
    def get_longitude(self):
        if self.check_postcode():
            return self.longitude
        else:
            print("The postcode is not valid")
    
    def get_region(self):
        if self.check_postcode():
            return self.region
        else:
            print("The postcode is not valid")
    
    def get_newURL(self):
        return self.newURL
            
            
    def getAll(self):
        if self.check_postcode():
            for key, value in self.all.items():
                print(key, value)
        else:
            print("The postcode is not valid")