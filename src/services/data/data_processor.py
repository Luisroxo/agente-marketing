"""
DataProcessor Moderno - Serviço de Processamento de Dados
Estrutura enterprise para o Agente Marketing IA
"""
import pandas as pd
import numpy as np
from typing import Optional, Dict, List, Any
from io import StringIO
from src.services.logging_config import get_logger
import logging

logger = logging.getLogger(__name__)


class DataProcessor:
    def __init__(self):
        self.data: Optional[pd.DataFrame] = None
        self.original_data: Optional[pd.DataFrame] = None
        self.metadata: Dict[str, Any] = {}
        logger = get_logger(__name__)

    def load_csv_data(self, uploaded_file) -> pd.DataFrame:
        """
        Carrega dados de um arquivo CSV.
        """
        try:
            if hasattr(uploaded_file, 'getvalue'):
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                self.data = pd.read_csv(stringio)
            else:
                self.data = pd.read_csv(uploaded_file)
            self.original_data = self.data.copy()
            self._update_metadata()
            logger.info(
                "Dados carregados: %d linhas, %d colunas",
                len(self.data),
                len(self.data.columns)
            )
            return self.data
        except Exception as e:
            logger.error("Erro ao carregar CSV: %s", str(e))
            raise Exception(f"Erro ao carregar dados: {str(e)}")

    def load_excel_data(
            self,
            uploaded_file,
            sheet_name: str = None) -> pd.DataFrame:
        """
        Carrega dados de um arquivo Excel.
        """
        try:
            self.data = pd.read_excel(uploaded_file, sheet_name=sheet_name)
            self.original_data = self.data.copy()
            self._update_metadata()
            logger.info(
                "Excel carregado: %d linhas, %d colunas",
                len(self.data),
                len(self.data.columns)
            )
            return self.data
        except Exception as e:
            logger.error("Erro ao carregar Excel: %s", str(e))
            raise Exception(f"Erro ao carregar Excel: {str(e)}")

    def clean_data(self, df: Optional[pd.DataFrame] = None) -> pd.DataFrame:
        """
        Limpa e padroniza o DataFrame.
        """
        if df is None:
            df = self.data.copy()
        df = df.dropna(how='all')
        df = df.dropna(axis=1, how='all')
        df.columns = self._standardize_column_names(df.columns)
        df = self._clean_string_columns(df)
        df = df.drop_duplicates()
        logger.info(
            "Limpeza completa: %s linhas, %s colunas",
            df.shape[0],
            df.shape[1]
        )
        return df

    def _standardize_column_names(self, columns: pd.Index) -> List[str]:
        """Padroniza nomes das colunas."""
        return [
            ''.join(
                c for c in str(col)
                .strip()
                .lower()
                .replace(' ', '_')
                .replace('-', '_')
                if c.isalnum() or c == '_'
            )
            for col in columns
        ]

    def _clean_string_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Limpa colunas de texto."""
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].astype(str).str.strip()
            df[col] = df[col].replace('', np.nan)
        return df

    def detect_column_types(
            self, df: Optional[pd.DataFrame] = None) -> Dict[str, List[str]]:
        """
        Detecta tipos de colunas automaticamente.
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
            if len(col_data) == 0:
                continue
            if col_data.nunique() / len(col_data) > 0.95:
                column_types['id'].append(col)
            elif pd.api.types.is_numeric_dtype(df[col]):
                column_types['numeric'].append(col)
            elif col_data.nunique() == 2:
                column_types['binary'].append(col)
            elif (
                col_data.nunique() <= 10 and
                col_data.nunique() / len(col_data) < 0.5
            ):
                column_types['categorical'].append(col)
            elif self._is_datetime_column(col_data):
                column_types['datetime'].append(col)
            else:
                column_types['text'].append(col)
        return column_types

    def _is_datetime_column(self, series: pd.Series) -> bool:
        """Verifica se uma coluna pode ser datetime."""
        try:
            sample = series.head(min(10, len(series)))
            pd.to_datetime(sample, errors='raise')
            return True
        except Exception:
            return False

    def get_data_summary(
            self, df: Optional[pd.DataFrame] = None) -> Dict[str, Any]:
        """
        Retorna resumo detalhado dos dados.
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
                'missing_percentage': (
                    df.isnull().sum().sum() /
                    (len(df) * len(df.columns)) * 100
                ) if len(df) > 0 and len(df.columns) > 0 else 0.0
            },
            'column_types': column_types,
            'data_quality': self._assess_data_quality(df),
            'statistical_summary': self._get_statistical_summary(df)
        }
        return summary

    def _assess_data_quality(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Avalia qualidade dos dados."""
        total_cells = len(df) * len(df.columns)
        completeness = (
            1 - df.isnull().sum().sum() / total_cells
        ) * 100 if total_cells > 0 else 0.0
        quality = {
            'completeness': completeness,
            'uniqueness': df.nunique().sum() / len(df) if len(df) > 0 else 0.0,
            'consistency': self._check_consistency(df),
            'duplicates': df.duplicated().sum()
        }
        return quality

    def _check_consistency(self, df: pd.DataFrame) -> float:
        """Verifica consistência dos dados."""
        consistent_score = 100.0
        for col in df.select_dtypes(include=['object']).columns:
            if df[col].dtype == 'object':
                if df[col].nunique() != df[col].str.lower().nunique():
                    consistent_score -= 5
        return max(0, consistent_score)

    def _get_statistical_summary(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Retorna resumo estatístico."""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            return {
                'numeric_summary': df[numeric_cols].describe().to_dict(),
                'correlations': (
                    df[numeric_cols].corr().to_dict()
                    if len(numeric_cols) > 1 else {}
                )
                # Adiciona newline ao final do arquivo
            }
        return {'numeric_summary': {}, 'correlations': {}}

    def _update_metadata(self):
        """Atualiza metadados do DataFrame."""
        if self.data is not None:
            self.metadata = {
                'last_updated': pd.Timestamp.now(),
                'shape': self.data.shape,
                'columns': list(self.data.columns),
                'dtypes': self.data.dtypes.to_dict()
            }

    def get_sample_data(self, n: int = 1000) -> pd.DataFrame:
        """
        Retorna uma amostra dos dados.
        """
        if self.data is None:
            return pd.DataFrame()
        if len(self.data) <= n:
            return self.data.copy()
        return self.data.sample(n=n, random_state=42)
