"""
🤖 Agente de IA para Marketing - MVP
Versão inicial do sistema para análise de dados e geração de planos de marketing
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os
import sys

# Adicionar o diretório raiz ao path para imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from utils.data_processor import DataProcessor
    from analysis.basic_analysis import BasicAnalyzer
    from templates.report_generator import ReportGenerator
    from api.google_sheets import google_sheets_data_loader, create_sample_google_form_data
    from utils.helpers import generate_sample_data, show_dataframe_info, DataQualityChecker
except ImportError as e:
    st.error(f"Erro ao importar módulos: {e}")
    st.stop()

# Configuração da página
st.set_page_config(
    page_title="Agente de IA - Marketing",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("🤖 Agente de IA para Marketing")
    st.markdown("### Análise inteligente de dados para estratégias de marketing eficazes")
    
    # Sidebar
    with st.sidebar:
        st.header("📊 Configurações")
        
        # Seleção do tipo de análise
        analysis_type = st.selectbox(
            "Tipo de Análise",
            ["Análise Básica", "Análise de Sentimentos", "Geração de Personas", "Plano Completo"]
        )
        
        # Upload de arquivos
        st.subheader("📁 Upload de Dados")
        
        data_source = st.radio(
            "Fonte dos dados:",
            ["Upload de arquivo", "Google Sheets", "Dados de exemplo"]
        )
        
        uploaded_file = None
        
        if data_source == "Upload de arquivo":
            uploaded_file = st.file_uploader(
                "Escolha um arquivo CSV ou Excel",
                type=['csv', 'xlsx', 'xls'],
                help="Faça upload dos dados de pesquisa do Google Forms ou dados offline"
            )
        
        elif data_source == "Google Sheets":
            st.info("📊 Configure o Google Sheets na seção abaixo")
        
        else:  # Dados de exemplo
            st.info("📋 Usando dados de exemplo para demonstração")
        
        # Opções avançadas
        if st.checkbox("Opções Avançadas"):
            st.slider("Número de Clusters (Personas)", 2, 10, 3)
            st.multiselect("Colunas para Análise", ["Todas"], default=["Todas"])
    
    # Área principal
    df = None
    
    # Carregar dados baseado na fonte selecionada
    with st.sidebar:
        data_source = st.radio(
            "Fonte dos dados:",
            ["Upload de arquivo", "Google Sheets", "Dados de exemplo"]
        )
        
        if data_source == "Upload de arquivo":
            uploaded_file = st.file_uploader(
                "Escolha um arquivo CSV ou Excel",
                type=['csv', 'xlsx', 'xls'],
                help="Faça upload dos dados de pesquisa do Google Forms ou dados offline"
            )
            if uploaded_file is not None:
                df = load_data(uploaded_file)
        
        elif data_source == "Google Sheets":
            df = google_sheets_data_loader()
        
        else:  # Dados de exemplo
            if st.button("📋 Carregar Dados de Exemplo"):
                df = generate_sample_data()
                st.success("✅ Dados de exemplo carregados!")
    
    if df is not None:
        try:
            # Verificar qualidade dos dados
            quality_checker = DataQualityChecker(df)
            quality_info = quality_checker.check_quality()
            
            st.success(f"✅ Dados carregados: {len(df)} registros")
            
            # Mostrar qualidade dos dados
            if quality_info["quality_score"] < 60:
                st.warning(f"⚠️ Qualidade dos dados: {quality_info['quality_score']}/100")
            else:
                st.info(f"📊 Qualidade dos dados: {quality_info['quality_score']}/100")
            
            # Tabs para diferentes visualizações
            tab1, tab2, tab3, tab4 = st.tabs(["📈 Dados", "🔍 Análise", "👤 Personas", "📄 Relatório"])
            
            with tab1:
                show_data_overview(df, quality_info)
            
            with tab2:
                show_analysis(df, analysis_type)
            
            with tab3:
                show_personas(df)
            
            with tab4:
                show_report_generation(df)
                
        except Exception as e:
            st.error(f"❌ Erro ao processar dados: {str(e)}")
            st.info("💡 Verifique se o arquivo está no formato correto")
    
    else:
        # Página inicial sem dados
        show_welcome_page()

def load_data(uploaded_file):
    """Carregar dados do arquivo uploadado"""
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        return df
    except Exception as e:
        st.error(f"Erro ao carregar arquivo: {str(e)}")
        return None

def show_welcome_page():
    """Página de boas-vindas"""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        ## 🎯 Como Usar
        
        1. **📁 Upload**: Faça upload de seus dados de pesquisa (CSV ou Excel)
        2. **🔍 Análise**: Escolha o tipo de análise desejada
        3. **📊 Insights**: Visualize os resultados e insights automáticos
        4. **📄 Relatório**: Gere um plano de marketing personalizado
        
        ### 📋 Formatos Suportados
        - Respostas do Google Forms (CSV)
        - Planilhas Excel personalizadas
        - Dados de pesquisas offline
        
        ### 🚀 Funcionalidades MVP
        - ✅ Análise descritiva básica
        - ✅ Visualizações interativas
        - ✅ Detecção automática de padrões
        - ✅ Geração de relatório inicial
        """)
        
        # Exemplo de dados
        if st.button("📋 Ver Exemplo de Dados"):
            show_sample_data()

