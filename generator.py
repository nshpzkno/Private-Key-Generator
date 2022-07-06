# PREMIUM LINK GENERATOR


import requests


link=open(r"links.txt").readlines() # file with non-premium links

URL= 'https://api.leechersparadise.com/link'
e=0

counter=0

for i in range (len(link)):
    DATA = {"downloadLink":link[counter],"apiKey":"FBB234HFFJDSFD&&D2C25AD4","user":"true"}
    e=0
    HEADERS = {
        'Content-Type': 'application/json',
    }

    response = requests.post(url=URL, headers=HEADERS, json=DATA)
    with open(r"premium.txt", "a") as f: # file with premium links
        f.write(response.json()['premiumLink']+'\n')
        counter+=1