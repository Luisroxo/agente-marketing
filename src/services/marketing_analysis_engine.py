"""
Motor de Análise IA para Marketing
Analisa perfil do cliente e gera insights estratégicos
"""
from src.services.logging_config import get_logger

logger = get_logger(__name__)
from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class ClientProfile:
    """Perfil estruturado do cliente"""

    nome: str
    setor: str
    porte: str
    orcamento: str
    desafios: List[str]
    canais_atuais: List[str]
    objetivo_principal: str
    prazo: str
    meta_crescimento: int
    observacoes: str


@dataclass
class MarketingInsight:
    """Insight gerado pela análise"""

    categoria: str
    titulo: str
    descricao: str
    prioridade: str  # "Alta", "Média", "Baixa"
    impacto_estimado: str
    complexidade: str
    prazo_implementacao: str


class MarketingAnalysisEngine:
    """Motor principal de análise de marketing"""

    def __init__(self):
        self.knowledge_base = self._load_knowledge_base()

    def analyze_client(self, client_data: Dict[str, Any]) -> Dict[str, Any]:
        """Análise completa do cliente"""

        profile = self._create_profile(client_data)

        # Análises específicas
        sector_analysis = self._analyze_sector(profile)
        challenge_analysis = self._analyze_challenges(profile)
        opportunity_analysis = self._find_opportunities(profile)
        budget_analysis = self._analyze_budget(profile)
        competition_analysis = self._analyze_competition(profile)

        # Gerar insights consolidados
        insights = self._generate_insights(
            profile,
            sector_analysis,
            challenge_analysis,
            opportunity_analysis,
            budget_analysis,
            competition_analysis,
        )

        # Score e métricas
        scores = self._calculate_scores(profile, insights)

        return {
            "profile": profile,
            "insights": insights,
            "scores": scores,
            "recommendations": self._generate_recommendations(profile, insights),
            "risk_assessment": self._assess_risks(profile),
            "success_metrics": self._define_success_metrics(profile),
        }

    def _create_profile(self, data: Dict[str, Any]) -> ClientProfile:
        """Criar perfil estruturado"""
        return ClientProfile(
            nome=data.get("nome", ""),
            setor=data.get("setor", ""),
            porte=data.get("porte", ""),
            orcamento=data.get("orcamento", ""),
            desafios=data.get("desafios", []),
            canais_atuais=data.get("canais_atuais", []),
            objetivo_principal=data.get("objetivo_principal", ""),
            prazo=data.get("prazo", ""),
            meta_crescimento=data.get("meta_crescimento", 0),
            observacoes=data.get("observacoes", ""),
        )

    def _load_knowledge_base(self) -> Dict[str, Any]:
        """Base de conhecimento sobre setores e estratégias"""
        return {
            "setores": {
                "Representação Comercial": {
                    "caracteristicas": [
                        "Ciclo de vendas longo",
                        "Relacionamento B2B",
                        "Múltiplos produtos/fornecedores",
                        "Dependência de networking",
                    ],
                    "desafios_comuns": [
                        "Dificuldade de diferenciação",
                        "Gestão de múltiplas linhas",
                        "Competição com venda direta",
                        "Necessidade de credibilidade técnica",
                    ],
                    "oportunidades": [
                        "Automação de processos",
                        "Marketing de relacionamento",
                        "Conteúdo educativo especializado",
                        "Lead scoring inteligente",
                    ],
                    "canais_eficazes": [
                        "LinkedIn",
                        "Email marketing",
                        "Eventos setoriais",
                        "Parcerias estratégicas",
                    ],
                },
                "E-commerce/Varejo Online": {
                    "caracteristicas": [
                        "Ciclo de vendas curto",
                        "Relacionamento B2C",
                        "Alta competição de preços",
                        "Dependência de tráfego digital",
                    ],
                    "desafios_comuns": [
                        "Carrinho abandonado",
                        "Custo de aquisição alto",
                        "Sazonalidade",
                        "Logística e entregas",
                    ],
                    "oportunidades": [
                        "Remarketing avançado",
                        "Personalização da experiência",
                        "Programa de fidelidade",
                        "Social commerce",
                    ],
                    "canais_eficazes": [
                        "Google Ads",
                        "Facebook/Instagram",
                        "Marketplaces",
                        "Influenciadores",
                    ],
                },
            },
            "desafios_solucoes": {
                "Baixa geração de leads": {
                    "solucoes": [
                        "Otimização de SEO",
                        "Lead magnets",
                        "Campanhas pagas segmentadas",
                        "Conteúdo viral",
                    ],
                    "ferramentas": [
                        "HubSpot",
                        "RD Station",
                        "Google Ads",
                        "Facebook Ads",
                    ],
                    "investimento_medio": "R$ 5.000 - R$ 20.000/mês",
                    "tempo_resultados": "2-4 meses",
                },
                "Conversão baixa": {
                    "solucoes": [
                        "A/B testing",
                        "Otimização de landing pages",
                        "Remarketing",
                        "Prova social",
                    ],
                    "ferramentas": [
                        "Hotjar",
                        "Optimizely",
                        "Google Optimize",
                        "Unbounce",
                    ],
                    "investimento_medio": "R$ 3.000 - R$ 15.000/mês",
                    "tempo_resultados": "1-3 meses",
                },
            },
            "orcamento_estrategias": {
                "Até R$ 5.000": {
                    "foco": ["SEO", "Email marketing", "Redes sociais orgânicas"],
                    "limitacoes": ["Pouco tráfego pago", "Resultados mais lentos"],
                    "roi_esperado": "120-150%",
                },
                "R$ 5.001 - R$ 15.000": {
                    "foco": ["Google Ads", "Facebook Ads", "Marketing de conteúdo"],
                    "limitacoes": ["Competição limitada", "Segmentação básica"],
                    "roi_esperado": "150-200%",
                },
                "R$ 15.001 - R$ 50.000": {
                    "foco": [
                        "Automação completa",
                        "Múltiplos canais",
                        "Personalização",
                    ],
                    "limitacoes": ["Necessita gestão especializada"],
                    "roi_esperado": "180-250%",
                },
            },
        }

    def _analyze_sector(self, profile: ClientProfile) -> Dict[str, Any]:
        """Análise específica do setor"""

        sector_data = self.knowledge_base["setores"].get(profile.setor, {})

        return {
            "caracteristicas": sector_data.get("caracteristicas", []),
            "desafios_tipicos": sector_data.get("desafios_comuns", []),
            "oportunidades": sector_data.get("oportunidades", []),
            "canais_recomendados": sector_data.get("canais_eficazes", []),
            "benchmarks": self._get_sector_benchmarks(profile.setor),
        }

    def _analyze_challenges(self, profile: ClientProfile) -> List[MarketingInsight]:
        """Análise dos desafios específicos"""

        insights = []

        for desafio in profile.desafios:
            solucao_data = self.knowledge_base["desafios_solucoes"].get(desafio, {})

            if solucao_data:
                insight = MarketingInsight(
                    categoria="Desafio",
                    titulo=f"Solução para: {desafio}",
                    descricao=f"Implementar: {', '.join(solucao_data.get('solucoes', [])[:2])}",
                    prioridade=self._calculate_priority(desafio, profile),
                    impacto_estimado=solucao_data.get(
                        "tempo_resultados", "Médio prazo"
                    ),
                    complexidade=self._assess_complexity(solucao_data),
                    prazo_implementacao=solucao_data.get(
                        "tempo_resultados", "2-4 meses"
                    ),
                )
                insights.append(insight)

        return insights

    def _find_opportunities(self, profile: ClientProfile) -> List[MarketingInsight]:
        """Identificar oportunidades baseadas no perfil"""

        opportunities = []

        # Análise de canais não utilizados
        sector_data = self.knowledge_base["setores"].get(profile.setor, {})
        canais_recomendados = sector_data.get("canais_eficazes", [])

        for canal in canais_recomendados:
            if canal not in profile.canais_atuais:
                opportunity = MarketingInsight(
                    categoria="Oportunidade",
                    titulo=f"Explorar {canal}",
                    descricao=f"Canal não utilizado com alto potencial para {profile.setor}",
                    prioridade="Alta"
                    if canal in ["Google Ads", "LinkedIn"]
                    else "Média",
                    impacto_estimado="Alto",
                    complexidade="Média",
                    prazo_implementacao="1-2 meses",
                )
                opportunities.append(opportunity)

        # Oportunidades baseadas no orçamento
        budget_opportunities = self._find_budget_opportunities(profile)
        opportunities.extend(budget_opportunities)

        return opportunities

    def _analyze_budget(self, profile: ClientProfile) -> Dict[str, Any]:
        """Análise do orçamento disponível"""

        budget_data = self.knowledge_base["orcamento_estrategias"].get(
            profile.orcamento, {}
        )

        return {
            "foco_recomendado": budget_data.get("foco", []),
            "limitacoes": budget_data.get("limitacoes", []),
            "roi_esperado": budget_data.get("roi_esperado", "Não definido"),
            "distribuicao_sugerida": self._suggest_budget_distribution(profile),
        }

    def _analyze_competition(self, profile: ClientProfile) -> Dict[str, Any]:
        """Análise da concorrência baseada no setor"""

        # Simulação de análise competitiva
        competition_intensity = {
            "E-commerce/Varejo Online": "Alta",
            "Representação Comercial": "Média",
            "Consultoria/Serviços": "Alta",
            "Tecnologia/Software": "Muito Alta",
        }

        intensity = competition_intensity.get(profile.setor, "Média")

        return {
            "intensidade": intensity,
            "principais_canais_concorrencia": self._get_competition_channels(
                profile.setor
            ),
            "vantagens_competitivas": self._identify_competitive_advantages(profile),
            "estrategias_diferenciacao": self._suggest_differentiation_strategies(
                profile
            ),
        }

    def _generate_insights(
        self, profile: ClientProfile, *analyses
    ) -> List[MarketingInsight]:
        """Consolidar insights de todas as análises"""

        all_insights = []

        # Adicionar insights de cada análise
        for analysis in analyses:
            if isinstance(analysis, list):
                all_insights.extend(analysis)

        # Insights adicionais baseados na combinação de fatores
        combo_insights = self._generate_combination_insights(profile)
        all_insights.extend(combo_insights)

        # Ordenar por prioridade
        priority_order = {"Alta": 3, "Média": 2, "Baixa": 1}
        all_insights.sort(
            key=lambda x: priority_order.get(x.prioridade, 0), reverse=True
        )

        return all_insights

    def _calculate_scores(
        self, profile: ClientProfile, insights: List[MarketingInsight]
    ) -> Dict[str, Any]:
        """Calcular scores e métricas"""

        # Score de potencial (baseado em múltiplos fatores)
        potential_score = self._calculate_potential_score(profile)

        # Score de complexidade
        complexity_score = self._calculate_complexity_score(profile, insights)

        # ROI projetado
        roi_projection = self._calculate_roi_projection(profile)

        # Prioridade geral
        priority = self._calculate_overall_priority(potential_score, complexity_score)

        return {
            "potential_score": potential_score,
            "complexity_score": complexity_score,
            "roi_projection": roi_projection,
            "priority": priority,
            "time_to_results": self._estimate_time_to_results(profile),
            "success_probability": self._calculate_success_probability(profile),
        }

    def _generate_recommendations(
        self, profile: ClientProfile, insights: List[MarketingInsight]
    ) -> List[str]:
        """Gerar recomendações prioritárias"""

        recommendations = []

        # Top 3 insights de maior prioridade
        top_insights = [i for i in insights if i.prioridade == "Alta"][:3]

        for insight in top_insights:
            recommendations.append(f"{insight.titulo}: {insight.descricao}")

        # Recomendações baseadas no orçamento
        budget_recs = self._get_budget_specific_recommendations(profile)
        recommendations.extend(budget_recs)

        return recommendations[:5]  # Limitar a 5 recomendações principais

    def _assess_risks(self, profile: ClientProfile) -> List[Dict[str, str]]:
        """Avaliar riscos do projeto"""

        risks = []

        # Riscos baseados no orçamento
        if profile.orcamento == "Até R$ 5.000":
            risks.append(
                {
                    "risk": "Orçamento limitado",
                    "description": "Recursos insuficientes para campanhas pagas competitivas",
                    "mitigation": "Focar em estratégias orgânicas e de baixo custo",
                }
            )

        # Riscos baseados no setor
        if profile.setor == "E-commerce/Varejo Online":
            risks.append(
                {
                    "risk": "Alta concorrência",
                    "description": "Mercado saturado com custos de aquisição altos",
                    "mitigation": "Diferenciação através de nicho específico",
                }
            )

        # Riscos baseados no prazo
        if profile.prazo == "1-3 meses":
            risks.append(
                {
                    "risk": "Prazo curto",
                    "description": "Expectativas de resultados em prazo muito apertado",
                    "mitigation": "Focar em estratégias de impacto rápido",
                }
            )

        return risks

    def _define_success_metrics(self, profile: ClientProfile) -> List[Dict[str, str]]:
        """Definir métricas de sucesso"""

        metrics = []

        # Métricas baseadas no objetivo
        if profile.objetivo_principal == "Aumentar vendas":
            metrics.extend(
                [
                    {
                        "metric": "Receita",
                        "target": f"+{profile.meta_crescimento}%",
                        "period": profile.prazo,
                    },
                    {
                        "metric": "Ticket médio",
                        "target": "+15%",
                        "period": profile.prazo,
                    },
                    {
                        "metric": "Taxa de conversão",
                        "target": "+25%",
                        "period": profile.prazo,
                    },
                ]
            )

        elif profile.objetivo_principal == "Gerar mais leads":
            metrics.extend(
                [
                    {
                        "metric": "Leads qualificados",
                        "target": f"+{profile.meta_crescimento}%",
                        "period": profile.prazo,
                    },
                    {
                        "metric": "Custo por lead",
                        "target": "-20%",
                        "period": profile.prazo,
                    },
                    {
                        "metric": "Taxa de conversão de leads",
                        "target": "+30%",
                        "period": profile.prazo,
                    },
                ]
            )

        # Métricas gerais sempre aplicáveis
        metrics.extend(
            [
                {"metric": "ROI", "target": "180%", "period": "6 meses"},
                {"metric": "ROAS", "target": "4:1", "period": "3 meses"},
            ]
        )

        return metrics

    # Métodos auxiliares de cálculo
    def _calculate_priority(self, desafio: str, profile: ClientProfile) -> str:
        """Calcular prioridade baseada no desafio e perfil"""
        high_priority_challenges = ["Baixa geração de leads", "Conversão baixa"]
        return "Alta" if desafio in high_priority_challenges else "Média"

    def _assess_complexity(self, solution_data: Dict[str, Any]) -> str:
        """Avaliar complexidade da solução"""
        tools_count = len(solution_data.get("ferramentas", []))
        return "Alta" if tools_count > 3 else "Média" if tools_count > 1 else "Baixa"

    def _calculate_potential_score(self, profile: ClientProfile) -> float:
        """Calcular score de potencial (0-10)"""
        score = 5.0  # Base

        # Ajustes baseados no orçamento
        budget_scores = {
            "Até R$ 5.000": 6.0,
            "R$ 5.001 - R$ 15.000": 7.5,
            "R$ 15.001 - R$ 50.000": 9.0,
            "Acima de R$ 100.000": 10.0,
        }
        score = budget_scores.get(profile.orcamento, score)

        # Ajustes baseados no prazo
        if profile.prazo in ["6-12 meses", "12+ meses"]:
            score += 0.5

        # Ajustes baseados no número de desafios (mais desafios = mais oportunidades)
        score += min(len(profile.desafios) * 0.2, 1.0)

        return min(score, 10.0)

    def _calculate_complexity_score(
        self, profile: ClientProfile, insights: List[MarketingInsight]
    ) -> str:
        """Calcular score de complexidade"""
        high_complexity_count = len([i for i in insights if i.complexidade == "Alta"])

        if high_complexity_count > 3:
            return "Alta"
        elif high_complexity_count > 1:
            return "Média"
        else:
            return "Baixa"

    def _calculate_roi_projection(self, profile: ClientProfile) -> str:
        """Calcular projeção de ROI"""
        budget_data = self.knowledge_base["orcamento_estrategias"].get(
            profile.orcamento, {}
        )
        return budget_data.get("roi_esperado", "150-180%")

    def _calculate_overall_priority(
        self, potential_score: float, complexity_score: str
    ) -> str:
        """Calcular prioridade geral do projeto"""
        if potential_score >= 8 and complexity_score != "Alta":
            return "Alta"
        elif potential_score >= 6:
            return "Média"
        else:
            return "Baixa"

    def _estimate_time_to_results(self, profile: ClientProfile) -> str:
        """Estimar tempo para primeiros resultados"""
        if profile.orcamento in ["R$ 15.001 - R$ 50.000", "Acima de R$ 100.000"]:
            return "2-4 semanas"
        else:
            return "6-8 semanas"

    def _calculate_success_probability(self, profile: ClientProfile) -> str:
        """Calcular probabilidade de sucesso"""
        score = 70  # Base

        # Fatores positivos
        if len(profile.desafios) <= 3:  # Foco
            score += 10
        if profile.prazo in ["6-12 meses", "12+ meses"]:  # Prazo realista
            score += 10
        if profile.orcamento not in ["Até R$ 5.000"]:  # Orçamento adequado
            score += 10

        return f"{min(score, 95)}%"

    # Métodos auxiliares específicos
    def _get_sector_benchmarks(self, setor: str) -> Dict[str, str]:
        """Obter benchmarks do setor"""
        benchmarks = {
            "Representação Comercial": {
                "conversion_rate": "2-5%",
                "sales_cycle": "3-6 meses",
                "average_deal": "R$ 50k-500k",
            },
            "E-commerce/Varejo Online": {
                "conversion_rate": "1-3%",
                "sales_cycle": "1-7 dias",
                "average_deal": "R$ 100-2000",
            },
        }
        return benchmarks.get(setor, {})

    def _find_budget_opportunities(
        self, profile: ClientProfile
    ) -> List[MarketingInsight]:
        """Encontrar oportunidades específicas do orçamento"""
        opportunities = []

        if profile.orcamento == "R$ 15.001 - R$ 50.000":
            opportunity = MarketingInsight(
                categoria="Orçamento",
                titulo="Implementar Automação Avançada",
                descricao="Orçamento permite automação completa de marketing",
                prioridade="Alta",
                impacto_estimado="Muito Alto",
                complexidade="Média",
                prazo_implementacao="2-3 meses",
            )
            opportunities.append(opportunity)

        return opportunities

    def _suggest_budget_distribution(self, profile: ClientProfile) -> Dict[str, str]:
        """Sugerir distribuição do orçamento"""
        if profile.orcamento == "R$ 5.001 - R$ 15.000":
            return {
                "Campanhas pagas": "60%",
                "Ferramentas/Software": "25%",
                "Conteúdo/Creative": "15%",
            }
        return {}

    def _get_competition_channels(self, setor: str) -> List[str]:
        """Obter canais principais da concorrência"""
        channels = {
            "E-commerce/Varejo Online": ["Google Ads", "Facebook", "Instagram"],
            "Representação Comercial": ["LinkedIn", "Email", "Eventos"],
        }
        return channels.get(setor, ["Google Ads", "Redes sociais"])

    def _identify_competitive_advantages(self, profile: ClientProfile) -> List[str]:
        """Identificar vantagens competitivas potenciais"""
        advantages = []

        if len(profile.canais_atuais) < 3:
            advantages.append("Oportunidade de expansão de canais")

        if profile.porte in ["Microempresa", "Pequena"]:
            advantages.append("Agilidade e flexibilidade de pequena empresa")

        return advantages

    def _suggest_differentiation_strategies(self, profile: ClientProfile) -> List[str]:
        """Sugerir estratégias de diferenciação"""
        strategies = [
            "Especialização em nicho específico",
            "Atendimento personalizado",
            "Experiência do cliente superior",
            "Preço competitivo com valor agregado",
        ]
        return strategies[:2]  # Top 2

    def _generate_combination_insights(
        self, profile: ClientProfile
    ) -> List[MarketingInsight]:
        """Gerar insights da combinação de fatores"""
        insights = []

        # Insight baseado em setor + objetivo
        if (
            profile.setor == "Representação Comercial"
            and profile.objetivo_principal == "Aumentar vendas"
        ):
            insight = MarketingInsight(
                categoria="Estratégia",
                titulo="Programa de Relacionamento B2B",
                descricao="Implementar programa estruturado de relacionamento para vendas complexas",
                prioridade="Alta",
                impacto_estimado="Alto",
                complexidade="Média",
                prazo_implementacao="3-4 meses",
            )
            insights.append(insight)

        return insights

    def _get_budget_specific_recommendations(self, profile: ClientProfile) -> List[str]:
        """Recomendações específicas do orçamento"""
        budget_data = self.knowledge_base["orcamento_estrategias"].get(
            profile.orcamento, {}
        )
        focus_areas = budget_data.get("foco", [])

        return [f"Priorizar investimento em {area}" for area in focus_areas[:2]]
