from dotenv import load_dotenv

load_dotenv()
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

def animal_answer(input_message):
    # 環境変数からAPI_KEYを取得
    llm = ChatOpenAI(
        model_name="gpt-4o-mini", 
        temperature=0
    )

    messages = [
        SystemMessage(content="あなたは優秀な動物の専門家です。"),
        HumanMessage(content=input_message),
    ]

    result = llm(messages)
    return result.content   

def plant_answer(input_message):
    # 環境変数からAPI_KEYを取得
    llm = ChatOpenAI(
        model_name="gpt-4o-mini", 
        temperature=0
    )

    messages = [
        SystemMessage(content="あなたは優秀な植物の専門家です。"),
        HumanMessage(content=input_message),
    ]

    result = llm(messages)
    return result.content

def expert_answer(input_message, expert_type):
    if expert_type == "動物の専門家":
        answer = animal_answer(input_message)
    elif expert_type == "植物の専門家":
        answer = plant_answer(input_message)
    else:
        return "専門家が見つかりません。"

    return f"{expert_type}の回答: {answer}"



st.write("##### 動作モード1: 動物の専門家")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで動物の専門家が答えてくれます。")
st.write("##### 動作モード2: 植物の専門家")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで植物の専門家が答えてくれます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["動物の専門家", "植物の専門家"]
)

st.divider()

if selected_item == "動物の専門家":
    input_message = st.text_input(label="動物に関する質問を入力してください。")

else:
    input_message = st.text_input(label="植物に関する質問を入力してください。")

if st.button("実行"):
    st.divider()

    if selected_item == "動物の専門家":
        if input_message:
            st.write(expert_answer(input_message, selected_item))

        else:
            st.error("質問を入力してから「実行」ボタンを押してください。")

    else:
        if input_message:
            st.write(expert_answer(input_message, selected_item))

        else:
            st.error("質問を入力してから「実行」ボタンを押してください。")

