"""
Configurações do projeto
"""
import os
from pathlib import Path

# Diretórios do projeto
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"
TEMPLATES_DIR = PROJECT_ROOT / "templates"

# Configurações da aplicação
APP_CONFIG = {
    "title": "Agente de IA para Marketing",
    "version": "1.0.0",
    "description": "Sistema inteligente para análise de dados e geração de planos de marketing",
    "max_file_size": 10 * 1024 * 1024,  # 10MB
    "supported_formats": [".csv", ".xlsx", ".xls"],
    "default_encoding": "utf-8"
}

# Configurações de análise
ANALYSIS_CONFIG = {
    "min_sample_size": 30,
    "correlation_threshold": 0.7,
    "outlier_method": "iqr",  # ou "zscore"
    "max_categories_display": 10,
    "missing_data_threshold": 20,  # percentual
}

# Configurações de NLP (para futuras implementações)
NLP_CONFIG = {
    "language": "pt",
    "sentiment_model": "transformers",
    "max_text_length": 1000,
    "min_text_length": 10
}

# Configurações de clustering (para futuras implementações)
CLUSTERING_CONFIG = {
    "default_clusters": 3,
    "max_clusters": 10,
    "min_cluster_size": 5,
    "algorithm": "kmeans"  # ou "hierarchical"
}

# APIs e integrações
API_CONFIG = {
    "google_sheets": {
        "scope": ["https://spreadsheets.google.com/feeds",
                 "https://www.googleapis.com/auth/drive"],
        "credentials_file": "credentials.json"
    },
    "openai": {
        "model": "gpt-3.5-turbo",
        "max_tokens": 1000,
        "temperature": 0.7
    }
}

# Configurações de export
EXPORT_CONFIG = {
    "report_formats": ["markdown", "docx", "pdf"],
    "default_format": "markdown",
    "include_charts": True,
    "chart_format": "png"
}