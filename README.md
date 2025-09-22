# Agente Marketing IA

Este projeto é um Agente de Marketing baseado em IA, desenvolvido em Python com Streamlit, seguindo arquitetura moderna e melhores práticas.

## � Principais Tecnologias

- **Python 3.12** - Linguagem principal
- **Streamlit 1.49.1** - Interface web interativa  
- **Pandas 2.1.3** - Processamento de dados
- **Plotly 6.3.0** - Visualização de dados
- **Google Sheets API** - Integração com planilhas
- **PostgreSQL** - Banco de dados (planejado)

## 🏗️ Estrutura do Projeto

O projeto segue uma arquitetura modular inspirada em padrões enterprise:

```
agente-marketing/
├── docs/                          # Documentação técnica
│   ├── architecture/              # Visão geral da arquitetura
│   ├── adr/                       # Architecture Decision Records
│   ├── api/                       # Documentação da API
│   └── chat-history.md            # Histórico de conversas
├── src/                           # Código fonte organizado
│   ├── components/                # Componentes reutilizáveis
│   ├── services/                  # Serviços e integrações
│   └── hooks/                     # Hooks customizados
├── utils/                         # Utilitários de processamento
├── analysis/                      # Módulos de análise
├── templates/                     # Templates de relatórios
├── api/                          # Integrações externas
├── app.py                        # Aplicação principal
└── requirements.txt              # Dependências
```

## 🎯 Funcionalidades

### ✅ Implementadas
- **Upload de Dados**: CSV, Excel e Google Sheets
- **Processamento**: Limpeza e validação automática
- **Análise**: Estatísticas, correlações e insights
- **Visualização**: Gráficos interativos e dashboards
- **Relatórios**: Geração automática de relatórios de marketing

### � Em Desenvolvimento
- **Autenticação**: Sistema de login seguro
- **Banco de Dados**: Migração para PostgreSQL
- **API**: Endpoints RESTful
- **Deploy**: Configuração de produção

### 📋 Planejadas
- **Frontend Moderno**: Migração para Next.js
- **Backend API**: Implementação com NestJS
- **Multi-tenant**: Suporte a múltiplas organizações
- **ML/IA**: Modelos preditivos avançados

## 🚀 Getting Started

### Pré-requisitos
- Python 3.12+
- pip ou conda

### Instalação

1. Clone o repositório:
```bash
git clone [url-do-repositorio]
cd agente-marketing
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
```bash
# Copie o arquivo de exemplo
cp .env.example .env
# Edite com suas credenciais
```

4. Execute a aplicação:
```bash
streamlit run app.py
```

5. Acesse: [http://localhost:8501](http://localhost:8501)

## 📊 Como Usar

### 1. Upload de Dados
- **CSV/Excel**: Use o uploader de arquivos na sidebar
- **Google Sheets**: Configure as credenciais da API no arquivo `.env`

### 2. Análise Automática
- O sistema processa e limpa os dados automaticamente
- Relatórios de qualidade são gerados em tempo real

### 3. Visualização
- **Visão Geral**: Métricas principais e KPIs
- **Análise Detalhada**: Correlações e tendências
- **Personas**: Segmentação de clientes
- **Relatórios**: Documentos exportáveis

## 🛠️ Desenvolvimento

### Estrutura de Código
- **Modular**: Componentes independentes e reutilizáveis
- **Type Hints**: Documentação inline do código
- **Error Handling**: Tratamento robusto de erros
- **Logging**: Sistema de logs estruturado

### Padrões Seguidos
- **PEP 8**: Estilo de código Python
- **Docstrings**: Documentação de funções
- **Git Flow**: Workflow de desenvolvimento
- **Semantic Versioning**: Versionamento semântico

## 📚 Documentação

- **[Arquitetura](docs/architecture/overview.md)** - Visão geral do sistema
- **[ADRs](docs/adr/)** - Decisões arquiteturais
- **[API](docs/api/specification.md)** - Documentação da API
- **[Histórico](docs/chat-history.md)** - Conversas e decisões
- **[Contributing](CONTRIBUTING.md)** - Guia de contribuição
- **[Changelog](CHANGELOG.md)** - Histórico de mudanças

## 🤝 Contribuindo

Contribuições são muito bem-vindas! Por favor, leia o [guia de contribuição](CONTRIBUTING.md) para detalhes sobre nosso código de conduta e processo de desenvolvimento.

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📈 Roadmap

### Fase 1: Consolidação (Q4 2025)
- [x] MVP funcional
- [x] Estrutura profissional
- [ ] Autenticação básica
- [ ] PostgreSQL

### Fase 2: API Backend (Q1 2026)
- [ ] NestJS API
- [ ] Autenticação JWT
- [ ] Banco robusto
- [ ] Testes automatizados

### Fase 3: Frontend Moderno (Q2 2026)
- [ ] Next.js interface
- [ ] Dashboard avançado
- [ ] Mobile responsive
- [ ] PWA

### Fase 4: Enterprise (Q3 2026)
- [ ] Multi-tenant
- [ ] LGPD compliance
- [ ] ML/IA avançada
- [ ] Marketplace de plugins

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👥 Equipe

- **Luis** - Product Owner & Developer
- **AI Assistant** - Technical Advisor

## 📞 Suporte

Para dúvidas ou suporte:
- 📋 **Issues**: [GitHub Issues](../../issues)
- 💬 **Discussions**: [GitHub Discussions](../../discussions)
- 📖 **Docs**: [Documentação Completa](docs/)

## 🎯 Status do Projeto

![Status](https://img.shields.io/badge/status-active-success)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.12+-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.49.1-red)

**Última atualização:** 22 de setembro de 2025

## 📁 Estrutura do Projeto

```
agente-marketing/
├── data/           # Dados brutos e processados
├── models/         # Modelos ML treinados
├── nlp/           # Processamento de linguagem
├── analysis/      # Análises e insights
├── templates/     # Templates de documentos
├── api/           # Integrações externas
├── interface/     # Frontend Streamlit
└── tests/         # Testes unitários
```

## 👥 Contribuição

Este é um projeto em desenvolvimento. Feedback e sugestões são bem-vindos!