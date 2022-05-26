import numpy as np
import os
from flask import Flask, request, render_template, make_response
import joblib
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components
import streamlit as st


st.set_page_config(page_title="IMDS Team", page_icon="🎥")

st.sidebar.image('static/rf team2.png', use_column_width=True )
st.sidebar.title('Menu')
pagSelecionada = st.sidebar.selectbox('Escolha uma seção',['Home', 'Arquitetura & Deploy do Projeto', 'EDA', 'Modelo', 'Próximos Passos', 'Equipe e Agradecimentos'])

if pagSelecionada == 'Home':

    st.title("Bem-vindo!")  
      
    st.markdown("Este trabalho foi realizado pelo grupo 2 do curso de [Data Science](https://www.digitalhouse.com/br/produtos/dados/data-science) da Escola Digital House. Os componentes do grupo são: [Danilo Federico](https://www.linkedin.com/in/danilo-federico-61b140b8/), [Eliel Reis](https://www.linkedin.com/in/eliel-reis-a059a861/), [Genival Junior](https://www.linkedin.com/in/genival-neves-brasil-junior/) e [Fábio Souza](https://www.linkedin.com/in/fabio-souza-a67321129/).")
    st.markdown("O tema escolhido para elaboração do projeto foi baseado na fonte de dados do IMDB sobre filmes.")
    st.markdown("### Do que se trata o projeto?")
    st.markdown("Nosso cliente é um streamer que fornece o serviço de catalogos de filmes para seus clientes, com o grande número de filmes desenvolvidos por empresas, torna-se necessário selecionar os filmes que possam engajar os consumidores da plataforma.")
    st.markdown("### Como responder à necessidade do cliente?")
    st.markdown("Construir um modelo agrupar os filmes com caracteristicas similares onde se torna extremamente útil para a empresa, pois ela pode planejar adequadamente sua estratégia de comunicação e serviço para alcançar esses consumidores e otimizar seu modelo de negócios, aumentando a receita.")  
       
    st.header("Repositório do Projeto:")
    st.markdown("● [Análise Exploratória](https://github.com/Chitolina/RandomForestTeam/tree/main/EDA)")     
    st.markdown("● [Gerenciamento de Tarefas](https://trello.com/b/Nypkyrp3/randomforest)")  
    st.markdown("● [Modelo Clusterizador](https://github.com/Chitolina/RandomForestTeam/blob/main/EDA/Funcao%20de%20Custo%20e%20Selecao%20de%20Modelo.ipynb)")
    st.markdown("● [Dashboard BI](https://github.com/Chitolina/RandomForestTeam/tree/main/BI_RANDOMF)")
    st.markdown("● [Apresentação](https://github.com/webercg/Health-Insurance-Cross-Sell-Prediction)")

elif pagSelecionada == 'Arquitetura & Deploy do Projeto':

    st.title("Arquitetura do Projeto")
    
    st.markdown('Para a nosssa engenharia de dados obtemos uma solução utilizando a API do TMDB e do IMDB, isso nos deu a oportunidade de trabalhar com as informações globais dessas companhias.')
    st.markdown('A organização e o processo dos dados foram feitas Jupyter utilizando Python e o deploy foi realizado utilizando Flask e Streamlit.')

    img = Image.open("static/structure.jpg") 
    st.image(img, caption='IMDS: Estrutura')


elif pagSelecionada == 'EDA':

    st.title("Análise Exploratória dos dados")

    components.iframe("https://app.powerbi.com/view?r=eyJrIjoiZjE1Y2FhOTMtMzJlOS00ZTgyLThhMjQtMWRjMjNiZGFlOWE1IiwidCI6IjNjZDM5YWMyLWViN2EtNDU5Ny1iNGFmLTc1Nzg2ZmE2YjQzYiJ9&pageName=ReportSection100bea7b4798115cbd5a", width=600, height=400)

elif pagSelecionada == 'Modelo':

    st.title("Modelo Clusterizador")

    components.iframe("https://app.powerbi.com/view?r=eyJrIjoiMDgyMDlkYzktNWY1Ny00Y2RjLWE0N2UtNDg3ZGYyNzkwMmZiIiwidCI6IjNjZDM5YWMyLWViN2EtNDU5Ny1iNGFmLTc1Nzg2ZmE2YjQzYiJ9", width=600, height=400)

elif pagSelecionada == 'Próximos Passos':

    st.title("Próximos Passos")
    
    st.markdown('Após realizarmos nosso projeto e concluirmos que a utilização do modelo atende uma demanda do mercado, estamos trabalhando para incluirPara a nosssa engenharia de dados obtemos uma solução utilizando a API do TMDB e do IMDB, isso nos deu a oportunidade de trabalhar com as informações globais dessas companhias.')
    st.markdown('A organização e o processo dos dados foram feitas Jupyter utilizando Python e o deploy foi realizado utilizando Flask e Streamlit.')


elif pagSelecionada == 'Equipe e Agradecimentos':
    st.title("Equipe e Agradecimentos")

    col1, col2, col3 = st.columns(3)

    with col1:
        img = Image.open("static/DN.jpeg" ) 
        st.image(img)
        st.write('')
        img = Image.open("static/ER.png" ) 
        st.image(img) 
        st.write('')
        img = Image.open("static/GJ.jpeg" ) 
        st.image(img)
        st.write('')
        img = Image.open("static/FS.jpeg" ) 
        st.image(img)    


    with col2:

        st.markdown("**Danilo Federico**")
        st.markdown('[LinkedIn](https://www.linkedin.com/in/danilo-federico-61b140b8/)')
        
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')

        st.markdown("**Eliel Reis**")
        st.markdown('[LinkedIn](https://www.linkedin.com/in/eliel-reis-a059a861/)')

        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')

        st.markdown("**Genival Junior**")
        st.markdown('[LinkedIn](https://www.linkedin.com/in/genival-neves-brasil-junior/)')

        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')

        st.markdown("**Fábio Souza**")
        st.markdown('[LinkedIn](https://www.linkedin.com/in/fabio-souza-a67321129/)')
