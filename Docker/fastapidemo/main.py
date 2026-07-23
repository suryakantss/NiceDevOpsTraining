from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/products")
def products():
    return [
        {"id": "P1", "name": "Mouse", "price": "500"},
        {"id": "P2", "name": "Pen", "price": "100"}
        ]
