"""
Gerador de Relatórios - Templates e geração automática de documentos
"""
import pandas as pd
from datetime import datetime
from typing import Dict, List, Optional
import os

class ReportGenerator:
    """Classe para geração de relatórios de marketing"""
    
    def __init__(self):
        self.data = None
        self.insights = {}
        self.template_dir = "templates"
    
    def set_data(self, df: pd.DataFrame, insights: Dict = None):
        """Definir dados e insights para o relatório"""
        self.data = df.copy()
        self.insights = insights or {}
    
    def generate_executive_summary(self) -> str:
        """Gerar resumo executivo"""
        if self.data is None:
            return "Dados não disponíveis para gerar resumo."
        
        total_records = len(self.data)
        date_generated = datetime.now().strftime('%d/%m/%Y às %H:%M')
        data_quality = self._calculate_data_quality()
        
        summary = f"""
# 📊 Resumo Executivo - Análise de Marketing

**Data de Geração:** {date_generated}
**Total de Registros:** {total_records:,}
**Qualidade dos Dados:** {data_quality:.1f}%

## 🎯 Principais Descobertas

### 📈 Volume e Qualidade
- Análise baseada em **{total_records:,} respostas** coletadas
- Dados **{data_quality:.1f}% completos** - {'Excelente' if data_quality > 90 else 'Boa' if data_quality > 80 else 'Aceitável' if data_quality > 70 else 'Baixa'} qualidade
- **{len(self.data.columns)} dimensões** diferentes analisadas

### 🔍 Insights Demográficos
{self._generate_demographic_insights()}

### 💡 Oportunidades Identificadas
{self._generate_opportunities()}

### ⚠️ Pontos de Atenção
{self._generate_attention_points()}
"""
        return summary
    
    def generate_full_report(self) -> str:
        """Gerar relatório completo"""
        report_sections = [
            self._generate_header(),
            self.generate_executive_summary(),
            self._generate_methodology(),
            self._generate_data_analysis(),
            self._generate_insights_section(),
            self._generate_recommendations(),
            self._generate_next_steps(),
            self._generate_footer()
        ]
        
        return "\n\n".join(report_sections)
    
    def _generate_header(self) -> str:
        """Gerar cabeçalho do relatório"""
        return f"""
# 🤖 Relatório de Análise de Marketing
## Insights Baseados em Dados para Estratégias Eficazes

**Agente de IA para Marketing v1.0**
**Gerado em:** {datetime.now().strftime('%d de %B de %Y às %H:%M')}

---
"""
    
    def _generate_methodology(self) -> str:
        """Gerar seção de metodologia"""
        return """
## 📋 Metodologia

### Coleta de Dados
- **Fonte:** Pesquisas online e dados offline
- **Período:** Dados mais recentes disponíveis
- **Método:** Análise automatizada com IA

### Técnicas de Análise
- ✅ Estatística descritiva
- ✅ Análise de padrões
- ✅ Detecção de outliers
- ✅ Análise de correlações
- 🔄 Análise de sentimentos (em desenvolvimento)
- 🔄 Clustering para personas (em desenvolvimento)

### Qualidade dos Dados
- Limpeza automática de dados
- Padronização de respostas
- Tratamento de valores ausentes
- Validação de consistência
"""
    
    def _generate_data_analysis(self) -> str:
        """Gerar seção de análise de dados"""
        if self.data is None:
            return "Dados não disponíveis para análise."
        
        numeric_cols = self.data.select_dtypes(include=['number']).columns.tolist()
        categorical_cols = self.data.select_dtypes(include=['object']).columns.tolist()
        
        analysis = f"""
## 📊 Análise dos Dados

### 📈 Variáveis Numéricas ({len(numeric_cols)} encontradas)
{self._analyze_numeric_variables(numeric_cols)}

### 📋 Variáveis Categóricas ({len(categorical_cols)} encontradas)
{self._analyze_categorical_variables(categorical_cols)}

### 🔗 Correlações e Padrões
{self._analyze_correlations()}
"""
        return analysis
    
    def _analyze_numeric_variables(self, numeric_cols: List[str]) -> str:
        """Analisar variáveis numéricas"""
        if not numeric_cols:
            return "- Nenhuma variável numérica encontrada"
        
        analysis = ""
        for col in numeric_cols[:5]:  # Limitar a 5 colunas
            mean_val = self.data[col].mean()
            std_val = self.data[col].std()
            analysis += f"- **{col.title()}**: Média {mean_val:.2f} (±{std_val:.2f})\n"
        
        if len(numeric_cols) > 5:
            analysis += f"- ... e mais {len(numeric_cols) - 5} variáveis\n"
        
        return analysis
    
    def _analyze_categorical_variables(self, categorical_cols: List[str]) -> str:
        """Analisar variáveis categóricas"""
        if not categorical_cols:
            return "- Nenhuma variável categórica encontrada"
        
        analysis = ""
        for col in categorical_cols[:5]:  # Limitar a 5 colunas
            unique_count = self.data[col].nunique()
            most_common = self.data[col].mode().iloc[0] if len(self.data[col].mode()) > 0 else "N/A"
            analysis += f"- **{col.title()}**: {unique_count} valores únicos, mais comum: '{most_common}'\n"
        
        if len(categorical_cols) > 5:
            analysis += f"- ... e mais {len(categorical_cols) - 5} variáveis\n"
        
        return analysis
    
    def _analyze_correlations(self) -> str:
        """Analisar correlações"""
        numeric_data = self.data.select_dtypes(include=['number'])
        
        if len(numeric_data.columns) < 2:
            return "- Dados insuficientes para análise de correlação"
        
        corr_matrix = numeric_data.corr()
        
        # Encontrar correlações fortes
        strong_corr_count = 0
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                if abs(corr_matrix.iloc[i, j]) > 0.7:
                    strong_corr_count += 1
        
        return f"- Encontradas **{strong_corr_count} correlações fortes** entre variáveis\n- Matriz de correlação disponível para análise detalhada"
    
    def _generate_insights_section(self) -> str:
        """Gerar seção de insights"""
        return f"""
## 💡 Insights Principais

### 🎯 Público-Alvo
{self._generate_target_audience_insights()}

### 📊 Comportamento do Cliente
{self._generate_behavior_insights()}

### 🏆 Oportunidades de Mercado
{self._generate_market_opportunities()}

### ⚡ Pontos de Melhoria
{self._generate_improvement_points()}
"""
    
    def _generate_target_audience_insights(self) -> str:
        """Gerar insights sobre público-alvo"""
        insights = []
        
        # Procurar colunas de idade
        age_cols = [col for col in self.data.columns if 'idade' in col.lower() or 'age' in col.lower()]
        if age_cols:
            age_mean = self.data[age_cols[0]].mean()
            insights.append(f"- Idade média do público: **{age_mean:.1f} anos**")
        
        # Procurar colunas de localização
        location_cols = [col for col in self.data.columns if any(word in col.lower() for word in ['cidade', 'estado', 'region', 'location'])]
        if location_cols:
            top_location = self.data[location_cols[0]].mode().iloc[0] if len(self.data[location_cols[0]].mode()) > 0 else "N/A"
            insights.append(f"- Principal região: **{top_location}**")
        
        if not insights:
            insights.append("- Dados demográficos limitados - recomendar coleta adicional")
        
        return "\n".join(insights)
    
    def _generate_behavior_insights(self) -> str:
        """Gerar insights sobre comportamento"""
        insights = []
        
        # Procurar colunas de satisfação
        satisfaction_cols = [col for col in self.data.columns 
                           if any(word in col.lower() for word in ['satisfação', 'satisfaction', 'nota', 'rating'])]
        
        if satisfaction_cols:
            for col in satisfaction_cols[:2]:  # Máximo 2 colunas
                if pd.api.types.is_numeric_dtype(self.data[col]):
                    avg_satisfaction = self.data[col].mean()
                    max_possible = self.data[col].max()
                    percentage = (avg_satisfaction / max_possible) * 100 if max_possible > 0 else 0
                    insights.append(f"- Satisfação em {col}: **{avg_satisfaction:.1f}/{max_possible:.0f}** ({percentage:.1f}%)")
        
        if not insights:
            insights.append("- Dados comportamentais limitados - implementar métricas de engajamento")
        
        return "\n".join(insights)
    
    def _generate_market_opportunities(self) -> str:
        """Gerar oportunidades de mercado"""
        opportunities = [
            "- **Segmentação por perfil**: Desenvolver personas baseadas nos dados coletados",
            "- **Personalização**: Criar campanhas direcionadas para diferentes grupos",
            "- **Canais preferenciais**: Identificar meios de comunicação mais eficazes"
        ]
        
        # Adicionar oportunidades baseadas nos dados
        if len(self.data) > 100:
            opportunities.append("- **Análise preditiva**: Volume de dados suficiente para modelagem avançada")
        
        return "\n".join(opportunities)
    
    def _generate_improvement_points(self) -> str:
        """Gerar pontos de melhoria"""
        improvements = []
        
        # Verificar qualidade dos dados
        data_quality = self._calculate_data_quality()
        if data_quality < 85:
            improvements.append(f"- **Qualidade dos dados**: Melhorar coleta (atual: {data_quality:.1f}%)")
        
        # Verificar tamanho da amostra
        if len(self.data) < 100:
            improvements.append("- **Tamanho da amostra**: Aumentar número de respondentes")
        
        # Verificar diversidade de dados
        categorical_cols = self.data.select_dtypes(include=['object']).columns.tolist()
        if len(categorical_cols) < 3:
            improvements.append("- **Diversidade de dados**: Coletar mais variáveis categóricas")
        
        if not improvements:
            improvements.append("- **Otimização contínua**: Implementar coleta automática e análise em tempo real")
        
        return "\n".join(improvements)
    
    def _generate_recommendations(self) -> str:
        """Gerar recomendações"""
        return """
## 🚀 Recomendações Estratégicas

### 📈 Curto Prazo (1-2 meses)
- **Implementar segmentação básica** baseada nos dados atuais
- **Criar campanhas direcionadas** para os grupos identificados
- **Melhorar coleta de dados** nas áreas com informações limitadas
- **Desenvolver dashboard** para monitoramento contínuo

### 🎯 Médio Prazo (3-6 meses)
- **Implementar análise de sentimentos** para feedback qualitativo
- **Desenvolver personas detalhadas** usando clustering avançado
- **Criar sistema de recomendações** personalizado
- **Estabelecer métricas de ROI** para campanhas

### 🏆 Longo Prazo (6+ meses)
- **Implementar IA preditiva** para antecipação de tendências
- **Desenvolver automação** de campanhas baseada em comportamento
- **Criar ecosystem integrado** de marketing data-driven
- **Estabelecer cultura** de decisões baseadas em dados
"""
    
    def _generate_next_steps(self) -> str:
        """Gerar próximos passos"""
        return """
## 📋 Próximos Passos

### ✅ Ações Imediatas
1. **Revisar insights** apresentados neste relatório
2. **Identificar lacunas** de dados prioritárias
3. **Definir KPIs** para acompanhamento
4. **Planejar coleta** de dados adicionais

### 🔄 Desenvolvimento Contínuo
1. **Expandir base de dados** com novas pesquisas
2. **Implementar funcionalidades** de IA avançada
3. **Automatizar geração** de relatórios
4. **Integrar com outras** ferramentas de marketing

### 📊 Monitoramento
- **Revisão mensal** dos dados e insights
- **Atualização trimestral** das estratégias
- **Avaliação anual** do ROI das iniciativas
"""
    
    def _generate_footer(self) -> str:
        """Gerar rodapé do relatório"""
        return f"""
---

## 📞 Suporte e Contato

**Agente de IA para Marketing v1.0**
- **Desenvolvido em:** {datetime.now().strftime('%B de %Y')}
- **Próxima atualização:** Análise de sentimentos e clustering avançado
- **Feedback:** Contribuições e sugestões são bem-vindas para melhorar as análises

*"Transformando dados em estratégias de marketing eficazes através da Inteligência Artificial"*
"""
    
    def _calculate_data_quality(self) -> float:
        """Calcular qualidade dos dados"""
        if self.data is None:
            return 0.0
        
        total_cells = len(self.data) * len(self.data.columns)
        missing_cells = self.data.isnull().sum().sum()
        quality = ((total_cells - missing_cells) / total_cells) * 100
        
        return quality
    
    def _generate_demographic_insights(self) -> str:
        """Gerar insights demográficos"""
        insights = []
        
        # Procurar informações demográficas
        demo_keywords = ['idade', 'age', 'sexo', 'gender', 'cidade', 'city', 'estado', 'state']
        demo_cols = [col for col in self.data.columns 
                    if any(keyword in col.lower() for keyword in demo_keywords)]
        
        if demo_cols:
            insights.append(f"- **{len(demo_cols)} variáveis demográficas** identificadas")
            
            for col in demo_cols[:3]:  # Máximo 3 colunas
                unique_count = self.data[col].nunique()
                insights.append(f"- {col.title()}: {unique_count} categorias diferentes")
        else:
            insights.append("- Dados demográficos limitados - recomendar expansão da coleta")
        
        return "\n".join(insights)
    
    def _generate_opportunities(self) -> str:
        """Gerar oportunidades"""
        opportunities = [
            "- **Segmentação inteligente** baseada em padrões identificados",
            "- **Personalização** de campanhas por perfil de cliente",
            "- **Otimização** de canais de comunicação mais eficazes"
        ]
        
        if len(self.data) > 200:
            opportunities.append("- **Modelagem preditiva** para antecipação de comportamentos")
        
        return "\n".join(opportunities)
    
    def _generate_attention_points(self) -> str:
        """Gerar pontos de atenção"""
        attention_points = []
        
        # Verificar tamanho da amostra
        if len(self.data) < 50:
            attention_points.append("- **Amostra pequena**: Resultados podem não ser representativos")
        
        # Verificar qualidade dos dados
        data_quality = self._calculate_data_quality()
        if data_quality < 80:
            attention_points.append(f"- **Qualidade dos dados**: {data_quality:.1f}% - Melhorar coleta")
        
        # Verificar diversidade
        categorical_cols = len(self.data.select_dtypes(include=['object']).columns)
        if categorical_cols < 2:
            attention_points.append("- **Diversidade limitada**: Coletar mais variáveis categóricas")
        
        if not attention_points:
            attention_points.append("- **Qualidade geral boa** - Continuar monitoramento regular")
        
        return "\n".join(attention_points)