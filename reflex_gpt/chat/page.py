import reflex as rx
from reflex_gpt import ui
from .state import ChatMessage, ChatState
from .form import chat_form

# Стили для сообщений
message_style = dict(
    display="inline-block", 
    padding="1em",
    border_radius="8px", 
    max_width=["30em", "30em", "50em", "50em", "50em", "50em"]
)

# Функция для получения подробного промпта
def get_detailed_prompt():
    return """
    Hello, my name is 杜铭. I am pursuing my Master's in Computer Technology (2021.09-2025.01) at Lanzhou University of Technology. My professor is 张玺君. 

    I hold a Bachelor's degree in Mechanical Engineering from Moscow Polytechnic University (2011.09-2015.06), and I have significant experience in both software development and mechanical design.

    My technical skills include:
    - Programming: ASP.NET Core, JavaScript, Python, C++/C#, Java, SQL
    - Frameworks: FastAPI, Django, Hibernate, Spring
    - Machine Learning: TensorFlow, PyTorch, ResNet, NLP, Transformers, CUDA

    Professional Experience:
    - 2023.2: Developed a chatbot for a Kazakhstani remittance company, handling client funds using Python, ChatGPT, SQL, FastAPI, and Django.
    - 2022.09-present: Worked on various projects using ASP.NET Core, FastAPI, and Java.

    Honors:
    - Chinese Language Learning Scholarship, Central South University (2017)
    - Double Degree from Moscow Bauman Technical University (2021)
    - Master's Degree Scholarship, Lanzhou University of Technology (2021)

    Links:
    - GitHub: DmitryMing (github.com)
    - LeetCode: https://leetcode.com/u/Dmitrii173173/
    - Kaggle: https://www.kaggle.com/dmitriiming
    - Codewars: https://www.codewars.com/users/Dmitrii173173
    """

# Функция для получения краткого промпта с навыками
def get_skills_prompt():
    return "Hello, my name is 杜铭. I study at Lanzhou University of Technology. My professor is 张玺君. I have experience in ASP.NET Core, JavaScript, Python, C++/C+, Java, Linux, TensorFlow, PyTorch, ResNet, NLP, and related technologies."

# Компонент для отображения сообщения
def message_box(chat_message: ChatMessage) -> rx.Component:
    return rx.box(
        rx.box(
            rx.markdown(
                chat_message.message,
                background_color=rx.cond(chat_message.is_bot, rx.color("mauve", 4), rx.color('blue', 4)),
                color=rx.cond(chat_message.is_bot, rx.color("mauve", 12), rx.color('blue', 12)),
                **message_style,
            ),
            text_align=rx.cond(chat_message.is_bot, "left", "right"),
            margin_top="1em",
        ),
        width="100%",
    )

# Страница чата
def chat_page():
    return ui.base_layout(
         rx.vstack(
             rx.hstack(
                rx.heading("Hello, my name is 杜铭, I study at Lanzhou University of Technology (兰州理工大学).", size="8"),
                rx.cond(ChatState.not_found, rx.text("Not found"), rx.text("Found")),
                rx.button("+ New Chat", on_click=ChatState.create_new_and_redirect)
            ),
            rx.box(
                rx.foreach(ChatState.messages, message_box),
                width='100%'
            ),
            chat_form(),
            margin="3rem auto",
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.text(get_skills_prompt(), font_size="1.2em", margin_top="1em")
    )
