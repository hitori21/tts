import requests
import base64
import os
from mtranslate import translate
from typing import Optional
import typer

app = typer.Typer()

class TTS:
    def __init__(self, text, voice="herta"):
        self.text = text
        self.language = 'ja'  
        self.audio_file = 'audio.wav'  
        self.voice = voice
        
    def translate(self, lang):
        self.language = lang
        self.text = translate(self.text, lang)

    def toAudio(self):
        if self.voice in "herta":
            char = "herta"
        elif self.voice in "shiroko":
            char = "sunaookami-shiroko"
        elif self.voice in "alice":
            char = "tendou-alice"
        elif self.voice in "yuuka":
            char = "hayase-yuuka"
        else:
            char = "herta"
        payload = {
            'data': [
                self.text,
                'Japanese',
                0.6,
                0.668,
                1,
                False
            ]
        }
        response = requests.post(f"https://arzxh-vits-models.hf.space/run/tts-{char}", json=payload)
        
        if response.status_code == 200:
            audio_base64 = response.json()['data'][1]
            self.save_audio(audio_base64.replace("data:audio/wav;base64,", ""))

    def save(self, file_name):
        self.audio_file = f'{file_name}.wav'
        self.toAudio()

    def save_audio(self, audio_base64):
        audio_data = base64.b64decode(audio_base64)
        with open(self.audio_file, 'wb') as file:
            file.write(audio_data)

    def play(self):
        os.system(f"vlc --intf dummy {self.audio_file} --play-and-exit")

@app.command()
def tts_cli(
    text: str = typer.Option(..., "--text", "-t", help="Teks yang akan dijadikan TTS"),
    voice: str = typer.Option("alice", "--voice", "-va", help="Suara karakter untuk TTS."),
    save: Optional[str] = typer.Option(None, "--save", "-s", help="Simpan file audio dengan nama"),
    lang: Optional[str] = typer.Option("ja", "--lang", "-l", help="Kode bahasa untuk menerjemahkan teks")
):
    tts = TTS(text, voice=voice)
    tts.translate(lang)
    tts.toAudio()
    
    if save:
        tts.save(save)
    else:
        tts.save("audio")
    
    tts.play()

if __name__ == "__main__":
    app()
