"""
Arquivo migrado de utils/helpers.py.
Funções utilitárias para processamento de dados.
"""
from src.services.logging_config import get_logger
logger = get_logger(__name__)

def exemplo_utilitario():
    """Exemplo de função utilitária com tratamento de erro padronizado."""
    try:
        # ... lógica da função ...
        pass
    except Exception as e:
        logger.error(f"Erro em exemplo_utilitario: {e}")
        raise
