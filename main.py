import streamlit as st
import os
from dotenv import load_dotenv
from datetime import datetime

st.set_page_config(
    page_title="Chatbot Kauan", 
    page_icon="🤖", 
    layout="centered"
)

# Importações do NOVO SDK do Google
from google import genai
from google.genai import types

# Carrega as variáveis do arquivo .env (Segurança)
load_dotenv()
chave_api = os.getenv("GEMINI_API_KEY")

# Inicializa o NOVO cliente do Gemini
client = genai.Client(api_key=chave_api)

data_atual = datetime.now().strftime("%d/%m/%Y")
instrucao = f"Você é um assistente virtual útil e direto. A data de hoje é {data_atual}. Responda sempre considerando o ano atual correto."

# Configura as regras da IA 
configuracao = types.GenerateContentConfig(
    system_instruction=instrucao,
    tools=[{"google_search": {}}]
)

# Menu Lateral 
with st.sidebar:
    st.title("⚙️ Configurações")
    st.markdown("Bem-vindo ao Chatbot de Kauan com IA integrada à web!")
    
    if st.button("🗑️ Limpar Histórico de Conversa"):
        st.session_state["lista_mensagens"] = []
        st.rerun()

# Título principal da interface
st.write("# Chatbot Kauan") 

if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

texto_usuario = st.chat_input("Digite sua mensagem")

# Exibe o histórico na tela com Avatares
for mensagem in st.session_state["lista_mensagens"]:
    icone = "🧑‍💻" if mensagem["role"] == "user" else "🤖"
    with st.chat_message(mensagem["role"], avatar=icone):
        st.write(mensagem["content"])

# Lógica de envio de novas mensagens
if texto_usuario: 
    # Exibe a mensagem do usuário
    st.chat_message("user", avatar="🧑‍💻").write(texto_usuario)
    st.session_state["lista_mensagens"].append({"role": "user", "content": texto_usuario})

    # Converte o histórico para o formato do novo SDK
    historico_gemini = []
    for m in st.session_state["lista_mensagens"][:-1]: 
        papel = "user" if m["role"] == "user" else "model"
        historico_gemini.append(
            types.Content(role=papel, parts=[types.Part.from_text(text=m["content"])])
        )

    try:
        # Inicia o chat
        chat = client.chats.create(
            model="gemini-2.5-flash",
            config=configuracao,
            history=historico_gemini
        )
        
        # Exibe a interface do assistente
        with st.chat_message("assistant", avatar="🤖"):
            
            with st.spinner("Pesquisando na web e pensando..."):
                
                resposta_stream = chat.send_message_stream(texto_usuario)
                
                def gerador_de_texto():
                    for pedaco in resposta_stream:
                        if pedaco.text:
                            yield pedaco.text
                
                texto_resposta = st.write_stream(gerador_de_texto())
                
        st.session_state["lista_mensagens"].append({"role": "assistant", "content": texto_resposta})
    
    except Exception as e:
        st.error(f"Erro ao chamar o Gemini: {e}")