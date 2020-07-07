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

# Exercise is to fetch data by key value pairs within dictionaries
# Create a function to return the above values (Key:value)
# Create a class and move the code inside the class
json_data = post_codes_req.json()

class get_json:
    #this method retrieves all the values
    def get_all_values(self, nested_dictionary):
        #for loop goes through the key:value pairs
        for key, value in nested_dictionary.items(): #.items retrieves all the key values pairs if there is a nested dictionary
            if type(value) is dict:   # if the value of a key is a dictionary, then you have found a nested dictionary
                self.get_all_values(value) # recall this method passing in that dictionary to iterate through it
            else:
                print(key, ":", value) # if the value of the dictionary is not a dict carry on looping through


json_reader = get_json() # Create instance of this function
json_reader.get_all_values(json_data)  # Returns all the values inside a dictionary including any nested dictionaries








