from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "API123456"}

@app.get("/abc")
def abc():
    return {"Hello": "abc"}

@app.get("/xyz")
def xyz():
    return 123