import pytest
from services.analysis.statistical_analysis import exemplo_analise

def test_exemplo_analise():
    # Apenas verifica se a função executa sem erro
    try:
        exemplo_analise()
    except Exception:
        pytest.fail("exemplo_analise levantou exceção inesperada")