def show_data_overview(df, quality_info=None):
    """Mostrar visão geral dos dados"""
    st.subheader("📊 Visão Geral dos Dados")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total de Registros", len(df))
    
    with col2:
        st.metric("Colunas", len(df.columns))
    
    with col3:
        st.metric("Dados Únicos", len(df.drop_duplicates()))
    
    with col4:
        missing_percentage = (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
        st.metric("Dados Faltantes", f"{missing_percentage:.1f}%")
    
    # Mostrar qualidade dos dados se disponível
    if quality_info:
        st.subheader("🔍 Qualidade dos Dados")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if quality_info["issues"]:
                st.warning("⚠️ **Problemas encontrados:**")
                for issue in quality_info["issues"]:
                    st.write(f"• {issue}")
            else:
                st.success("✅ Nenhum problema crítico encontrado")
        
        with col2:
            if quality_info["recommendations"]:
                st.info("💡 **Recomendações:**")
                for rec in quality_info["recommendations"]:
                    st.write(f"• {rec}")
    
    # Preview dos dados
    st.subheader("👀 Preview dos Dados")
    st.dataframe(df.head(10), use_container_width=True)
    
    # Informações das colunas
    st.subheader("📋 Informações das Colunas")
    col_info = pd.DataFrame({
        'Coluna': df.columns,
        'Tipo': df.dtypes,
        'Valores Únicos': [df[col].nunique() for col in df.columns],
        'Nulos': [df[col].isnull().sum() for col in df.columns],
        'Nulos (%)': [(df[col].isnull().sum() / len(df) * 100).round(2) for col in df.columns]
    })
    st.dataframe(col_info, use_container_width=True)

def show_analysis(df, analysis_type):
    """Mostrar análises dos dados"""
    st.subheader(f"🔍 {analysis_type}")
    
    if analysis_type == "Análise Básica":
        show_basic_analysis(df)
    elif analysis_type == "Análise de Sentimentos":
        show_sentiment_analysis(df)
    elif analysis_type == "Geração de Personas":
        show_persona_generation(df)
    else:
        st.info("Funcionalidade em desenvolvimento...")

def show_basic_analysis(df):
    """Análise básica dos dados"""
    # Detectar colunas numéricas e categóricas
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    if numeric_cols:
        st.subheader("📈 Análise Numérica")
        selected_numeric = st.selectbox("Selecione uma coluna numérica", numeric_cols)
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig_hist = px.histogram(df, x=selected_numeric, title=f"Distribuição de {selected_numeric}")
            st.plotly_chart(fig_hist, use_container_width=True)
        
        with col2:
            fig_box = px.box(df, y=selected_numeric, title=f"Box Plot de {selected_numeric}")
            st.plotly_chart(fig_box, use_container_width=True)
    
    if categorical_cols:
        st.subheader("📊 Análise Categórica")
        selected_categorical = st.selectbox("Selecione uma coluna categórica", categorical_cols)
        
        # Contagem de valores
        value_counts = df[selected_categorical].value_counts().head(10)
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig_bar = px.bar(x=value_counts.index, y=value_counts.values, 
                           title=f"Top 10 valores de {selected_categorical}")
            st.plotly_chart(fig_bar, use_container_width=True)
        
        with col2:
            fig_pie = px.pie(values=value_counts.values, names=value_counts.index,
                           title=f"Distribuição de {selected_categorical}")
            st.plotly_chart(fig_pie, use_container_width=True)

def show_sentiment_analysis(df):
    """Análise de sentimentos (placeholder)"""
    st.info("🔧 Funcionalidade em desenvolvimento")
    st.markdown("""
    ### Próximas implementações:
    - Análise de sentimentos em texto livre
    - Detecção de temas principais
    - Classificação automática de feedback
    """)

def show_persona_generation(df):
    """Geração de personas (placeholder)"""
    st.info("🔧 Funcionalidade em desenvolvimento")
    st.markdown("""
    ### Próximas implementações:
    - Clustering automático de usuários
    - Geração de personas baseadas em dados
    - Perfis detalhados com características
    """)

def show_personas(df):
    """Tab de personas"""
    st.subheader("👤 Análise de Personas")
    st.info("Funcionalidade será implementada na Fase 2")

def show_report_generation(df):
    """Tab de geração de relatório"""
    st.subheader("📄 Geração de Relatório")
    
    if st.button("🚀 Gerar Relatório Básico"):
        with st.spinner("Gerando relatório..."):
            report = generate_basic_report(df)
            st.success("✅ Relatório gerado!")
            
            # Mostrar relatório
            st.markdown(report)
            
            # Opção de download
            st.download_button(
                label="📥 Download do Relatório",
                data=report,
                file_name=f"relatorio_marketing_{datetime.now().strftime('%Y%m%d_%H%M')}.md",
                mime="text/markdown"
            )

def generate_basic_report(df):
    """Gerar relatório básico"""
    # Usar o ReportGenerator
    report_gen = ReportGenerator()
    report_gen.set_data(df)
    
    # Gerar análises básicas
    analyzer = BasicAnalyzer()
    analyzer.set_data(df)
    insights = analyzer.generate_insights()
    
    # Gerar relatório completo
    full_report = report_gen.generate_full_report()
    
    return full_report

def show_sample_data():
    """Mostrar dados de exemplo"""
    sample_data = {
        'Nome': ['João Silva', 'Maria Santos', 'Pedro Costa'],
        'Idade': [25, 34, 28],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte'],
        'Interesse': ['Tecnologia', 'Moda', 'Esportes'],
        'Satisfacao': [8, 9, 7],
        'Recomendaria': ['Sim', 'Sim', 'Talvez']
    }
    
    st.subheader("📋 Exemplo de Estrutura de Dados")
    st.dataframe(pd.DataFrame(sample_data))
    
    st.markdown("""
    **Colunas sugeridas para seus dados:**
    - Dados demográficos (idade, cidade, gênero)
    - Preferências e interesses
    - Avaliações e feedback
    - Comportamento de compra
    - Canais de comunicação preferidos
    """)

if __name__ == "__main__":
    main()