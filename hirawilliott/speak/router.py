from fastapi import APIRouter, Response

from google.cloud import texttospeech


router = APIRouter(
    prefix="/speak",
    tags=["speak"],
    dependencies=[],
)

# Instantiates a client
client = texttospeech.TextToSpeechClient()

japanese_voice = texttospeech.VoiceSelectionParams(
    language_code="ja-JP", ssml_gender=texttospeech.SsmlVoiceGender.MALE
)
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)


"""
<speak>
  Step 1, take a deep breath. <break time="200ms"/>
  Step 2, exhale.
  Step 3, take a deep breath again. <break strength="weak"/>
  Step 4, exhale.
</speak>
"""


@router.get("/{text}")
async def read_japanese(text: str):
    synthesis_input = texttospeech.SynthesisInput(
        ssml=f'<speak>あ、あ<break time="1000ms"/> テスト</speak>'
    )

    speech = client.synthesize_speech(
        input=synthesis_input, voice=japanese_voice, audio_config=audio_config
    )
    return Response(content=speech.audio_content, media_type="audio/mpeg")
