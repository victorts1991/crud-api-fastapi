from fastapi import FastAPI
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI(
    title = 'My FastAPI API',
    version = '1.0.0',
    description = 'Api de exemplo com FastAPI'
)

# Banco de dados de usuários em memória para autenticação
users = {
    "user1": "password1",
    "user2": "password2"
}

security = HTTPBasic()

def verify_password(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password
    if username in users and users[username] == password:
        return username
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais inválidas",
        headers={"WWW-Authenticate": "Basic"}
    )

@app.get('/')
async def home(username: str = Depends(verify_password)):
    return 'Hello World!'