# Contributing to Agente Marketing IA

Obrigado pelo seu interesse em contribuir! Este documento fornece diretrizes para contribuir com o projeto.

## 🚀 Como Contribuir

### 1. Setup do Ambiente
```bash
# Clone o repositório
git clone [url-do-repo]
cd agente-marketing

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com suas configurações
```

### 2. Estrutura do Projeto
Familiarize-se com a [arquitetura do projeto](docs/architecture/overview.md) e a [organização de pastas](src/ARQUITETURA.md).

### 3. Workflow de Desenvolvimento

#### Branches
- `main`: Código de produção estável
- `develop`: Código de desenvolvimento
- `feature/nome-da-feature`: Novas funcionalidades
- `bugfix/nome-do-bug`: Correções de bugs
- `docs/nome-da-doc`: Atualizações de documentação

#### Processo
1. **Fork** o repositório
2. **Clone** seu fork localmente
3. **Crie** uma branch para sua contribuição
4. **Desenvolva** seguindo as diretrizes
5. **Teste** suas mudanças
6. **Commit** seguindo convenções
7. **Push** para seu fork
8. **Abra** um Pull Request

## 📝 Diretrizes de Código

### Python Style Guide
- Seguir **PEP 8**
- Usar **type hints** em todas as funções
- **Docstrings** obrigatórias para classes e funções públicas
- Máximo de **88 caracteres** por linha (Black formatter)

### Estrutura de Commits
Usamos [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): description

[optional body]

[optional footer(s)]
```

#### Tipos
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `style`: Formatação (não afeta código)
- `refactor`: Refatoração
- `test`: Testes
- `chore`: Manutenção

#### Exemplos
```
feat(analysis): add customer segmentation algorithm
fix(upload): resolve CSV encoding issues
docs(api): update endpoint documentation
```

### Code Review Checklist
- [ ] Código segue PEP 8
- [ ] Type hints implementados
- [ ] Docstrings presentes
- [ ] Testes adicionados/atualizados
- [ ] Documentação atualizada
- [ ] Sem código comentado desnecessário
- [ ] Variáveis e funções com nomes descritivos

## 🧪 Testes

### Executando Testes
```bash
# Testes unitários
python -m pytest tests/

# Testes com cobertura
python -m pytest --cov=src tests/

# Testes específicos
python -m pytest tests/test_data_processor.py
```

### Escrevendo Testes
- Um arquivo de teste por módulo
- Nomenclatura: `test_nome_do_modulo.py`
- Classes de teste: `TestNomeDoModulo`
- Métodos de teste: `test_funcionalidade_especifica`

## 📚 Documentação

### Docstrings
```python
def process_data(data: pd.DataFrame, options: dict) -> pd.DataFrame:
    """
    Processa dados de marketing para análise.
    
    Args:
        data: DataFrame com dados brutos
        options: Opções de processamento
        
    Returns:
        DataFrame processado e limpo
        
    Raises:
        ValueError: Se dados estão em formato inválido
    """
```

### Documentação Técnica
- **ADRs**: Para decisões arquiteturais importantes
- **API Docs**: Para endpoints e interfaces
- **README**: Para informações gerais

## 🐛 Reportando Bugs

### Template de Bug Report
```markdown
**Descrição**
Descrição clara e concisa do bug.

**Reprodução**
Passos para reproduzir:
1. Vá para '...'
2. Clique em '....'
3. Veja erro

**Comportamento Esperado**
O que deveria acontecer.

**Screenshots**
Se aplicável, adicione screenshots.

**Ambiente**
- OS: [e.g. Windows 10]
- Python: [e.g. 3.12]
- Versão do projeto: [e.g. 1.0.0]
```

## 💡 Sugerindo Melhorias

### Template de Feature Request
```markdown
**Problema**
Descrição clara do problema que esta feature resolve.

**Solução Proposta**
Descrição clara da solução desejada.

**Alternativas Consideradas**
Outras soluções que você considerou.

**Contexto Adicional**
Qualquer outro contexto sobre a feature.
```

## 🎯 Áreas Prioritárias

### Contribuições Bem-vindas
1. **Autenticação**: Implementar sistema de login
2. **Database**: Migração para PostgreSQL
3. **Testes**: Aumentar cobertura de testes
4. **Performance**: Otimizações de processamento
5. **UI/UX**: Melhorias na interface Streamlit
6. **Documentação**: Guias e tutoriais

### Tecnologias Futuras
- **FastAPI/NestJS**: Backend API
- **Next.js**: Frontend moderno
- **Docker**: Containerização
- **CI/CD**: Automação de deploy

## 📞 Comunidade

### Canais de Comunicação
- **Issues**: Para bugs e feature requests
- **Discussions**: Para perguntas e ideias
- **Pull Requests**: Para contribuições de código

### Código de Conduta
Esperamos que todos os contribuidores sigam nosso código de conduta baseado em:
- **Respeito**: Trate todos com cortesia
- **Inclusão**: Ambiente acolhedor para todos
- **Colaboração**: Trabalhe junto para melhorar o projeto
- **Profissionalismo**: Mantenha discussões construtivas

## 🙏 Reconhecimento

Todos os contribuidores serão reconhecidos no README principal e releases notes.

---

**Dúvidas?** Abra uma issue ou discussion. Estamos aqui para ajudar!