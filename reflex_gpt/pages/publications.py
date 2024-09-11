import reflex as rx
from reflex_gpt import ui

def publications_page() -> rx.Component:
    return ui.base_layout(
        rx.vstack(
            rx.heading(
                "My publications",
                size="9",
                margin_bottom="200px",
                color="#1E90FF"
            ),
            rx.hstack(
                rx.box(
                    rx.link(
                        rx.image(
                            src="/image_1_xgb.jpg",
                            width="200px",
                            height="auto",
                            border_radius="25%",
                            object_fit="cover",
                        ),
                        href="https://medium.com/@dmitrii.perfilev2020/easy-to-use-xgboost-for-mushroom-classification-a-step-by-step-guide-1b14cbf879b2",
                        target="_blank",
                    ),
                    rx.text(
                        "XGBoost",
                        font_size="18px",
                        padding_top="10px",
                        text_align="center",
                    ),
                    align="center",
                    padding="10px",
                    border="2px solid #00BFFF",
                    border_radius="15px",
                    box_shadow="0 4px 8px rgba(0, 0, 0, 0.1)",
                ),
                rx.box(
                    rx.link(
                        rx.image(
                            src="/image_2_image_proc.jpg",
                            width="200px",
                            height="auto",
                            border_radius="25%",
                            object_fit="cover",
                        ),
                        href="https://medium.com/@dmitrii.perfilev2020/image-processing-7c7eee25f41d",
                        target="_blank",
                    ),
                    rx.text(
                        "Image Processing",
                        font_size="18px",
                        padding_top="10px",
                        text_align="center",
                    ),
                    align="center",
                    padding="10px",
                    border="2px solid #00BFFF",
                    border_radius="15px",
                    box_shadow="0 4px 8px rgba(0, 0, 0, 0.1)",
                ),
                spacing="40",
                justify="center",
            ),
            spacing="20",
            justify="center",
            min_height="85vh",
        ),
    )
