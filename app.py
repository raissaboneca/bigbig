import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# Configuração da Página
st.set_page_config(page_title="Logistics Big Data Control", layout="wide")

st.title("🚛 Sistema de Otimização de Frota - 5.000 Caminhões")
st.markdown("### Monitoramento em Tempo Real e Análise Preditiva")

# Sidebar - Filtros de Big Data
st.sidebar.header("Filtros Globais")
regiao = st.sidebar.multiselect("Região", ["Norte", "Sul", "Sudeste", "Nordeste", "Centro-Oeste"], default=["Sudeste"])
status = st.sidebar.selectbox("Status da Frota", ["Todos", "Em Trânsito", "Manutenção", "Aguardando Carga"])

# KPI's Principais
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total da Frota", "5,000", "Ativos")
col2.metric("Economia de Combustível (Mês)", "12.5%", "↑ 2.1%")
col3.metric("Ocupação Média", "88%", "↑ 5%")
col4.metric("Alertas de Manutenção", "42", "-5", delta_color="normal")

# Simulação de Dados de Localização (Big Data)
@st.cache_data
def get_map_data():
    # Simulando coordenadas para visualização
    data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [-23.55, -46.63],
        columns=['lat', 'lon']
    )
    return data

map_data = get_map_data()

# Visualização de Mapa Térmico de Tráfego
st.subheader("📍 Densidade da Frota e Rotas Críticas")
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/dark-v9',
    initial_view_state=pdk.ViewState(
        latitude=-23.55,
        longitude=-46.63,
        zoom=10,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=map_data,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
        ),
    ],
))

# Insights de Big Data
st.subheader("🧠 Insights Preditivos (Machine Learning)")
col_a, col_b = st.columns(2)

with col_a:
    st.write("**Previsão de Gastos (Próximos 30 dias)**")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Diesel', 'Pneus', 'Manutenção'])
    st.area_chart(chart_data)

with col_b:
    st.write("**Top Rotas por Eficiência**")
    st.table(pd.DataFrame({
        'Rota': ['SP -> RJ', 'MG -> SP', 'GO -> MT'],
        'Eficiência': ['98%', '94%', '91%'],
        'Custo/Km': ['R$ 2,10', 'R$ 2,35', 'R$ 2,50']
    }))

st.info("Este protótipo utiliza processamento em nuvem para lidar com o volume de dados de 5.000 dispositivos IoT.")
