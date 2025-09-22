"""
Utilitários gerais do projeto
"""
import pandas as pd
import streamlit as st
from typing import Optional, Dict, List, Any
import logging
from datetime import datetime

def setup_logging():
    """Configurar logging do projeto"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('agente_marketing.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def validate_dataframe(df: pd.DataFrame) -> Dict[str, Any]:
    """Validar DataFrame carregado"""
    validation_results = {
        "is_valid": True,
        "errors": [],
        "warnings": [],
        "info": {}
    }
    
    # Verificar se não está vazio
    if df.empty:
        validation_results["is_valid"] = False
        validation_results["errors"].append("DataFrame está vazio")
        return validation_results
    
    # Informações básicas
    validation_results["info"] = {
        "rows": len(df),
        "columns": len(df.columns),
        "memory_usage_mb": df.memory_usage(deep=True).sum() / 1024**2,
        "missing_percentage": (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
    }
    
    # Verificações de qualidade
    if len(df) < 10:
        validation_results["warnings"].append("Amostra muito pequena (< 10 registros)")
    
    if validation_results["info"]["missing_percentage"] > 50:
        validation_results["warnings"].append("Muitos dados faltantes (> 50%)")
    
    # Verificar colunas duplicadas
    if df.columns.duplicated().any():
        validation_results["warnings"].append("Colunas duplicadas encontradas")
    
    # Verificar linhas completamente duplicadas
    duplicated_rows = df.duplicated().sum()
    if duplicated_rows > 0:
        validation_results["warnings"].append(f"{duplicated_rows} linhas duplicadas encontradas")
    
    return validation_results

def format_number(number: float, decimals: int = 2) -> str:
    """Formatar números para exibição"""
    if pd.isna(number):
        return "N/A"
    
    if abs(number) >= 1_000_000:
        return f"{number/1_000_000:.{decimals}f}M"
    elif abs(number) >= 1_000:
        return f"{number/1_000:.{decimals}f}K"
    else:
        return f"{number:.{decimals}f}"

def format_percentage(value: float, decimals: int = 1) -> str:
    """Formatar percentuais"""
    if pd.isna(value):
        return "N/A"
    return f"{value:.{decimals}f}%"

def create_download_link(content: str, filename: str, label: str = "Download"):
    """Criar link de download para conteúdo texto"""
    import base64
    
    b64 = base64.b64encode(content.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">{label}</a>'
    return href

def safe_division(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Divisão segura evitando divisão por zero"""
    try:
        if denominator == 0:
            return default
        return numerator / denominator
    except (TypeError, ZeroDivisionError):
        return default

def detect_encoding(file_path: str) -> str:
    """Detectar encoding de arquivo"""
    import chardet
    
    try:
        with open(file_path, 'rb') as file:
            raw_data = file.read(10000)  # Ler primeiros 10KB
            result = chardet.detect(raw_data)
            return result['encoding'] or 'utf-8'
    except:
        return 'utf-8'

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Limpar nomes das colunas"""
    df_clean = df.copy()
    
    # Remover espaços e caracteres especiais
    df_clean.columns = (df_clean.columns
                       .str.strip()
                       .str.lower()
                       .str.replace(' ', '_')
                       .str.replace('[^a-zA-Z0-9_]', '', regex=True))
    
    # Evitar nomes vazios
    for i, col in enumerate(df_clean.columns):
        if col == '' or col is None:
            df_clean.columns.values[i] = f'coluna_{i}'
    
    return df_clean

def get_memory_usage(df: pd.DataFrame) -> Dict[str, str]:
    """Obter uso de memória do DataFrame"""
    memory_usage = df.memory_usage(deep=True)
    
    return {
        "total": format_bytes(memory_usage.sum()),
        "per_column": {col: format_bytes(usage) 
                      for col, usage in memory_usage.items()}
    }

def format_bytes(bytes_value: int) -> str:
    """Formatar bytes para leitura humana"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.1f} {unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.1f} TB"

def generate_sample_data() -> pd.DataFrame:
    """Gerar dados de exemplo para demonstração"""
    import numpy as np
    
    np.random.seed(42)  # Para reprodutibilidade
    
    n_samples = 100
    
    # Dados demográficos
    idades = np.random.normal(35, 10, n_samples).astype(int)
    idades = np.clip(idades, 18, 70)
    
    generos = np.random.choice(['Masculino', 'Feminino', 'Outro'], n_samples, p=[0.45, 0.50, 0.05])
    
    cidades = np.random.choice([
        'São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília', 
        'Salvador', 'Curitiba', 'Recife', 'Porto Alegre'
    ], n_samples, p=[0.25, 0.15, 0.12, 0.10, 0.10, 0.10, 0.08, 0.10])
    
    # Dados de comportamento
    satisfacao = np.random.choice(range(1, 11), n_samples, p=[0.02, 0.03, 0.05, 0.08, 0.12, 0.15, 0.20, 0.15, 0.12, 0.08])
    
    recomendaria = np.random.choice(['Sim', 'Não', 'Talvez'], n_samples, p=[0.6, 0.2, 0.2])
    
    interesses = np.random.choice([
        'Tecnologia', 'Esportes', 'Música', 'Viagem', 'Culinária', 
        'Moda', 'Livros', 'Cinema', 'Jogos', 'Arte'
    ], n_samples)
    
    # Frequência de uso
    frequencia = np.random.choice([
        'Diariamente', 'Semanalmente', 'Mensalmente', 'Raramente', 'Nunca'
    ], n_samples, p=[0.3, 0.35, 0.20, 0.10, 0.05])
    
    # Criar DataFrame
    sample_data = pd.DataFrame({
        'idade': idades,
        'genero': generos,
        'cidade': cidades,
        'satisfacao': satisfacao,
        'recomendaria': recomendaria,
        'interesse_principal': interesses,
        'frequencia_uso': frequencia,
        'data_resposta': pd.date_range('2024-01-01', periods=n_samples, freq='D')[:n_samples]
    })
    
    return sample_data

