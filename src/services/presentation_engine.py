"""
Módulo de Apresentação de Propostas
Cria apresentações profissionais para propostas de marketing
"""
from src.services.logging_config import get_logger

logger = get_logger(__name__)
from dataclasses import dataclass
from typing import List, Dict, Optional
import streamlit as st


@dataclass
class PresentationSlide:
    """Slide da apresentação"""

    title: str
    content: str
    slide_type: str  # "cover", "content", "chart", "table", "summary"
    order: int
    notes: Optional[str] = None


@dataclass
class PresentationTheme:
    """Tema da apresentação"""

    primary_color: str
    secondary_color: str
    accent_color: str
    background_color: str
    text_color: str
    font_family: str


class ProposalPresentation:
    """Gerador de apresentações de propostas"""

    def __init__(self):
        self.themes = self._load_themes()
        self.default_theme = "professional"

    def _load_themes(self) -> Dict[str, PresentationTheme]:
        """Carregar temas de apresentação"""
        return {
            "professional": PresentationTheme(
                primary_color="#1f4e79",
                secondary_color="#2e75b6",
                accent_color="#ffd700",
                background_color="#ffffff",
                text_color="#333333",
                font_family="Arial, sans-serif",
            ),
            "modern": PresentationTheme(
                primary_color="#2c3e50",
                secondary_color="#3498db",
                accent_color="#e74c3c",
                background_color="#ecf0f1",
                text_color="#2c3e50",
                font_family="Helvetica, sans-serif",
            ),
            "creative": PresentationTheme(
                primary_color="#8e44ad",
                secondary_color="#9b59b6",
                accent_color="#f39c12",
                background_color="#f8f9fa",
                text_color="#2c3e50",
                font_family="Georgia, serif",
            ),
        }

    def generate_presentation(
        self, proposal, theme_name: str = "professional"
    ) -> List[PresentationSlide]:
        """Gerar apresentação completa"""

        theme = self.themes.get(theme_name, self.themes[self.default_theme])
        slides = []

        # Slide 1: Capa
        slides.append(self._create_cover_slide(proposal, theme))

        # Slide 2: Agenda
        slides.append(self._create_agenda_slide(theme))

        # Slide 3: Situação Atual
        slides.append(self._create_situation_slide(proposal, theme))

        # Slide 4: Análise e Oportunidades
        slides.append(self._create_analysis_slide(proposal, theme))

        # Slide 5: Nossa Proposta
        slides.append(self._create_proposal_overview_slide(proposal, theme))

        # Slides 6-N: Estratégias (uma por slide)
        for i, strategy in enumerate(proposal.strategies, 6):
            slides.append(self._create_strategy_slide(strategy, i, theme))

        # Slide N+1: Cronograma
        slides.append(self._create_timeline_slide(proposal, theme))

        # Slide N+2: Investimento e ROI
        slides.append(self._create_investment_slide(proposal, theme))

        # Slide N+3: Métricas de Sucesso
        slides.append(self._create_metrics_slide(proposal, theme))

        # Slide N+4: Próximos Passos
        slides.append(self._create_next_steps_slide(proposal, theme))

        # Slide N+5: Obrigado/Contato
        slides.append(self._create_closing_slide(theme))

        return slides

    def _create_cover_slide(
        self, proposal, theme: PresentationTheme
    ) -> PresentationSlide:
        """Criar slide de capa"""

        content = f"""
        <div style="text-align: center; padding: 50px; background: linear-gradient(135deg, {theme.primary_color}, {theme.secondary_color}); color: white; border-radius: 15px;">
            <h1 style="font-size: 3em; margin-bottom: 20px; font-family: {theme.font_family};">
                🎯 Proposta de Marketing
            </h1>
            <h2 style="font-size: 2em; margin-bottom: 30px; opacity: 0.9;">
                {proposal.client_name}
            </h2>
            <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px; margin: 30px auto; max-width: 500px;">
                <p style="font-size: 1.3em; margin: 10px 0;">
                    <strong>📊 Score de Potencial:</strong> {proposal.scores.get('potential_score', 8.5):.1f}/10
                </p>
                <p style="font-size: 1.3em; margin: 10px 0;">
                    <strong>💰 ROI Projetado:</strong> {proposal.expected_roi}
                </p>
                <p style="font-size: 1.3em; margin: 10px 0;">
                    <strong>⏰ Duração:</strong> {proposal.project_duration}
                </p>
            </div>
            <p style="font-size: 1.1em; margin-top: 40px; opacity: 0.8;">
                {proposal.creation_date.strftime('%d de %B de %Y')}
            </p>
        </div>
        """

        return PresentationSlide(
            title="Proposta de Marketing",
            content=content,
            slide_type="cover",
            order=1,
            notes="Slide de abertura com informações principais da proposta",
        )

    def _create_agenda_slide(self, theme: PresentationTheme) -> PresentationSlide:
        """Criar slide de agenda"""

        content = f"""
        <div style="padding: 30px; font-family: {theme.font_family};">
            <h2 style="color: {theme.primary_color}; border-bottom: 3px solid {theme.accent_color}; padding-bottom: 10px;">
                📋 Agenda da Apresentação
            </h2>
            
            <div style="margin-top: 40px;">
                <div style="display: flex; align-items: center; margin: 20px 0; padding: 15px; background: {theme.background_color}; border-left: 5px solid {theme.secondary_color}; border-radius: 5px;">
                    <span style="font-size: 2em; margin-right: 20px;">📊</span>
                    <div>
                        <h3 style="margin: 0; color: {theme.primary_color};">Situação Atual</h3>
                        <p style="margin: 5px 0; color: {theme.text_color};">Análise do cenário e desafios identificados</p>
                    </div>
                </div>
                
                <div style="display: flex; align-items: center; margin: 20px 0; padding: 15px; background: {theme.background_color}; border-left: 5px solid {theme.secondary_color}; border-radius: 5px;">
                    <span style="font-size: 2em; margin-right: 20px;">🎯</span>
                    <div>
                        <h3 style="margin: 0; color: {theme.primary_color};">Nossa Proposta</h3>
                        <p style="margin: 5px 0; color: {theme.text_color};">Estratégias personalizadas para seus objetivos</p>
                    </div>
                </div>
                
                <div style="display: flex; align-items: center; margin: 20px 0; padding: 15px; background: {theme.background_color}; border-left: 5px solid {theme.secondary_color}; border-radius: 5px;">
                    <span style="font-size: 2em; margin-right: 20px;">📈</span>
                    <div>
                        <h3 style="margin: 0; color: {theme.primary_color};">Resultados Esperados</h3>
                        <p style="margin: 5px 0; color: {theme.text_color};">ROI, métricas e cronograma de implementação</p>
                    </div>
                </div>
                
                <div style="display: flex; align-items: center; margin: 20px 0; padding: 15px; background: {theme.background_color}; border-left: 5px solid {theme.secondary_color}; border-radius: 5px;">
                    <span style="font-size: 2em; margin-right: 20px;">🚀</span>
                    <div>
                        <h3 style="margin: 0; color: {theme.primary_color};">Próximos Passos</h3>
                        <p style="margin: 5px 0; color: {theme.text_color};">Como começamos a implementação</p>
                    </div>
                </div>
            </div>
        </div>
        """

        return PresentationSlide(
            title="Agenda",
            content=content,
            slide_type="content",
            order=2,
            notes="Apresentar estrutura da proposta e principais tópicos",
        )

    def _create_situation_slide(
        self, proposal, theme: PresentationTheme
    ) -> PresentationSlide:
        """Criar slide da situação atual"""

        # Extrair informações da análise
        situation = proposal.situation_analysis

        content = f"""
        <div style="padding: 30px; font-family: {theme.font_family};">
            <h2 style="color: {theme.primary_color}; border-bottom: 3px solid {theme.accent_color}; padding-bottom: 10px;">
                📊 Situação Atual
            </h2>
            
            <div style="margin-top: 30px; background: {theme.background_color}; padding: 25px; border-radius: 10px; border-left: 5px solid {theme.secondary_color};">
                <div style="white-space: pre-line; color: {theme.text_color}; line-height: 1.6;">
                    {situation}
                </div>
            </div>
            
            <div style="margin-top: 30px; text-align: center; padding: 20px; background: linear-gradient(45deg, {theme.accent_color}20, {theme.secondary_color}20); border-radius: 10px;">
                <h3 style="color: {theme.primary_color}; margin-bottom: 15px;">🎯 Conclusão</h3>
                <p style="font-size: 1.2em; color: {theme.text_color}; font-weight: bold;">
                    Identificamos oportunidades claras para otimização e crescimento
                </p>
            </div>
        </div>
        """

        return PresentationSlide(
            title="Situação Atual",
            content=content,
            slide_type="content",
            order=3,
            notes="Contextualizar o cliente sobre sua situação atual e desafios",
        )

    def _create_analysis_slide(
        self, proposal, theme: PresentationTheme
    ) -> PresentationSlide:
        """Criar slide de análise e oportunidades"""

        content = f"""
        <div style="padding: 30px; font-family: {theme.font_family};">
            <h2 style="color: {theme.primary_color}; border-bottom: 3px solid {theme.accent_color}; padding-bottom: 10px;">
                💡 Análise e Oportunidades
            </h2>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 30px;">
                
                <div style="background: {theme.background_color}; padding: 25px; border-radius: 10px; border-top: 5px solid #28a745;">
                    <h3 style="color: #28a745; margin-bottom: 15px;">✅ Pontos Fortes</h3>
                    <ul style="color: {theme.text_color}; line-height: 1.6;">
                        <li>Operação estabelecida no mercado</li>
                        <li>Base de clientes existente</li>
                        <li>Conhecimento do setor</li>
                        <li>Potencial de crescimento identificado</li>
                    </ul>
                </div>
                
                <div style="background: {theme.background_color}; padding: 25px; border-radius: 10px; border-top: 5px solid #ffc107;">
                    <h3 style="color: #ffc107; margin-bottom: 15px;">🚀 Oportunidades</h3>
                    <ul style="color: {theme.text_color}; line-height: 1.6;">
                        <li>Automação de processos</li>
                        <li>Novos canais de marketing</li>
                        <li>Otimização da conversão</li>
                        <li>Expansão da base de clientes</li>
                    </ul>
                </div>
                
            </div>
            
            <div style="margin-top: 30px; text-align: center; padding: 25px; background: linear-gradient(135deg, {theme.primary_color}20, {theme.secondary_color}20); border-radius: 10px;">
                <h3 style="color: {theme.primary_color}; margin-bottom: 15px;">📈 Potencial Identificado</h3>
                <div style="display: flex; justify-content: space-around; margin-top: 20px;">
                    <div style="text-align: center;">
                        <div style="font-size: 2.5em; color: {theme.accent_color}; font-weight: bold;">
                            {proposal.scores.get('potential_score', 8.5):.1f}/10
                        </div>
                        <div style="color: {theme.text_color};">Score de Potencial</div>
                    </div>
                    <div style="text-align: center;">
                        <div style="font-size: 2.5em; color: {theme.accent_color}; font-weight: bold;">
                            {proposal.expected_roi}
                        </div>
                        <div style="color: {theme.text_color};">ROI Esperado</div>
                    </div>
                </div>
            </div>
        </div>
        """

        return PresentationSlide(
            title="Análise e Oportunidades",
            content=content,
            slide_type="content",
            order=4,
            notes="Destacar o potencial identificado e oportunidades de crescimento",
        )

    def _create_proposal_overview_slide(
        self, proposal, theme: PresentationTheme
    ) -> PresentationSlide:
        """Criar slide de visão geral da proposta"""

        content = f"""
        <div style="padding: 30px; font-family: {theme.font_family};">
            <h2 style="color: {theme.primary_color}; border-bottom: 3px solid {theme.accent_color}; padding-bottom: 10px;">
                🎯 Nossa Proposta
            </h2>
            
            <div style="margin-top: 30px; text-align: center;">
                <div style="background: linear-gradient(135deg, {theme.primary_color}, {theme.secondary_color}); color: white; padding: 30px; border-radius: 15px; margin-bottom: 30px;">
                    <h3 style="font-size: 1.8em; margin-bottom: 20px;">
                        Plano Estratégico Personalizado
                    </h3>
                    <p style="font-size: 1.2em; opacity: 0.9; line-height: 1.6;">
                        Desenvolvemos uma estratégia sob medida para maximizar seus resultados
                        e alcançar seus objetivos de crescimento.
                    </p>
                </div>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-top: 30px;">
                
                <div style="text-align: center; padding: 20px; background: {theme.background_color}; border-radius: 10px; border-top: 3px solid {theme.secondary_color};">
                    <div style="font-size: 2.5em; margin-bottom: 10px;">{len(proposal.strategies)}</div>
                    <div style="color: {theme.text_color}; font-weight: bold;">Estratégias</div>
                    <div style="color: {theme.text_color}; font-size: 0.9em;">Personalizadas</div>
                </div>
                
                <div style="text-align: center; padding: 20px; background: {theme.background_color}; border-radius: 10px; border-top: 3px solid {theme.secondary_color};">
                    <div style="font-size: 2.5em; margin-bottom: 10px;">📈</div>
                    <div style="color: {theme.text_color}; font-weight: bold;">ROI</div>
                    <div style="color: {theme.text_color}; font-size: 0.9em;">{proposal.expected_roi}</div>
                </div>
                
                <div style="text-align: center; padding: 20px; background: {theme.background_color}; border-radius: 10px; border-top: 3px solid {theme.secondary_color};">
                    <div style="font-size: 2.5em; margin-bottom: 10px;">⏰</div>
                    <div style="color: {theme.text_color}; font-weight: bold;">Duração</div>
                    <div style="color: {theme.text_color}; font-size: 0.9em;">{proposal.project_duration}</div>
                </div>
                
                <div style="text-align: center; padding: 20px; background: {theme.background_color}; border-radius: 10px; border-top: 3px solid {theme.secondary_color};">
                    <div style="font-size: 2.5em; margin-bottom: 10px;">🎯</div>
                    <div style="color: {theme.text_color}; font-weight: bold;">Foco</div>
                    <div style="color: {theme.text_color}; font-size: 0.9em;">Resultados</div>
                </div>
                
            </div>
        </div>
        """

        return PresentationSlide(
            title="Nossa Proposta",
            content=content,
            slide_type="content",
            order=5,
            notes="Apresentar visão geral da proposta e valor agregado",
        )

    def _create_strategy_slide(
        self, strategy, slide_number: int, theme: PresentationTheme
    ) -> PresentationSlide:
        """Criar slide para uma estratégia específica"""

        content = f"""
        <div style="padding: 30px; font-family: {theme.font_family};">
            <h2 style="color: {theme.primary_color}; border-bottom: 3px solid {theme.accent_color}; padding-bottom: 10px;">
                📌 {strategy.nome}
            </h2>
            
            <div style="margin-top: 30px;">
                <div style="background: {theme.background_color}; padding: 25px; border-radius: 10px; margin-bottom: 25px;">
                    <h3 style="color: {theme.secondary_color}; margin-bottom: 15px;">🎯 Objetivo</h3>
                    <p style="color: {theme.text_color}; font-size: 1.1em; line-height: 1.6;">
                        {strategy.objetivo}
                    </p>
                </div>
                
                <div style="background: {theme.background_color}; padding: 25px; border-radius: 10px; margin-bottom: 25px;">
                    <h3 style="color: {theme.secondary_color}; margin-bottom: 15px;">📋 Descrição</h3>
                    <p style="color: {theme.text_color}; line-height: 1.6;">
                        {strategy.descricao}
                    </p>
                </div>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                    
                    <div style="background: {theme.background_color}; padding: 20px; border-radius: 10px;">
                        <h4 style="color: {theme.secondary_color}; margin-bottom: 15px;">⚙️ Implementação</h4>
                        <p style="color: {theme.text_color}; line-height: 1.6;">
                            {strategy.implementacao}
                        </p>
                    </div>
                    
                    <div style="background: {theme.background_color}; padding: 20px; border-radius: 10px;">
                        <h4 style="color: {theme.secondary_color}; margin-bottom: 15px;">📊 Métricas</h4>
                        <div style="color: {theme.text_color};">
                            <div style="margin: 10px 0; padding: 8px 12px; background: {theme.accent_color}20; border-radius: 5px;">
                                <strong>💰 Investimento:</strong> {strategy.investimento_estimado}
                            </div>
                            <div style="margin: 10px 0; padding: 8px 12px; background: #28a74520; border-radius: 5px;">
                                <strong>📈 ROI:</strong> {strategy.roi_esperado}
                            </div>
                            <div style="margin: 10px 0; padding: 8px 12px; background: {theme.secondary_color}20; border-radius: 5px;">
                                <strong>⏰ Prazo:</strong> {strategy.prazo_implementacao}
                            </div>
                        </div>
                    </div>
                    
                </div>
            </div>
        </div>
        """

        return PresentationSlide(
            title=f"Estratégia: {strategy.nome}",
            content=content,
            slide_type="content",
            order=slide_number,
            notes=f"Detalhar implementação e benefícios da estratégia {strategy.nome}",
        )

    def _create_timeline_slide(
        self, proposal, theme: PresentationTheme
    ) -> PresentationSlide:
        """Criar slide do cronograma"""

        timeline = proposal.implementation_timeline

        content = f"""
        <div style="padding: 30px; font-family: {theme.font_family};">
            <h2 style="color: {theme.primary_color}; border-bottom: 3px solid {theme.accent_color}; padding-bottom: 10px;">
                📅 Cronograma de Implementação
            </h2>
            
            <div style="margin-top: 30px;">
                <div style="text-align: center; margin-bottom: 30px; padding: 20px; background: linear-gradient(45deg, {theme.accent_color}20, {theme.secondary_color}20); border-radius: 10px;">
                    <h3 style="color: {theme.primary_color}; margin-bottom: 10px;">
                        🎯 Duração Total: {timeline.get('total_duration', '24 semanas')}
                    </h3>
                    <p style="color: {theme.text_color};">
                        Implementação gradual com resultados mensuráveis a cada fase
                    </p>
                </div>
            </div>
        """

        # Adicionar fases
        for i, phase in enumerate(
            timeline.get("phases", [])[:4], 1
        ):  # Máximo 4 fases no slide
            content += f"""
            <div style="margin: 20px 0; padding: 20px; background: {theme.background_color}; border-left: 5px solid {theme.secondary_color}; border-radius: 5px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <h3 style="color: {theme.primary_color}; margin: 0;">
                        {phase.get('phase', f'Fase {i}')}
                    </h3>
                    <span style="background: {theme.accent_color}; color: white; padding: 5px 15px; border-radius: 20px; font-weight: bold;">
                        {phase.get('duration', 'A definir')}
                    </span>
                </div>
                <div style="color: {theme.text_color};">
                    <strong>Principais atividades:</strong>
                </div>
                <ul style="color: {theme.text_color}; margin: 10px 0;">
            """

            for activity in phase.get("activities", [])[
                :3
            ]:  # Máximo 3 atividades por fase
                content += f"<li>{activity}</li>"

            content += """
                </ul>
            </div>
            """

        content += """
        </div>
        """

        return PresentationSlide(
            title="Cronograma",
            content=content,
            slide_type="content",
            order=len(proposal.strategies) + 6,
            notes="Apresentar cronograma detalhado e marcos importantes",
        )

    def _create_investment_slide(
        self, proposal, theme: PresentationTheme
    ) -> PresentationSlide:
        """Criar slide de investimento"""

        investment = proposal.investment_breakdown

        content = f"""
        <div style="padding: 30px; font-family: {theme.font_family};">
            <h2 style="color: {theme.primary_color}; border-bottom: 3px solid {theme.accent_color}; padding-bottom: 10px;">
                💰 Investimento e ROI
            </h2>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 30px;">
                
                <div style="background: {theme.background_color}; padding: 25px; border-radius: 10px;">
                    <h3 style="color: {theme.secondary_color}; margin-bottom: 20px; text-align: center;">
                        💳 Estrutura de Investimento
                    </h3>
                    
                    <div style="margin: 15px 0; padding: 15px; background: white; border-radius: 8px; border-left: 4px solid {theme.accent_color};">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="color: {theme.text_color}; font-weight: bold;">Setup Inicial</span>
                            <span style="color: {theme.primary_color}; font-weight: bold; font-size: 1.2em;">
                                R$ {investment.get('setup_inicial', {}).get('value', 5000):,.0f}
                            </span>
                        </div>
                        <div style="color: {theme.text_color}; font-size: 0.9em; margin-top: 5px;">
                            Configuração e setup de ferramentas
                        </div>
                    </div>
                    
                    <div style="margin: 15px 0; padding: 15px; background: white; border-radius: 8px; border-left: 4px solid {theme.secondary_color};">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="color: {theme.text_color}; font-weight: bold;">Mensal Recorrente</span>
                            <span style="color: {theme.primary_color}; font-weight: bold; font-size: 1.2em;">
                                R$ {investment.get('mensal_recorrente', {}).get('value', 10000):,.0f}
                            </span>
                        </div>
                        <div style="color: {theme.text_color}; font-size: 0.9em; margin-top: 5px;">
                            Campanhas e otimizações mensais
                        </div>
                    </div>
                    
                    <div style="margin: 15px 0; padding: 15px; background: linear-gradient(45deg, {theme.accent_color}20, {theme.secondary_color}20); border-radius: 8px; border: 2px solid {theme.accent_color};">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="color: {theme.primary_color}; font-weight: bold;">Total 6 Meses</span>
                            <span style="color: {theme.primary_color}; font-weight: bold; font-size: 1.4em;">
                                {proposal.total_investment}
                            </span>
                        </div>
                    </div>
                </div>
                
                <div style="background: {theme.background_color}; padding: 25px; border-radius: 10px; text-align: center;">
                    <h3 style="color: {theme.secondary_color}; margin-bottom: 20px;">
                        📈 Retorno Esperado
                    </h3>
                    
                    <div style="margin: 20px 0; padding: 30px; background: linear-gradient(135deg, {theme.primary_color}20, {theme.secondary_color}20); border-radius: 15px;">
                        <div style="font-size: 3em; color: {theme.accent_color}; font-weight: bold; margin-bottom: 10px;">
                            {proposal.expected_roi}
                        </div>
                        <div style="color: {theme.primary_color}; font-weight: bold; font-size: 1.2em;">
                            ROI Projetado
                        </div>
                        <div style="color: {theme.text_color}; margin-top: 10px;">
                            em {proposal.project_duration}
                        </div>
                    </div>
                    
                    <div style="margin-top: 20px; padding: 20px; background: #28a74520; border-radius: 10px;">
                        <div style="color: #28a745; font-weight: bold; font-size: 1.1em; margin-bottom: 10px;">
                            💡 Valor Gerado Estimado
                        </div>
                        <div style="color: {theme.text_color}; font-size: 1.3em; font-weight: bold;">
                            R$ {investment.get('roi_projetado', '180.000')}
                        </div>
                    </div>
                </div>
                
            </div>
        </div>
        """

        return PresentationSlide(
            title="Investimento e ROI",
            content=content,
            slide_type="content",
            order=len(proposal.strategies) + 7,
            notes="Demonstrar estrutura de investimento e retorno esperado",
        )

    def _create_metrics_slide(
        self, proposal, theme: PresentationTheme
    ) -> PresentationSlide:
        """Criar slide de métricas"""

        content = f"""
        <div style="padding: 30px; font-family: {theme.font_family};">
            <h2 style="color: {theme.primary_color}; border-bottom: 3px solid {theme.accent_color}; padding-bottom: 10px;">
                📊 Métricas de Sucesso
            </h2>
            
            <div style="margin-top: 30px;">
                <div style="text-align: center; margin-bottom: 30px; padding: 20px; background: linear-gradient(45deg, {theme.accent_color}20, {theme.secondary_color}20); border-radius: 10px;">
                    <h3 style="color: {theme.primary_color}; margin-bottom: 10px;">
                        🎯 Como Mediremos o Sucesso
                    </h3>
                    <p style="color: {theme.text_color};">
                        Acompanhamento transparente com relatórios regulares
                    </p>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
        """

        # Adicionar métricas principais
        key_metrics = [
            {
                "icon": "📈",
                "name": "ROI Global",
                "target": proposal.expected_roi,
                "color": "#28a745",
            },
            {"icon": "💰", "name": "Receita", "target": "+50%", "color": "#007bff"},
            {"icon": "🎯", "name": "Conversão", "target": "+25%", "color": "#fd7e14"},
            {"icon": "📊", "name": "Leads", "target": "+40%", "color": "#6f42c1"},
        ]

        for metric in key_metrics:
            content += f"""
            <div style="background: {theme.background_color}; padding: 20px; border-radius: 10px; text-align: center; border-top: 3px solid {metric['color']};">
                <div style="font-size: 2.5em; margin-bottom: 10px;">{metric['icon']}</div>
                <div style="color: {theme.text_color}; font-weight: bold; margin-bottom: 5px;">{metric['name']}</div>
                <div style="color: {metric['color']}; font-size: 1.5em; font-weight: bold;">{metric['target']}</div>
            </div>
            """

        content += f"""
                </div>
                
                <div style="margin-top: 30px; padding: 25px; background: {theme.background_color}; border-radius: 10px;">
                    <h3 style="color: {theme.secondary_color}; margin-bottom: 15px;">📋 Relatórios e Acompanhamento</h3>
                    <div style="color: {theme.text_color}; line-height: 1.8;">
                        <div style="margin: 10px 0;">📊 <strong>Relatórios semanais</strong> com métricas principais</div>
                        <div style="margin: 10px 0;">📈 <strong>Dashboard em tempo real</strong> para acompanhamento contínuo</div>
                        <div style="margin: 10px 0;">🎯 <strong>Reuniões mensais</strong> de análise e otimização</div>
                        <div style="margin: 10px 0;">📋 <strong>Relatório trimestral</strong> completo com recomendações</div>
                    </div>
                </div>
            </div>
        </div>
        """

        return PresentationSlide(
            title="Métricas de Sucesso",
            content=content,
            slide_type="content",
            order=len(proposal.strategies) + 8,
            notes="Demonstrar como o sucesso será medido e acompanhado",
        )

    def _create_next_steps_slide(
        self, proposal, theme: PresentationTheme
    ) -> PresentationSlide:
        """Criar slide de próximos passos"""

        content = f"""
        <div style="padding: 30px; font-family: {theme.font_family};">
            <h2 style="color: {theme.primary_color}; border-bottom: 3px solid {theme.accent_color}; padding-bottom: 10px;">
                🚀 Próximos Passos
            </h2>
            
            <div style="margin-top: 30px;">
                <div style="text-align: center; margin-bottom: 30px; padding: 25px; background: linear-gradient(135deg, {theme.primary_color}, {theme.secondary_color}); color: white; border-radius: 15px;">
                    <h3 style="font-size: 1.8em; margin-bottom: 15px;">
                        ⚡ Vamos Começar!
                    </h3>
                    <p style="font-size: 1.2em; opacity: 0.9;">
                        Pronto para acelerar seus resultados de marketing?
                    </p>
                </div>
            </div>
        """

        # Adicionar próximos passos
        for i, step in enumerate(proposal.next_steps[:5], 1):
            content += f"""
            <div style="margin: 20px 0; padding: 20px; background: {theme.background_color}; border-radius: 10px; border-left: 5px solid {theme.secondary_color}; display: flex; align-items: center;">
                <div style="background: {theme.accent_color}; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 20px; flex-shrink: 0;">
                    {i}
                </div>
                <div style="color: {theme.text_color}; line-height: 1.6;">
                    {step.replace(f'{i}. ', '')}
                </div>
            </div>
            """

        content += f"""
            <div style="margin-top: 40px; text-align: center; padding: 25px; background: {theme.background_color}; border-radius: 15px; border: 2px solid {theme.accent_color};">
                <h3 style="color: {theme.primary_color}; margin-bottom: 15px;">
                    📞 Vamos Conversar!
                </h3>
                <p style="color: {theme.text_color}; font-size: 1.1em; margin-bottom: 20px;">
                    Estamos prontos para implementar sua estratégia de marketing
                </p>
                <div style="display: flex; justify-content: center; gap: 30px; margin-top: 20px;">
                    <div style="color: {theme.primary_color}; font-weight: bold;">
                        📧 contato@agenciamarketing.com
                    </div>
                    <div style="color: {theme.primary_color}; font-weight: bold;">
                        📱 (11) 99999-9999
                    </div>
                </div>
            </div>
        </div>
        """

        return PresentationSlide(
            title="Próximos Passos",
            content=content,
            slide_type="content",
            order=len(proposal.strategies) + 9,
            notes="Explicar próximos passos e facilitar tomada de decisão",
        )

    def _create_closing_slide(self, theme: PresentationTheme) -> PresentationSlide:
        """Criar slide de encerramento"""

        content = f"""
        <div style="text-align: center; padding: 50px; background: linear-gradient(135deg, {theme.primary_color}, {theme.secondary_color}); color: white; border-radius: 15px; font-family: {theme.font_family};">
            <h1 style="font-size: 3em; margin-bottom: 30px;">
                🙏 Obrigado!
            </h1>
            
            <div style="font-size: 1.5em; margin-bottom: 40px; opacity: 0.9;">
                Esperamos trabalhar juntos para acelerar seus resultados
            </div>
            
            <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 15px; margin: 30px auto; max-width: 500px;">
                <h3 style="margin-bottom: 20px;">📞 Entre em Contato</h3>
                
                <div style="margin: 15px 0; font-size: 1.2em;">
                    📧 contato@agenciamarketing.com
                </div>
                <div style="margin: 15px 0; font-size: 1.2em;">
                    📱 (11) 99999-9999
                </div>
                <div style="margin: 15px 0; font-size: 1.2em;">
                    🌐 www.agenciamarketing.com.br
                </div>
            </div>
            
            <div style="margin-top: 40px; font-size: 1.1em; opacity: 0.8;">
                🤖 Agente de Marketing IA - Seu parceiro estratégico
            </div>
        </div>
        """

        return PresentationSlide(
            title="Obrigado",
            content=content,
            slide_type="cover",
            order=len(self.themes) + 10,
            notes="Encerrar apresentação e reforçar contato",
        )


