import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

print("Enter the Place detais")
x = input()

querystring = {"q":x}

headers = {
	"X-RapidAPI-Key": "622f43aa87mshf3fbb459ef3b059p16f66fjsnbb7a12a55c94",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

res = response.json()
final = {}
for key,value in res.items():
    if(key == 'location'):
        details = value
        for i in range(len(value)):
            final = value
            break
        for key,value in final.items():
            print(key, '.....', value)

cur = res['current']
for key,value in cur.items():
    if(key=='condition'):
        new = value
        for key,value in new.items():
            print(key, '.....', value)
            continue
    print(key, '.....', value)