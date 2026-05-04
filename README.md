# 🤖 Chatbot Kauan

> Um assistente virtual inteligente e dinâmico, alimentado por IA com acesso em tempo real à internet e interface moderna.

![Capa do Projeto](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=googlebard&logoColor=white)

---

## 📖 Sobre o Projeto

O **Chatbot Kauan** é uma aplicação web desenvolvida em Python que utiliza o mais recente SDK oficial do Google (`google-genai`) para interagir com o modelo **Gemini 2.0 Flash**. O grande diferencial deste assistente é a sua conexão com a ferramenta nativa de pesquisa do Google (Search Grounding), permitindo que ele cruze dados, pesquise informações atuais e traga respostas precisas sobre eventos recentes que modelos tradicionais offline não conseguem responder.

Tudo isso envelopado em uma interface limpa construída com **Streamlit**, focada na melhor experiência de usuário (UX).

---

## ✨ Principais Funcionalidades

* 🌐 **Pesquisa Web em Tempo Real:** Conexão direta com o Google Search. O bot pesquisa eventos atuais, placares de jogos e notícias de hoje antes de responder.
* ⌨️ **Resposta em Streaming (Máquina de Escrever):** A interface exibe a resposta da IA de forma gradual, palavra por palavra, entregando uma experiência fluida idêntica à das plataformas oficiais.
* 🧠 **Memória de Contexto:** O chatbot lembra de toda a conversa graças ao gerenciamento de estado de sessão, permitindo diálogos complexos e contínuos.
* 🎨 **Interface Intuitiva e Avatares:** Layout clean com avatares personalizados para o usuário (`🧑‍💻`) e para a IA (`🤖`), além de indicadores visuais (Spinner) enquanto o bot "pensa".
* ⚙️ **Gerenciamento Rápido:** Menu lateral dedicado com botão de ação rápida para limpar o histórico da conversa e reiniciar o contexto.

---

## 💻 Tecnologias Utilizadas

O projeto adota as melhores práticas de desenvolvimento, focando em segurança, código limpo e bibliotecas modernas:

* **Python:** Linguagem base da aplicação.
* **Streamlit:** Framework para criação rápida da interface gráfica e gerenciamento do estado da aplicação (`st.session_state`).
* **Google GenAI SDK:** Nova biblioteca oficial do Google para comunicação via API com os modelos Gemini.
* **Python-dotenv:** Gerenciamento seguro de variáveis de ambiente para proteção da chave de API.

---

## 🚀 Como Executar o Projeto

1. Faça o clone deste repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/chatbot-kauan.git](https://github.com/SEU_USUARIO/chatbot-kauan.git)
   
2. Acesse a pasta do projeto:
   ```bash
   cd chatbot-kauan

3. Instale as dependências necessárias:
   ```bash
   pip install streamlit google-genai python-dotenv

4. Configure sua chave de API:
   Crie um arquivo chamado .env na raiz do projeto.
   Adicione a sua chave do Google AI Studio no seguinte formato:
   ```bash
   GEMINI_API_KEY=sua_chave_api_aqui

5. Inicie a aplicação:
   ```bash
   py -m streamlit run main.py

---

🛡️ Licença & Copyright
Copyright (c) 2026 Kauan Santana Almeida. Todos os direitos reservados.
      

   

   
