from typing import Annotated
from fastapi import APIRouter, Depends, Query, Response

from google.cloud.texttospeech import (
    SynthesisInput,
    TextToSpeechClient,
    VoiceSelectionParams,
    AudioConfig,
)

from hirawilliott.speak.dependencies import (
    speech_audio_config,
    speech_client,
    speech_japanese_voice,
)


router = APIRouter(
    prefix="/speak",
    tags=["speak"],
    dependencies=[],
)


"""
<speak>
  Step 1, take a deep breath. <break time="200ms"/>
  Step 2, exhale.
  Step 3, take a deep breath again. <break strength="weak"/>
  Step 4, exhale.
</speak>
"""


@router.get("")
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
