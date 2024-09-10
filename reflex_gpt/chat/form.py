import reflex as rx
from .state import ChatState

def chat_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.text_area(
                name='message',
                placeholder='Your message',
                required=True,
                width='100%',
                on_key_down=ChatState.handle_key_down,
            ),
            rx.hstack(
                rx.button('Submit', type='submit'),
                rx.cond(
                    ChatState.user_did_submit,
                    rx.text("Submitted"),
                    rx.fragment(),
                )
            )
        ),
        on_submit=ChatState.handle_submit,
        reset_on_submit=True
    )


class ChatState:
    user_did_submit = False

    @staticmethod
    def handle_submit(values):
        ChatState.user_did_submit = True

    @staticmethod
    def handle_key_down(event):
        if event.key_code == 13:
            ChatState.handle_submit(event.target.form.values)
