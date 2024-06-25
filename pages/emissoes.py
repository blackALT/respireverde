# *******************************************************************************#
# Respire Verde
# Author: Wanessa Souza
# RU: 2573850 UNINTER
# Projeto da Atividade Extensionista IV - Implementação
# *******************************************************************************#

import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from config import page_config_wide
from config import page_footer
import json

page_config_wide()


def noticias_bloco(a, b):
    with open("everything.json", encoding="utf8") as file:
        news = json.load(file)

    st.subheader("Atualizações diárias", divider="gray")
    if news["status"] == "ok":
        if news["totalResults"] == 0:
            st.info("Sem notícias sobre 'Efeito Estufa' publicadas hoje!")
            st.write(
                "Visite a página [**Notícias e Atualizações**](noticias) para ver notícias anteriores"
            )
        else:
            for article in news["articles"][a:b]:
                st.markdown(f"#### [{article['title']}]({article['url']})")
                st.markdown(f"**Fonte**: {article['source']['name']}")
                st.markdown(f"**Publicado em**: {article['publishedAt']}")
                st.markdown(f"{article['description']}")

    st.markdown("""[Saiba mais](noticias)""")


def carregar_dados_brasil():
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
    dados_ano = {
        "Anos": [2000, 2005, 2010, 2015, 2020],
        "CO2": [7.74, 7.70, 7.66, 3.65, 3.74],
        "CH4": [1.92, 2.25, 2.26, 2.20, 2.18],
        "N2O": [0.71, 0.9, 0.92, 0.87, 0.95],
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


def pagina_emissoes():

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
            <h1 style="color:rgb(23, 48, 28);text-align:center;"> Emissões de GEE</h1>
            <p style="color:#ffffff;text-align:center;"> Reduzindo Nossa Pegada de Carbono</p>
        </div>
            """,
        unsafe_allow_html=True,
    )
    st.divider()

    df_ano, df_setor, df_per_capita, df_desmatamento = carregar_dados_brasil()

    tab1, tab2 = st.tabs(["Brasil", "Mundo"])

    with tab1:
        col1, col2 = st.columns([2, 2])
        with col1:
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
                "**Fonte de Dados**: Global Carbon Budget (2023) [Saiba mais](https://OurWorldInData.org/co2-and-greenhouse-gas-emissions)"
            )
            st.divider()

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

        with col2:
            # Emissões por gás
            st.subheader("Total de Emissões líquidas em 2016")
            st.markdown(
                """
                Setores	|Emissão total	|Contrib. setorial (%)	|CO2|	CH4|	N2O|	HFC|
                |-----------|-----------|-----------|-----------|-----------|-----------|-----------|
                |Energia	|422,5	|32%	|399,8	|12,7	|10	|-|
                |Processos Industriais	|90,1|	7%|	78,1|	0,8	|0,5	|10,2|
                |Agropecuária|	439,2	|34%	|-|	274,8	|164,4	|-|
                |Mudança de Uso da Terra|	290,9	|22%|	269	|14,1|	7,8	|-|
                |Tratamento de Resíduos|	62,9|	5%	|0,2|	60,2|	2,4|	-|

            """
            )
            st.write(
                "**Fonte de Dados**: ESTIMATIVAS ANUAIS DE EMISSÕES DE GASES DE EFEITO ESTUFA NO BRASIL 5ª Edição 2020 [Saiba mais](https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/sirene/publicacoes/estimativas-anuais-de-emissoes-gee/arquivos/livro_digital_5ed_estimativas_anuais.pdf)"
            )
            st.divider()

        with col2:
            # Gráfico de Emissões por Setor
            st.header("Emissões por Setor no Brasil")
            st.bar_chart(df_setor.set_index("Setor"))
            st.area_chart(df_setor.set_index("Setor"))

            st.write(
                "**Fonte de Dados**: SEEG [Saiba mais](https://plataforma.seeg.eco.br/?highlight=br-net-emissions-by-sector-nci)"
            )

        with col1:
            # Gráfico de Desmatamento e Emissões de CO2
            st.header("Desmatamento e Emissões de CO2")
            st.area_chart(df_desmatamento.set_index("Ano"))

            st.divider()

    with tab2:
        col1, col2 = st.columns([2, 2])
        with col1:
            st.subheader("Emissões per capita no Mundo ")
            st.write("**Toneladas per capita**")
            data = pd.read_csv("data/world_per_capita.csv")
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

        with col2:
            # Gráfico de Emissões per Capita
            st.subheader("Comparação com outros países")
            data = pd.DataFrame(
                {
                    "País": ["Brasil", "EUA", "China", "Índia", "Reino Unido"],
                    "Emissões per Capita (tCO2e)": [2.2, 14.9, 8.0, 2.0, 4.7],
                }
            )
            chart = (
                alt.Chart(data)
                .mark_bar()
                .encode(y="Emissões per Capita (tCO2e)", x="País")
                .interactive()
            )
            st.altair_chart(chart, theme=None, use_container_width=True)

            st.write(
                "**Fonte de Dados**: CO₂ and Greenhouse Gas Emissions [Saiba mais](https://ourworldindata.org/co2-and-greenhouse-gas-emissions)"
            )
            st.divider()

    ####################
    # Footer
    ####################

    page_footer()


def pagina_sobre_gee():

    col1, col2 = st.columns([2, 1])
    with col2:
        st.image(
            "https://images.pexels.com/photos/60575/smoke-smoking-chimney-fireplace-60575.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
        )
        st.write(
            "**Imagem:** [Pexels](https://www.pexels.com/photo/smoke-coming-out-of-factory-pipes-60575/)"
        )

        st.markdown(
            """
        ## Impactos no Clima Global

        ### Aquecimento Global

        O aumento na concentração de GEE intensifica o efeito estufa, resultando em um aquecimento global. Este aumento na temperatura média da Terra tem diversos impactos, incluindo:

        - **Derretimento das Calotas Polares e Glaciares**: Contribui para o aumento do nível do mar.
        - **Aumento do Nível do Mar**: Pode causar inundações em áreas costeiras.
        - **Mudanças nos Padrões Climáticos**: Alterações nos padrões de precipitação, aumentando a incidência de eventos extremos como secas, tempestades e furacões.
        - **Impacto na Biodiversidade**: Espécies podem ser forçadas a migrar ou podem enfrentar extinção devido às mudanças em seus habitats.

        ### Acidificação dos Oceanos

        O aumento na concentração de CO₂ também leva à maior absorção desse gás pelos oceanos, resultando na acidificação da água. Isso pode ter efeitos devastadores na vida marinha, especialmente para organismos calcários como corais e moluscos.

        ### Problemas de Saúde

        As mudanças climáticas podem exacerbar problemas de saúde, aumentando a incidência de doenças respiratórias, alergias e propagação de doenças transmitidas por vetores, como a malária.
    
        """
        )
    with col1:
        st.markdown(
            """
        # Gases de Efeito Estufa

        ## O que são os Gases de Efeito Estufa?

        Gases de efeito estufa (GEE) são compostos químicos presentes na atmosfera que têm a capacidade de absorver e emitir radiação infravermelha. Este processo é essencial para manter a Terra aquecida e garantir a habitabilidade do planeta, um fenômeno conhecido como efeito estufa. No entanto, o aumento na concentração desses gases, principalmente devido à atividade humana, tem intensificado esse efeito, resultando no aquecimento global.

        ## Principais Gases de Efeito Estufa

        1. **Dióxido de Carbono (CO₂)**
        - **Fonte Principal**: Queima de combustíveis fósseis (carvão, petróleo e gás natural), desmatamento e processos industriais.
        - **Impacto**: Responsável por cerca de 75% do aquecimento global provocado pelos GEE.

        2. **Metano (CH₄)**
        - **Fonte Principal**: Agricultura (principalmente produção de arroz e pecuária), aterros sanitários, e extração de combustíveis fósseis.
        - **Impacto**: Possui um potencial de aquecimento global cerca de 25 vezes maior que o CO₂ em um período de 100 anos.

        3. **Óxidos de Nitrogênio (N₂O)**
        - **Fonte Principal**: Uso de fertilizantes nitrogenados, queima de biomassa e atividades industriais.
        - **Impacto**: Cerca de 300 vezes mais potente que o CO₂ em termos de capacidade de aquecimento global.

        4. **Gases Fluorados (HFCs, PFCs, SF₆)**
        - **Fonte Principal**: Produção industrial, sistemas de refrigeração, e equipamentos elétricos.
        - **Impacto**: Altamente potentes, apesar de presentes em menores concentrações.

        ## Fontes dos Gases de Efeito Estufa

        ### Naturais

        - **Respiração e decomposição de seres vivos**: Todos os organismos vivos respiram e, ao fazê-lo, liberam CO₂.
        - **Erupções vulcânicas**: Vulcões liberam grandes quantidades de CO₂ e outros gases.
        - **Oceano**: Os oceanos absorvem e liberam CO₂ de forma natural.

        ### Humanas (Antropogênicas)

        - **Queima de Combustíveis Fósseis**: Em veículos, usinas de energia e indústrias.
        - **Desmatamento**: A remoção de florestas reduz a capacidade de absorção de CO₂.
        - **Agricultura**: Principalmente a produção de gado e cultivo de arroz.
        - **Indústria**: Processos industriais que utilizam ou produzem gases fluorados.
        - **Resíduos**: A decomposição de resíduos orgânicos em aterros produz metano.
    """
        )

    page_footer()


def pagina_solucoes():
    col1, col2 = st.columns([2, 1])
    with col2:
        st.image(
            "https://images.pexels.com/photos/957024/forest-trees-perspective-bright-957024.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
        )
        st.write(
            "**Imagem:** [Pexels](https://www.pexels.com/photo/worms-eyeview-of-green-trees-957024/)"
        )
        noticias_bloco(4, 7)

    st.divider()
    with col1:
        st.markdown(
            """
        # Soluções para Reduzir os Gases de Efeito Estufa

        A redução dos gases de efeito estufa requer um esforço coletivo que envolve a adoção de tecnologias limpas, práticas sustentáveis, políticas eficazes e a conscientização da sociedade. Cada ação, por menor que seja, contribui para a mitigação das mudanças climáticas e para a preservação do planeta para as futuras gerações.

        ## Energias Renováveis

        ### Fontes de Energia

        - **Solar**: Instalação de painéis solares em residências, empresas e usinas solares.
        - **Eólica**: Investimento em parques eólicos tanto onshore (em terra) quanto offshore (no mar).
        - **Hidrelétrica**: Construção e modernização de usinas hidrelétricas com menor impacto ambiental.
        - **Biomassa**: Utilização de resíduos orgânicos para geração de energia.

        ### Benefícios

        - Redução da dependência de combustíveis fósseis.
        - Emissão zero de gases de efeito estufa durante a produção de energia.

        [Leia mais em](https://ourworldindata.org/renewable-energy)

        ## Eficiência Energética

        ### Edificações

        - **Isolamento Térmico**: Melhoria do isolamento térmico em edifícios para reduzir a necessidade de aquecimento e ar condicionado.
        - **Iluminação LED**: Substituição de lâmpadas incandescentes e fluorescentes por LEDs.
        - **Aparelhos Eficientes**: Uso de eletrodomésticos e equipamentos de alta eficiência energética.

        ### Indústria

        - **Processos Otimizados**: Implementação de tecnologias que aumentem a eficiência dos processos industriais.
        - **Recuperação de Energia**: Aproveitamento de calor residual e outras formas de energia que seriam desperdiçadas.

        ### Transporte

        - **Veículos Elétricos**: Promoção do uso de carros, ônibus e caminhões elétricos.
        - **Transporte Público**: Investimento em infraestrutura de transporte público eficiente e sustentável.
        - **Mobilidade Ativa**: Incentivo ao uso de bicicletas e caminhadas.
        """
        )
    st.divider()
    col3, col4 = st.columns([1, 2])
    with col3:
        st.image(
            "https://images.pexels.com/photos/265216/pexels-photo-265216.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
        )
        st.write(
            "**Imagem:** [Pexels](https://www.pexels.com/photo/worms-eyeview-of-green-trees-957024/)"
        )
    with col4:
        st.markdown(
            """
        ## Agricultura Sustentável
        ### Técnicas Agrícolas

        - **Rotação de Culturas**: Prática de rotação de culturas para manter a saúde do solo.
        - **Agricultura de Precisão**: Uso de tecnologias para otimizar o uso de recursos (água, fertilizantes, etc.).
        - **Agroflorestas**: Integração de árvores nas práticas agrícolas.

        ### Pecuária

        - **Manejo de Pastagens**: Melhor gestão de pastagens para aumentar a absorção de carbono.
        - **Alimentação do Gado**: Uso de aditivos na alimentação do gado para reduzir a emissão de metano.

        ## Florestamento e Reflorestamento

        ### Plantio de Árvores

        - **Reflorestamento**: Recuperação de áreas desmatadas com plantio de árvores nativas.
        - **Florestamento**: Criação de novas florestas em áreas que não tinham cobertura florestal.

        ### Conservação de Florestas

        - **Proteção de Florestas Existentes**: Implementação de políticas para proteger florestas primárias e secundárias.
        - **Controle do Desmatamento**: Fiscalização e aplicação de leis contra o desmatamento ilegal.

        ## Gestão de Resíduos

        ### Redução de Resíduos

        - **Redução no Uso de Plásticos**: Promoção do uso de materiais alternativos e recicláveis.
        - **Reciclagem**: Expansão de programas de reciclagem para reduzir a quantidade de resíduos enviados aos aterros.

        ### Tratamento de Resíduos

        - **Compostagem**: Transformação de resíduos orgânicos em composto.
        - **Aterros Sanitários**: Melhor gestão de aterros para capturar e utilizar o metano produzido pela decomposição dos resíduos.
    """
        )
    st.divider()
    col5, col6 = st.columns([2, 1])
    with col5:
        st.markdown(
            """
        ## Políticas e Regulamentações

        ### Acordos Internacionais

        - **Acordo de Paris**: Compromissos nacionais e internacionais para limitar o aumento da temperatura global.

        ### Políticas Nacionais

        - **Incentivos Fiscais**: Subsídios e incentivos fiscais para energias renováveis e tecnologias de eficiência energética.
        - **Regulamentações de Emissões**: Estabelecimento de limites para emissões de gases de efeito estufa por setores industriais e de transporte.

        ## Educação e Conscientização

        ### Programas Educacionais

        - **Educação Ambiental**: Inclusão de temas sobre mudanças climáticas e sustentabilidade no currículo escolar.
        - **Campanhas de Conscientização**: Campanhas públicas para informar a população sobre a importância da redução de GEE e ações que podem ser tomadas.
        
        [Saiba mais](educacao)
        """
        )
    with col6:
        url = "https://images.pexels.com/photos/19802113/pexels-photo-19802113/free-photo-of-climate-change-and-the-future-of-the-world.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
        st.image(url)
        st.write(f"**Imagem:** [Pexels]({url})")

    page_footer()


def pagina_legislacao():
    col1, col2 = st.columns([2, 1])
    with col2:
        url = "https://images.pexels.com/photos/19802113/pexels-photo-19802113/free-photo-of-climate-change-and-the-future-of-the-world.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
        st.image(url)
        st.write("**Imagem:** [Pexels](url)")
        noticias_bloco(10, 15)
    with col1:
        st.markdown(
            """
            
        # Leis e Políticas sobre Emissões de Gases de Efeito Estufa

        As leis e políticas para reduzir as emissões de gases de efeito estufa variam de acordo com cada país ou região, mas compartilham o objetivo comum de mitigar os efeitos das mudanças climáticas. No Brasil, a Política Nacional sobre Mudança do Clima e outros programas específicos têm um papel crucial. No cenário global, acordos como o Acordo de Paris e legislações específicas de países como o Reino Unido e a Califórnia representam passos significativos para enfrentar o desafio das emissões de GEE.

        ## Brasil

        ### 1. [Política Nacional sobre Mudança do Clima (PNMC)](https://antigo.mma.gov.br/clima/politica-nacional-sobre-mudanca-do-clima.html)
        - **Lei**: Lei nº 12.187/2009
        - **Objetivo**: Estabelece compromissos de redução de emissões de GEE e promove ações de mitigação e adaptação às mudanças climáticas.
        - **Metas**: Redução voluntária de 36,1% a 38,9% das emissões projetadas até 2020.

        ### 2. [Plano Nacional sobre Mudança do Clima (PNMC)](http://www.planalto.gov.br/ccivil_03/_Ato2007-2010/2010/Decreto/D7390.htm)
        - **Diretriz**: Decreto nº 7.390/2010
        - **Objetivo**: Detalha a implementação da PNMC, incluindo ações setoriais para alcançar as metas de redução de emissões.
        - **Setores Focados**: Energia, agricultura, indústria, transportes e resíduos sólidos.

        ### 3. [Programa de Agricultura de Baixo Carbono (ABC e ABC+)](https://www.gov.br/agricultura/pt-br/assuntos/sustentabilidade/planoabc-abcmais)
        - **Iniciativa**: Ministério da Agricultura, Pecuária e Abastecimento
        - **Objetivo**: Incentivar práticas agrícolas sustentáveis e reduzir as emissões de GEE na agropecuária.
        - **Práticas**: Recuperação de pastagens degradadas, plantio direto, integração lavoura-pecuária-floresta.

        ### 4. [Plano Nacional de Adaptação à Mudança do Clima (PNA)](https://antigo.mma.gov.br/clima/adaptacao/plano-nacional-de-adaptacao.html)
        - **Iniciativa**: Ministério do Meio Ambiente
        - **Objetivo**: Identificar e promover ações de adaptação às mudanças climáticas em diversos setores.
        - **Setores Focados**: Saúde, segurança hídrica, agricultura, biodiversidade, cidades.

        ## Mundo

        ### 1. [Acordo de Paris](https://antigo.mma.gov.br/clima/convencao-das-nacoes-unidas/acordo-de-paris.html)
        - **Adotado**: 2015, na 21ª Conferência das Partes (COP21) da UNFCCC
        - **Objetivo**: Manter o aumento da temperatura global bem abaixo de 2°C acima dos níveis pré-industriais, com esforços para limitar o aumento a 1,5°C.
        - **Compromissos**: Cada país deve apresentar Contribuições Nacionalmente Determinadas (NDCs) e revisá-las a cada cinco anos.

        ### 2. [Protocolo de Kyoto](https://www12.senado.leg.br/noticias/entenda-o-assunto/protocolo-de-kyoto)
        - **Adotado**: 1997, na 3ª Conferência das Partes (COP3) da UNFCCC
        - **Objetivo**: Estabelecer metas de redução de emissões de GEE para países desenvolvidos.
        - **Período de Vigência**: 2008-2012 (Primeiro Período de Compromisso) e 2013-2020 (Segundo Período de Compromisso).

        ### 3. [Regulação Europeia de Emissões de CO₂](https://www.europarl.europa.eu/topics/pt/article/20180305STO99003/reducao-das-emissoes-de-carbono-metas-e-politicas-da-ue)
        - **Iniciativa**: União Europeia
        - **Diretriz**: Regulamento (UE) 2018/842
        - **Objetivo**: Reduzir as emissões de GEE em pelo menos 40% até 2030, em comparação com os níveis de 1990.
        - **Mecanismos**: Sistema de Comércio de Emissões da UE (EU ETS), metas nacionais de redução.

        ### 4. [Lei de Mudança Climática do Reino Unido](https://www.theccc.org.uk/what-is-climate-change/a-legal-duty-to-act/)
        - **Lei**: Climate Change Act 2008
        - **Objetivo**: Reduzir as emissões de GEE em pelo menos 80% até 2050, em comparação com os níveis de 1990.
        - **Mecanismos**: Orçamentos de carbono quinquenais, criação do Comitê de Mudança Climática para monitorar e aconselhar o governo.

        ### 5. [Política Climática da Califórnia](https://www.optelgroup.com/pt-br/blog/compreenda-a-mais-recente-legislacao-climatica-da-california-sb-253-e-sb-261/)
        - **Lei**: Global Warming Solutions Act (AB 32)
        - **Objetivo**: Reduzir as emissões de GEE aos níveis de 1990 até 2020, com metas adicionais para 2030 e 2050.
        - **Mecanismos**: Sistema de Cap-and-Trade, regulamentações de eficiência energética, padrões de emissões para veículos.
               
    """
        )
    page_footer()


def pagina_calculadora():
    st.switch_page("pages/calculadora.py")


def pagina_inicio():
    st.switch_page("index.py")


paginas = {
    "🏭 Emissões de GEE": pagina_emissoes,
    "🏭 O que são GEE": pagina_sobre_gee,
    "🏭 Soluções e Redução": pagina_solucoes,
    "🏭 Legislação e Políticas": pagina_legislacao,
    "🏭 Calculadora de Emissões": pagina_calculadora,
    "🏡 Página Inicial": pagina_inicio,
}

st.sidebar.title("Menu - Emissões de GEE")
pagina_selecionada = st.sidebar.selectbox("Ir para", list(paginas.keys()))
pagina_atual = paginas[pagina_selecionada]()
