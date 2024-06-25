# *******************************************************************************#
# Respire Verde
# Author: Wanessa Souza
# RU: 2573850 UNINTER
# Projeto da Atividade Extensionista IV - Implementação
# *******************************************************************************#


import streamlit as st
from config import page_config_wide
from config import page_footer

################
# Page settings
################

page_config_wide()


####################
# Start Page content
####################


def pagina_educacao():

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
            <h1 style="color:rgb(23, 48, 28);text-align:center;">Recursos Educacionais</h1>
            <p style="color:#ffffff;text-align:center;">Rumo à Sustentabilidade com Menos Emissões</p>
        </div>
            """,
        unsafe_allow_html=True,
    )
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("O que são as mudanças climáticas?")
        VIDEO_URL = "https://www.youtube.com/watch?v=b_FV_XLw7eY"
        st.video(VIDEO_URL, subtitles="")

        st.markdown(
            """
            - **Créditos: Laboratório de Ecologia de Ecossistemas UFS**
            - **URL:** https://www.youtube.com/watch?v=b_FV_XLw7eY
            - **Saiba mais:** https://brasil.un.org/pt-br/175180-o-que-s%C3%A3o-mudan%C3%A7as-clim%C3%A1ticas
        """
        )

        st.divider()
    with col2:
        st.subheader("O QUE É EFEITO ESTUFA?")
        VIDEO_URL = "https://www.youtube.com/watch?v=VABv89_yifo"
        st.video(VIDEO_URL, subtitles="")

        st.markdown(
            """
            - **Créditos: Instituto Brasileiro de Agricultura Sustentável**
            - **URL:** https://www.youtube.com/watch?v=VABv89_yifo
        """
        )

        st.divider()

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Esse é o maior desafio da humanidade")
        VIDEO_URL = "https://www.youtube.com/watch?v=sgBF3XrJhvY"
        st.video(VIDEO_URL, subtitles="")

        st.markdown(
            """
            - **Créditos: Atila Iamarino**
            - **URL:** https://www.youtube.com/watch?v=sgBF3XrJhvY
        """
        )

        st.divider()

    with col4:
        st.subheader("Transição para uma economia de baixo carbono")
        VIDEO_URL = "https://www.youtube.com/watch?v=p3mPAA42OmM"
        st.video(VIDEO_URL, subtitles="")

        st.markdown(
            """
            - **Créditos: Exame**
            - **URL:** https://www.youtube.com/watch?v=p3mPAA42OmM
        """
        )

        st.divider()

    ####################
    # Footer
    ####################

    page_footer()


def pagina_acoes():

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
            <h1 style="color:rgb(23, 48, 28);text-align:center;">Ações locais e globais</h1>
            <p style="color:#ffffff;text-align:center;">Consciência e Ação Contra as Emissões de GEE</p>
        </div>
            """,
        unsafe_allow_html=True,
    )
    st.divider()

    st.markdown(
        """
    
    - https://www.instagram.com/recifesustentavel/?hl=en
    - https://emlurb.recife.pe.gov.br/acoes-socioambientais-1
    - https://www.gov.br/mma/pt-br
    - https://www.gov.br/inpe/pt-br
    - https://www.oc.eco.br/
    - https://agenciabrasil.ebc.com.br/
    - https://climainfo.org.br/
    - https://www.diariodepernambuco.com.br/noticia/vidaurbana/2024/03/recife-ganha-econucleo-para-educacao-ambiental.html
    - https://www.folhape.com.br/especiais/forum-nordeste-2023/prefeitura-promove-acoes-que-estimulam-a-sustentabilidade/288706/
    """
    )


####################
# End Page content
####################

#############
# Subpáginas
#############


def pagina_inicio():
    st.switch_page("index.py")


def pagina_calculadora():
    st.switch_page("pages/calculadora.py")

    # https://www.sigaverde.com/calcule-aqui-a-emissao-de-carbono-da-sua-frota/
    # https://sosma.org.br/calcule-sua-emissao-de-co2
    # https://esalqlastrop.com.br/capa.asp?pi=calculadora_emissoes


# Cria um menu interativo
paginas = {
    "📚 Recursos Educacionais": pagina_educacao,
    "🌎 Ações locais e globais": pagina_acoes,
    "🏡 Página Inicial": pagina_inicio,
}

# Renderiza o menu e a página selecionada
st.sidebar.title("Menu - Emissões de GEE")
pagina_selecionada = st.sidebar.selectbox("Ir para", list(paginas.keys()))
pagina_atual = paginas[pagina_selecionada]()
