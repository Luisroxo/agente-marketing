"""
Integração com Google Sheets API
"""
import pandas as pd
from typing import Optional, List, Dict, Any
import streamlit as st
import json
import os

# Try to import gspread, handle if not available
try:
    import gspread
    from google.oauth2.service_account import Credentials
    GSPREAD_AVAILABLE = True
except ImportError:
    GSPREAD_AVAILABLE = False

class GoogleSheetsIntegration:
    """Classe para integração com Google Sheets"""
    
    def __init__(self):
        self.gc = None
        self.credentials = None
        self.is_authenticated = False
    
    def authenticate(self, credentials_dict: Optional[Dict] = None, 
                    credentials_file: Optional[str] = None) -> bool:
        """Autenticar com Google Sheets API"""
        if not GSPREAD_AVAILABLE:
            st.error("📦 gspread não está instalado. Execute: pip install gspread google-auth")
            return False
        
        try:
            # Definir scopes necessários
            scopes = [
                "https://spreadsheets.google.com/feeds",
                "https://www.googleapis.com/auth/drive"
            ]
            
            # Tentar autenticar com credenciais fornecidas
            if credentials_dict:
                self.credentials = Credentials.from_service_account_info(
                    credentials_dict, scopes=scopes
                )
            elif credentials_file and os.path.exists(credentials_file):
                self.credentials = Credentials.from_service_account_file(
                    credentials_file, scopes=scopes
                )
            else:
                st.warning("🔑 Credenciais do Google não configuradas")
                return False
            
            # Inicializar cliente
            self.gc = gspread.authorize(self.credentials)
            self.is_authenticated = True
            
            st.success("✅ Conectado ao Google Sheets!")
            return True
            
        except Exception as e:
            st.error(f"❌ Erro na autenticação: {str(e)}")
            return False
    
    def list_spreadsheets(self, limit: int = 10) -> List[Dict[str, str]]:
        """Listar planilhas disponíveis"""
        if not self.is_authenticated:
            return []
        
        try:
            spreadsheets = []
            for sheet in self.gc.openall()[:limit]:
                spreadsheets.append({
                    'id': sheet.id,
                    'title': sheet.title,
                    'url': sheet.url
                })
            return spreadsheets
            
        except Exception as e:
            st.error(f"❌ Erro ao listar planilhas: {str(e)}")
            return []
    
    def read_spreadsheet(self, spreadsheet_url: str, 
                        worksheet_name: Optional[str] = None) -> Optional[pd.DataFrame]:
        """Ler dados de uma planilha"""
        if not self.is_authenticated:
            st.error("❌ Não autenticado. Configure as credenciais primeiro.")
            return None
        
        try:
            # Abrir planilha
            if spreadsheet_url.startswith('http'):
                spreadsheet = self.gc.open_by_url(spreadsheet_url)
            else:
                spreadsheet = self.gc.open(spreadsheet_url)
            
            # Selecionar worksheet
            if worksheet_name:
                worksheet = spreadsheet.worksheet(worksheet_name)
            else:
                worksheet = spreadsheet.sheet1  # Primeira aba
            
            # Obter todos os dados
            data = worksheet.get_all_records()
            
            if not data:
                st.warning("⚠️ Planilha vazia ou sem dados")
                return None
            
            # Converter para DataFrame
            df = pd.DataFrame(data)
            
            st.success(f"✅ Dados carregados: {len(df)} registros da planilha '{worksheet.title}'")
            return df
            
        except Exception as e:
            st.error(f"❌ Erro ao ler planilha: {str(e)}")
            return None
    
    def get_worksheet_info(self, spreadsheet_url: str) -> List[Dict[str, Any]]:
        """Obter informações das abas da planilha"""
        if not self.is_authenticated:
            return []
        
        try:
            if spreadsheet_url.startswith('http'):
                spreadsheet = self.gc.open_by_url(spreadsheet_url)
            else:
                spreadsheet = self.gc.open(spreadsheet_url)
            
            worksheets_info = []
            for worksheet in spreadsheet.worksheets():
                worksheets_info.append({
                    'title': worksheet.title,
                    'rows': worksheet.row_count,
                    'cols': worksheet.col_count,
                    'id': worksheet.id
                })
            
            return worksheets_info
            
        except Exception as e:
            st.error(f"❌ Erro ao obter informações: {str(e)}")
            return []

