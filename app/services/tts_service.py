
from elevenlabs import generate

def synthesize_speech(text):
    return generate(text=text, voice="Rachel", model="eleven_monolingual_v1")
