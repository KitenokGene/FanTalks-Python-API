import requests, json

class FanTalksAPI:
    def __init__(self, token):
        self.token = token
        self.headers = {"authorization": f"Bearer {token}"}
    
    def getUnansweredDonates(self):
        kek = requests.get("https://www.donationalerts.com/api/v1/askmequestion?statuses[]=unanswered&page=1", headers=self.headers)
        jsonParty = json.loads(kek.content.decode("UTF-8"))
        return jsonParty["data"]
    
    def getAllDonates(self):
        kek = requests.get("https://www.donationalerts.com/api/v1/askmequestion", headers=self.headers)
        jsonParty = json.loads(kek.content.decode("UTF-8"))
        return jsonParty["data"]
    
    # soon: answerToDonate, createDonate, getCategories, createCategory, ...


# example using
app = FanTalksAPI("your token")
for item in app.getUnansweredDonates():
    donationUsername = item["inquirer"]["name"]
    donationText = item["content"]
    donateCost = item["cost"]
    currency = item["cost_currency"]
    print(f"{donationUsername} > {donationText} ({donateCost} {currency})")