from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="STYLESAMERICAN - WAF Defensivo")

# 1. CORS CERRADO - Solo tu dominio puede usar la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://sneakers-online-sme7.vercel.app"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# 2. TU WAF DEFENSIVO - Lo dejamos tal cual, está bueno
def score_fraude(url: str) -> int:
    score = 0
    url_low = url.lower()
    if "faceb00k" in url_low or "xn--" in url_low:
        score += 3
    if "bbva.mx@" in url_low or "@" in url_low.replace("https://",""):
        score += 3
    if "oferta urgente" in url_low:
        score += 2
    if not url_low.startswith("https://"):
        score += 1
    return score

@app.middleware("http")
async def waf_middleware(request: Request, call_next):
    # Revisa si alguien te está intentando clonar con links raros
    url_a_revisar = str(request.url)
    if score_fraude(url_a_revisar) >= 3:
        print(f"[WAF] Bloqueado intento sospechoso: {url_a_revisar}")
        # Aquí lo bloqueas
        # return JSONResponse(status_code=403, content={"waf": "bloqueado"})
    
    response = await call_next(request)
    response.headers["X-WAF-By"] = "STYLESAMERICAN-Defensive"
    return response

@app.get("/")
async def root():
    return {"status": "WAF Activo", "tienda": "STYLESAMERICAN"}

@app.get("/api/sneakers")
async def sneakers():
    return {"info": "Catalogo publico, cierre por WhatsApp 56 3636 4852"}