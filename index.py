# *******************************************************************************#
# Respire Verde
# Author: Wanessa Souza
# RU: 2573850 UNINTER
# Projeto da Atividade Extensionista IV - Implementação
# *******************************************************************************#


import streamlit as st
import requests
import config
from datetime import date
import json
import time
import pandas as pd
import altair as alt
import numpy as np

###############
# Page settings
################

from config import page_config_wide
from config import carregar_dados

page_config_wide()


def pagina_inicio():

    st.markdown(
        """
        <div style="
         background: rgb(71,101,84);
        background: linear-gradient(0deg, rgba(71,101,84,1) 36%, rgba(255,255,255,1) 56%, rgba(255,255,255,1) 67%); 
        padding:10px;border-radius:10px";
        position: inherit;
        left: 0;  
        bottom: 0;
        width: 100%>
            <h1 style="color:rgb(23, 48, 28);text-align:center;"> Portal Respire Verde</h1>
            <p style="color:#ffffff;text-align:center;"> Um website dedicado a fornecer informações sobre emissões de gases de efeito estufa.  🌱</p>
        </div>
            """,
        unsafe_allow_html=True,
    )
    st.divider()

    col1, col2 = st.columns([2, 1])

    with col1:
        with st.container():
            st.markdown(
                """
                ### O que são :green[**gases estufa**]? 

                Gases de efeito estufa (GEE) são compostos químicos presentes na atmosfera que têm a capacidade de absorver e emitir radiação infravermelha. 
                
                Este processo é essencial para manter a Terra aquecida e garantir a habitabilidade do planeta, um fenômeno conhecido como efeito estufa. 
                
                No entanto, o aumento na concentração desses gases, principalmente devido à atividade humana, tem intensificado esse efeito, resultando no aquecimento global.

                [**Saiba mais**](emissoes)
            """
            )

    with col2:

        VIDEO_URL = "https://www.youtube.com/watch?v=VABv89_yifo"
        st.video(VIDEO_URL, subtitles="")

    cola, colb = st.columns([1, 2])
    with cola:
        VIDEO_URL = "https://www.youtube.com/watch?v=sgBF3XrJhvY"
        st.video(VIDEO_URL, subtitles="")

    with colb:
        st.markdown(
            """
             ### Porque é importante combater o :green[**Aquecimento Global**]?

        O aumento na concentração de GEE intensifica o efeito estufa, resultando em um aquecimento global.
        
        Este aumento na temperatura média da Terra tem diversos impactos, incluindo:

        - **Derretimento das Calotas Polares e Glaciares**: Contribui para o aumento do nível do mar.
        - **Aumento do Nível do Mar**: Pode causar inundações em áreas costeiras.
        - **Mudanças nos Padrões Climáticos**: Alterações nos padrões de precipitação, aumentando a incidência de eventos extremos como secas, tempestades e furacões.
        - **Impacto na Biodiversidade**: Espécies podem ser forçadas a migrar ou podem enfrentar extinção devido às mudanças em seus habitats.

        [**Saiba mais**](emissoes)
            """
        )

    st.subheader("Dados de Emissões", divider="gray")

    col3, col4 = st.columns([2, 2])

    with col3:
        st.subheader("Emissões per capita no Brasil ")
        st.write("**Toneladas per capita**")
        data = pd.read_csv("data/brazil_per_capita.csv")

        chart = (
            alt.Chart(data)
            .mark_line()
            .encode(
                x="Ano",
                y="CO2",
            )
            .interactive()
        )
        st.altair_chart(chart, theme=None, use_container_width=True)
        st.write(
            "**Fonte de Dados**: CO₂ and Greenhouse Gas Emissions [Saiba mais](https://OurWorldInData.org/co2-and-greenhouse-gas-emissions)"
        )
        st.divider()

    with col3:
        st.subheader("Emissões Totais no Brasil por GEE")
        st.write("**Toneladas per capita**")
        data = pd.DataFrame(
            {
                "Anos": [2000, 2005, 2010, 2015, 2020],
                "CO2": [7.74, 7.70, 7.66, 3.65, 3.74],
                "CH4": [1.92, 2.25, 2.26, 2.20, 2.18],
                "N2O": [0.71, 0.9, 0.92, 0.87, 0.95],
            }
        )

        chart = (
            alt.Chart(data)
            .transform_fold(["CO2", "CH4", "N2O"])
            .mark_line()
            .encode(x="Anos:O", y="value:Q", color="key:N")
            .interactive()
        )
        st.altair_chart(chart, theme=None, use_container_width=True)

        st.write(
            "**Fonte de Dados**: Historical GHG Emissions (2021) [Saiba mais](https://www.climatewatchdata.org/ghg-emissions)"
        )

    with open("everything.json", encoding="utf8") as file:
        news = json.load(file)

    with col4:
        st.subheader("Atualizações diárias", divider="gray")
        if news["status"] == "ok":
            if news["totalResults"] == 0:
                st.info("Sem notícias sobre 'Efeito Estufa' publicadas hoje!")
                st.write(
                    "Visite a página [**Notícias e Atualizações**](noticias) para ver notícias anteriores"
                )
            else:
                for article in news["articles"][0:3]:
                    st.markdown(f"#### [{article['title']}]({article['url']})")
                    st.markdown(f"**Fonte**: {article['source']['name']}")
                    st.markdown(f"**Publicado em**: {article['publishedAt']}")
                    st.markdown(f"{article['description']}")
                    st.image(article["urlToImage"], use_column_width=True)

        st.markdown("""[Saiba mais](noticias)""")
    with col3:
        df_ano, df_setor, df_per_capita, df_desmatamento = carregar_dados()

        st.header("Emissões por Setor no Brasil")
        st.bar_chart(df_setor.set_index("Setor"))

        st.header("Desmatamento na Amazônia e Emissões de CO2")
        st.area_chart(df_desmatamento.set_index("Ano"))
        st.write(
            "**Fonte**: [Imazon](https://imazon.org.br/imprensa/desmatamento-na-amazonia-chega-a-10-781-km%C2%B2-nos-ultimos-12-meses-maior-area-em-15-anos/)"
        )

    ####################
    # Footer
    ####################

    from config import page_footer

    page_footer()


