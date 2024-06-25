# *******************************************************************************#
# Respire Verde
# Author: Wanessa Souza
# RU: 2573850 UNINTER
# Projeto da Atividade Extensionista IV - Implementação
# *******************************************************************************#


import streamlit as st
import requests
import json
from config import page_config
from config import page_footer


################
# Page settings
################

page_config()


##############
# Page content
##############


def pagina_noticias():
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
            <h1 style="color:rgb(23, 48, 28);text-align:center;"> Notícias e Atualizações</h1>
            <p style="color:#ffffff;text-align:center;">Ar Puro, Planeta Saudável: Juntos Contra as Emissões de Gases Estufa</p>
        </div>
            """,
        unsafe_allow_html=True,
    )
    st.divider()

    with open("everything.json", encoding="utf8") as file:
        news = json.load(file)
        st.header("Atualizações diárias")

        tab1, tab2, tab3 = st.tabs(
            ["**Notícias recentes**", "Outras notícias", "Arquivadas"]
        )

        def carrega_news(last_page, page):
            for article in news["articles"][last_page:page]:
                st.markdown(f"### [{article['title']}]({article['url']})")
                st.markdown(f"**Fonte**: {article['source']['name']}")
                st.markdown(f"**Publicado em**: {article['publishedAt']}")
                st.markdown(f"{article['description']}")
                st.image(article["urlToImage"], use_column_width=True)
                # st.markdown("---")

        with tab1:
            col1, col2 = st.columns([4, 1])
            with col1:
                carrega_news(0, 10)

        with tab2:
            col3, col4 = st.columns([4, 1])
            with col3:
                carrega_news(10, 20)

        with tab3:
            col5, col6 = st.columns([4, 1])
            with col5:
                carrega_news(20, 100)

    ####################
    # Footer
    ####################

    page_footer()


####################
# End Page content
####################


def pagina_artigos():
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
            <h1 style="color:rgb(23, 48, 28);text-align:center;">Artigos e Entrevistas</h1>
            <p style="color:#ffffff;text-align:center;">Fique por dentro!</p>
        </div>
            """,
        unsafe_allow_html=True,
    )
    st.divider()

    st.markdown(
        """
        Estes sites oferecem uma ampla gama de recursos, incluindo artigos científicos, entrevistas com especialistas, relatórios e notícias atualizadas sobre emissões de gases de efeito estufa e mudanças climáticas.
        ## Sites Nacionais (Brasil)

        1. **[Ministério do Meio Ambiente (MMA)](https://www.gov.br/mma/pt-br)**
        - **Descrição**: Órgão governamental responsável pela política ambiental no Brasil, incluindo mudanças climáticas.
        - **Recursos**: Notícias, relatórios, entrevistas e documentos oficiais.

        2. **[Instituto Nacional de Pesquisas Espaciais (INPE)](http://www.inpe.br/)**
        - **Descrição**: O INPE realiza pesquisas científicas sobre a atmosfera, clima e monitoramento ambiental.
        - **Recursos**: Publicações, dados climáticos, artigos científicos e entrevistas com pesquisadores.

        3. **[Observatório do Clima](https://www.oc.eco.br/)**
        - **Descrição**: Coalizão de organizações da sociedade civil que promove a luta contra as mudanças climáticas no Brasil.
        - **Recursos**: Relatórios, artigos, comunicados de imprensa e entrevistas.

        4. **[Agência Brasil](https://agenciabrasil.ebc.com.br/)**
        - **Descrição**: Serviço de notícias da Empresa Brasil de Comunicação (EBC), cobrindo temas de meio ambiente e mudanças climáticas.
        - **Recursos**: Notícias, reportagens, entrevistas e análises.

        5. **[ClimaInfo](https://climainfo.org.br/)**
        - **Descrição**: Portal de notícias focado em mudanças climáticas e sustentabilidade, oferecendo uma curadoria diária de notícias e artigos.
        - **Recursos**: Notícias, artigos, entrevistas e boletins informativos.

         ## Sites Internacionais

        1. **[Intergovernmental Panel on Climate Change (IPCC)](https://www.ipcc.ch/)**
        - **Descrição**: O IPCC é a principal organização global fornecendo relatórios científicos sobre as mudanças climáticas, suas causas, impactos e possíveis soluções.
        - **Recursos**: Relatórios, artigos científicos e resumos para formuladores de políticas.

        2. **[United Nations Framework Convention on Climate Change (UNFCCC)](https://unfccc.int/)**
        - **Descrição**: A UNFCCC promove a cooperação internacional para combater as mudanças climáticas e publica relatórios e documentos sobre as negociações e acordos climáticos.
        - **Recursos**: Artigos, comunicados de imprensa, entrevistas e documentos de conferências.

        3. **[NASA Global Climate Change](https://climate.nasa.gov/)**
        - **Descrição**: A NASA fornece dados e pesquisas sobre mudanças climáticas, com foco em estudos de caso específicos e impacto global.
        - **Recursos**: Artigos, entrevistas com cientistas, dados climáticos e ferramentas interativas.

        4. **[Environmental Protection Agency (EPA) - Climate Change](https://www.epa.gov/climate-change)**
        - **Descrição**: A EPA dos EUA oferece informações detalhadas sobre as causas e efeitos das mudanças climáticas e as ações para mitigar os impactos.
        - **Recursos**: Relatórios, artigos científicos, entrevistas e recursos educacionais.

        5. **[World Resources Institute (WRI)](https://www.wri.org/)**
        - **Descrição**: O WRI é uma organização de pesquisa global que fornece análises e soluções práticas para proteger o meio ambiente e melhorar a vida das pessoas.
        - **Recursos**: Relatórios, artigos, blogs e entrevistas com especialistas.
           
            """
    )


def pagina_inicio():
    st.switch_page("index.py")


# Cria um menu interativo
paginas = {
    "📰 Notícias e Atualizações": pagina_noticias,
    "📢 Artigos e Entrevistas": pagina_artigos,
    "🏡 Página Inicial": pagina_inicio,
}

# Renderiza o menu e a página selecionada
st.sidebar.title("Menu - Notícias")
pagina_selecionada = st.sidebar.selectbox("Ir para", list(paginas.keys()))
pagina_atual = paginas[pagina_selecionada]()