def show_dataframe_info(df: pd.DataFrame, title: str = "Informações do DataFrame"):
    """Mostrar informações detalhadas do DataFrame no Streamlit"""
    st.subheader(title)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Linhas", len(df))
    
    with col2:
        st.metric("Colunas", len(df.columns))
    
    with col3:
        missing_pct = (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
        st.metric("Dados Faltantes", f"{missing_pct:.1f}%")
    
    with col4:
        duplicates = df.duplicated().sum()
        st.metric("Duplicados", duplicates)
    
    # Informações detalhadas das colunas
    if st.expander("Detalhes das Colunas"):
        col_info = pd.DataFrame({
            'Tipo': df.dtypes,
            'Valores Únicos': [df[col].nunique() for col in df.columns],
            'Nulos': df.isnull().sum(),
            'Nulos (%)': (df.isnull().sum() / len(df) * 100).round(2)
        })
        st.dataframe(col_info)

def export_to_excel(dfs: Dict[str, pd.DataFrame], filename: str = "relatorio_dados.xlsx"):
    """Exportar múltiplos DataFrames para Excel"""
    import io
    
    output = io.BytesIO()
    
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        for sheet_name, df in dfs.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    return output.getvalue()

class DataQualityChecker:
    """Verificador de qualidade de dados"""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.quality_score = 0
        self.issues = []
        self.recommendations = []
    
    def check_quality(self) -> Dict[str, Any]:
        """Verificar qualidade geral dos dados"""
        self._check_completeness()
        self._check_consistency()
        self._check_uniqueness()
        self._check_validity()
        
        return {
            "quality_score": self.quality_score,
            "issues": self.issues,
            "recommendations": self.recommendations
        }
    
    def _check_completeness(self):
        """Verificar completude dos dados"""
        missing_pct = (self.df.isnull().sum().sum() / (len(self.df) * len(self.df.columns))) * 100
        
        if missing_pct < 5:
            self.quality_score += 25
        elif missing_pct < 15:
            self.quality_score += 15
            self.issues.append(f"Dados faltantes moderados: {missing_pct:.1f}%")
        else:
            self.quality_score += 5
            self.issues.append(f"Muitos dados faltantes: {missing_pct:.1f}%")
            self.recommendations.append("Melhorar processo de coleta de dados")
    
    def _check_consistency(self):
        """Verificar consistência dos dados"""
        # Verificar tipos de dados inconsistentes
        inconsistent_cols = 0
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                # Verificar se coluna numérica foi tratada como texto
                try:
                    pd.to_numeric(self.df[col].dropna())
                    inconsistent_cols += 1
                except:
                    pass
        
        if inconsistent_cols == 0:
            self.quality_score += 25
        else:
            self.quality_score += 10
            self.issues.append(f"{inconsistent_cols} colunas com tipos inconsistentes")
            self.recommendations.append("Padronizar tipos de dados")
    
    def _check_uniqueness(self):
        """Verificar duplicação"""
        duplicate_pct = (self.df.duplicated().sum() / len(self.df)) * 100
        
        if duplicate_pct == 0:
            self.quality_score += 25
        elif duplicate_pct < 5:
            self.quality_score += 15
            self.issues.append(f"Poucos duplicados: {duplicate_pct:.1f}%")
        else:
            self.quality_score += 5
            self.issues.append(f"Muitos duplicados: {duplicate_pct:.1f}%")
            self.recommendations.append("Implementar validação de duplicados")
    
    def _check_validity(self):
        """Verificar validade dos dados"""
        # Verificações básicas de validade
        valid_score = 25
        
        # Verificar outliers extremos em colunas numéricas
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        outlier_cols = 0
        
        for col in numeric_cols:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            outliers = self.df[(self.df[col] < Q1 - 3*IQR) | (self.df[col] > Q3 + 3*IQR)]
            
            if len(outliers) > len(self.df) * 0.1:  # Mais de 10% outliers
                outlier_cols += 1
        
        if outlier_cols > 0:
            valid_score -= outlier_cols * 5
            self.issues.append(f"{outlier_cols} colunas com muitos outliers")
            self.recommendations.append("Investigar e tratar outliers")
        
        self.quality_score += max(valid_score, 5)