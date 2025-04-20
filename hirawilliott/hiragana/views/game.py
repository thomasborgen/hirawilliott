import random
from typing import Annotated
from fastapi import Depends
from hypermedia import B, H2, Audio, Div, Element, Figure, Image, Title
import urllib

from hirawilliott.components import base
from hirawilliott.hiragana.dependencies import get_characters

from hirawilliott.hiragana.database import db, Hiragana


def _choice_renderer(hiragana: Hiragana, correct: bool = False) -> Element:
    audio = None

    if not correct:
        audio = Audio(
            src=f'/speak?text={hiragana.character}<break strength="strong"/>{hiragana.word}',
            class_="hidden",
            id=f"audio_{hiragana.romaji}",
        )

    return Div(
        Div(
            H2(hiragana.character, class_="card-title text-7xl mx-auto"),
            class_="card-body",
        ),
        Figure(
            Image(
                src=f"/hiragana/static/hiragana/{hiragana.image}",
                alt="Shoes",
            ),
            class_="opacity-0",
            _="on load wait for 4s then transition opacity to 1",
        ),
        audio and audio or "",
        id=hiragana.romaji,
        class_="card bg-base-100 shadow-xl w-1/3 flex-1",
        _=correct is False and 'on click transition my background-color to "red"',
        hx_get="" if correct else None,
        hx_target="#main",
    )


def render_game_partial(
    characters: Annotated[list[str], Depends(get_characters)],
) -> Element:
    """Render only game form."""

    a = characters.pop(random.randint(0, len(characters) - 1))
    a_hiragana = db.get(a)[0]
    b = characters.pop(random.randint(0, len(characters) - 1))
    b_hiragana = db.get(b)[0]
    c = characters.pop(random.randint(0, len(characters) - 1))
    c_hiragana = db.get(c)[0]
    d = characters.pop(random.randint(0, len(characters) - 1))
    d_hiragana = db.get(d)[0]

    target = random.randint(0, 3)

    target_hiragana = [a_hiragana, b_hiragana, c_hiragana, d_hiragana][target]

    speech = f'{target_hiragana.character}<break strength="strong"/>. {target_hiragana.character}<break time="1000ms"/>{target_hiragana.word}'

    return Div(
        Div(
            _choice_renderer(a_hiragana, correct=target == 0),
            _choice_renderer(b_hiragana, correct=target == 1),
            class_="flex flex-row gap-2 px-2 justify-center",
        ),
        Div(
            _choice_renderer(c_hiragana, correct=target == 2),
            _choice_renderer(d_hiragana, correct=target == 3),
            class_="flex flex-row gap-2 px-2 justify-center",
        ),
        Audio(
            src=f"/speak?text={speech}",
            class_="hidden",
            autoplay="true",
        ),
        class_="h-screen width-screen flex flex-col justify-center items-center gap-2",
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
