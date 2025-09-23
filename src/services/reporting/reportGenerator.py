"""
Arquivo migrado de templates/report_generator.py.
Funções utilitárias para geração de relatórios.
"""
from src.services.logging_config import get_logger
logger = get_logger(__name__)


def exemplo_gerador():
    """Exemplo de função utilitária com tratamento de erro padronizado."""
    try:
        # ... lógica da função ...
        pass
    except Exception as e:
        logger.error(f"Erro em exemplo_gerador: {e}")
        raise
