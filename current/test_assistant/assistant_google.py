from __future__ import division
from gtts import gTTS
import re
import sys
import os
import time
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from MicrophoneStream import MicrophoneStream
from speech_functions import process_speech
from speech_functions import remove_spaces

import subprocess

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms
CWD = os.getcwd()
# Google Speech recognition api key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getcwd() + "/googleAuth2.json"


simple_recipe = ['get a glass', 'fill it with water', 'enjoy']


def listen_print_loop(responses):
    num_chars_printed = 0
    for response in responses:
        if not response.results:
            continue
        result = response.results[0]
        if not result.alternatives:
            continue
        transcript = result.alternatives[0].transcript
        # process_speech(remove_spaces(transcript))
        if re.match(r'(\s)*(hello)\b', transcript, re.I):
            output_text = process_speech(transcript.split())   
            overwrite_chars = ' ' * (num_chars_printed - len(transcript))
            if not result.is_final:
                sys.stdout.write(transcript + overwrite_chars + '\r')
                sys.stdout.flush()
                num_chars_printed = len(transcript)
            else:
                print(transcript + overwrite_chars)
                if output_text == None:
                    output_text = simple_recipe.pop(0)
                speaker = gTTS(text=output_text, lang='en', slow=False)
                speaker.save(CWD + "/gtts_speech.mp3")
                os.system("mpg321 -q " + CWD + "/gtts_speech.mp3")
            

                if re.search(r'\b(exit|quit)\b', transcript, re.I):
                    print('Exiting..')
                    break
                # DO FINAL ACTION HERE
                
                # time.sleep(5)
                # END OF FINAL ACTION
                num_chars_printed = 0


def main():
    language_code = 'en-US'
    client = speech.SpeechClient()
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code)
    streaming_config = types.StreamingRecognitionConfig(
        config=config,
        interim_results=True)
    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (types.StreamingRecognizeRequest(audio_content=content)
                    for content in audio_generator)
        responses = client.streaming_recognize(streaming_config, requests)
        # Now, put the transcription responses to use.
        listen_print_loop(responses)


if __name__ == '__main__':
    main()
