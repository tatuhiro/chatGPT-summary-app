# -*- coding: utf-8 -*-
import streamlit as st
from langchain.chat_models import ChatOpenAI

# APIキーとカスタムエンドポイント
api_key = st.secrets["OPENAI_API_KEY"]
api_base = "https://api.openai.iniad.org/api/v1/"

# LangChainのChatOpenAIモデルを初期化
chat = ChatOpenAI(
    model_name="gpt-4o-mini",  # モデル名はINIAD側に合わせて
    temperature=0,
    openai_api_key=api_key,
    openai_api_base=api_base
)

st.title("INIAD ChatGPT 要約アプリ")

text = st.text_area("要約したい文章を入力してください")

if st.button("要約する"):
    if text:
        messages = [
            {"role": "system", "content": "以下の文章を日本語で簡潔に要約してください。"},
            {"role": "user", "content": text}
        ]
        result = chat.invoke(messages)
        st.write(result.content)
