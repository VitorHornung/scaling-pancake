from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 127.0.0.1:8000//teste
@app.get("/teste")
async def funcaoteste():
    return {"teste": "deu certo"}
