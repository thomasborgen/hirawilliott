from typing import Annotated
from fastapi import APIRouter, Depends, Query, Request, Response
from fastapi.responses import HTMLResponse
from hypermedia import Element
from hypermedia.fastapi import full, htmx

from google.cloud.texttospeech import (
    SynthesisInput,
    TextToSpeechClient,
    VoiceSelectionParams,
    AudioConfig,
)

from hirawilliott.hiragana.views.game import render_game, render_game_partial
from hirawilliott.hiragana.views.index import (
    render_index,
    render_index_partial,
)
from hirawilliott.speak.dependencies import (
    speech_audio_config,
    speech_client,
    speech_japanese_voice,
)

router = APIRouter(
    prefix="/hiragana",
    dependencies=[],
)


@router.get("", response_class=HTMLResponse)
@htmx
async def hiragana_index(
    request: Request,
    partial: Element = Depends(render_index_partial),
    full: Element = Depends(full(render_index)),
) -> None:
    """Return the index page."""


@router.get("/game", response_class=HTMLResponse)
@htmx
async def game_index(
    request: Request,
    partial: Element = Depends(render_game_partial),
    full: Element = Depends(full(render_game)),
) -> None:
    """Return the index page."""


# あ、あ<break time="1000ms"/> テスト


@router.get("/speak")
async def read_japanese(
    text: Annotated[str, Query()],
    client: Annotated[TextToSpeechClient, Depends(speech_client)],
    voice: Annotated[VoiceSelectionParams, Depends(speech_japanese_voice)],
    audio_config: Annotated[AudioConfig, Depends(speech_audio_config)],
) -> None:
    synthesis_input = SynthesisInput(ssml=f"<speak>{text}</speak>")

    speech = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    return Response(content=speech.audio_content, media_type="audio/mpeg")
