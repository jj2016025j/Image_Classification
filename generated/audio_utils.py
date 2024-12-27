import os
from pydub.generators import Sine
from file_utils import generate_random_string, create_directory

def generate_audio(folder, duration=1000, frequency=440):
    """Generate an audio file with a sine wave."""
    create_directory(folder)
    filename = os.path.join(folder, generate_random_string() + '.wav')
    tone = Sine(frequency).to_audio_segment(duration=duration)
    tone.export(filename, format='wav')
    print(f"Generated audio: {filename}")
