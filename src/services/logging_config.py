import logging
import sys

LOG_FORMAT = "[%(asctime)s] %(levelname)s [%(name)s]: %(message)s"
LOG_LEVEL = logging.INFO

# Configuração centralizada de logging para todo o projeto
logging.basicConfig(
    level=LOG_LEVEL,
    format=LOG_FORMAT,
    stream=sys.stdout
)

def get_logger(name: str) -> logging.Logger:
    """Obtém um logger já configurado para o projeto."""
    return logging.getLogger(name)
