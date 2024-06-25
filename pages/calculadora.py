# *******************************************************************************#
# Respire Verde
# Author: Wanessa Souza
# RU: 2573850 UNINTER
# Projeto da Atividade Extensionista IV - Implementação
# *******************************************************************************#


import streamlit as st
from config import page_footer
from config import page_config_wide
import time

################
# Page settings
################

page_config_wide()

##############
# Page content
##############


def pagina_calculadora():

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
            <h1 style="color:rgb(23, 48, 28);text-align:center;">Calculadora de Emissões</h1>
            <p style="color:#ffffff;text-align:center;">Nós podemos construir um Futuro com menos Gases Estufa!</p>
        </div>
            """,
        unsafe_allow_html=True,
    )
    st.divider()

    col1, col2 = st.columns([1, 2])
    with col1:

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
                "**Escolha o tipo de veículo:** ",
                (
                    "carro_gasolina",
                    "carro_diesel",
                    "carro_eletrico",
                    "moto",
                    "onibus",
                    "caminhao",
                ),
            )
            km_percorridos = st.number_input(
                "**Digite o número de quilômetros percorridos:** "
            )

            emissoes_co2 = calcular_emissoes(tipo_veiculo, km_percorridos)

            if emissoes_co2 is not None:
                if st.button("Calcular"):
                    with st.spinner("Loading..."):
                        time.sleep(1)
                    st.success(
                        f"Um **{tipo_veiculo}** que percorreu **{km_percorridos}** km produziu aproximadamente **{round(emissoes_co2,2)}** kg de CO₂."
                    )
            else:
                st.error("Tipo de veículo não reconhecido. Por favor, tente novamente.")

        if __name__ == "__main__":
            main()

    with col2:
        st.subheader("Como calcular a emissão de carbono de um veículo?")
        st.write(
            "A calculadora considera diferentes tipos de veículos e os quilômetros percorridos para calcular as emissões de CO₂ com base no **fator de emissão**. "
        )
        st.warning(
            "O fator de emissão é o valor de emissões de CO2 em **kg/quilômetro** percorrido."
        )
        st.write(
            "O cálculo das emissões de carbono de um veículo baseia-se na quantidade de combustível consumido e no fator de emissão do combustível, que é a quantidade de CO₂ emitida por unidade de combustível queimado."
        )
        st.write(
            "O processo geral para calcular as emissões de carbono de um veículo envolve os seguintes passos:"
        )
        st.write(
            "1. **Determinar o consumo de combustível**: Calcule a quantidade de combustível consumido pelo veículo para percorrer uma certa distância."
        )
        st.write(
            "2. **Obter o fator de emissão do combustível**: Este fator é geralmente fornecido em gramas de CO₂ por litro de combustível consumido."
        )
        st.write(
            "3. **Calcular as emissões de CO₂**: Multiplique a quantidade de combustível consumido pelo fator de emissão."
        )

        st.info(
            """
        Fórmula para Calcular as Emissões de CO₂

        **Emissões de CO₂** = Consumo de Combustível **x** Fator de Emissão"""
        )

    ####################
    # Footer
    ####################

    page_footer()


def pagina_inicio():
    st.switch_page("index.py")


# Cria um menu interativo
paginas = {
    "📟 Calculadora de Emissões": pagina_calculadora,
    "🏡 Página Inicial": pagina_inicio,
}

# Renderiza o menu e a página selecionada
st.sidebar.title("Menu - Emissões de GEE")
pagina_selecionada = st.sidebar.selectbox("Ir para", list(paginas.keys()))
pagina_atual = paginas[pagina_selecionada]()
