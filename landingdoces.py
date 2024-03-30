import streamlit as st
from streamlit_ace import st_ace

# Configuração da página
st.set_page_config(
    page_title="Neusa Doces Caseiros",
    page_icon="logococada.ico",
    layout="wide",  # Definindo o layout para "wide" para ter espaço para o sidebar
    initial_sidebar_state="expanded"  # Expandindo o sidebar por padrão
)

# Logo da página
st.sidebar.image("logococada1.png", use_column_width=True)

# Sidebar com a opção de escolher entre as fotos
st.sidebar.title("Imagens dos nossos produtos:")
album = st.sidebar.radio('', ['Cocadas', 'Cocada de Maracujá', 'Cocada Queimada', 'Paçocas Caseiras'])

# Galeria de imagens
images = {
    'Cocadas': 'cocadas_2.jpg',
    'Cocada de Maracujá': 'cocada_maracujá.jpg',
    'Cocada Queimada': 'cocada_queimada.jpg',
    'Paçocas Caseiras': 'pacocas2.jpg'
}

# Verificando se a chave selecionada existe no dicionário de imagens
if album in images:
    st.image(images[album],  width=400, caption=album)
             

# Conteúdo principal no centro da página
st.title('Bem-vindo à nossa Landing Page')
st.write('As melhores Cocadas da cidade! Feitas com amor e ingredientes naturais.')

# Descrição do produto
st.write("""
#### Por que escolher nossas Cocadas?

- Feitas artesanalmente com ingredientes naturais.
- Variedade de sabores para todos os gostos.
- Entrega rápida e segura em todo Brasil.
""")

# Formulário de contato
st.subheader('Entre em contato conosco!')
name = st.text_input('Seu Nome:', max_chars=50)
email = st.text_input('E-mail:', max_chars=50)
phone = st.text_input('Telefone:', max_chars=15)
assunto = st.text_input('Deixe sua mensagem:', max_chars=1000)

if st.button('Enviar'):
    # Aqui você pode adicionar a lógica para processar o pedido, enviar um e-mail de confirmação, etc.
    st.success('Mensagem enviada com sucesso! Entraremos em contato em breve.')

# Ícones de redes sociais
st.subheader('Siga-nos nas redes sociais:')
st.markdown("""
[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white)](https://www.facebook.com/neusadocescaseiros)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://www.instagram.com/neusadocescaseiros)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-%2325D366.svg?style=for-the-badge&logo=WhatsApp&logoColor=white)](https://api.whatsapp.com/send?phone=5519996316194)
""")

# Rodapé
st.markdown("""
Feito com ❤️ por Mariana Bordignon. [Contate-nos](mailto:tiahmah@hotmail.com)
""")

st.markdown("""
<div style="text-align:center;">
Todos os direitos reservados à Neusa Doces Caseiros ®
</div>
""", unsafe_allow_html=True)

