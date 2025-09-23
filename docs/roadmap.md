
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
  - [ ] app_simples.py
  - [x] app_tally_integration.py (REMOVIDO — legado, não utilizado)
  - [ ] apps duplicados em src/
- [ ] Padronizar nomenclatura de arquivos e funções
- [ ] Adotar padrão de logging centralizado
- [ ] Implementar tratamento de erros consistente

## 3. Testes Automatizados
- [ ] Planejar cobertura de testes
  - [ ] Listar funções críticas para teste unitário
  - [ ] Listar fluxos para teste de integração
- [ ] Implementar testes unitários em tests/
  - [ ] Testar src/services/data_processor.py
  - [ ] Testar src/services/basic_analysis.py
  - [ ] Testar src/services/google_sheets.py
- [ ] Implementar testes de integração
  - [ ] Testar fluxo completo de processamento de dados
  - [ ] Testar integração com Google Sheets
- [ ] Automatizar execução dos testes (pytest)

## 4. Documentação e ADRs
- [ ] Atualizar README.md com nova estrutura e exemplos de uso
- [ ] Atualizar ARQUITETURA.md com fluxos reais do código migrado
- [ ] Atualizar/expandir ADRs conforme decisões de arquitetura
- [ ] Documentar exemplos de uso dos serviços e componentes
- [ ] Documentar variáveis de ambiente e setup

## 5. Autenticação e Banco de Dados (Fase 2)
- [ ] Planejar modelo de usuários e autenticação
  - [ ] Definir modelo de dados para usuários
  - [ ] Escolher biblioteca de autenticação (ex: FastAPI Auth, OAuth)
- [ ] Integrar PostgreSQL
  - [ ] Definir modelo de dados relacional
  - [ ] Criar migrations iniciais
  - [ ] Integrar ORM (ex: SQLAlchemy)
- [ ] Refatorar serviços para usar banco relacional
  - [ ] Persistir dados de análise
  - [ ] Persistir logs e relatórios
- [ ] Implementar testes de autenticação e banco

## 6. CI/CD e Qualidade
- [ ] Configurar workflow GitHub Actions
  - [ ] Rodar testes unitários e integração em cada push
  - [ ] Validar cobertura mínima
- [ ] Adotar linter e formatter automáticos (ex: black, flake8)
- [ ] Documentar fluxo de CI/CD

## 7. Evolução Futura (Opcional)
- [ ] Planejar integração com backend enterprise (NestJS)
- [ ] Planejar migração do frontend para Next.js
- [ ] Adicionar monitoramento e alertas (Sentry, Prometheus)
- [ ] Implementar exportação de relatórios automáticos
