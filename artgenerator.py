import requests
from PIL import Image
from io import BytesIO

apitoken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjEwMDNkMjNjNmEyMmNiNzY4YWY5MDNhMTJlOWNmN2JmIiwiY3JlYXRlZF9hdCI6IjIwMjUtMDYtMTBUMDM6MzQ6MzEuOTYyNTM0In0.s7NhvDsBUaMzA_eoNIh9kV-kIdh4cE3rSFb3IBDC6VM"
print("Welcome to AI art lab")
userinput = input("Enter your image prompt: ")
url = "https://api.monsterapi.ai/v1/generate/txt2img"
headers = {"Authorization": f"Bearer {apitoken}"}
response = requests.post(url, json={"prompt": userinput, "safe_filter": True}, headers=headers)

if response.status_code == 200:
    print("Loading...")
    processid = response.json().get("process_id")

    while True:
        statusdata = requests.get(f"https://api.monsterapi.ai/v1/status/{processid}", headers=headers).json()
        status = statusdata.get("status")

        if status == "COMPLETED":
            imageurl = statusdata['result']['output'][0]
            img = Image.open(BytesIO(requests.get(imageurl).content))
            img.show()
            print()
            break
        elif status == "FAILED":
            print("Image generation failed")
            break
else:
    print(f"Error: {response.status_code}")