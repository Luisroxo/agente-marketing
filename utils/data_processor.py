"""
Processador de Dados - Utilitário para limpeza e preparação de dados
"""
import pandas as pd
import numpy as np
from typing import Optional, Dict, List, Tuple

class DataProcessor:
    """Classe para processamento e limpeza de dados"""
    
    def __init__(self):
        self.data = None
        self.original_data = None
        
    def load_data(self, file_path: str) -> pd.DataFrame:
        """Carregar dados de arquivo"""
        try:
            if file_path.endswith('.csv'):
                self.data = pd.read_csv(file_path)
            elif file_path.endswith(('.xlsx', '.xls')):
                self.data = pd.read_excel(file_path)
            else:
                raise ValueError("Formato de arquivo não suportado")
            
            self.original_data = self.data.copy()
            return self.data
            
        except Exception as e:
            raise Exception(f"Erro ao carregar dados: {str(e)}")
    
    def clean_data(self, df: Optional[pd.DataFrame] = None) -> pd.DataFrame:
        """Limpeza básica dos dados"""
        if df is None:
            df = self.data.copy()
        
        # Remover linhas completamente vazias
        df = df.dropna(how='all')
        
        # Remover colunas completamente vazias
        df = df.dropna(axis=1, how='all')
        
        # Padronizar nomes das colunas
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
        
        # Remover espaços em branco extras em colunas de texto
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].astype(str).str.strip()
        
        return df
    
    def detect_column_types(self, df: Optional[pd.DataFrame] = None) -> Dict[str, List[str]]:
        """Detectar tipos de colunas automaticamente"""
        if df is None:
            df = self.data
        
        column_types = {
            'numeric': [],
            'categorical': [],
            'text': [],
            'datetime': [],
            'binary': []
        }
        
        for col in df.columns:
            # Verificar se é numérico
            if pd.api.types.is_numeric_dtype(df[col]):
                column_types['numeric'].append(col)
            
            # Verificar se é categoria (poucos valores únicos)
            elif df[col].nunique() <= 10 and df[col].nunique() / len(df) < 0.5:
                column_types['categorical'].append(col)
            
            # Verificar se é binário (sim/não, verdadeiro/falso, etc.)
            elif df[col].nunique() == 2:
                column_types['binary'].append(col)
            
            # Verificar se pode ser datetime
            elif self._is_datetime_column(df[col]):
                column_types['datetime'].append(col)
            
            # Caso contrário, é texto
            else:
                column_types['text'].append(col)
        
        return column_types
    
    def _is_datetime_column(self, series: pd.Series) -> bool:
        """Verificar se uma coluna pode ser datetime"""
        try:
            pd.to_datetime(series.dropna().head(10))
            return True
        except:
            return False
    
    def get_data_summary(self, df: Optional[pd.DataFrame] = None) -> Dict:
        """Obter resumo dos dados"""
        if df is None:
            df = self.data
        
        summary = {
            'total_rows': len(df),
            'total_columns': len(df.columns),
            'missing_values': df.isnull().sum().sum(),
            'missing_percentage': (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100,
            'duplicate_rows': df.duplicated().sum(),
            'memory_usage': df.memory_usage(deep=True).sum() / 1024**2,  # MB
            'column_types': self.detect_column_types(df)
        }
        
        return summary
    
    def standardize_text_responses(self, df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        """Padronizar respostas de texto comum"""
        standardization_map = {
            # Sim/Não variations
            'sim': ['sim', 'yes', 's', 'si', 'verdadeiro', 'true', '1'],
            'não': ['não', 'nao', 'no', 'n', 'falso', 'false', '0'],
            
            # Qualidade variations  
            'excelente': ['excelente', 'excellent', 'ótimo', 'otimo', 'perfeito'],
            'bom': ['bom', 'good', 'bem', 'ok', 'okay'],
            'regular': ['regular', 'average', 'médio', 'medio', 'normal'],
            'ruim': ['ruim', 'bad', 'péssimo', 'pessimo', 'terrível', 'terrivel']
        }
        
        df_clean = df.copy()
        
        for col in columns:
            if col in df_clean.columns:
                for standard, variations in standardization_map.items():
                    mask = df_clean[col].str.lower().isin(variations)
                    df_clean.loc[mask, col] = standard
        
        return df_clean
    
    def encode_categorical_variables(self, df: pd.DataFrame, columns: List[str]) -> Tuple[pd.DataFrame, Dict]:
        """Codificar variáveis categóricas"""
        df_encoded = df.copy()
        encoding_maps = {}
        
        for col in columns:
            if col in df_encoded.columns:
                # Criar mapeamento
                unique_values = df_encoded[col].dropna().unique()
                encoding_map = {value: idx for idx, value in enumerate(unique_values)}
                encoding_maps[col] = encoding_map
                
                # Aplicar codificação
                df_encoded[f'{col}_encoded'] = df_encoded[col].map(encoding_map)
        
        return df_encoded, encoding_maps