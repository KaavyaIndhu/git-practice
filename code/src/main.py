from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return {"message": "Hello from kaavya"}
@app.get("/health")
def health():
    return{"status":"ok"}
@app.get("/fee")
def fee(amount:float):
    return{"amount":amount, "fee": amount*0.02}

