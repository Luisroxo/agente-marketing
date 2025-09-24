# Roadmap Técnico — Agente Marketing (Migração Enterprise + Modularização)

## Regras de Execução Automática

1. **Execução automática:** Todas as tarefas e subtarefas devem ser executadas imediatamente, sem pedir autorização prévia.
2. **Perguntar só se houver impacto:** Só interrompa para perguntar ao usuário se a tarefa for causar algum impacto relevante no projeto (ex: downtime, perda de dados, breaking change).
3. **Commits apenas ao final da tarefa principal:** Só realize commit/git quando TODAS as subtarefas da tarefa principal estiverem concluídas. Siga o fluxo:
  ```bash
  git add .
  git commit -m "feat: concluir [nome da tarefa]"
  git push
  ```
4. Após cada conclusão, avance automaticamente para a próxima tarefa.

## Rotina de Conclusão de Tarefas

1. **Sub-subtarefas** → após executar, marcar como concluída no roadmap.
2. **Subtarefas** → só considerar concluída quando TODAS as sub-subtarefas estiverem feitas.
3. **Tarefa principal** → só considerar concluída quando TODAS as subtarefas estiverem feitas.  
  - Executar commit/git apenas neste momento (ver regras acima).
4. Após cada conclusão, avance para a próxima tarefa automaticamente.

## 1. Migração do Core para Estrutura Enterprise
- [x] Mapear funcionalidades e módulos existentes
  - [x] Listar todos os scripts principais (app.py, init.py, run.py, etc)
  - [x] Listar funções utilitárias em utils/
  - [x] Listar módulos de análise, templates, integração API
- [x] Planejar estrutura de destino
  - [x] Definir destino de cada função/módulo (src/services, src/components, src/hooks)
  - [x] Atualizar ARQUITETURA.md com novo diagrama de pastas
- [ ] Migrar código para src/
  - [x] Migrar funções de processamento para src/services/
    - [x] data_processor.py
    - [x] helpers.py
    - [x] basic_analysis.py
  - [x] Migrar componentes de interface para src/components/
  - [x] Elementos Streamlit customizados
    - [ ] Layouts e painéis
  - [x] Migrar integrações externas para src/services/
    - [x] google_sheets.py
    - [x] report_generator.py
  - [x] Migrar hooks customizados para src/hooks/
    - [x] Hooks de estado, cache, etc
  - [x] Atualizar imports em todos os scripts
  - [x] Remover duplicidades e código legado
- [ ] Refatorar entrypoints
  - [x] Atualizar app.py/init.py/run.py para usar módulos migrados
  - [x] Garantir compatibilidade com Streamlit (REMOVIDO — frontend Lovable)

## 2. Padronização e Limpeza de Código
- [ ] Remover POCs e apps legados não utilizados
  - [x] app_simples.py (REMOVIDO — não utilizado)
  - [x] app_tally_integration.py (REMOVIDO — legado, não utilizado)
  - [x] apps duplicados em src/ (NÃO ENCONTRADO — estrutura limpa)
- [x] Padronizar nomenclatura de arquivos e funções
- [x] Adotar padrão de logging centralizado
- [x] Implementar tratamento de erros consistente

## 3. Testes Automatizados
- [x] Planejar cobertura de testes
  - [x] Listar funções críticas para teste unitário
  - [ ] Listar fluxos para teste de integração
- [x] Implementar testes unitários em tests/
  - [x] Testar src/services/data_processor.py
  - [x] Testar src/services/analysis/analysis_service.py
  - [x] Testar src/services/reporting/reporting_service.py
  - [x] Testar src/services/analysis/statistical_analysis.py
  - [x] Testar src/services/external/googleSheetsService.py
- [ ] Implementar testes de integração
  - [x] Testar fluxo completo de processamento de dados
  - [x] Testar integração com Google Sheets
- [x] Automatizar execução dos testes (pytest)

## 4. Documentação e ADRs
- [x] Atualizar README.md com nova estrutura e exemplos de uso
- [x] Atualizar ARQUITETURA.md com fluxos reais do código migrado
- [x] Atualizar/expandir ADRs conforme decisões de arquitetura
- [x] Documentar exemplos de uso dos serviços e componentes
- [x] Documentar variáveis de ambiente e setup

## 5. Autenticação e Banco de Dados (Fase 2)
- [x] Planejar modelo de usuários e autenticação
  - [x] Definir modelo de dados para usuários
  - [x] Escolher biblioteca de autenticação (ex: FastAPI Auth, OAuth)
- [x] Integrar PostgreSQL (usando SQLite para testes locais)
  - [x] Definir modelo de dados relacional
  - [x] Criar migrations iniciais (via SQLAlchemy)
  - [x] Integrar ORM (ex: SQLAlchemy)
- [x] Refatorar serviços para usar banco relacional
  - [x] Persistir dados de análise
  - [x] Persistir logs e relatórios
- [x] Implementar testes de autenticação e banco

## 6. CI/CD e Qualidade
- [x] Configurar workflow GitHub Actions
  - [x] Rodar testes unitários e integração em cada push
  - [x] Validar cobertura mínima
- [x] Adotar linter e formatter automáticos (ex: black, flake8)
- [x] Documentar fluxo de CI/CD

## 7. Evolução Futura (Opcional)
- [ ] Planejar integração com backend enterprise (NestJS)
- [ ] Planejar migração do frontend para Next.js
- [ ] Adicionar monitoramento e alertas (Sentry, Prometheus)
- [ ] Implementar exportação de relatórios automáticos
