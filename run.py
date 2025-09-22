"""
Script para executar o Agente de IA para Marketing
"""
import subprocess
import sys
import os
from pathlib import Path

def check_dependencies():
    """Verificar se as dependências estão instaladas"""
    try:
        import streamlit
        import pandas
        import plotly
        print("✅ Dependências principais instaladas")
        return True
    except ImportError as e:
        print(f"❌ Dependência faltando: {e}")
        return False

def install_dependencies():
    """Instalar dependências"""
    print("🔧 Instalando dependências...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Erro ao instalar dependências")
        return False

def run_app():
    """Executar a aplicação Streamlit"""
    print("🚀 Iniciando Agente de IA para Marketing...")
    print("📱 A aplicação será aberta no seu navegador")
    print("🔗 URL: http://localhost:8501")
    print("\n" + "="*50)
    print("Para parar a aplicação, pressione Ctrl+C")
    print("="*50 + "\n")
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Aplicação encerrada pelo usuário")
    except Exception as e:
        print(f"❌ Erro ao executar aplicação: {e}")

def main():
    """Função principal"""
    print("🤖 Agente de IA para Marketing - Setup")
    print("="*40)
    
    # Verificar se estamos no diretório correto
    if not Path("app.py").exists():
        print("❌ Execute este script no diretório do projeto (onde está o app.py)")
        return
    
    # Verificar dependências
    if not check_dependencies():
        print("\n📦 Instalando dependências necessárias...")
        if not install_dependencies():
            print("❌ Falha na instalação. Instale manualmente com:")
            print("   pip install -r requirements.txt")
            return
    
    # Executar aplicação
    print("\n" + "="*40)
    run_app()

if __name__ == "__main__":
    main()