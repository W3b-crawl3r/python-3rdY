from datetime import datetime
from fastapi import FastAPI
#web server : running of my app
import uvicorn

#implement web service /REST using fast api

app=FastAPI()

@app.get("/date")
def now():
    return datetime.now()

if __name__ == '__main__':
    uvicorn.run("test_api:app")



