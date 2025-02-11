from fastapi import Depends
from hypermedia import H1, Button, Div, Element, Paragraph, Title

from hirawilliott.components import base


def render_index_partial() -> Element:
    """Render only index form."""
    return Div(
        Div(
            Div(
                H1("Hirawilliott", class_="text-5xl font-bold"),
                Paragraph("Hiragana practice for kids", class_="py-6"),
                Button(
                    "Practice!",
                    class_="btn btn-primary fluid",
                    hx_get="/hiragana",
                    hx_push_url="true",
                    hx_target="#main",
                ),
                class_="max-w-md",
            ),
            class_="hero-content text-center",
        ),
        class_="hero bg-base-200 min-h-screen",
    )


def render_index(
    partial: Element = Depends(render_index_partial),
) -> Element:
    """Render the full page, with index form."""
    return base().extend("head", Title("Hirawilliott")).extend("main", partial)
