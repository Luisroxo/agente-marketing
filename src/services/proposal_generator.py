from src.services.logging_config import get_logger

logger = get_logger(__name__)
"""
Gerador de Propostas de Marketing
Cria propostas profissionais baseadas na análise IA
"""

from dataclasses import dataclass
from typing import List, Dict, Any
from datetime import datetime

@dataclass
class ProposalSection:
    """Seção da proposta"""
    title: str
    content: str
    order: int
    section_type: str  # "text", "table", "chart", "metrics"

@dataclass
class MarketingStrategy:
    """Estratégia de marketing para a proposta"""
    nome: str
    descricao: str
    objetivo: str
    implementacao: str
    investimento_estimado: str
    roi_esperado: str
    prazo_implementacao: str
    complexidade: str
    metricas_sucesso: List[str]
    riscos: List[str]

@dataclass
class MarketingProposal:
    """Proposta completa de marketing"""
    client_name: str
    consultant_name: str
    creation_date: datetime
    proposal_id: str
    
    # Seções da proposta
    executive_summary: str
    situation_analysis: str
    strategies: List[MarketingStrategy]
    implementation_timeline: Dict[str, Any]
    investment_breakdown: Dict[str, Any]
    success_metrics: List[Dict[str, str]]
    risk_assessment: List[Dict[str, str]]
    next_steps: List[str]
    
    # Metadados
    total_investment: str
    expected_roi: str
    project_duration: str
    complexity_score: str

