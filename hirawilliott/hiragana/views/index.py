from fastapi import Depends
from hypermedia import (
    Div,
    Element,
    Form,
    Input,
    Label,
    Span,
    Title,
)

from hirawilliott.components import base


def _row_renderer(characters: list[str]) -> Element:
    return Label(
        Input(
            type="checkbox",
            name="characters",
            value=",".join(characters),
            class_="checkbox checkbox-primary",
        ),
        Span(
            ", ".join(characters),
        ),
        # class_="label cursor-pointer",
        class_="card bg-base-100 w-100 mx-4 shadow-xl flex flex-row items-center justify-start gap-4 label cursor-pointer",
    )


def render_index_partial() -> Element:
    """Render only index form."""
    return Div(
        Form(
            _row_renderer(["あ", "い", "う", "え", "お"]),
            _row_renderer(["か", "き", "く", "け", "こ"]),
            _row_renderer(["さ", "し", "す", "せ", "そ"]),
            _row_renderer(["た", "ち", "つ", "て", "と"]),
            _row_renderer(["な", "に", "ぬ", "ね", "の"]),
            _row_renderer(["は", "ひ", "ふ", "へ", "ほ"]),
            _row_renderer(["ま", "み", "む", "め", "も"]),
            _row_renderer(["や", "ゆ", "よ"]),
            _row_renderer(["ら", "り", "る", "れ", "ろ"]),
            _row_renderer(["わ", "を", "ん"]),
            Input(
                type="submit",
                value="Start",
                class_="btn btn-primary w-100 absolute bottom-4 right-4 left-4",
            ),
            hx_get="/hiragana/game",
            hx_push_url="true",
            hx_target="#main",
            class_="width-screen flex flex-col gap-2 p-4",
        ),
        class_="min-h-screen width-screen",
    )


def render_index(
    partial: Element = Depends(render_index_partial),
) -> Element:
    """Render the full page, with index form."""
    return (
        base()
        .extend("head", Title("Hirawilliott - Hiragana Practice"))
        .extend("main", partial)
    )
