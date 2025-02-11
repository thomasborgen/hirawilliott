import random
from fastapi import Depends
from hypermedia import H2, Div, Element, Figure, Image, Title

from hirawilliott.components import base
from hirawilliott.hiragana.dependencies import get_characters


def _choice_renderer(character: str, correct: bool = False) -> Element:
    return Div(
        Div(
            H2(character, class_="card-title text-7xl m-auto"),
            class_="card-body",
        ),
        Figure(
            Image(
                src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp",
                alt="Shoes",
            ),
        ),
        class_="card bg-base-100 shadow-xl",
        hx_get="" if correct else None,
        hx_target="#main",
    )


def render_game_partial(
    characters: list[str] = Depends(get_characters),
) -> Element:
    """Render only game form."""
    a = characters.pop(random.randint(0, len(characters) - 1))
    b = characters.pop(random.randint(0, len(characters) - 1))
    c = characters.pop(random.randint(0, len(characters) - 1))
    d = characters.pop(random.randint(0, len(characters) - 1))

    target = random.randint(0, 3)

    return Div(
        Div(
            _choice_renderer(a, correct=target == 0),
            _choice_renderer(b, correct=target == 1),
            class_="flex flex-row gap-2 px-2",
        ),
        Div(
            _choice_renderer(c, correct=target == 2),
            _choice_renderer(d, correct=target == 3),
            class_="flex flex-row gap-2 px-2",
        ),
        class_="min-h-screen width-screen flex flex-col justify-center items-center gap-2",
    )


def render_game(
    partial: Element = Depends(render_game_partial),
) -> Element:
    """Render the full page, with game form."""
    return (
        base()
        .extend("head", Title("Hirawilliott - Hiragana Practice"))
        .extend("main", partial)
    )
