from fastapi import FastAPI

app = FastAPI(
    title = 'My FastAPI API',
    version = '1.0.0',
    description = 'Api de exemplo com FastAPI'
)

@app.get('/')
async def home():
    return 'Hello World!'