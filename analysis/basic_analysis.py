"""
Analisador Básico - Funcionalidades de análise estatística e insights iniciais
"""
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

class BasicAnalyzer:
    """Classe para análises estatísticas básicas"""
    
    def __init__(self):
        self.data = None
        self.insights = {}
    
    def set_data(self, df: pd.DataFrame):
        """Definir dados para análise"""
        self.data = df.copy()
    
    def descriptive_statistics(self, columns: Optional[List[str]] = None) -> Dict:
        """Estatísticas descritivas para colunas numéricas"""
        if self.data is None:
            raise ValueError("Dados não carregados")
        
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
        
        if columns:
            numeric_cols = [col for col in columns if col in numeric_cols]
        
        stats_dict = {}
        
        for col in numeric_cols:
            stats_dict[col] = {
                'mean': self.data[col].mean(),
                'median': self.data[col].median(),
                'std': self.data[col].std(),
                'min': self.data[col].min(),
                'max': self.data[col].max(),
                'q25': self.data[col].quantile(0.25),
                'q75': self.data[col].quantile(0.75),
                'skewness': self.data[col].skew(),
                'kurtosis': self.data[col].kurtosis()
            }
        
        return stats_dict
    
    def categorical_analysis(self, columns: Optional[List[str]] = None) -> Dict:
        """Análise de variáveis categóricas"""
        if self.data is None:
            raise ValueError("Dados não carregados")
        
        categorical_cols = self.data.select_dtypes(include=['object']).columns.tolist()
        
        if columns:
            categorical_cols = [col for col in columns if col in categorical_cols]
        
        analysis_dict = {}
        
        for col in categorical_cols:
            value_counts = self.data[col].value_counts()
            
            analysis_dict[col] = {
                'unique_values': self.data[col].nunique(),
                'most_frequent': value_counts.index[0] if len(value_counts) > 0 else None,
                'most_frequent_count': value_counts.iloc[0] if len(value_counts) > 0 else 0,
                'least_frequent': value_counts.index[-1] if len(value_counts) > 0 else None,
                'least_frequent_count': value_counts.iloc[-1] if len(value_counts) > 0 else 0,
                'value_distribution': value_counts.to_dict(),
                'concentration_ratio': value_counts.iloc[0] / len(self.data) if len(value_counts) > 0 else 0
            }
        
        return analysis_dict
    
    def correlation_analysis(self) -> Tuple[pd.DataFrame, List[Tuple[str, str, float]]]:
        """Análise de correlação entre variáveis numéricas"""
        if self.data is None:
            raise ValueError("Dados não carregados")
        
        numeric_data = self.data.select_dtypes(include=[np.number])
        correlation_matrix = numeric_data.corr()
        
        # Encontrar correlações fortes (> 0.7 ou < -0.7)
        strong_correlations = []
        
        for i in range(len(correlation_matrix.columns)):
            for j in range(i+1, len(correlation_matrix.columns)):
                corr_value = correlation_matrix.iloc[i, j]
                if abs(corr_value) > 0.7:
                    col1 = correlation_matrix.columns[i]
                    col2 = correlation_matrix.columns[j]
                    strong_correlations.append((col1, col2, corr_value))
        
        return correlation_matrix, strong_correlations
    
    def detect_outliers(self, method: str = 'iqr') -> Dict:
        """Detectar outliers em variáveis numéricas"""
        if self.data is None:
            raise ValueError("Dados não carregados")
        
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
        outliers_dict = {}
        
        for col in numeric_cols:
            if method == 'iqr':
                outliers = self._detect_outliers_iqr(self.data[col])
            elif method == 'zscore':
                outliers = self._detect_outliers_zscore(self.data[col])
            else:
                raise ValueError("Método deve ser 'iqr' ou 'zscore'")
            
            outliers_dict[col] = {
                'outlier_indices': outliers.tolist(),
                'outlier_count': len(outliers),
                'outlier_percentage': (len(outliers) / len(self.data)) * 100
            }
        
        return outliers_dict
    
    def _detect_outliers_iqr(self, series: pd.Series) -> np.ndarray:
        """Detectar outliers usando método IQR"""
        Q1 = series.quantile(0.25)
        Q3 = series.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = series[(series < lower_bound) | (series > upper_bound)].index
        return outliers.values
    
    def _detect_outliers_zscore(self, series: pd.Series, threshold: float = 3) -> np.ndarray:
        """Detectar outliers usando Z-score"""
        z_scores = np.abs(stats.zscore(series.dropna()))
        outliers = series[z_scores > threshold].index
        return outliers.values
    
    def generate_insights(self) -> List[str]:
        """Gerar insights automáticos baseados na análise"""
        if self.data is None:
            raise ValueError("Dados não carregados")
        
        insights = []
        
        # Insights sobre tamanho dos dados
        total_rows = len(self.data)
        if total_rows < 30:
            insights.append("⚠️ Amostra pequena (< 30 registros). Resultados podem não ser representativos.")
        elif total_rows > 1000:
            insights.append("✅ Amostra robusta com mais de 1000 registros.")
        
        # Insights sobre dados faltantes
        missing_percentage = (self.data.isnull().sum().sum() / (len(self.data) * len(self.data.columns))) * 100
        if missing_percentage > 20:
            insights.append(f"⚠️ Alto percentual de dados faltantes ({missing_percentage:.1f}%). Considere melhorar a coleta.")
        elif missing_percentage < 5:
            insights.append("✅ Baixo percentual de dados faltantes. Boa qualidade dos dados.")
        
        # Insights sobre variáveis categóricas
        categorical_analysis = self.categorical_analysis()
        for col, analysis in categorical_analysis.items():
            if analysis['concentration_ratio'] > 0.8:
                insights.append(f"📊 A variável '{col}' tem alta concentração ({analysis['concentration_ratio']:.1%}) no valor '{analysis['most_frequent']}'.")
        
        # Insights sobre correlações
        _, strong_corrs = self.correlation_analysis()
        if strong_corrs:
            insights.append(f"🔗 Encontradas {len(strong_corrs)} correlações fortes entre variáveis numéricas.")
        
        # Insights sobre outliers
        outliers = self.detect_outliers()
        high_outlier_cols = [col for col, data in outliers.items() if data['outlier_percentage'] > 10]
        if high_outlier_cols:
            insights.append(f"🎯 Colunas com muitos outliers (>10%): {', '.join(high_outlier_cols)}")
        
        return insights
    
    def market_research_insights(self) -> Dict:
        """Insights específicos para pesquisa de marketing"""
        insights = {
            'demographic_patterns': [],
            'satisfaction_insights': [],
            'behavioral_patterns': [],
            'recommendations': []
        }
        
        if self.data is None:
            return insights
        
        # Procurar colunas relacionadas a idade
        age_cols = [col for col in self.data.columns if 'idade' in col.lower() or 'age' in col.lower()]
        if age_cols:
            age_col = age_cols[0]
            age_stats = self.data[age_col].describe()
            insights['demographic_patterns'].append(
                f"Idade média dos respondentes: {age_stats['mean']:.1f} anos (range: {age_stats['min']:.0f}-{age_stats['max']:.0f})"
            )
        
        # Procurar colunas de satisfação
        satisfaction_cols = [col for col in self.data.columns 
                           if any(word in col.lower() for word in ['satisfação', 'satisfaction', 'nota', 'rating', 'score'])]
        
        for col in satisfaction_cols:
            if pd.api.types.is_numeric_dtype(self.data[col]):
                avg_satisfaction = self.data[col].mean()
                insights['satisfaction_insights'].append(
                    f"Satisfação média em '{col}': {avg_satisfaction:.1f}"
                )
        
        # Procurar padrões de comportamento
        behavior_cols = [col for col in self.data.columns 
                        if any(word in col.lower() for word in ['frequência', 'frequency', 'uso', 'usage', 'compra', 'purchase'])]
        
        for col in behavior_cols:
            if col in self.data.columns:
                value_counts = self.data[col].value_counts()
                if len(value_counts) > 0:
                    most_common = value_counts.index[0]
                    percentage = (value_counts.iloc[0] / len(self.data)) * 100
                    insights['behavioral_patterns'].append(
                        f"Comportamento mais comum em '{col}': {most_common} ({percentage:.1f}%)"
                    )
        
        # Gerar recomendações
        if len(self.data) < 100:
            insights['recommendations'].append("Aumentar amostra para pelo menos 100 respondentes")
        
        if missing_percentage := (self.data.isnull().sum().sum() / (len(self.data) * len(self.data.columns))) * 100 > 15:
            insights['recommendations'].append("Melhorar qualidade da coleta de dados")
        
        insights['recommendations'].append("Implementar segmentação baseada em clustering")
        insights['recommendations'].append("Desenvolver análise de sentimentos para feedback qualitativo")
        
        return insights