def pagina_emissoes():
    st.switch_page("pages/emissoes.py")


def pagina_noticias():
    st.switch_page("pages/noticias.py")


def pagina_educacao():
    st.switch_page("pages/educacao.py")


def pagina_sobre():
    st.switch_page("pages/sobre.py")


def pagina_calculadora():
    st.switch_page("pages/calculadora.py")


def teste():
    st.switch_page("pages/teste.py")


# Menu interativo

paginas = {
    "🏡 Página Inicial": pagina_inicio,
    "🏭 Emissões de GEE": pagina_emissoes,
    "📰 Notícias": pagina_noticias,
    "📚 Recursos Educacionais": pagina_educacao,
    "❓ Sobre": pagina_sobre,
    "📟 Calculadora de Emissões": pagina_calculadora,
}

st.sidebar.title("Menu - Início")
pagina_selecionada = st.sidebar.selectbox("Ir para", list(paginas.keys()))
pagina_atual = paginas[pagina_selecionada]()

st.sidebar.header("Calculadora de Emissões", divider="gray")

with st.sidebar:

    def calcular_emissoes(tipo_veiculo, km_percorridos):
        fatores_emissao = {
            "carro_gasolina": 0.2392,
            "carro_diesel": 0.2700,
            "carro_eletrico": 0.0500,
            "moto": 0.1030,
            "onibus": 0.8220,
            "caminhao": 1.3000,
        }

        if tipo_veiculo in fatores_emissao:
            emissoes_co2 = fatores_emissao[tipo_veiculo] * float(km_percorridos)
            return emissoes_co2
        else:
            return None

    def main():

        tipo_veiculo = st.selectbox(
            "Escolha o tipo de veículo: ",
            (
                "carro_gasolina",
                "carro_diesel",
                "carro_eletrico",
                "moto",
                "onibus",
                "caminhao",
            ),
        )
        km_percorridos = st.number_input("Digite o número de quilômetros percorridos: ")

        emissoes_co2 = calcular_emissoes(tipo_veiculo, km_percorridos)

        if emissoes_co2 is not None:
            if st.button("Calcular"):
                with st.spinner("Loading..."):
                    time.sleep(1)
                st.success(
                    f"Um **{tipo_veiculo}** que percorreu **{km_percorridos}** km produziu aproximadamente **{round(emissoes_co2,2)}** kg de CO₂."
                )
        else:
            st.write("Tipo de veículo não reconhecido. Por favor, tente novamente.")

    if __name__ == "__main__":
        main()
