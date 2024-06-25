# *******************************************************************************#
# Respire Verde
# Author: Wanessa Souza
# RU: 2573850 UNINTER
# Projeto da Atividade Extensionista IV - Implementação
# *******************************************************************************#

import streamlit as st
from config import page_config
from config import page_footer

################
# Page settings
################

page_config()

##############
# Page content
##############


def pagina_sobre():

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
            <h1 style="color:rgb(23, 48, 28);text-align:center;"> Sobre o projeto</h1>
            <p style="color:#ffffff;text-align:center;">Consciência e Ação Contra as Emissões de Gases de Efeito Estufa</p>
        </div>
            """,
        unsafe_allow_html=True,
    )
    st.divider()

    st.write(
        "O :green[**Respire Verde**] 🌱 é um website dedicado a fornecer informações abrangentes sobre emissões de gases de efeito estufa (GEE) soluções para reduzi-las."
    )
    st.write(
        "Nosso objetivo é conscientizar o público sobre a importância de mitigar as emissões de GEE para combater as mudanças climáticas e fornecer recursos práticos para indivíduos, empresas e governos tomarem medidas eficazes."
    )
    st.write(
        "O website foi desenvolvido pela aluna **(RU: 2573850)** como projeto da Atividade Extensionista IV - Implementação"
    )

    pagina_contato()

    ####################
    # Footer
    ####################

    page_footer()


def pagina_contato():
    st.header("Entre em contato conosco! 📞")

    # Formulário de contato
    with st.form(key="contact_form"):
        name = st.text_input("Nome")
        email = st.text_input("E-mail")
        message = st.text_area("Mensagem")

        submit_button = st.form_submit_button(label="Enviar")

    with open("contato.txt", "a", encoding="utf8") as file:
        salvar_mensagem = f"Nome: {name} E-mail: {email} Mensagem: {message}\n"
        file.write(salvar_mensagem)
        file.close()

    if submit_button:
        st.success(f"Obrigado pelo seu contato, {name}!")
        st.info(f"Enviaremos uma resposta para {email} em breve.")
        st.write("Sua mensagem:")
        st.write(message)


def pagina_dados():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader("Fontes de dados")
        st.write("---")

        st.markdown(
            """
            - **Data source**: Global Carbon Budget (2023)
            OurWorldInData.org/co2-and-greenhouse-gas-emissions

            - **Fonte**: Sistema de Estimativa de Emissões e Remoções de Gases de Efeito Estufa (SEEG)- Observatório do Clima (OC), 2023/v11.1
            
            """
        )


def pagina_inicio():
    st.switch_page("index.py")


####################
# Menu interativo
####################

paginas = {
    "❓ Sobre": pagina_sobre,
    "📈Fonte de Dados": pagina_dados,
    "🏡 Página Inicial": pagina_inicio,
}

st.sidebar.title("Menu - Sobre")
pagina_selecionada = st.sidebar.selectbox("Ir para", list(paginas.keys()))
pagina_atual = paginas[pagina_selecionada]()
