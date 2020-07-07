#3rd iteraction - create same functionality with OOP - class and a method
#create a method called check_status_code():
#create a class live_web_status_code:
#out put should be the same as we achieved without OOP.

import requests

class live_web_status_code:

    def check_status_code():

        post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
        if post_codes_req.status_code:
            print("success")

        elif post_codes_req.status_code:
            print("sorry page not available")
            return

print(live_web_status_code.check_status_code())