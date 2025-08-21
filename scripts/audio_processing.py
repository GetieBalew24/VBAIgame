import openai
import pyaudio

import os
from pathlib import Path
import websockets
import base64
import json
import numpy as np
import pygame
import io


def record_audio(chunk_size=1024, rate=44100):
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=rate,
        input=True,
        frames_per_buffer=chunk_size,
    )
    print("Recording...")
    frames = []
    try:
        while True:
            data = stream.read(chunk_size)
            frames.append(np.frombuffer(data, dtype=np.int16))
    except KeyboardInterrupt:
        print("Recording stopped.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    return np.concatenate(frames)


async def send_receive_audio(audio_data, api_key):
    uri = "wss://api.openai.com/v1/realtime"
    headers = {"Authorization": f"Bearer {api_key}"}
    async with websockets.connect(uri, extra_headers=headers) as websocket:
        await websocket.send(json.dumps({"type": "start", "content_type": "audio/raw"}))
        await websocket.send(audio_data.tobytes())
        await websocket.send(json.dumps({"type": "stop"}))
        async for message in websocket:
            response = json.loads(message)
            if "audio" in response:
                audio_content = base64.b64decode(response["audio"]["content"])
                return audio_content


def play_audio(file_path):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.quit()
    except Exception as e:
        print(f"An error occurred while playing audio: {e}")


def text_to_speech(text, filename="speech.mp3", voice="alloy"):
    try:
        response = openai.Audio.create(model="tts-1", input=text, voice=voice)
        speech_file_path = Path(filename)
        with open(speech_file_path, "wb") as audio_file:
            audio_file.write(response["audio"])
        print(f"Audio content written to file {filename}")
        return speech_file_path
    except Exception as e:
        print(f"An error occurred during text-to-speech conversion: {e}")
        return None
