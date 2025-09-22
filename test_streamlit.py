import streamlit as st
import pandas as pd
import sys
import os

st.title("🧪 Teste do Agente Marketing")
st.write("### ✅ Streamlit funcionando!")

# Teste de imports
try:
    import plotly.express as px
    st.write("✅ Plotly importado com sucesso")
except:
    st.write("❌ Erro ao importar Plotly")

try:
    from utils.data_processor import DataProcessor
    st.write("✅ DataProcessor importado com sucesso")
except Exception as e:
    st.write(f"❌ Erro ao importar DataProcessor: {e}")

try:
    from analysis.basic_analysis import BasicAnalyzer
    st.write("✅ BasicAnalyzer importado com sucesso")
except Exception as e:
    st.write(f"❌ Erro ao importar BasicAnalyzer: {e}")

# Teste de dados simples
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 6, 8, 10]
})

st.write("### 📊 Teste de Visualização")
st.dataframe(df)

# Mostra informações do sistema
st.write("### 💻 Informações do Sistema")
st.write(f"- Python: {sys.version}")
st.write(f"- Diretório atual: {os.getcwd()}")
st.write(f"- Streamlit version: {st.__version__}")

st.success("🎉 Teste concluído! Sistema funcionando corretamente.")