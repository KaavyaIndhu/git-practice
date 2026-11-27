transactions=[
    { "id": 1,"amount": 100, "country" : "INDIA", "is_new_device" : True},
    {"id": 2, "amount":200, "country": "USA", "is_new_device":False},
    {"id": 3, "amount":300, "country": "CANADA", "is_new_device":True},
    {"id": 4, "amount":400, "country": "INDIA", "is_new_device":False}
]

def risk_score(t):
    score=0
    if t["amount"]>100000:
        score+=50
    if t["country"] !="INDIA":
        score+=30
    if t["is_new_device"]:
        score+=20
    return score

def risk_score1(txn):
    score = risk_score(txn)
    if score>=60:
        return "HIGH"
    elif score<60 and score>=30:
        return "MEDIUM"
    else:
        return "LOW"

for t in transactions:
    print(f"Transaction {t['id']}: score {risk_score(t)} -> {risk_score1(t)}")

    