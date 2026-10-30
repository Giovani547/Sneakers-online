from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="STYLESAMERICAN - API Segura")

# Solo tu dominio puede hablarle a tu API, no todo el internet
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://sneakers-online-theta.vercel.app"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "STYLESAMERICAN API - WAF Activo", "checkout": "via WhatsApp"}

@app.get("/api/sneakers")
async def listar():
    return {"aviso": "Todo cierre es por WhatsApp 56 3636 4852"}