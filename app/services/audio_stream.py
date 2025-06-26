import asyncio, websockets
from services.stt_service import transcribe_audio
from services.tts_service import synthesize_speech
from services.llm_service import chat_completion

async def handle_audio(websocket, path):
    context = []
    async for message in websocket:
        audio_chunk = extract_audio(message)
        user_text = transcribe_audio(audio_chunk)
        context.append({"role": "user", "content": user_text})
        reply = chat_completion(context)
        context.append({"role": "assistant", "content": reply})
        audio_reply = synthesize_speech(reply)
        await websocket.send(audio_reply)

start_server = websockets.serve(handle_audio, "0.0.0.0", 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
