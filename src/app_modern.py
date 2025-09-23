"""
Configuração principal do aplicativo Streamlit modernizado
Estrutura enterprise para o Agente Marketing IA
"""

import streamlit as st
import pandas as pd
from pathlib import Path
import sys
import os

# Adicionar src ao path para imports
PROJECT_ROOT = Path(__file__).parent.parent
SRC_PATH = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_PATH))

# Imports dos serviços modernos
try:
    from services.data.dataProcessor import DataProcessor
    from services.analysis.analysisService import AnalysisService
    from services.reporting.reportingService import ReportingService
    from components.widgets.DataUploader import DataUploader
    from components.charts.ChartRenderer import ChartRenderer
    MODERN_SERVICES = True
    st.success("✅ Serviços Enterprise carregados")
except ImportError:
    # Fallback para estrutura legacy
    sys.path.insert(0, str(PROJECT_ROOT))
    from utils.data_processor import DataProcessor
    from analysis.basic_analysis import BasicAnalyzer as AnalysisService
    from templates.report_generator import ReportGenerator as ReportingService
    MODERN_SERVICES = False
    st.warning("⚠️ Usando serviços legados")
    
    # Componentes simples para fallback
    class DataUploader:
        @staticmethod
        def render():
            return st.file_uploader("Choose a CSV file", type="csv")
    
    class ChartRenderer:
        @staticmethod
        def render_plotly_chart(fig):
            return st.plotly_chart(fig, use_container_width=True)

