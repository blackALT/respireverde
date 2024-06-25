# *******************************************************************************#
# Respire Verde
# Author: Wanessa Souza
# RU: 2573850 UNINTER
# Projeto da Atividade Extensionista IV - Implementação
# *******************************************************************************#

import streamlit as st
import pandas as pd


def page_config():
    st.set_page_config(
        page_title="Respire Verde",
        page_icon="🌱",
        layout="centered",  # wide
        initial_sidebar_state="auto",  # collapsed
    )

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style.css")


def page_footer():
    st.markdown(
        """
    <div class="footer">
        <p> © 2024 Respire Verde 🌱 Desenvolvido por <a href="https://github.com/blackALT" target="_blank"> blackALT</a> (RU: 2573850)
        <img src="https://res.cloudinary.com/drwsupfyj/image/upload/v1714026198/environmentalnewsscraper/vbbpbt86no6rmbue5xs5.png" style="width: 1%;" /><br>
        <p>
    </div>
    """,
        unsafe_allow_html=True,
    )


def page_config_wide():
    st.set_page_config(
        page_title="Respire Verde",
        page_icon="🌱",
        layout="wide",  # wide
        initial_sidebar_state="auto",  # auto
    )

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style.css")


def carregar_dados():
    dados_ano = {
        "Anos": [2000, 2005, 2010, 2015, 2020],
        "CO2": [7.74, 7.70, 7.66, 3.65, 3.74],
        "CH4": [1.92, 2.25, 2.26, 2.20, 2.18],
        "N2O": [0.71, 0.9, 0.92, 0.87, 0.95],
    }
    dados_setor = {
        "Setor": [
            "Energia",
            "Agropecuária",
            "Indústria",
            "Resíduos",
            "Mudança de Uso da Terra",
        ],
        "(MtCO2e) - 2000": [
            289423.802,
            538083.795,
            64582.524,
            49292.167,
            1232626.474,
        ],
        "(MtCO2e) - 2005": [
            317593.020,
            577673.796,
            67165.009,
            60773.856,
            1293865.042,
        ],
        "(MtCO2e) - 2010": [
            372390.739,
            523332.037,
            78792.582,
            69765.171,
            160274.912,
        ],
        "(MtCO2e) - 2015": [
            451898.398,
            504182.708,
            79483.185,
            81909.448,
            353481.172,
        ],
        "(MtCO2e) - 2020": [
            387412.259,
            437849.859,
            76275.474,
            91239.143,
            454770.269,
        ],
    }
    dados_per_capita = {
        "País": ["Brasil", "EUA", "China", "Índia", "Reino Unido"],
        "Emissões per Capita (tCO2e)": [2.2, 14.9, 8.0, 2.0, 4.7],
    }
    dados_desmatamento = {
        "Ano": [2010, 2015, 2020],
        "Desmatamento (mil km²)": [1489, 3323, 6543],
        "Emissões de CO2 (MtCO2e)": [7.66, 3.65, 3.74],
    }
    return (
        pd.DataFrame(dados_ano),
        pd.DataFrame(dados_setor),
        pd.DataFrame(dados_per_capita),
        pd.DataFrame(dados_desmatamento),
    )
