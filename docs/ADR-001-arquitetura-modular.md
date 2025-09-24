# ADR-001: Arquitetura Modular e Enterprise

## Contexto

O projeto Agente Marketing foi migrado de uma estrutura monolítica para uma arquitetura modular, baseada em domínios e boas práticas enterprise. O objetivo é garantir escalabilidade, testabilidade e facilidade de evolução futura (Next.js/NestJS).

## Decisão

- Adotar estrutura de pastas por domínio (`services`, `components`, `hooks`)
- Separar serviços de dados, análise, relatórios e integrações externas
- Manter compatibilidade com módulos legados durante a transição
- Implementar testes unitários e de integração para todos os serviços
- Documentar fluxos reais e exemplos de uso
- Utilizar type hints e docstrings em todos os novos módulos

## Consequências

- Maior clareza e organização do código
- Facilidade para onboarding de novos devs
- Testes automatizados garantem qualidade
- Evolução facilitada para backend/frontend enterprise
- Documentação e exemplos aceleram uso dos serviços

## Status

Decisão aplicada e validada em 23/09/2025

---