def setup_google_sheets_sidebar():
    """Configurar sidebar para Google Sheets"""
    st.sidebar.subheader("📊 Google Sheets")
    
    # Opção para usar Google Sheets
    use_google_sheets = st.sidebar.checkbox("Usar Google Sheets", value=False)
    
    if use_google_sheets:
        st.sidebar.markdown("### 🔑 Configuração")
        
        # Opções de autenticação
        auth_method = st.sidebar.selectbox(
            "Método de Autenticação",
            ["Upload de Credenciais", "Cole JSON das Credenciais"]
        )
        
        gs_integration = GoogleSheetsIntegration()
        
        if auth_method == "Upload de Credenciais":
            credentials_file = st.sidebar.file_uploader(
                "Upload do arquivo credentials.json",
                type=['json'],
                help="Baixe as credenciais da Google Cloud Console"
            )
            
            if credentials_file:
                try:
                    credentials_dict = json.loads(credentials_file.read())
                    if gs_integration.authenticate(credentials_dict=credentials_dict):
                        return gs_integration
                except Exception as e:
                    st.sidebar.error(f"Erro ao processar credenciais: {str(e)}")
        
        else:  # Cole JSON
            credentials_text = st.sidebar.text_area(
                "Cole o JSON das credenciais",
                height=100,
                help="Cole todo o conteúdo do arquivo credentials.json"
            )
            
            if credentials_text:
                try:
                    credentials_dict = json.loads(credentials_text)
                    if gs_integration.authenticate(credentials_dict=credentials_dict):
                        return gs_integration
                except Exception as e:
                    st.sidebar.error(f"Erro ao processar credenciais: {str(e)}")
        
        # Instruções
        with st.sidebar.expander("📖 Como obter credenciais"):
            st.markdown("""
            1. Vá para [Google Cloud Console](https://console.cloud.google.com/)
            2. Crie um projeto ou selecione existente
            3. Ative as APIs: Google Sheets e Google Drive
            4. Crie uma conta de serviço
            5. Baixe o arquivo JSON das credenciais
            6. Faça upload aqui
            """)
    
    return None

def google_sheets_data_loader():
    """Interface para carregar dados do Google Sheets"""
    gs_integration = setup_google_sheets_sidebar()
    
    if gs_integration and gs_integration.is_authenticated:
        st.subheader("📊 Carregar Dados do Google Sheets")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            spreadsheet_url = st.text_input(
                "URL ou Nome da Planilha",
                placeholder="https://docs.google.com/spreadsheets/d/... ou nome da planilha"
            )
        
        with col2:
            if st.button("🔍 Listar Minhas Planilhas"):
                spreadsheets = gs_integration.list_spreadsheets()
                if spreadsheets:
                    st.write("**Suas planilhas:**")
                    for sheet in spreadsheets:
                        st.write(f"- [{sheet['title']}]({sheet['url']})")
        
        if spreadsheet_url:
            # Obter informações das abas
            worksheets_info = gs_integration.get_worksheet_info(spreadsheet_url)
            
            if worksheets_info:
                st.write("**Abas disponíveis:**")
                worksheet_names = [ws['title'] for ws in worksheets_info]
                
                selected_worksheet = st.selectbox(
                    "Selecione a aba",
                    [''] + worksheet_names
                )
                
                if selected_worksheet and st.button("📥 Carregar Dados"):
                    df = gs_integration.read_spreadsheet(
                        spreadsheet_url, 
                        selected_worksheet
                    )
                    
                    if df is not None:
                        return df
    
    return None

# Função utilitária para demonstração
def create_sample_google_form_data():
    """Criar dados de exemplo no formato Google Forms"""
    data = {
        'Timestamp': ['2024-01-15 10:30:00', '2024-01-15 11:45:00', '2024-01-15 14:20:00'],
        'Nome completo': ['João Silva', 'Maria Santos', 'Pedro Costa'],
        'Idade': [28, 34, 25],
        'E-mail': ['joao@email.com', 'maria@email.com', 'pedro@email.com'],
        'Como você conheceu nossa empresa?': ['Google', 'Instagram', 'Amigos'],
        'Qual seu nível de satisfação? [1-10]': [8, 9, 7],
        'Você recomendaria nossos serviços?': ['Sim', 'Sim', 'Talvez'],
        'Qual seu principal interesse?': ['Tecnologia', 'Moda', 'Esportes'],
        'Com que frequência você usa nossos serviços?': ['Diariamente', 'Semanalmente', 'Mensalmente'],
        'Comentários adicionais': [
            'Ótimo atendimento!',
            'Produto de qualidade',
            'Preço um pouco alto'
        ]
    }
    
    return pd.DataFrame(data)