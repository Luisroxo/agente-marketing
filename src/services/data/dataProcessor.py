"""
DataProcessor Moderno - Serviço de Processamento de Dados
Estrutura enterprise para o Agente Marketing IA
"""
import pandas as pd
import numpy as np
from typing import Optional, Dict, List, Tuple, Any
import streamlit as st
from io import StringIO
import logging

logger = logging.getLogger(__name__)

class DataProcessor:
    """
    Serviço moderno para processamento e limpeza de dados
    Versão enterprise com melhor estrutura e error handling
    """
    
    def __init__(self):
        self.data: Optional[pd.DataFrame] = None
        self.original_data: Optional[pd.DataFrame] = None
        self.metadata: Dict[str, Any] = {}
        
    def load_csv_data(self, uploaded_file) -> pd.DataFrame:
        """
        Carregar dados de arquivo CSV do Streamlit
        
        Args:
            uploaded_file: Arquivo carregado via st.file_uploader
            
        Returns:
            DataFrame com os dados carregados
        """
        try:
            # Converter para string se necessário
            if hasattr(uploaded_file, 'getvalue'):
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                self.data = pd.read_csv(stringio)
            else:
                self.data = pd.read_csv(uploaded_file)
            
            self.original_data = self.data.copy()
            self._update_metadata()
            
            logger.info(f"Dados carregados: {len(self.data)} linhas, {len(self.data.columns)} colunas")
            return self.data
            
        except Exception as e:
            logger.error(f"Erro ao carregar CSV: {str(e)}")
            raise Exception(f"Erro ao carregar dados: {str(e)}")
    
    def load_excel_data(self, uploaded_file, sheet_name: str = None) -> pd.DataFrame:
        """
        Carregar dados de arquivo Excel
        
        Args:
            uploaded_file: Arquivo carregado
            sheet_name: Nome da planilha (opcional)
            
        Returns:
            DataFrame com os dados carregados
        """
        try:
            self.data = pd.read_excel(uploaded_file, sheet_name=sheet_name)
            self.original_data = self.data.copy()
            self._update_metadata()
            
            logger.info(f"Excel carregado: {len(self.data)} linhas, {len(self.data.columns)} colunas")
            return self.data
            
        except Exception as e:
            logger.error(f"Erro ao carregar Excel: {str(e)}")
            raise Exception(f"Erro ao carregar Excel: {str(e)}")
    
    def clean_data(self, df: Optional[pd.DataFrame] = None) -> pd.DataFrame:
        """
        Limpeza avançada dos dados
        
        Args:
            df: DataFrame para limpar (usa self.data se None)
            
        Returns:
            DataFrame limpo
        """
        if df is None:
            df = self.data.copy()
        
        original_shape = df.shape
        
        # Remover linhas completamente vazias
        df = df.dropna(how='all')
        
        # Remover colunas completamente vazias
        df = df.dropna(axis=1, how='all')
        
        # Padronizar nomes das colunas
        df.columns = self._standardize_column_names(df.columns)
        
        # Limpeza de strings
        df = self._clean_string_columns(df)
        
        # Remover duplicatas
        df = df.drop_duplicates()
        
        # Log das mudanças
        new_shape = df.shape
        logger.info(f"Limpeza completa: {original_shape} -> {new_shape}")
        
        return df
    
    def _standardize_column_names(self, columns: pd.Index) -> List[str]:
        """Padronizar nomes das colunas"""
        standardized = []
        for col in columns:
            # Converter para string e limpar
            clean_col = str(col).strip().lower()
            # Remover caracteres especiais e substituir espaços
            clean_col = clean_col.replace(' ', '_').replace('-', '_')
            # Remover caracteres não alfanuméricos (exceto _)
            clean_col = ''.join(c for c in clean_col if c.isalnum() or c == '_')
            standardized.append(clean_col)
        return standardized
    
    def _clean_string_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Limpar colunas de texto"""
        for col in df.select_dtypes(include=['object']).columns:
            # Remover espaços extras
            df[col] = df[col].astype(str).str.strip()
            # Substituir strings vazias por NaN
            df[col] = df[col].replace('', np.nan)
        return df
    
    def detect_column_types(self, df: Optional[pd.DataFrame] = None) -> Dict[str, List[str]]:
        """
        Detectar tipos de colunas automaticamente
        
        Args:
            df: DataFrame para analisar
            
        Returns:
            Dicionário com tipos de colunas categorizados
        """
        if df is None:
            df = self.data
        
        column_types = {
            'numeric': [],
            'categorical': [],
            'text': [],
            'datetime': [],
            'binary': [],
            'id': []
        }
        
        for col in df.columns:
            col_data = df[col].dropna()
            
            # ID columns (muitos valores únicos)
            if col_data.nunique() / len(col_data) > 0.95:
                column_types['id'].append(col)
            
            # Numeric columns
            elif pd.api.types.is_numeric_dtype(df[col]):
                column_types['numeric'].append(col)
            
            # Binary columns (exactly 2 unique values)
            elif col_data.nunique() == 2:
                column_types['binary'].append(col)
            
            # Categorical columns (few unique values)
            elif col_data.nunique() <= 10 and col_data.nunique() / len(col_data) < 0.5:
                column_types['categorical'].append(col)
            
            # DateTime columns
            elif self._is_datetime_column(col_data):
                column_types['datetime'].append(col)
            
            # Text columns
            else:
                column_types['text'].append(col)
        
        return column_types
    
    def _is_datetime_column(self, series: pd.Series) -> bool:
        """Verificar se uma coluna pode ser datetime"""
        try:
            # Testar com uma amostra pequena
            sample = series.head(min(10, len(series)))
            pd.to_datetime(sample, errors='raise')
            return True
        except:
            return False
    
    def get_data_summary(self, df: Optional[pd.DataFrame] = None) -> Dict[str, Any]:
        """
        Obter resumo detalhado dos dados
        
        Args:
            df: DataFrame para analisar
            
        Returns:
            Dicionário com resumo completo
        """
        if df is None:
            df = self.data
        
        column_types = self.detect_column_types(df)
        
        summary = {
            'basic_info': {
                'total_rows': len(df),
                'total_columns': len(df.columns),
                'memory_usage': df.memory_usage(deep=True).sum(),
                'missing_values': df.isnull().sum().sum(),
                'missing_percentage': (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
            },
            'column_types': column_types,
            'data_quality': self._assess_data_quality(df),
            'statistical_summary': self._get_statistical_summary(df)
        }
        
        return summary
    
    def _assess_data_quality(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Avaliar qualidade dos dados"""
        quality = {
            'completeness': (1 - df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100,
            'uniqueness': df.nunique().sum() / len(df),
            'consistency': self._check_consistency(df),
            'duplicates': df.duplicated().sum()
        }
        return quality
    
    def _check_consistency(self, df: pd.DataFrame) -> float:
        """Verificar consistência dos dados"""
        # Implementação básica - pode ser expandida
        consistent_score = 100.0
        
        # Verificar formatos inconsistentes em colunas de texto
        for col in df.select_dtypes(include=['object']).columns:
            if df[col].dtype == 'object':
                # Verificar se há mistura de maiúsculas/minúsculas
                if df[col].nunique() != df[col].str.lower().nunique():
                    consistent_score -= 5
        
        return max(0, consistent_score)
    
    def _get_statistical_summary(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Obter resumo estatístico"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        if len(numeric_cols) > 0:
            return {
                'numeric_summary': df[numeric_cols].describe().to_dict(),
                'correlations': df[numeric_cols].corr().to_dict() if len(numeric_cols) > 1 else {}
            }
        
        return {'numeric_summary': {}, 'correlations': {}}
    
    def _update_metadata(self):
        """Atualizar metadados"""
        if self.data is not None:
            self.metadata = {
                'last_updated': pd.Timestamp.now(),
                'shape': self.data.shape,
                'columns': list(self.data.columns),
                'dtypes': self.data.dtypes.to_dict()
            }
    
    def get_sample_data(self, n: int = 1000) -> pd.DataFrame:
        """
        Obter amostra dos dados para processamento rápido
        
        Args:
            n: Número de linhas da amostra
            
        Returns:
            DataFrame com amostra dos dados
        """
        if self.data is None:
            return pd.DataFrame()
        
        if len(self.data) <= n:
            return self.data.copy()
        
        return self.data.sample(n=n, random_state=42)