class ProposalGenerator:
    """Gerador principal de propostas"""
    
    def __init__(self):
        self.templates = self._load_templates()
        self.default_consultant = "Consultor de Marketing IA"
    
    def generate_proposal(self, client_data: Dict[str, Any], analysis_data: Dict[str, Any]) -> MarketingProposal:
        """Gerar proposta completa"""
        
        # Extrair dados necessários
        client_name = client_data.get('nome', 'Cliente')
        proposal_id = self._generate_proposal_id(client_name)
        
        # Gerar seções da proposta
        executive_summary = self._generate_executive_summary(client_data, analysis_data)
        situation_analysis = self._generate_situation_analysis(client_data, analysis_data)
        strategies = self._generate_strategies(client_data, analysis_data)
        timeline = self._generate_timeline(strategies)
        investment = self._generate_investment_breakdown(client_data, strategies)
        metrics = self._generate_success_metrics(client_data, analysis_data)
        risks = self._generate_risk_assessment(analysis_data)
        next_steps = self._generate_next_steps(strategies)
        
        # Calcular totais
        total_investment = self._calculate_total_investment(investment)
        expected_roi = analysis_data['scores'].get('roi_projection', '180%')
        duration = self._estimate_project_duration(strategies)
        complexity = analysis_data['scores'].get('complexity_score', 'Média')
        
        proposal = MarketingProposal(
            client_name=client_name,
            consultant_name=self.default_consultant,
            creation_date=datetime.now(),
            proposal_id=proposal_id,
            executive_summary=executive_summary,
            situation_analysis=situation_analysis,
            strategies=strategies,
            implementation_timeline=timeline,
            investment_breakdown=investment,
            success_metrics=metrics,
            risk_assessment=risks,
            next_steps=next_steps,
            total_investment=total_investment,
            expected_roi=expected_roi,
            project_duration=duration,
            complexity_score=complexity
        )
        
        return proposal
    
    def _load_templates(self) -> Dict[str, str]:
        """Carregar templates de proposta"""
        return {
            "executive_summary": """
            Com base na análise detalhada do perfil de **{client_name}**, identificamos oportunidades 
            significativas para otimização de resultados no setor de **{sector}**.
            
            **Situação Atual:**
            - Principais desafios: {main_challenges}
            - Orçamento disponível: {budget}
            - Objetivo principal: {main_objective}
            
            **Nossa Recomendação:**
            - Score de potencial: {potential_score}/10
            - ROI projetado: {roi_projection}
            - Prazo para resultados: {time_to_results}
            - Probabilidade de sucesso: {success_probability}
            
            Este plano estratégico foi desenvolvido especificamente para atender às necessidades 
            identificadas e maximizar o retorno sobre o investimento.
            """,
            
            "situation_analysis": """
            **Análise da Situação Atual**
            
            **Pontos Fortes Identificados:**
            {strengths}
            
            **Principais Desafios:**
            {challenges}
            
            **Oportunidades de Mercado:**
            {opportunities}
            
            **Análise da Concorrência:**
            {competition_analysis}
            
            **Recomendações Prioritárias:**
            {priority_recommendations}
            """
        }
    
    def _generate_proposal_id(self, client_name: str) -> str:
        """Gerar ID único da proposta"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M")
        client_initials = ''.join([word[0].upper() for word in client_name.split()[:3]])
        return f"PROP-{client_initials}-{timestamp}"
    
    def _generate_executive_summary(self, client_data: Dict[str, Any], analysis_data: Dict[str, Any]) -> str:
        """Gerar resumo executivo"""
        
        template = self.templates["executive_summary"]
        scores = analysis_data['scores']
        
        # Formatar principais desafios
        challenges = client_data.get('desafios', [])
        main_challenges = ', '.join(challenges[:3]) if challenges else 'Crescimento sustentável'
        
        summary = template.format(
            client_name=client_data.get('nome', 'Cliente'),
            sector=client_data.get('setor', 'Setor específico'),
            main_challenges=main_challenges,
            budget=client_data.get('orcamento', 'A definir'),
            main_objective=client_data.get('objetivo_principal', 'Crescimento'),
            potential_score=scores.get('potential_score', 8.5),
            roi_projection=scores.get('roi_projection', '180%'),
            time_to_results=scores.get('time_to_results', '2-4 semanas'),
            success_probability=scores.get('success_probability', '85%')
        )
        
        return summary.strip()
    
    def _generate_situation_analysis(self, client_data: Dict[str, Any], analysis_data: Dict[str, Any]) -> str:
        """Gerar análise da situação"""
        
        recommendations = analysis_data.get('recommendations', [])
        insights = analysis_data.get('insights', [])
        
        # Extrair pontos fortes dos insights
        strengths = self._extract_strengths_from_sector(client_data.get('setor'))
        
        # Formatar desafios
        challenges_text = '\n'.join([f"• {d}" for d in client_data.get('desafios', [])])
        
        # Extrair oportunidades dos insights
        opportunities = [i.descricao for i in insights if i.categoria == "Oportunidade"][:3]
        opportunities_text = '\n'.join([f"• {o}" for o in opportunities])
        
        # Análise da concorrência
        competition_text = self._generate_competition_analysis(client_data.get('setor'))
        
        # Recomendações prioritárias
        recommendations_text = '\n'.join([f"• {r}" for r in recommendations[:3]])
        
        analysis = f"""
        **Pontos Fortes Identificados:**
        {strengths}
        
        **Principais Desafios:**
        {challenges_text}
        
        **Oportunidades de Mercado:**
        {opportunities_text}
        
        **Análise da Concorrência:**
        {competition_text}
        
        **Recomendações Prioritárias:**
        {recommendations_text}
        """
        
        return analysis.strip()
    
    def _generate_strategies(self, client_data: Dict[str, Any], analysis_data: Dict[str, Any]) -> List[MarketingStrategy]:
        """Gerar estratégias baseadas na análise"""
        
        strategies = []
        insights = analysis_data.get('insights', [])
        
        # Pegar insights de alta prioridade
        high_priority_insights = [i for i in insights if i.prioridade == "Alta"]
        
        for i, insight in enumerate(high_priority_insights[:4], 1):  # Máximo 4 estratégias
            
            strategy = MarketingStrategy(
                nome=insight.titulo,
                descricao=insight.descricao,
                objetivo=self._map_insight_to_objective(insight, client_data),
                implementacao=self._generate_implementation_plan(insight, client_data),
                investimento_estimado=self._estimate_strategy_investment(insight, client_data),
                roi_esperado=self._estimate_strategy_roi(insight),
                prazo_implementacao=insight.prazo_implementacao,
                complexidade=insight.complexidade,
                metricas_sucesso=self._define_strategy_metrics(insight, client_data),
                riscos=self._identify_strategy_risks(insight)
            )
            
            strategies.append(strategy)
        
        return strategies
    
    def _generate_timeline(self, strategies: List[MarketingStrategy]) -> Dict[str, Any]:
        """Gerar cronograma de implementação"""
        
        timeline = {
            "phases": [],
            "total_duration": "24 semanas",
            "milestones": []
        }
        
        # Fase 1: Setup e Planejamento
        timeline["phases"].append({
            "phase": "Fase 1: Setup e Planejamento",
            "duration": "2 semanas",
            "activities": [
                "Configuração inicial de ferramentas",
                "Definição de KPIs e métricas",
                "Setup de tracking e analytics",
                "Alinhamento da equipe"
            ],
            "deliverables": ["Dashboard de métricas", "Plano detalhado", "Configuração de ferramentas"]
        })
        
        # Fases baseadas nas estratégias
        for i, strategy in enumerate(strategies[:3], 2):
            timeline["phases"].append({
                "phase": f"Fase {i}: {strategy.nome}",
                "duration": strategy.prazo_implementacao,
                "activities": [
                    f"Implementação de {strategy.nome}",
                    "Testes e otimizações",
                    "Monitoramento de resultados",
                    "Ajustes baseados em dados"
                ],
                "deliverables": [
                    f"Estratégia {strategy.nome} ativa",
                    "Relatório de resultados",
                    "Otimizações implementadas"
                ]
            })
        
        # Fase final: Análise e Expansão
        timeline["phases"].append({
            "phase": f"Fase {len(strategies) + 2}: Análise e Expansão",
            "duration": "4 semanas",
            "activities": [
                "Análise completa de resultados",
                "Otimização de estratégias de sucesso",
                "Planejamento de expansão",
                "Relatório final e próximos passos"
            ],
            "deliverables": [
                "Relatório completo de ROI",
                "Recomendações para continuidade",
                "Plano de expansão"
            ]
        })
        
        # Marcos importantes
        timeline["milestones"] = [
            {"week": 2, "milestone": "Setup completo"},
            {"week": 8, "milestone": "Primeira estratégia ativa"},
            {"week": 16, "milestone": "Todas estratégias implementadas"},
            {"week": 24, "milestone": "Análise final e relatório"}
        ]
        
        return timeline
    
    def _generate_investment_breakdown(self, client_data: Dict[str, Any], strategies: List[MarketingStrategy]) -> Dict[str, Any]:
        """Gerar breakdown do investimento"""
        
        budget = client_data.get('orcamento', 'R$ 5.001 - R$ 15.000')
        
        # Extrair valor numérico do orçamento
        if "5.000" in budget:
            monthly_budget = 5000
        elif "15.000" in budget:
            monthly_budget = 12500  # Valor médio
        elif "50.000" in budget:
            monthly_budget = 32500  # Valor médio
        else:
            monthly_budget = 10000  # Default
        
        breakdown = {
            "setup_inicial": {
                "value": 5000,
                "description": "Configuração inicial, setup de ferramentas, treinamento"
            },
            "mensal_recorrente": {
                "value": monthly_budget,
                "description": "Investimento mensal em campanhas, ferramentas e otimizações"
            },
            "distribuicao_mensal": {
                "campanhas_pagas": int(monthly_budget * 0.6),
                "ferramentas_software": int(monthly_budget * 0.25),
                "conteudo_creative": int(monthly_budget * 0.15)
            },
            "total_6_meses": (monthly_budget * 6) + 5000,
            "roi_projetado": f"{int(((monthly_budget * 6) + 5000) * 1.8):,}".replace(',', '.')
        }
        
        return breakdown
    
    def _generate_success_metrics(self, client_data: Dict[str, Any], analysis_data: Dict[str, Any]) -> List[Dict[str, str]]:
        """Gerar métricas de sucesso"""
        
        metrics = analysis_data.get('success_metrics', [])
        
        # Se não houver métricas da análise, gerar baseado no objetivo
        if not metrics:
            objective = client_data.get('objetivo_principal', 'Aumentar vendas')
            growth_target = client_data.get('meta_crescimento', 50)
            
            if objective == "Aumentar vendas":
                metrics = [
                    {"metric": "Receita", "target": f"+{growth_target}%", "period": "6 meses"},
                    {"metric": "Ticket médio", "target": "+15%", "period": "6 meses"},
                    {"metric": "Taxa de conversão", "target": "+25%", "period": "6 meses"}
                ]
            elif objective == "Gerar mais leads":
                metrics = [
                    {"metric": "Leads qualificados", "target": f"+{growth_target}%", "period": "6 meses"},
                    {"metric": "Custo por lead", "target": "-20%", "period": "6 meses"},
                    {"metric": "Taxa de conversão leads", "target": "+30%", "period": "6 meses"}
                ]
            else:
                metrics = [
                    {"metric": "Objetivo principal", "target": f"+{growth_target}%", "period": "6 meses"},
                    {"metric": "ROI", "target": "180%", "period": "6 meses"},
                    {"metric": "ROAS", "target": "4:1", "period": "3 meses"}
                ]
        
        # Adicionar métricas universais
        metrics.extend([
            {"metric": "ROI Global", "target": "180%", "period": "6 meses"},
            {"metric": "ROAS", "target": "4:1", "period": "3 meses"},
            {"metric": "Redução CAC", "target": "20%", "period": "6 meses"}
        ])
        
        return metrics
    
    def _generate_risk_assessment(self, analysis_data: Dict[str, Any]) -> List[Dict[str, str]]:
        """Gerar avaliação de riscos"""
        
        risks = analysis_data.get('risk_assessment', [])
        
        # Se não houver riscos da análise, usar riscos padrão
        if not risks:
            risks = [
                {
                    "risk": "Concorrência acirrada",
                    "description": "Mercado competitivo pode elevar custos de aquisição",
                    "mitigation": "Diferenciação através de proposta de valor única"
                },
                {
                    "risk": "Mudanças no mercado",
                    "description": "Alterações nas preferências do consumidor",
                    "mitigation": "Monitoramento contínuo e adaptação rápida"
                },
                {
                    "risk": "Limitações de orçamento",
                    "description": "Recursos insuficientes para competir em todos os canais",
                    "mitigation": "Foco em canais com melhor ROI comprovado"
                }
            ]
        
        return risks
    
    def _generate_next_steps(self, strategies: List[MarketingStrategy]) -> List[str]:
        """Gerar próximos passos"""
        
        next_steps = [
            "1. Aprovação da proposta e definição do cronograma de implementação",
            "2. Setup inicial das ferramentas e configuração de analytics",
            "3. Definição final dos KPIs e sistema de monitoramento"
        ]
        
        # Adicionar passos baseados nas estratégias
        for i, strategy in enumerate(strategies[:3], 4):
            next_steps.append(f"{i}. Início da implementação: {strategy.nome}")
        
        next_steps.extend([
            f"{len(strategies) + 4}. Primeira reunião de acompanhamento (semana 2)",
            f"{len(strategies) + 5}. Relatório de resultados iniciais (semana 4)"
        ])
        
        return next_steps
    
    # Métodos auxiliares
    def _extract_strengths_from_sector(self, sector: str) -> str:
        """Extrair pontos fortes baseados no setor"""
        
        sector_strengths = {
            "Representação Comercial": """
            • Relacionamento estabelecido com clientes B2B
            • Experiência em múltiplos canais de vendas
            • Conhecimento aprofundado de ciclos de vendas complexos
            • Network de contatos no setor
            """,
            "E-commerce/Varejo Online": """
            • Operação digital já estabelecida
            • Capacidade de scaling rápido
            • Dados de comportamento do cliente disponíveis
            • Flexibilidade para testar novas estratégias
            """,
            "Consultoria/Serviços": """
            • Expertise reconhecida no mercado
            • Relacionamento próximo com clientes
            • Alto ticket médio
            • Potencial para recorrência
            """
        }
        
        return sector_strengths.get(sector, "• Posicionamento consolidado no mercado\n• Experiência operacional\n• Base de clientes estabelecida")
    
    def _generate_competition_analysis(self, sector: str) -> str:
        """Gerar análise da concorrência"""
        
        competition_analysis = {
            "Representação Comercial": "Mercado com concorrência média, oportunidade de diferenciação através de especialização técnica e relacionamento.",
            "E-commerce/Varejo Online": "Alta concorrência, necessário foco em nicho específico e experiência diferenciada do cliente.",
            "Consultoria/Serviços": "Concorrência baseada em expertise, oportunidade através de marketing de conteúdo e thought leadership."
        }
        
        return competition_analysis.get(sector, "Análise detalhada da concorrência será realizada na fase de implementação.")
    
    def _map_insight_to_objective(self, insight, client_data: Dict[str, Any]) -> str:
        """Mapear insight para objetivo específico"""
        objective = client_data.get('objetivo_principal', 'Crescimento')
        return f"Contribuir para: {objective} através de {insight.titulo.lower()}"
    
    def _generate_implementation_plan(self, insight, client_data: Dict[str, Any]) -> str:
        """Gerar plano de implementação"""
        return f"Implementação em {insight.prazo_implementacao} através de metodologia estruturada com testes A/B e otimização contínua."
    
    def _estimate_strategy_investment(self, insight, client_data: Dict[str, Any]) -> str:
        """Estimar investimento da estratégia"""
        budget = client_data.get('orcamento', 'R$ 5.001 - R$ 15.000')
        
        if "5.000" in budget:
            return "R$ 2.000 - R$ 3.000"
        elif "15.000" in budget:
            return "R$ 5.000 - R$ 8.000"
        elif "50.000" in budget:
            return "R$ 15.000 - R$ 25.000"
        else:
            return "R$ 5.000 - R$ 10.000"
    
    def _estimate_strategy_roi(self, insight) -> str:
        """Estimar ROI da estratégia"""
        roi_map = {
            "Alta": "200-300%",
            "Média": "150-200%",
            "Baixa": "120-150%"
        }
        return roi_map.get(insight.prioridade, "150-200%")
    
    def _define_strategy_metrics(self, insight, client_data: Dict[str, Any]) -> List[str]:
        """Definir métricas da estratégia"""
        return [
            f"Implementação de {insight.titulo}",
            "Melhoria na métrica-chave",
            "ROI da estratégia específica"
        ]
    
    def _identify_strategy_risks(self, insight) -> List[str]:
        """Identificar riscos da estratégia"""
        return [
            f"Complexidade de implementação: {insight.complexidade}",
            "Necessidade de ajustes durante execução"
        ]
    
    def _calculate_total_investment(self, investment: Dict[str, Any]) -> str:
        """Calcular investimento total"""
        total = investment.get('total_6_meses', 100000)
        return f"R$ {total:,.0f}".replace(',', '.')
    
    def _estimate_project_duration(self, strategies: List[MarketingStrategy]) -> str:
        """Estimar duração do projeto"""
        return "6 meses (24 semanas)"