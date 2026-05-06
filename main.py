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
    # Exibe a mensagem do usuário na tela temporariamente (sem salvar ainda no histórico permanente)
    st.chat_message("user", avatar="🧑‍💻").write(texto_usuario)

    # Converte o histórico estável para o formato do novo SDK
    historico_gemini = []
    for m in st.session_state["lista_mensagens"]: 
        papel = "user" if m["role"] == "user" else "model"
        historico_gemini.append(
            types.Content(role=papel, parts=[types.Part.from_text(text=m["content"])])
        )

    try:
        # Inicia o chat com histórico garantidamente correto e alternado
        chat = client.chats.create(
            model="gemini-2.0-flash",
            config=configuracao,
            history=historico_gemini
        )
        
        # Exibe a interface do assistente
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("Pesquisando na web e pensando..."):
                resposta_stream = chat.send_message_stream(texto_usuario)
                
                def gerador_de_texto():
                    for pedaco in resposta_stream:
                        try:
                            if pedaco.text:
                                yield pedaco.text
                        except Exception:
                            # Captura bloqueios de segurança do Google no meio do caminho sem derrubar o app
                            yield "\n\n⚠️ *[Resposta interrompida devido às políticas de segurança de conteúdo do Google]*"
                            break
                
                texto_resposta = st.write_stream(gerador_de_texto())
                
        # SÓ SALVAMOS NO HISTÓRICO SE A REQUISIÇÃO TEVE SUCESSO COMPLETO
        st.session_state["lista_mensagens"].append({"role": "user", "content": texto_usuario})
        st.session_state["lista_mensagens"].append({"role": "assistant", "content": texto_resposta})
    
    except Exception as e:
        if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
            st.error("⏳ Opa! Muitas pessoas estão usando o chatbot agora e atingimos o limite gratuito do Google. Por favor, espere um momento e tente novamente!")
        else:
            st.error(f"Erro ao chamar o Gemini: {e}")