def display_presentation_interface():
    """Interface para exibir apresentação"""

    st.markdown("## 🎯 **Apresentação da Proposta**")

    if "current_proposal" not in st.session_state:
        st.warning("⚠️ Nenhuma proposta carregada. Gere uma proposta primeiro.")
        return

    proposal = st.session_state["current_proposal"]

    # Opções de tema
    theme_options = {
        "Profissional": "professional",
        "Moderno": "modern",
        "Criativo": "creative",
    }

    selected_theme = st.selectbox(
        "🎨 Escolha o tema da apresentação:", list(theme_options.keys())
    )

    if st.button("🎯 Gerar Apresentação"):
        with st.spinner("🔄 Preparando apresentação..."):
            # Gerar apresentação
            presenter = ProposalPresentation()
            slides = presenter.generate_presentation(
                proposal, theme_options[selected_theme]
            )

            # Salvar slides
            st.session_state["presentation_slides"] = slides

        st.success("✅ Apresentação gerada com sucesso!")

        # Exibir slides
        display_slides(slides)


def display_slides(slides: List[PresentationSlide]):
    """Exibir slides da apresentação"""

    st.markdown("---")
    st.markdown("## 🎬 **Apresentação Gerada**")

    # Navegação entre slides
    if len(slides) > 1:
        slide_titles = [f"Slide {i+1}: {slide.title}" for i, slide in enumerate(slides)]
        selected_slide_index = st.selectbox(
            "📋 Navegar pelos slides:",
            range(len(slide_titles)),
            format_func=lambda x: slide_titles[x],
        )
    else:
        selected_slide_index = 0

    # Exibir slide selecionado
    if slides:
        current_slide = slides[selected_slide_index]

        # Título do slide
        st.markdown(f"### {current_slide.title}")

        # Conteúdo do slide
        st.markdown(current_slide.content, unsafe_allow_html=True)

        # Notas do apresentador
        if current_slide.notes:
            with st.expander("📝 Notas do Apresentador", expanded=False):
                st.info(current_slide.notes)

        # Navegação
        col1, col2, col3 = st.columns(3)

        with col1:
            if selected_slide_index > 0:
                if st.button("⬅️ Slide Anterior"):
                    st.rerun()

        with col2:
            st.markdown(f"**Slide {selected_slide_index + 1} de {len(slides)}**")

        with col3:
            if selected_slide_index < len(slides) - 1:
                if st.button("➡️ Próximo Slide"):
                    st.rerun()

    # Opções de exportação
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📱 Modo Apresentação"):
            st.info("🚀 Modo apresentação (Em desenvolvimento)")

    with col2:
        if st.button("📄 Exportar PDF"):
            st.info("📄 Exportação para PDF (Em desenvolvimento)")

    with col3:
        if st.button("📧 Enviar por Email"):
            st.info("📧 Envio por email (Em desenvolvimento)")
