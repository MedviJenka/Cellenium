import os
from gtts import gTTS
from dataclasses import dataclass
from core.infrastructure.modules.executor import Executor


@dataclass
class VoiceGenerator(Executor):

    language: str = 'en'

    def generate_voice(self, text, filename='output.mp3'):
        tts = gTTS(text=text, lang=self.language, slow=False)
        tts.save(filename)
        os.system(f"start {filename}")

    def execute(self, text: str) -> None:
        start = "Hey Mia, Take a note."
        end = "Thank you Mia."
        self.generate_voice(f'{start}, {text}, {end}')


voice_generator = VoiceGenerator()
if __name__ == '__main__':
    voice_generator.execute(text='test 1')