# Configuração da página
st.set_page_config(
    page_title="🤖 Agente Marketing IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """Função principal da aplicação"""
    
    # Header principal
    st.title("🤖 Agente de IA para Marketing")
    st.markdown("### 📊 Análise Inteligente de Dados de Marketing")
    
    # Sidebar para configurações
    with st.sidebar:
        st.header("⚙️ Configurações")
        st.info("**Versão Enterprise** 🚀\nEstrutura modular implementada")
        
        # Upload de dados
        st.subheader("📤 Upload de Dados")
        uploaded_file = DataUploader.render()
        
        if uploaded_file is not None:
            st.success("✅ Arquivo carregado!")
    
    # Conteúdo principal em tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Visão Geral", 
        "🔍 Análise", 
        "👥 Personas", 
        "📋 Relatórios"
    ])
    
    with tab1:
        render_overview_tab(uploaded_file)
    
    with tab2:
        render_analysis_tab(uploaded_file)
    
    with tab3:
        render_personas_tab(uploaded_file)
    
    with tab4:
        render_reports_tab(uploaded_file)

def render_overview_tab(uploaded_file):
    """Renderiza aba de visão geral"""
    st.header("📊 Visão Geral dos Dados")
    
    if uploaded_file is None:
        st.info("👆 Faça upload de um arquivo CSV para começar")
        show_demo_data()
        return
    
    # Processar dados
    try:
        processor = DataProcessor()
        data = processor.load_csv_data(uploaded_file)
        
        # Métricas principais
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("📊 Total de Registros", len(data))
        
        with col2:
            st.metric("📋 Colunas", len(data.columns))
        
        with col3:
            st.metric("🔍 Dados Válidos", len(data.dropna()))
        
        with col4:
            missing_pct = (data.isnull().sum().sum() / (len(data) * len(data.columns))) * 100
            st.metric("⚠️ Dados Faltantes", f"{missing_pct:.1f}%")
        
        # Preview dos dados
        st.subheader("🔍 Preview dos Dados")
        st.dataframe(data.head(), use_container_width=True)
        
    except Exception as e:
        st.error(f"❌ Erro ao processar dados: {e}")

def render_analysis_tab(uploaded_file):
    """Renderiza aba de análise"""
    st.header("🔍 Análise Detalhada")
    
    if uploaded_file is None:
        st.info("👆 Faça upload de um arquivo CSV para análise")
        return
    
    try:
        processor = DataProcessor()
        data = processor.load_csv_data(uploaded_file)
        
        analyzer = AnalysisService()
        analyzer.set_data(data)
        insights = analyzer.generate_insights()
        
        st.subheader("💡 Insights Automáticos")
        for insight in insights:
            st.success(f"✨ {insight}")
        
        # Gráficos de análise
        st.subheader("📈 Visualizações")
        numeric_columns = data.select_dtypes(include=['number']).columns
        
        if len(numeric_columns) >= 2:
            import plotly.express as px
            fig = px.scatter(data, x=numeric_columns[0], y=numeric_columns[1])
            ChartRenderer.render_plotly_chart(fig)
        
    except Exception as e:
        st.error(f"❌ Erro na análise: {e}")

def render_personas_tab(uploaded_file):
    """Renderiza aba de personas"""
    st.header("👥 Personas de Cliente")
    
    if uploaded_file is None:
        st.info("👆 Faça upload de um arquivo CSV para gerar personas")
        return
    
    st.info("🔄 Funcionalidade em desenvolvimento")
    st.markdown("""
    **Próximas implementações:**
    - Segmentação automática de clientes
    - Geração de personas baseada em dados
    - Análise de comportamento
    - Recomendações personalizadas
    """)

def render_reports_tab(uploaded_file):
    """Renderiza aba de relatórios"""
    st.header("📋 Geração de Relatórios")
    
    if uploaded_file is None:
        st.info("👆 Faça upload de um arquivo CSV para gerar relatórios")
        return
    
    try:
        processor = DataProcessor()
        data = processor.load_csv_data(uploaded_file)
        
        report_generator = ReportingService()
        report_generator.set_data(data)
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📄 Gerar Relatório Executivo"):
                report = report_generator.generate_executive_summary()
                st.markdown(report)
        
        with col2:
            if st.button("📊 Relatório Completo"):
                report = report_generator.generate_full_report()
                st.markdown(report)
        
    except Exception as e:
        st.error(f"❌ Erro ao gerar relatório: {e}")

def show_demo_data():
    """Mostra dados de demonstração"""
    st.subheader("🎯 Dados de Demonstração")
    
    # Seletor de tipo de demo
    demo_type = st.selectbox(
        "📊 Escolha o tipo de demonstração:",
        ["Dados Gerais", "🎯 Representante Comercial - Canais de Vendas"],
        key="demo_selector"
    )
    
    if demo_type == "Dados Gerais":
        # Criar dados de exemplo gerais
        demo_data = pd.DataFrame({
            'Cliente': [f'Cliente_{i}' for i in range(1, 11)],
            'Idade': [25, 30, 35, 28, 42, 38, 29, 33, 27, 31],
            'Valor_Compra': [150, 200, 180, 220, 300, 250, 170, 190, 160, 210],
            'Categoria': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C']
        })
        
        st.dataframe(demo_data, use_container_width=True)
        
        # Gráfico de exemplo
        import plotly.express as px
        fig = px.bar(demo_data, x='Cliente', y='Valor_Compra', color='Categoria')
        st.plotly_chart(fig, use_container_width=True)
    
    else:
        # Demo específico para Representante Comercial
        show_sales_channel_demo()

def show_sales_channel_demo():
    """Demo específico para representante comercial"""
    st.markdown("### 🎯 **Demo: Gestão de Canais de Vendas**")
    st.info("💼 **Cenário:** Representante comercial especializado em vendas para Governo, E-commerce e Automação de Leads")
    
    # Dados demo para representante comercial
    demo_vendas = pd.DataFrame({
        'Data': ['2024-01-15', '2024-01-20', '2024-02-01', '2024-02-15', '2024-03-01', 
                '2024-03-10', '2024-04-05', '2024-04-20', '2024-05-10', '2024-06-01'],
        'Canal': ['Governo', 'E-commerce', 'E-commerce', 'Automação', 'Governo', 
                 'Automação', 'E-commerce', 'Governo', 'Automação', 'Governo'],
        'Tipo_Cliente': ['Prefeitura', 'Startup', 'PME', 'Empresa_Media', 'Estado',
                        'Grande_Empresa', 'PME', 'Municipio', 'Startup', 'Federal'],
        'Valor_Negocio': [250000, 45000, 25000, 35000, 180000, 75000, 22000, 195000, 48000, 500000],
        'Status': ['Fechado', 'Fechado', 'Fechado', 'Fechado', 'Negociando', 
                  'Fechado', 'Fechado', 'Negociando', 'Fechado', 'Negociando'],
        'ROI': [1.8, 2.1, 2.8, 2.3, 1.5, 2.0, 2.7, 1.4, 2.1, 1.8],
        'Tempo_Conversao': [120, 30, 15, 45, 90, 50, 20, 100, 30, 180]
    })
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_vendas = demo_vendas[demo_vendas['Status'] == 'Fechado']['Valor_Negocio'].sum()
        st.metric("💰 Vendas Fechadas", f"R$ {total_vendas:,.0f}")
    
    with col2:
        pipeline = demo_vendas[demo_vendas['Status'] == 'Negociando']['Valor_Negocio'].sum()
        st.metric("🔄 Pipeline Ativo", f"R$ {pipeline:,.0f}")
    
    with col3:
        roi_medio = demo_vendas[demo_vendas['Status'] == 'Fechado']['ROI'].mean()
        st.metric("📈 ROI Médio", f"{roi_medio:.1f}x")
    
    with col4:
        tempo_medio = demo_vendas[demo_vendas['Status'] == 'Fechado']['Tempo_Conversao'].mean()
        st.metric("⏱️ Tempo Médio", f"{tempo_medio:.0f} dias")
    
    # Gráficos por canal
    col1, col2 = st.columns(2)
    
    with col1:
        # Vendas por canal
        import plotly.express as px
        vendas_canal = demo_vendas.groupby('Canal')['Valor_Negocio'].sum().reset_index()
        fig_canal = px.pie(vendas_canal, values='Valor_Negocio', names='Canal', 
                          title="💰 Distribuição de Vendas por Canal")
        st.plotly_chart(fig_canal, use_container_width=True)
    
    with col2:
        # ROI por canal
        roi_canal = demo_vendas[demo_vendas['Status'] == 'Fechado'].groupby('Canal')['ROI'].mean().reset_index()
        fig_roi = px.bar(roi_canal, x='Canal', y='ROI', 
                        title="📈 ROI Médio por Canal",
                        color='ROI', color_continuous_scale='RdYlGn')
        st.plotly_chart(fig_roi, use_container_width=True)
    
    # Insights específicos
    st.markdown("### 💡 **Insights Gerados:**")
    
    insights = [
        "🏆 **Canal Governo** tem maior ticket médio (R$ 281.250) mas ciclo mais longo (130 dias)",
        "⚡ **Canal E-commerce** oferece conversão mais rápida (22 dias) com bom ROI (2.5x)",
        "🎯 **Canal Automação** apresenta melhor ROI (2.1x) e equilibrio tempo/valor",
        "📊 **Pipeline de R$ 875.000** em negociação concentrado no setor governamental",
        "🚀 **Recomendação:** Intensificar automação e otimizar processos do canal governo"
    ]
    
    for insight in insights:
        st.success(insight)
    
    # Mostrar dados detalhados
    with st.expander("📋 Ver dados detalhados do demo"):
        st.dataframe(demo_vendas)

if __name__ == "__main__":
    main()