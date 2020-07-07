import requests
import json
post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
print(post_codes_req.status_code)
print(post_codes_req.content)
print(post_codes_req.headers)

print(post_codes_req.status_code)
print(type(post_codes_req.headers))
print(post_codes_req)


#Why should we use built in packages
# first iteraction
if post_codes_req.status_code == 200:
    print("success")

elif post_codes_req.status_code == 400:
    print("sorry page not available")

#second iteraction
if post_codes_req.status_code:
    print("success")

elif post_codes_req.status_code:
    print("sorry page not available")

print(post_codes_req.json())
json_data = post_codes_req.json()

for key in json_data:
    print(key)

print(json_data)



for list in key[0:6]:
    print(list)