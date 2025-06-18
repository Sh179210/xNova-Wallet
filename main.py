from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def home():
    return {'msg': 'Welcome to xNova Wallet!'}