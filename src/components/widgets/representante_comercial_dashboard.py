"""
Componente de Dashboard - Representante Comercial
Migrado de dashboards/representante_comercial_dashboard.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
...existing code...
    """Dashboard específico para análise de canais de vendas"""
    st.header("🎯 Dashboard Executivo - Gestão de Canais")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        total_vendas = df[df["Status"] == "Fechado"]["Valor_Negocio"].sum()
        st.metric("💰 Vendas Fechadas", f"R$ {total_vendas:,.0f}")
    with col2:
        pipeline = df[df["Status"] == "Negociando"]["Valor_Negocio"].sum()
        st.metric("🔄 Pipeline Ativo", f"R$ {pipeline:,.0f}")
    with col3:
        roi_medio = df[df["Status"] == "Fechado"]["ROI"].mean()
        st.metric("📈 ROI Médio", f"{roi_medio:.1f}x")
    with col4:
        tempo_medio = df[df["Status"] == "Fechado"]["Tempo_Conversao"].mean()
        st.metric("⏱️ Tempo Médio", f"{tempo_medio:.0f} dias")
    st.subheader("📊 Performance por Canal de Vendas")
    col1, col2 = st.columns(2)
    with col1:
        vendas_canal = (
            df.groupby("Canal")
            .agg({"Valor_Negocio": "sum", "ROI": "mean"})
            .reset_index()
        )
        fig_canal = px.bar(
            vendas_canal,
            x="Canal",
            y="Valor_Negocio",
            title="💰 Receita por Canal",
            color="ROI",
            color_continuous_scale="RdYlGn",
        )
        st.plotly_chart(fig_canal, use_container_width=True)
    with col2:
        fig_roi = px.box(
            df[df["Status"] == "Fechado"],
            x="Canal",
            y="ROI",
            title="📈 Distribuição ROI por Canal",
        )
        st.plotly_chart(fig_roi, use_container_width=True)
    st.subheader("📅 Evolução Temporal das Vendas")
    df["Data"] = pd.to_datetime(df["Data"])
    vendas_tempo = (
        df[df["Status"] == "Fechado"]
        .groupby([df["Data"].dt.to_period("M"), "Canal"])["Valor_Negocio"]
        .sum()
        .reset_index()
    )
    vendas_tempo["Data"] = vendas_tempo["Data"].astype(str)

    def create_sales_channel_dashboard(df):
        """Dashboard específico para análise de canais de vendas"""
        st.header("🎯 Dashboard Executivo - Gestão de Canais")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            total_vendas = df[df["Status"] == "Fechado"]["Valor_Negocio"].sum()
            st.metric("💰 Vendas Fechadas", f"R$ {total_vendas:,.0f}")
        with col2:
            pipeline = df[df["Status"] == "Negociando"]["Valor_Negocio"].sum()
            st.metric("🔄 Pipeline Ativo", f"R$ {pipeline:,.0f}")
        with col3:
            roi_medio = df[df["Status"] == "Fechado"]["ROI"].mean()
            st.metric("📈 ROI Médio", f"{roi_medio:.1f}x")
        with col4:
            tempo_medio = df[df["Status"] == "Fechado"]["Tempo_Conversao"].mean()
            st.metric("⏱️ Tempo Médio", f"{tempo_medio:.0f} dias")
        st.subheader("📊 Performance por Canal de Vendas")
        col1, col2 = st.columns(2)
        with col1:
            vendas_canal = (
                df.groupby("Canal")
                .agg({"Valor_Negocio": "sum", "ROI": "mean"})
                .reset_index()
            )
            fig_canal = px.bar(
                vendas_canal,
                x="Canal",
                y="Valor_Negocio",
                title="💰 Receita por Canal",
                color="ROI",
                color_continuous_scale="RdYlGn",
            )
            st.plotly_chart(fig_canal, use_container_width=True)
        with col2:
            fig_roi = px.box(
                df[df["Status"] == "Fechado"],
                x="Canal",
                y="ROI",
                title="📈 Distribuição ROI por Canal",
            )
            st.plotly_chart(fig_roi, use_container_width=True)
        st.subheader("📅 Evolução Temporal das Vendas")
        df["Data"] = pd.to_datetime(df["Data"])
        vendas_tempo = (
            df[df["Status"] == "Fechado"]
            .groupby([df["Data"].dt.to_period("M"), "Canal"])["Valor_Negocio"]
            .sum()
            .reset_index()
        )
        vendas_tempo["Data"] = vendas_tempo["Data"].astype(str)
        fig_tempo = px.line(
            vendas_tempo,
            x="Data",
            y="Valor_Negocio",
            color="Canal",
            title="📅 Evolução de Vendas por Canal",
        )
        st.plotly_chart(fig_tempo, use_container_width=True)
