from langchain_core.messages import HumanMessage,AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
import gradio as gr
load_dotenv()
llm=ChatGroq(
    model='openai/gpt-oss-20b'
)
system_prompt="""
You are a cat vet doctore the user ask question about cat you have to answer the question in a friendly and helpful way according to your experience your asnwer should be not more than 5 lines.
"""
prompt=ChatPromptTemplate.from_messages([
('system',system_prompt),
MessagesPlaceholder(variable_name='history'),
('user',"{user_input}")
])

history=[]

parser=StrOutputParser()

chain=prompt | llm | parser

# while True:
#     user_input=input("You: ")
#     if user_input.lower() in ['exit','quit','bye']:
#         print("Goodbye!")
#         break
#     result=chain.invoke({"user_input":user_input,'history':history})
#     print(f"Vet: {result}")
#     history.append(HumanMessage(content=user_input))
#     history.append(AIMessage(content=result))

page=gr.Blocks(
    title="Chat with Cat Vet",
    theme=gr.themes.Soft()
)
def chat(user_input,history):
    print(user_input,history)

    langchain_history=[]
    for item in history:
        if item['role']=='user':
            langchain_history.append(HumanMessage(content=item['content']))
        elif item['role']=='assistant':
            langchain_history.append(AIMessage(content=item['content']))
    response=chain.invoke({'user_input':user_input,'history':langchain_history})
    return "",history+[{'role':'user','content':user_input},{'role':'assistant','content':response}]
def clear_chat():
    return "",[]
with page:
    gr.Markdown(
        """
        # Chat with Cat Vet
        Get help and advice from our friendly cat vet
        """
    )

    chatbot=gr.Chatbot(type='messages',show_label=False,avatar_images=[None,'03_Langchain_AI_Assistant/vettt.jpg'])
    msg=gr.Textbox(show_label=False,placeholder="Type your message here...")
    clear=gr.Button("Clear Chat",variant='secondary')
    clear.click(clear_chat,outputs=[msg,chatbot])
    msg.submit(chat,[msg,chatbot],[msg,chatbot])

page.launch()