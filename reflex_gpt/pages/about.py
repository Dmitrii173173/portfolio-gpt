import reflex as rx

from reflex_gpt import ui

def about_us_page() -> rx.Component:
    # About us Page
    return ui.base_layout(
        rx.vstack(
            rx.heading("Welcome to Reflex About!", size="9"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
        rx.text(
            """
            Hello, my name is 杜铭. I am pursuing my Master's in Computer Technology (2021.09-2025.01) 
            at Lanzhou University of Technology.

            I hold a Bachelor's degree in Mechanical Engineering from Moscow Polytechnic University (2011.09-2015.06),
            and I have significant experience in both software development and mechanical design.

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
            - GitHub: https://github.com/Dmitrii173173
            - LeetCode: https://leetcode.com/u/Dmitrii173173/
            - Kaggle: https://www.kaggle.com/dmitriiming
            - Codewars: https://www.codewars.com/users/Dmitrii173173
            """
        )
    )
