import reflex as rx

from reflex_gpt import ui

def about_us_page() -> rx.Component:
    # About us Page
    return ui.base_layout(
        rx.vstack(
            rx.heading("Hello there!", size="9", align="center"),
            rx.text(
                "Hello, my name is 杜铭. I am pursuing my Master's in Computer Technology (2021.09-2025.01) at Lanzhou University of Technology.",
                size="4",
                weight="medium",
                align="center",
            ),
            rx.text(
                """
                I hold a Bachelor's degree in Mechanical Engineering from Moscow Polytechnic University (2011.09-2015.06), 
                and I have significant experience in both software development and mechanical design.
                """,
                size="3",
                weight="regular",
                align="center",
            ),
            rx.box(
                rx.heading("Technical Skills", size="5", align="left"),
                rx.text(
                    "- Programming: ASP.NET Core, JavaScript, Python, C++/C#, Java, SQL\n"
                    "- Frameworks: FastAPI, Django, Hibernate, Spring\n"
                    "- Machine Learning: TensorFlow, PyTorch, ResNet, NLP, Transformers, CUDA",
                    size="3",
                    weight="light",
                    align="left",
                    color_scheme="indigo"
                ),
                padding="16px"
            ),
            rx.box(
                rx.heading("Professional Experience", size="5", align="left"),
                rx.text(
                    "- 2023.2: Developed a chatbot for a Kazakhstani remittance company, handling client funds using Python, ChatGPT, SQL, FastAPI, and Django.\n"
                    "- 2022.09-present: Worked on various projects using ASP.NET Core, FastAPI, and Java.",
                    size="3",
                    weight="light",
                    align="left",
                    color_scheme="cyan"
                ),
                padding="16px"
            ),
            rx.box(
                rx.heading("Honors", size="5", align="left"),
                rx.text(
                    "- Chinese Language Learning Scholarship, Central South University (2017)\n"
                    "- Double Degree from Moscow Bauman Technical University (2021)\n"
                    "- Master's Degree Scholarship, Lanzhou University of Technology (2021)",
                    size="3",
                    weight="light",
                    align="left",
                    color_scheme="crimson"
                ),
                padding="16px"
            ),
            rx.box(
                rx.heading("Links", size="5", align="left"),
                rx.text(
                    "- GitHub: [Dmitrii173173](https://github.com/Dmitrii173173)\n"
                    "- LeetCode: [Dmitrii173173](https://leetcode.com/u/Dmitrii173173/)\n"
                    "- Kaggle: [Dmitriiming](https://www.kaggle.com/dmitriiming)\n"
                    "- Codewars: [Dmitrii173173](https://www.codewars.com/users/Dmitrii173173)",
                    size="3",
                    weight="light",
                    align="left",
                    color_scheme="orange"
                ),
                padding="16px"
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )
