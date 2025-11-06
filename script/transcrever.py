from openai import OpenAI
from pathlib import Path
import os

# Cria o cliente com sua API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Caminho do arquivo de áudio
audio_path = Path(r"F:\desenvolvimento\transcricao-audio\audio\audio1.mp3")

# Verifica se o arquivo existe
if not audio_path.exists():
    raise FileNotFoundError(f"Arquivo não encontrado: {audio_path}")

# Faz a transcrição com o novo método
with open(audio_path, "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="gpt-4o-mini-transcribe",
        file=audio_file
    )

print("\n🗣️ Transcrição literal:")
print(transcript.text)