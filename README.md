# Sneakers Online MX - E-commerce Seguro Enterprise
![Banner](IMG-20261017-WA3432.jpg)
![WAF](https://img.shields.io/badge/WAF-Activo-green)
![Stack](https://img.shields.io/badge/Python%2BSwift-FastAPI-blue)
![MX](https://img.shields.io/badge/Focus-Mexico-red)

**Autor:** Giovani Martinez Guzman | Ecatepec, MX | Fibotech
**Live Demo:** Localhost:8000 | **WAF:** ANTI-SUPLANTACIÓN TOTAL

E-commerce de sneakers con blindaje anti-fraude para México. No es solo tienda, es tienda **segura**.

### 🚀 Qué lo hace PRO
- **WAF Defensivo:** Detecta faceb00k, xn--, bbva.mx@phishing
- **Checkout Seguro:** CURP/RFC, 3D Secure, no guarda tarjetas - LFPDPPP
- **Backend:** FastAPI + scoring 0-100
- **Seguridad MX:** Headers `X-WAF-By: Giovani-Martinez`

### 🛠️ Quick Start
```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
# Docs en http://localhost:8000/docs
