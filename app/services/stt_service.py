from deepgram import Deepgram

def transcribe_audio(audio_bytes):
    # Assume conversion to linear PCM already done
    dg = Deepgram("DEEPGRAM_API_KEY")
    response = dg.transcription.prerecorded({'buffer': audio_bytes, 'mimetype': 'audio/wav'})
    return response['results']['channels'][0]['alternatives'][0]['transcript']
    
