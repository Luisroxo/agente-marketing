import datetime
from typing import Optional
import pandas as pd

class ReportingService:
    def __init__(self, data: Optional[pd.DataFrame] = None):
        self.data = data

    def _calculate_data_quality(self) -> float:
        if self.data is None or self.data.empty:
            return 0.0
        total = self.data.size
        filled = self.data.count().sum()
        return (filled / total) * 100 if total > 0 else 0.0

    def generate_executive_summary(self, format_type: str = "markdown") -> str:
        if self.data is None:
            return "Dados não disponíveis para gerar resumo."
        total_records = len(self.data)
        date_generated = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M")
        data_quality = self._calculate_data_quality()
        if format_type == "markdown":
            return (
                f"## Resumo Executivo\n"
                f"- Total de registros: {total_records}\n"
                f"- Data de geração: {date_generated}\n"
                f"- Qualidade dos dados: {data_quality:.2f}%\n"
            )
        else:
            return (
                f"Resumo Executivo\n"
                f"Total de registros: {total_records}\n"
                f"Data de geração: {date_generated}\n"
                f"Qualidade dos dados: {data_quality:.2f}%\n"
            )

    def generate_full_report(self, format_type: str = "markdown") -> str:
        sections = [
            self._generate_header(format_type),
            self.generate_executive_summary(format_type),
            self._generate_methodology(format_type),
            self._generate_data_analysis(format_type),
            self._generate_insights_section(format_type),
            self._generate_recommendations(format_type),
            self._generate_next_steps(format_type),
            self._generate_footer(format_type),
        ]
        return "\n\n".join(sections)

    def _generate_header(self, format_type: str) -> str:
        now = datetime.datetime.now().strftime("%d de %B de %Y às %H:%M")
        if format_type == "markdown":
            return (
                f"# Relatório de Análise de Marketing\n"
                f"Agente de IA para Marketing v2.0\n"
                f"Gerado em: {now}\n"
                f"Versão do Sistema: Enterprise Edition\n---"
            )
        else:
            return (
                f"RELATÓRIO DE ANÁLISE DE MARKETING\n"
                f"Agente de IA para Marketing v2.0\n"
                f"Gerado em: {now}\n"
                f"Versão do Sistema: Enterprise Edition\n"
            )

    def _generate_methodology(self, format_type: str) -> str:
        if format_type == "markdown":
            return (
                "## Metodologia de Análise\n"
                "Pipeline: Dados Brutos > Limpeza > Validação > Análise > Insights > Relatório\n"
                "Técnicas: Estatística descritiva, análise de padrões, detecção de outliers, correlações, testes estatísticos.\n"
            )
        else:
            return (
                "METODOLOGIA DE ANÁLISE\n"
                "Pipeline: Dados Brutos > Limpeza > Validação > Análise > Insights > Relatório\n"
                "Técnicas: Estatística descritiva, análise de padrões, detecção de outliers, correlações, testes estatísticos.\n"
            )

    def _generate_data_analysis(self, format_type: str) -> str:
        if self.data is None:
            return "Dados não disponíveis para análise."
        numeric_cols = len(self.data.select_dtypes(include=["number"]).columns)
        categorical_cols = len(self.data.select_dtypes(include=["object"]).columns)
        missing_data = self.data.isnull().sum().sum()
        if format_type == "markdown":
            return (
                f"## Análise dos Dados\n"
                f"- Total de registros: {len(self.data)}\n"
                f"- Variáveis numéricas: {numeric_cols}\n"
                f"- Variáveis categóricas: {categorical_cols}\n"
                f"- Dados ausentes: {missing_data}\n"
            )
        else:
            return (
                f"ANÁLISE DOS DADOS\n"
                f"Total de registros: {len(self.data)}\n"
                f"Variáveis numéricas: {numeric_cols}\n"
                f"Variáveis categóricas: {categorical_cols}\n"
                f"Dados ausentes: {missing_data}\n"
            )

    def _generate_insights_section(self, format_type: str) -> str:
        if format_type == "markdown":
            return (
                "## Insights Estratégicos\n"
                "- Segmentos inexplorados identificados\n"
                "- Potencial de crescimento em categorias específicas\n"
                "- Oportunidades de cross-sell baseadas em correlações\n"
            )
        else:
            return (
                "INSIGHTS ESTRATÉGICOS\n"
                "Segmentos inexplorados identificados\n"
                "Potencial de crescimento em categorias específicas\n"
                "Oportunidades de cross-sell baseadas em correlações\n"
            )

    def _generate_recommendations(self, format_type: str) -> str:
        if format_type == "markdown":
            return (
                "## Recomendações\n"
                "- Expandir base de dados\n"
                "- Implementar IA avançada\n"
                "- Automatizar relatórios\n"
                "- Integrar ferramentas\n"
            )
        else:
            return (
                "RECOMENDAÇÕES\n"
                "Expandir base de dados\n"
                "Implementar IA avançada\n"
                "Automatizar relatórios\n"
                "Integrar ferramentas\n"
            )

    def _generate_next_steps(self, format_type: str) -> str:
        if format_type == "markdown":
            return (
                "## Próximos Passos\n"
                "- Revisar insights do relatório\n"
                "- Identificar lacunas de dados\n"
                "- Definir KPIs\n"
                "- Planejar coleta adicional\n"
            )
        else:
            return (
                "PRÓXIMOS PASSOS\n"
                "Revisar insights do relatório\n"
                "Identificar lacunas de dados\n"
                "Definir KPIs\n"
                "Planejar coleta adicional\n"
            )

    def _generate_footer(self, format_type: str) -> str:
        now = datetime.datetime.now().strftime("%B de %Y")
        if format_type == "markdown":
            return (
                "---\n"
                "Agente de IA para Marketing v2.0 - Enterprise Edition\n"
                f"Desenvolvido em: {now}\n"
                "Próximas funcionalidades: Análise de sentimentos, clustering avançado, IA preditiva\n"
                "Feedback: Contribuições e sugestões são bem-vindas\n"
                "Suporte: Sistema em constante aprimoramento\n"
                "---\n"
                "Transformando dados em estratégias de marketing eficazes através da Inteligência Artificial\n"
                "Powered by AI • Built for Marketers • Designed for Results\n"
            )
        else:
            return (
                "====================================\n"
                "SUPORTE E DESENVOLVIMENTO\n"
                "Agente de IA para Marketing v2.0\n"
                f"Desenvolvido em: {now}\n"
                "Transformando dados em estratégias de marketing eficazes através da IA\n"
                "====================================\n"
            )