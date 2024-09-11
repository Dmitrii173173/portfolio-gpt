# import time
import reflex as rx
import sqlmodel

from typing import List, Optional
from reflex_gpt.models import ChatSession, ChatSessionMessageModel

from . import ai

class ChatMessage(rx.Base):
    message: str
    is_bot: bool = False


class ChatState(rx.State):
    chat_session: ChatSession = None
    not_found: Optional[bool] = None
    did_submit: bool = False
    messages: List[ChatMessage] = []

    @rx.var
    def user_did_submit(self) -> bool:
        return self.did_submit
    
    def get_session_id(self) -> int:
        try:
            my_session_id = int(self.router.page.params.get('session_id'))
        except:
            my_session_id = None
        return my_session_id
    
    def create_new_chat_session(self):
        with rx.session() as db_session:
            obj = ChatSession()
            db_session.add(obj) # prepare to save
            db_session.commit() # actually save
            db_session.refresh(obj)
            self.chat_session = obj
            return obj

    def clear_ui(self):
        self.chat_session = None
        self.not_found = None
        self.did_submit = False
        self.messages = []

    def create_new_and_redirect(self):
        self.clear_ui()
        new_chat_session = self.create_new_chat_session()
        return rx.redirect(f"/chat/{new_chat_session.id}")

    def clear_and_start_new(self):
        self.clear_ui()
        self.create_new_chat_session()
        yield

    def get_session_from_db(self, session_id=None):
        if session_id is None:
            session_id = self.get_session_id()
        # ChatSession.id == session_id
        with rx.session() as db_session:
            sql_statement = sqlmodel.select(
                ChatSession
            ).where(
                ChatSession.id == session_id
            )
            result = db_session.exec(sql_statement).one_or_none()
            if result is None:
                self.not_found = True
            else:
                self.not_found = False
            self.chat_session = result
            messages = result.messages
            for msg_obj in messages:
                msg_txt = msg_obj.content
                is_bot = False if msg_obj.role == "user" else True
                self.append_message_to_ui(msg_txt, is_bot=is_bot)
            
    
    def on_detail_load(self):
        session_id = self.get_session_id()
        reload_detail = False
        if not self.chat_session:
            reload_detail = True
        else:
            """has a session"""
            if self.chat_session.id != session_id:
                reload_detail = True

        if reload_detail:
            self.clear_ui()
            if isinstance(session_id, int):
                self.get_session_from_db(session_id=session_id)

    def on_load(self):
        print("running on load")
        self.clear_ui()
        self.create_new_chat_session()

    def insert_message_to_db(self, content, role='unknown'):
        print("insert message data to db")
        if self.chat_session is None:
            return
        if not isinstance(self.chat_session, ChatSession):
            return 
        with rx.session() as db_session:
            data = {
                "session_id": self.chat_session.id,
                "content": content,
                "role": role
            }
            obj = ChatSessionMessageModel(**data)
            db_session.add(obj) # prepare to save
            db_session.commit() # actually save

    def append_message_to_ui(self, message, is_bot:bool=False):
        self.messages.append(
            ChatMessage(
                message=message,
                is_bot = is_bot
            )
        )
        
    def get_gpt_messages(self):
        gpt_messages = [
            {
                "role": "system",
                "content": (
                    "Hello, my name is 杜铭. I am pursuing my Master's in Computer Technology (2021.09-2025.01) "
                    "at Lanzhou University of Technology. My professor is 张玺君.\n\n"
                    "I hold a Bachelor's degree in Mechanical Engineering from Moscow Polytechnic University (2011.09-2015.06), "
                    "and I have significant experience in both software development and mechanical design.\n\n"
                    "My technical skills include:\n"
                    "- Programming: ASP.NET Core, JavaScript, Python, C++/C#, Java, SQL\n"
                    "- Frameworks: FastAPI, Django, Hibernate, Spring\n"
                    "- Machine Learning: TensorFlow, PyTorch, ResNet, NLP, Transformers, CUDA\n\n"
                    "Professional Experience:\n"
                    "- 2023.2: Developed a chatbot for a Kazakhstani remittance company, handling client funds using Python, ChatGPT, SQL, FastAPI, and Django.\n"
                    "- 2022.09-present: Worked on various projects using ASP.NET Core, FastAPI, and Java.\n\n"
                    "Honors:\n"
                    "- Chinese Language Learning Scholarship, Central South University (2017)\n"
                    "- Double Degree from Moscow Bauman Technical University (2021)\n"
                    "- Master's Degree Scholarship, Lanzhou University of Technology (2021)\n\n"
                    "Links:\n"
                    "- GitHub: DmitryMing (github.com)\n"
                    "- LeetCode: https://leetcode.com/u/Dmitrii173173/\n"
                    "- Kaggle: https://www.kaggle.com/dmitriiming\n"
                    "- Codewars: https://www.codewars.com/users/Dmitrii173173\n\n"
                    "You are an AI assistant that helps with academic questions and general inquiries. Respond professionally and in markdown format."
                )
            }
        ]
        for chat_message in self.messages:
            role = 'user'
            if chat_message.is_bot:
                role = 'system'
            gpt_messages.append({
                "role": role,
                "content": chat_message.message
            })
        return gpt_messages

    async def handle_submit(self, form_data:dict):
        print('here is our form data', form_data)
        user_message = form_data.get('message')
        if user_message:
            self.did_submit = True
            self.append_message_to_ui(user_message, is_bot=False)
            self.insert_message_to_db(user_message, role='user')
            yield
            gpt_messages = self.get_gpt_messages()
            bot_response = ai.get_llm_response(gpt_messages)
            self.did_submit = False
            self.append_message_to_ui(bot_response, is_bot=True)
            self.insert_message_to_db(bot_response, role='system')
            yield
