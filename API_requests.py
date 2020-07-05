import requests

class website_check:
    def check_response_code():
        response_fb = requests.get("https://www.facebook.com/")
        if response_fb.status_code == 200:
            print("The page has been loaded successfully")
        elif response_fb.status_code == 400:
            print("Page not found")
        elif response_fb.status_code == 404:
            print("Something has gone wrong")
        else:
            pass
        print(response_fb.status_code)
        print(response_fb.headers)
        print(response_fb.content)

website_check.check_response_code()
