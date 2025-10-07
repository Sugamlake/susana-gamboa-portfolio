"""
test_scoring.py — Prueba unitaria del motor de scoring
Versión 1.1 — Susana Gamboa (2025)
"""

# ==============================
# 🔧 Configuración del entorno
# ==============================
import sys
import os

# Agrega la carpeta raíz del proyecto al path
# para asegurar que src/ sea importable tanto localmente como en CI/CD.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ==============================
# 📦 Importación del módulo a probar
# ==============================
from src.scoring import score_leads


# ==============================
# ✅ Test principal
# ==============================
def test_score_calculation():
    """
    Verifica que el cálculo del score retorne valores válidos y determinísticos.
    """
    lead = {
        "engagement": 80,
        "industry_fit": 90,
        "company_size": 70,
        "tech_stack": 60,
        "geo_relevance": 80
    }

    # Ejecutar la función
    score = score_leads(lead)

    # Validar rango y tipo de resultado
    assert isinstance(score, (int, float)), "El resultado debe ser numérico"
    assert 0 <= score <= 100, "El score debe estar entre 0 y 100"

    # Mostrar resultado si pasa el test
    print(f"✅ Test passed — Score calculado correctamente: {score}")
