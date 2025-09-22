"""
Analisador Moderno - Serviço enterprise de análise estatística e insights
Estrutura atualizada para o Agente Marketing IA
"""
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional, Any
from scipy import stats
import warnings
warnings.filterwarnings('ignore')
import logging

logger = logging.getLogger(__name__)

class AnalysisService:
    """
    Serviço moderno para análises estatísticas e geração de insights
    Versão enterprise com melhor estrutura e funcionalidades avançadas
    """
    
    def __init__(self):
        self.data: Optional[pd.DataFrame] = None
        self.insights: Dict[str, Any] = {}
        self.analysis_cache: Dict[str, Any] = {}
    
    def set_data(self, df: pd.DataFrame) -> None:
        """
        Definir dados para análise
        
        Args:
            df: DataFrame com os dados para análise
        """
        self.data = df.copy()
        self.analysis_cache.clear()  # Limpar cache ao definir novos dados
        logger.info(f"Dados definidos para análise: {len(df)} linhas, {len(df.columns)} colunas")
    
    def descriptive_statistics(self, columns: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Estatísticas descritivas para colunas numéricas
        
        Args:
            columns: Lista de colunas específicas para analisar
            
        Returns:
            Dicionário com estatísticas descritivas
        """
        if self.data is None:
            raise ValueError("Dados não carregados")
        
        cache_key = f"descriptive_{str(columns)}"
        if cache_key in self.analysis_cache:
            return self.analysis_cache[cache_key]
        
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
        
        if columns:
            numeric_cols = [col for col in columns if col in numeric_cols]
        
        stats_dict = {}
        
        for col in numeric_cols:
            col_data = self.data[col].dropna()
            
            stats_dict[col] = {
                'count': len(col_data),
                'mean': col_data.mean(),
                'median': col_data.median(),
                'mode': col_data.mode().iloc[0] if len(col_data.mode()) > 0 else None,
                'std': col_data.std(),
                'variance': col_data.var(),
                'min': col_data.min(),
                'max': col_data.max(),
                'range': col_data.max() - col_data.min(),
                'q25': col_data.quantile(0.25),
                'q75': col_data.quantile(0.75),
                'iqr': col_data.quantile(0.75) - col_data.quantile(0.25),
                'skewness': col_data.skew(),
                'kurtosis': col_data.kurtosis(),
                'coefficient_variation': (col_data.std() / col_data.mean()) * 100 if col_data.mean() != 0 else 0
            }
        
        self.analysis_cache[cache_key] = stats_dict
        return stats_dict
    
    def categorical_analysis(self, columns: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Análise avançada de variáveis categóricas
        
        Args:
            columns: Lista de colunas específicas para analisar
            
        Returns:
            Dicionário com análise categórica
        """
        if self.data is None:
            raise ValueError("Dados não carregados")
        
        cache_key = f"categorical_{str(columns)}"
        if cache_key in self.analysis_cache:
            return self.analysis_cache[cache_key]
        
        categorical_cols = self.data.select_dtypes(include=['object', 'category']).columns.tolist()
        
        if columns:
            categorical_cols = [col for col in columns if col in categorical_cols]
        
        analysis_dict = {}
        
        for col in categorical_cols:
            col_data = self.data[col].dropna()
            value_counts = col_data.value_counts()
            
            # Calcular índice de diversidade (Shannon)
            proportions = value_counts / len(col_data)
            shannon_diversity = -sum(p * np.log(p) for p in proportions if p > 0)
            
            analysis_dict[col] = {
                'total_count': len(col_data),
                'unique_values': col_data.nunique(),
                'most_frequent': value_counts.index[0] if len(value_counts) > 0 else None,
                'most_frequent_count': value_counts.iloc[0] if len(value_counts) > 0 else 0,
                'most_frequent_percentage': (value_counts.iloc[0] / len(col_data)) * 100 if len(value_counts) > 0 else 0,
                'least_frequent': value_counts.index[-1] if len(value_counts) > 0 else None,
                'least_frequent_count': value_counts.iloc[-1] if len(value_counts) > 0 else 0,
                'value_distribution': value_counts.to_dict(),
                'concentration_ratio': value_counts.iloc[0] / len(col_data) if len(value_counts) > 0 else 0,
                'shannon_diversity': shannon_diversity,
                'top_3_values': value_counts.head(3).to_dict()
            }
        
        self.analysis_cache[cache_key] = analysis_dict
        return analysis_dict
    
    def correlation_analysis(self, method: str = 'pearson') -> Tuple[pd.DataFrame, List[Tuple[str, str, float]]]:
        """
        Análise de correlação entre variáveis numéricas
        
        Args:
            method: Método de correlação ('pearson', 'spearman', 'kendall')
            
        Returns:
            Tuple com matriz de correlação e lista de correlações fortes
        """
        if self.data is None:
            raise ValueError("Dados não carregados")
        
        cache_key = f"correlation_{method}"
        if cache_key in self.analysis_cache:
            return self.analysis_cache[cache_key]
        
        numeric_data = self.data.select_dtypes(include=[np.number])
        
        if len(numeric_data.columns) < 2:
            logger.warning("Menos de 2 colunas numéricas para análise de correlação")
            return pd.DataFrame(), []
        
        correlation_matrix = numeric_data.corr(method=method)
        
        # Encontrar correlações fortes (> 0.7 ou < -0.7)
        strong_correlations = []
        
        for i in range(len(correlation_matrix.columns)):
            for j in range(i+1, len(correlation_matrix.columns)):
                corr_value = correlation_matrix.iloc[i, j]
                if not np.isnan(corr_value) and abs(corr_value) > 0.7:
                    col1 = correlation_matrix.columns[i]
                    col2 = correlation_matrix.columns[j]
                    strong_correlations.append((col1, col2, corr_value))
        
        result = (correlation_matrix, strong_correlations)
        self.analysis_cache[cache_key] = result
        return result
    
    def detect_outliers(self, method: str = 'iqr', threshold: float = 3.0) -> Dict[str, Any]:
        """
        Detectar outliers em variáveis numéricas com múltiplos métodos
        
        Args:
            method: Método de detecção ('iqr', 'zscore', 'modified_zscore')
            threshold: Threshold para métodos baseados em score
            
        Returns:
            Dicionário com outliers detectados
        """
        if self.data is None:
            raise ValueError("Dados não carregados")
        
        cache_key = f"outliers_{method}_{threshold}"
        if cache_key in self.analysis_cache:
            return self.analysis_cache[cache_key]
        
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
        outliers_dict = {}
        
        for col in numeric_cols:
            col_data = self.data[col].dropna()
            
            if method == 'iqr':
                outliers = self._detect_outliers_iqr(col_data)
            elif method == 'zscore':
                outliers = self._detect_outliers_zscore(col_data, threshold)
            elif method == 'modified_zscore':
                outliers = self._detect_outliers_modified_zscore(col_data, threshold)
            else:
                raise ValueError("Método deve ser 'iqr', 'zscore' ou 'modified_zscore'")
            
            outliers_dict[col] = {
                'outlier_indices': outliers.tolist(),
                'outlier_values': self.data.loc[outliers, col].tolist() if len(outliers) > 0 else [],
                'outlier_count': len(outliers),
                'outlier_percentage': (len(outliers) / len(col_data)) * 100,
                'method_used': method
            }
        
        self.analysis_cache[cache_key] = outliers_dict
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
        z_scores = np.abs(stats.zscore(series))
        outliers = series[z_scores > threshold].index
        return outliers.values
    
    def _detect_outliers_modified_zscore(self, series: pd.Series, threshold: float = 3.5) -> np.ndarray:
        """Detectar outliers usando Modified Z-score (mais robusto)"""
        median = series.median()
        mad = np.median(np.abs(series - median))
        modified_z_scores = 0.6745 * (series - median) / mad
        outliers = series[np.abs(modified_z_scores) > threshold].index
        return outliers.values
    
    def generate_insights(self) -> List[str]:
        """
        Gerar insights automáticos baseados na análise
        
        Returns:
            Lista de insights em formato texto
        """
        if self.data is None:
            raise ValueError("Dados não carregados")
        
        insights = []
        
        # Insights sobre tamanho dos dados
        total_rows = len(self.data)
        if total_rows < 30:
            insights.append("⚠️ Amostra pequena (< 30 registros). Resultados podem não ser representativos.")
        elif total_rows > 1000:
            insights.append("✅ Amostra robusta com mais de 1000 registros.")
        else:
            insights.append(f"📊 Amostra moderada com {total_rows} registros.")
        
        # Insights sobre dados faltantes
        missing_percentage = (self.data.isnull().sum().sum() / (len(self.data) * len(self.data.columns))) * 100
        if missing_percentage > 20:
            insights.append(f"⚠️ Alto percentual de dados faltantes ({missing_percentage:.1f}%). Considere melhorar a coleta.")
        elif missing_percentage < 5:
            insights.append("✅ Baixo percentual de dados faltantes. Boa qualidade dos dados.")
        else:
            insights.append(f"📋 Percentual moderado de dados faltantes ({missing_percentage:.1f}%).")
        
        # Insights sobre variáveis categóricas
        try:
            categorical_analysis = self.categorical_analysis()
            for col, analysis in categorical_analysis.items():
                if analysis['concentration_ratio'] > 0.8:
                    insights.append(f"📊 A variável '{col}' tem alta concentração ({analysis['concentration_ratio']:.1%}) no valor '{analysis['most_frequent']}'.")
                elif analysis['shannon_diversity'] > 2:
                    insights.append(f"🌟 A variável '{col}' apresenta alta diversidade de valores.")
        except Exception as e:
            logger.warning(f"Erro na análise categórica: {e}")
        
        # Insights sobre correlações
        try:
            _, strong_corrs = self.correlation_analysis()
            if strong_corrs:
                insights.append(f"🔗 Encontradas {len(strong_corrs)} correlações fortes entre variáveis numéricas.")
                if len(strong_corrs) > 3:
                    insights.append("💡 Muitas correlações fortes podem indicar multicolinearidade.")
        except Exception as e:
            logger.warning(f"Erro na análise de correlação: {e}")
        
        # Insights sobre outliers
        try:
            outliers = self.detect_outliers()
            high_outlier_cols = [col for col, data in outliers.items() if data['outlier_percentage'] > 10]
            if high_outlier_cols:
                insights.append(f"🎯 Colunas com muitos outliers (>10%): {', '.join(high_outlier_cols)}")
        except Exception as e:
            logger.warning(f"Erro na detecção de outliers: {e}")
        
        return insights
    
    def market_research_insights(self) -> Dict[str, List[str]]:
        """
        Insights específicos para pesquisa de marketing
        
        Returns:
            Dicionário com insights categorizados
        """
        insights = {
            'demographic_patterns': [],
            'satisfaction_insights': [],
            'behavioral_patterns': [],
            'data_quality': [],
            'recommendations': []
        }
        
        if self.data is None:
            return insights
        
        # Análise demográfica
        age_cols = [col for col in self.data.columns if 'idade' in col.lower() or 'age' in col.lower()]
        if age_cols:
            age_col = age_cols[0]
            if pd.api.types.is_numeric_dtype(self.data[age_col]):
                age_stats = self.data[age_col].describe()
                insights['demographic_patterns'].append(
                    f"Idade média: {age_stats['mean']:.1f} anos (range: {age_stats['min']:.0f}-{age_stats['max']:.0f})"
                )
                
                # Segmentação por idade
                if age_stats['mean'] < 30:
                    insights['demographic_patterns'].append("Perfil jovem predominante")
                elif age_stats['mean'] > 50:
                    insights['demographic_patterns'].append("Perfil maduro predominante")
        
        # Análise de satisfação
        satisfaction_cols = [col for col in self.data.columns 
                           if any(word in col.lower() for word in ['satisfação', 'satisfaction', 'nota', 'rating', 'score'])]
        
        for col in satisfaction_cols:
            if pd.api.types.is_numeric_dtype(self.data[col]):
                avg_satisfaction = self.data[col].mean()
                scale_max = self.data[col].max()
                satisfaction_percentage = (avg_satisfaction / scale_max) * 100
                
                insights['satisfaction_insights'].append(
                    f"Satisfação média em '{col}': {avg_satisfaction:.1f} ({satisfaction_percentage:.1f}% da escala)"
                )
                
                if satisfaction_percentage < 60:
                    insights['satisfaction_insights'].append(f"⚠️ Baixa satisfação em {col}")
                elif satisfaction_percentage > 80:
                    insights['satisfaction_insights'].append(f"✅ Alta satisfação em {col}")
        
        # Análise comportamental
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
        
        # Qualidade dos dados
        missing_percentage = (self.data.isnull().sum().sum() / (len(self.data) * len(self.data.columns))) * 100
        insights['data_quality'].append(f"Completude dos dados: {100 - missing_percentage:.1f}%")
        
        duplicate_percentage = (self.data.duplicated().sum() / len(self.data)) * 100
        insights['data_quality'].append(f"Registros únicos: {100 - duplicate_percentage:.1f}%")
        
        # Recomendações
        if len(self.data) < 100:
            insights['recommendations'].append("Aumentar amostra para pelo menos 100 respondentes")
        
        if missing_percentage > 15:
            insights['recommendations'].append("Melhorar qualidade da coleta de dados")
        
        insights['recommendations'].append("Implementar segmentação baseada em clustering")
        insights['recommendations'].append("Desenvolver análise de sentimentos para feedback qualitativo")
        insights['recommendations'].append("Criar dashboards interativos para monitoramento contínuo")
        
        return insights
    
    def statistical_tests(self, column1: str, column2: str = None, test_type: str = 'auto') -> Dict[str, Any]:
        """
        Realizar testes estatísticos
        
        Args:
            column1: Primeira coluna para teste
            column2: Segunda coluna (opcional)
            test_type: Tipo de teste ('auto', 'ttest', 'chi2', 'anova')
            
        Returns:
            Resultado do teste estatístico
        """
        if self.data is None:
            raise ValueError("Dados não carregados")
        
        result = {'test_performed': None, 'statistic': None, 'p_value': None, 'interpretation': None}
        
        try:
            if column2 is None:
                # Teste de normalidade para uma variável
                if pd.api.types.is_numeric_dtype(self.data[column1]):
                    stat, p_value = stats.normaltest(self.data[column1].dropna())
                    result = {
                        'test_performed': 'Normalidade (D\'Agostino)',
                        'statistic': stat,
                        'p_value': p_value,
                        'interpretation': 'Normal' if p_value > 0.05 else 'Não normal'
                    }
            else:
                # Testes entre duas variáveis
                if test_type == 'auto':
                    if (pd.api.types.is_numeric_dtype(self.data[column1]) and 
                        pd.api.types.is_numeric_dtype(self.data[column2])):
                        # T-test para variáveis numéricas
                        stat, p_value = stats.ttest_ind(
                            self.data[column1].dropna(), 
                            self.data[column2].dropna()
                        )
                        result = {
                            'test_performed': 'T-test independente',
                            'statistic': stat,
                            'p_value': p_value,
                            'interpretation': 'Diferença significativa' if p_value < 0.05 else 'Sem diferença significativa'
                        }
                    else:
                        # Chi-quadrado para variáveis categóricas
                        contingency = pd.crosstab(self.data[column1], self.data[column2])
                        stat, p_value, _, _ = stats.chi2_contingency(contingency)
                        result = {
                            'test_performed': 'Chi-quadrado',
                            'statistic': stat,
                            'p_value': p_value,
                            'interpretation': 'Associação significativa' if p_value < 0.05 else 'Sem associação significativa'
                        }
        
        except Exception as e:
            logger.error(f"Erro no teste estatístico: {e}")
            result['error'] = str(e)
        
        return result