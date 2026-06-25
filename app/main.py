from fastapi import FastAPI

app = FastAPI(
    title="My Azure API",
    description="A FastAPI application deployed on Azure App Service",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "FastAPI is running on Azure App Service",
    }


@app.get("/helloworld")
def hello_world():
    return {"message": "Hello World!"}
