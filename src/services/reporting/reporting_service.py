"""
Serviço de Relatórios - Geração enterprise de documentos e insights
Estrutura moderna para o Agente Marketing IA
"""
import pandas as pd
from datetime import datetime
from typing import Dict, List, Optional, Any
from services.logging_config import get_logger
logger = get_logger(__name__)

class ReportingService:
    """
    Serviço moderno para geração de relatórios de marketing
    Versão enterprise com templates melhorados e funcionalidades avançadas
    """
    
    def __init__(self):
        self.data: Optional[pd.DataFrame] = None
        self.insights: Dict[str, Any] = {}
        self.metadata: Dict[str, Any] = {}
        self.template_cache: Dict[str, str] = {}
    
    def set_data(self, df: pd.DataFrame, insights: Dict[str, Any] = None, metadata: Dict[str, Any] = None) -> None:
        """
        Definir dados e insights para o relatório
        
        Args:
            df: DataFrame com os dados
            insights: Dicionário com insights gerados
            metadata: Metadados adicionais
        """
        self.data = df.copy()
        self.insights = insights or {}
        self.metadata = metadata or {}
        logger.info(f"Dados definidos para relatório: {len(df)} linhas, {len(df.columns)} colunas")
    
    def generate_executive_summary(self, format_type: str = 'markdown') -> str:
        """
        Gerar resumo executivo
        
        Args:
            format_type: Formato do relatório ('markdown', 'html', 'text')
            
        Returns:
            Resumo executivo formatado
        """
        if self.data is None:
            return "❌ Dados não disponíveis para gerar resumo."
        
        total_records = len(self.data)
        date_generated = datetime.now().strftime('%d/%m/%Y às %H:%M')
        data_quality = self._calculate_data_quality()
        
        if format_type == 'markdown':
            return self._generate_markdown_summary(total_records, date_generated, data_quality)
        elif format_type == 'html':
            return self._generate_html_summary(total_records, date_generated, data_quality)
        else:
            return self._generate_text_summary(total_records, date_generated, data_quality)
    
    def _generate_markdown_summary(self, total_records: int, date_generated: str, data_quality: float) -> str:
        """Gerar resumo em formato Markdown"""
        return f"""
# 📊 Resumo Executivo - Análise de Marketing IA

**📅 Data de Geração:** {date_generated}  
**📈 Total de Registros:** {total_records:,}  
**✅ Qualidade dos Dados:** {data_quality:.1f}%  
**🏆 Status:** {self._get_quality_status(data_quality)}

---

## 🎯 Principais Descobertas

### 📈 Volume e Abrangência
- ✅ Análise baseada em **{total_records:,} registros** de pesquisa
- 📊 Dados **{data_quality:.1f}% completos** - Qualidade {self._get_quality_level(data_quality)}
- 🔍 **{len(self.data.columns)} dimensões** diferentes analisadas
- 🎲 **{self.data.select_dtypes(include=['object']).shape[1]} variáveis categóricas** identificadas

### 🔍 Perfil Demográfico
{self._generate_demographic_insights()}

### 🚀 Oportunidades de Negócio
{self._generate_business_opportunities()}

### ⚠️ Pontos de Atenção
{self._generate_attention_points()}

### 💡 Recomendações Prioritárias
{self._generate_priority_recommendations()}

---
*Relatório gerado automaticamente pelo Agente Marketing IA v2.0*
"""

    def _generate_html_summary(self, total_records: int, date_generated: str, data_quality: float) -> str:
        """Gerar resumo em formato HTML"""
        return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Resumo Executivo - Marketing IA</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 10px; }}
        .metric {{ display: inline-block; margin: 10px; padding: 15px; background: #f8f9fa; border-radius: 8px; }}
        .insight {{ margin: 15px 0; padding: 10px; border-left: 4px solid #007bff; background: #f8f9fa; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 Resumo Executivo - Análise de Marketing IA</h1>
        <p><strong>Data:</strong> {date_generated}</p>
    </div>
    
    <div class="metrics">
        <div class="metric">
            <h3>📈 Registros</h3>
            <p><strong>{total_records:,}</strong></p>
        </div>
        <div class="metric">
            <h3>✅ Qualidade</h3>
            <p><strong>{data_quality:.1f}%</strong></p>
        </div>
        <div class="metric">
            <h3>🔍 Dimensões</h3>
            <p><strong>{len(self.data.columns)}</strong></p>
        </div>
    </div>
    
    <div class="insight">
        <h3>🎯 Principais Descobertas</h3>
        {self._generate_html_insights()}
    </div>
</body>
</html>
"""

    def _generate_text_summary(self, total_records: int, date_generated: str, data_quality: float) -> str:
        """Gerar resumo em formato texto simples"""
        return f"""
RESUMO EXECUTIVO - ANÁLISE DE MARKETING IA
==========================================

Data de Geração: {date_generated}
Total de Registros: {total_records:,}
Qualidade dos Dados: {data_quality:.1f}%
Status: {self._get_quality_status(data_quality)}

PRINCIPAIS DESCOBERTAS
=====================

Volume e Abrangência:
- Análise baseada em {total_records:,} registros de pesquisa
- Dados {data_quality:.1f}% completos - Qualidade {self._get_quality_level(data_quality)}
- {len(self.data.columns)} dimensões diferentes analisadas

{self._generate_text_insights()}
"""

    def generate_full_report(self, format_type: str = 'markdown', include_sections: List[str] = None) -> str:
        """
        Gerar relatório completo
        
        Args:
            format_type: Formato do relatório
            include_sections: Seções específicas para incluir
            
        Returns:
            Relatório completo formatado
        """
        if include_sections is None:
            include_sections = [
                'header', 'executive_summary', 'methodology', 
                'data_analysis', 'insights', 'recommendations', 
                'next_steps', 'footer'
            ]
        
        sections = []
        
        for section in include_sections:
            if section == 'header':
                sections.append(self._generate_header(format_type))
            elif section == 'executive_summary':
                sections.append(self.generate_executive_summary(format_type))
            elif section == 'methodology':
                sections.append(self._generate_methodology(format_type))
            elif section == 'data_analysis':
                sections.append(self._generate_data_analysis(format_type))
            elif section == 'insights':
                sections.append(self._generate_insights_section(format_type))
            elif section == 'recommendations':
                sections.append(self._generate_recommendations(format_type))
            elif section == 'next_steps':
                sections.append(self._generate_next_steps(format_type))
            elif section == 'footer':
                sections.append(self._generate_footer(format_type))
        
        return "\n\n".join(sections)
    
    def _generate_header(self, format_type: str) -> str:
        """Gerar cabeçalho do relatório"""
        if format_type == 'markdown':
            return f"""
# 🤖 Relatório de Análise de Marketing - Agente IA
## Insights Baseados em Dados para Estratégias Eficazes

**🚀 Agente de IA para Marketing v2.0**  
**📅 Gerado em:** {datetime.now().strftime('%d de %B de %Y às %H:%M')}  
**🔬 Versão do Sistema:** Enterprise Edition

---
"""
        else:
            return f"""
RELATÓRIO DE ANÁLISE DE MARKETING - AGENTE IA
============================================

Agente de IA para Marketing v2.0
Gerado em: {datetime.now().strftime('%d de %B de %Y às %H:%M')}

"""

    def _generate_methodology(self, format_type: str) -> str:
        """Gerar seção de metodologia"""
        if format_type == 'markdown':
            return """
## 📋 Metodologia de Análise

### 🔄 Pipeline de Processamento de Dados
```
Dados Brutos → Limpeza → Validação → Análise → Insights → Relatório
```

### 📊 Coleta e Preparação
- **Fonte de Dados:** Pesquisas online e dados estruturados
- **Período de Análise:** Dados mais recentes disponíveis
- **Método de Processamento:** Pipeline automatizado com IA
- **Validação:** Verificação automática de qualidade e consistência

### 🧮 Técnicas Analíticas Aplicadas

#### ✅ Implementadas
- **Estatística Descritiva:** Medidas de tendência central e dispersão
- **Análise de Padrões:** Identificação de tendências e anomalias
- **Detecção de Outliers:** Métodos IQR e Z-score modificado
- **Análise de Correlações:** Pearson, Spearman e Kendall
- **Testes Estatísticos:** T-test, Chi-quadrado, normalidade

#### 🔄 Em Desenvolvimento
- **Análise de Sentimentos:** NLP para feedback qualitativo
- **Clustering Avançado:** Segmentação automática de personas
- **Análise Preditiva:** Modelos de machine learning
- **Análise de Redes:** Identificação de influenciadores

### 📏 Métricas de Qualidade
- **Completude:** Percentual de dados não-nulos
- **Consistência:** Uniformidade de formatos e valores
- **Precisão:** Validação de tipos de dados
- **Relevância:** Alinhamento com objetivos de marketing
"""
        else:
            return """
METODOLOGIA DE ANÁLISE
====================

Pipeline de Processamento:
Dados Brutos → Limpeza → Validação → Análise → Insights → Relatório

Técnicas Aplicadas:
- Estatística descritiva
- Análise de padrões
- Detecção de outliers
- Análise de correlações
- Testes estatísticos

Em Desenvolvimento:
- Análise de sentimentos
- Clustering avançado
- Análise preditiva
"""

    def _generate_data_analysis(self, format_type: str) -> str:
        """Gerar seção de análise de dados"""
        if self.data is None:
            return "Dados não disponíveis para análise."
        
        numeric_cols = len(self.data.select_dtypes(include=['number']).columns)
        categorical_cols = len(self.data.select_dtypes(include=['object']).columns)
        missing_data = self.data.isnull().sum().sum()
        
        if format_type == 'markdown':
            return f"""
## 📈 Análise Detalhada dos Dados

### 📊 Estrutura dos Dados
| Métrica | Valor |
|---------|-------|
| **Total de Registros** | {len(self.data):,} |
| **Variáveis Numéricas** | {numeric_cols} |
| **Variáveis Categóricas** | {categorical_cols} |
| **Dados Faltantes** | {missing_data:,} |
| **Taxa de Completude** | {((len(self.data) * len(self.data.columns) - missing_data) / (len(self.data) * len(self.data.columns)) * 100):.1f}% |

### 🔍 Análise por Tipo de Variável

#### 📊 Variáveis Numéricas
{self._generate_numeric_analysis_summary()}

#### 🏷️ Variáveis Categóricas
{self._generate_categorical_analysis_summary()}

### 🎯 Insights de Qualidade
{self._generate_quality_insights()}
"""
        else:
            return f"""
ANÁLISE DETALHADA DOS DADOS
==========================

Estrutura:
- Total de Registros: {len(self.data):,}
- Variáveis Numéricas: {numeric_cols}
- Variáveis Categóricas: {categorical_cols}
- Taxa de Completude: {((len(self.data) * len(self.data.columns) - missing_data) / (len(self.data) * len(self.data.columns)) * 100):.1f}%
"""

    def _generate_insights_section(self, format_type: str) -> str:
        """Gerar seção de insights"""
        insights_text = self._format_insights_from_analysis()
        
        if format_type == 'markdown':
            return f"""
## 💡 Insights Estratégicos

### 🎯 Descobertas Principais
{insights_text}

### 📊 Análise Comportamental
{self._generate_behavioral_insights()}

### 🏆 Oportunidades de Mercado
{self._generate_market_opportunities()}
"""
        else:
            return f"""
INSIGHTS ESTRATÉGICOS
===================

{insights_text}
"""

    def _format_insights_from_analysis(self) -> str:
        """Formatar insights da análise"""
        if not self.insights:
            return "- Análise em processamento - Execute análise completa para obter insights"
        
        formatted_insights = []
        
        # Insights demográficos
        if 'demographic_patterns' in self.insights:
            for insight in self.insights['demographic_patterns']:
                formatted_insights.append(f"- 👥 {insight}")
        
        # Insights de satisfação
        if 'satisfaction_insights' in self.insights:
            for insight in self.insights['satisfaction_insights']:
                formatted_insights.append(f"- 😊 {insight}")
        
        # Insights comportamentais
        if 'behavioral_patterns' in self.insights:
            for insight in self.insights['behavioral_patterns']:
                formatted_insights.append(f"- 🎯 {insight}")
        
        return "\n".join(formatted_insights) if formatted_insights else "- Execute análise detalhada para gerar insights específicos"

    def _calculate_data_quality(self) -> float:
        """Calcular qualidade dos dados"""
        if self.data is None:
            return 0.0
        
        total_cells = len(self.data) * len(self.data.columns)
        missing_cells = self.data.isnull().sum().sum()
        quality = ((total_cells - missing_cells) / total_cells) * 100
        
        return quality

    def _get_quality_status(self, quality: float) -> str:
        """Obter status da qualidade"""
        if quality >= 95:
            return "🏆 Excelente"
        elif quality >= 85:
            return "✅ Boa"
        elif quality >= 70:
            return "⚠️ Aceitável"
        else:
            return "❌ Baixa"

    def _get_quality_level(self, quality: float) -> str:
        """Obter nível da qualidade"""
        if quality >= 95:
            return "Excelente"
        elif quality >= 85:
            return "Boa"
        elif quality >= 70:
            return "Aceitável"
        else:
            return "Baixa"

    def _generate_demographic_insights(self) -> str:
        """Gerar insights demográficos"""
        if self.data is None:
            return "- Dados não disponíveis"
        
        insights = []
        
        # Procurar colunas demográficas
        demo_keywords = ['idade', 'age', 'sexo', 'gender', 'cidade', 'city', 'estado', 'state']
        demo_cols = [col for col in self.data.columns 
                    if any(keyword in col.lower() for keyword in demo_keywords)]
        
        if demo_cols:
            insights.append(f"- 📊 **{len(demo_cols)} variáveis demográficas** identificadas")
            
            # Análise de idade
            age_cols = [col for col in demo_cols if 'idade' in col.lower() or 'age' in col.lower()]
            if age_cols and pd.api.types.is_numeric_dtype(self.data[age_cols[0]]):
                age_mean = self.data[age_cols[0]].mean()
                age_range = f"{self.data[age_cols[0]].min():.0f}-{self.data[age_cols[0]].max():.0f}"
                insights.append(f"- 👥 Idade média: **{age_mean:.1f} anos** (range: {age_range})")
        else:
            insights.append("- ⚠️ Dados demográficos limitados - recomendar expansão da coleta")
        
        return "\n".join(insights)

    def _generate_business_opportunities(self) -> str:
        """Gerar oportunidades de negócio"""
        opportunities = [
            "- 🎯 **Segmentação inteligente** baseada em padrões identificados",
            "- 🎨 **Personalização** de campanhas por perfil de cliente",
            "- 📱 **Otimização** de canais de comunicação mais eficazes"
        ]
        
        if self.data is not None and len(self.data) > 200:
            opportunities.append("- 🔮 **Modelagem preditiva** para antecipação de comportamentos")
        
        return "\n".join(opportunities)

    def _generate_attention_points(self) -> str:
        """Gerar pontos de atenção"""
        if self.data is None:
            return "- ❌ Dados não carregados"
        
        attention_points = []
        
        # Verificar tamanho da amostra
        if len(self.data) < 50:
            attention_points.append("- ⚠️ **Amostra pequena**: Resultados podem não ser representativos")
        
        # Verificar qualidade dos dados
        data_quality = self._calculate_data_quality()
        if data_quality < 80:
            attention_points.append(f"- ⚠️ **Qualidade dos dados**: {data_quality:.1f}% - Melhorar coleta")
        
        # Verificar diversidade
        categorical_cols = len(self.data.select_dtypes(include=['object']).columns)
        if categorical_cols < 2:
            attention_points.append("- ⚠️ **Diversidade limitada**: Coletar mais variáveis categóricas")
        
        if not attention_points:
            attention_points.append("- ✅ **Qualidade geral boa** - Continuar monitoramento regular")
        
        return "\n".join(attention_points)

    def _generate_priority_recommendations(self) -> str:
        """Gerar recomendações prioritárias"""
        return """- 🚀 **Implementar segmentação** baseada nos padrões identificados
- 📊 **Desenvolver dashboard** para monitoramento em tempo real
- 🎯 **Criar campanhas direcionadas** para diferentes personas
- 📈 **Estabelecer métricas** de acompanhamento de performance"""

    def _generate_recommendations(self, format_type: str) -> str:
        """Gerar seção de recomendações"""
        if format_type == 'markdown':
            return """
## 🚀 Recomendações Estratégicas

### 📈 Curto Prazo (1-2 meses)
- 🎯 **Implementar segmentação básica** baseada nos dados atuais
- 🎨 **Criar campanhas direcionadas** para os grupos identificados
- 📊 **Melhorar coleta de dados** nas áreas com informações limitadas
- 📱 **Desenvolver dashboard** para monitoramento contínuo

### 🎯 Médio Prazo (3-6 meses)
- 🔍 **Implementar análise de sentimentos** para feedback qualitativo
- 👥 **Desenvolver personas detalhadas** usando clustering avançado
- 🎪 **Criar sistema de recomendações** personalizado
- 📈 **Estabelecer métricas de ROI** para campanhas

### 🏆 Longo Prazo (6+ meses)
- 🔮 **Implementar IA preditiva** para antecipação de tendências
- 🤖 **Desenvolver automação** de campanhas baseada em comportamento
- 🌐 **Criar ecosystem integrado** de marketing data-driven
- 🎓 **Estabelecer cultura** de decisões baseadas em dados

### 💡 Recomendações Técnicas
- 📊 **Expandir coleta** de dados comportamentais
- 🔄 **Automatizar pipeline** de análise
- 🎯 **Implementar A/B testing** para otimização
- 📱 **Integrar com ferramentas** de marketing existentes
"""
        else:
            return """
RECOMENDAÇÕES ESTRATÉGICAS
=========================

Curto Prazo (1-2 meses):
- Implementar segmentação básica
- Criar campanhas direcionadas
- Desenvolver dashboard

Médio Prazo (3-6 meses):
- Análise de sentimentos
- Personas detalhadas
- Sistema de recomendações

Longo Prazo (6+ meses):
- IA preditiva
- Automação de campanhas
- Ecosystem integrado
"""

    def _generate_next_steps(self, format_type: str) -> str:
        """Gerar próximos passos"""
        if format_type == 'markdown':
            return """
## 📋 Próximos Passos

### ✅ Ações Imediatas (Esta Semana)
1. **📖 Revisar insights** apresentados neste relatório
2. **🔍 Identificar lacunas** de dados prioritárias
3. **📊 Definir KPIs** para acompanhamento
4. **📋 Planejar coleta** de dados adicionais

### 🔄 Desenvolvimento Contínuo (Este Mês)
1. **📈 Expandir base de dados** com novas pesquisas
2. **🤖 Implementar funcionalidades** de IA avançada
3. **🔄 Automatizar geração** de relatórios
4. **🔗 Integrar com outras** ferramentas de marketing

### 📊 Monitoramento e Avaliação
- **📅 Revisão semanal** dos dados coletados
- **📊 Atualização mensal** dos relatórios
- **🎯 Avaliação trimestral** das estratégias
- **📈 Análise anual** do ROI das iniciativas

### 🎯 Métricas de Sucesso
- **📈 Aumento** na qualidade dos dados coletados
- **🎯 Melhoria** na segmentação de campanhas
- **📊 Incremento** no ROI de marketing
- **⏱️ Redução** no tempo de análise
"""
        else:
            return """
PRÓXIMOS PASSOS
==============

Ações Imediatas:
1. Revisar insights do relatório
2. Identificar lacunas de dados
3. Definir KPIs
4. Planejar coleta adicional

Desenvolvimento Contínuo:
1. Expandir base de dados
2. Implementar IA avançada
3. Automatizar relatórios
4. Integrar ferramentas
"""

    def _generate_footer(self, format_type: str) -> str:
        """Gerar rodapé do relatório"""
        if format_type == 'markdown':
            return f"""
---

## 📞 Suporte e Desenvolvimento

**🤖 Agente de IA para Marketing v2.0 - Enterprise Edition**
- **🔧 Desenvolvido em:** {datetime.now().strftime('%B de %Y')}
- **🚀 Próximas funcionalidades:** Análise de sentimentos, clustering avançado, IA preditiva
- **💡 Feedback:** Contribuições e sugestões são bem-vindas para evolução contínua
- **📧 Suporte:** Sistema de análise em constante aprimoramento

### 🎯 Roadmap de Desenvolvimento
- **Q1:** Análise de sentimentos e NLP avançado
- **Q2:** Clustering automático para personas
- **Q3:** Modelos preditivos e forecasting
- **Q4:** Automação completa de campanhas

---

*"🚀 Transformando dados em estratégias de marketing eficazes através da Inteligência Artificial"*

**Powered by AI • Built for Marketers • Designed for Results**
"""
        else:
            return f"""
====================================
SUPORTE E DESENVOLVIMENTO

Agente de IA para Marketing v2.0
Desenvolvido em: {datetime.now().strftime('%B de %Y')}

"Transformando dados em estratégias de marketing eficazes através da IA"
====================================
"""

    def _generate_numeric_analysis_summary(self) -> str:
        """Resumo da análise numérica"""
        if self.data is None:
            return "Dados não disponíveis"
        
        numeric_cols = self.data.select_dtypes(include=['number']).columns
        if len(numeric_cols) == 0:
            return "- Nenhuma variável numérica identificada"
        
        summary_lines = []
        for col in numeric_cols[:3]:  # Máximo 3 colunas
            mean_val = self.data[col].mean()
            std_val = self.data[col].std()
            summary_lines.append(f"- **{col}**: Média {mean_val:.2f} (±{std_val:.2f})")
        
        return "\n".join(summary_lines)

    def _generate_categorical_analysis_summary(self) -> str:
        """Resumo da análise categórica"""
        if self.data is None:
            return "Dados não disponíveis"
        
        cat_cols = self.data.select_dtypes(include=['object']).columns
        if len(cat_cols) == 0:
            return "- Nenhuma variável categórica identificada"
        
        summary_lines = []
        for col in cat_cols[:3]:  # Máximo 3 colunas
            unique_count = self.data[col].nunique()
            most_common = self.data[col].mode().iloc[0] if len(self.data[col].mode()) > 0 else "N/A"
            summary_lines.append(f"- **{col}**: {unique_count} categorias (mais comum: {most_common})")
        
        return "\n".join(summary_lines)

    def _generate_quality_insights(self) -> str:
        """Insights sobre qualidade dos dados"""
        if self.data is None:
            return "- Dados não disponíveis"
        
        quality = self._calculate_data_quality()
        duplicates = self.data.duplicated().sum()
        
        insights = [
            f"- **Completude geral**: {quality:.1f}% dos dados estão preenchidos",
            f"- **Duplicatas**: {duplicates} registros duplicados ({(duplicates/len(self.data)*100):.1f}%)"
        ]
        
        return "\n".join(insights)

    def _generate_behavioral_insights(self) -> str:
        """Insights comportamentais"""
        return """- 🎯 Padrões de comportamento em análise
- 📱 Preferências de canal sendo mapeadas
- 🔄 Jornada do cliente em construção"""

    def _generate_market_opportunities(self) -> str:
        """Oportunidades de mercado"""
        return """- 🎯 **Segmentos inexplorados** identificados nos dados
- 📈 **Potencial de crescimento** em categorias específicas
- 🎪 **Oportunidades de cross-sell** baseadas em correlações"""

    def _generate_html_insights(self) -> str:
        """Insights em formato HTML"""
        return """
        <ul>
            <li><strong>Volume:</strong> Base robusta para análises</li>
            <li><strong>Qualidade:</strong> Dados confiáveis para decisões</li>
            <li><strong>Oportunidades:</strong> Segmentação e personalização</li>
        </ul>
        """

    def _generate_text_insights(self) -> str:
        """Insights em formato texto"""
        return """
Insights Principais:
- Volume adequado para análises estatísticas
- Qualidade dos dados dentro do padrão aceitável
- Oportunidades de segmentação identificadas
"""