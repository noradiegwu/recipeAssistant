# Recipe Assistant

## TO-DO

1. Speech (commands and utterances): [Wesley]
	- continuously gather speech
		* there is a streaming limit so test for length of stream allowed, if needed switch to the async version of google speech
	- only output text heard from user (ignore tts output)
	- clean up functions to only output a string of text for what was recognized, once per cycle (command response cycle)
2. UI: [Nneoma]
	- get setup with tKinter, make basic application window.
		* ingredients list
		* recipe list
		* "text entry" - what was heard
		* results (text from tts and other output)
3. Data: [Sam]
	- yummly (python library)
	- bigoven api (meh...)
4. Context: [Sam]
	- convert recipes to some sort of finite state machine...
	- work on representation of world state...
5. QA:
	- basic navigation (next/last etc)
	- basic step info (how much, how to)
	- 2nd level/recursion ]-> how much of this, what about that

*wake words?*

## SETUP

### GENERAL:

+ [General python speech recognition](https://pypi.python.org/pypi/SpeechRecognition/)
	- pip install [pyaudio](https://people.csail.mit.edu/hubert/pyaudio/)
		* (and portaudio for mac)
		* [common error](https://l.facebook.com/l.php?u=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F5921947%2Fpyaudio-installation-error-command-gcc-failed-with-exit-status-1&h=ATMRQvGccZ6Za0AJJjBxUhYyV5Wa4T1baVKuBF2uidoBgARUENxhpP_wbn9DgwlnKLx9xBnT_2tp3DPL9ecQPMtHAGq4KsACp1UDCBsbXAtFHQTLzZKY31tF)
	- pip install pocketsphinx
	- pip install SpeechRecognition
+ [Google Cloud Services python env](https://cloud.google.com/python/setup)
	- download python2 and pip (python 3 isn't fully supported...)
		* the Google Cloud SDK requires Python 2.7.9 or later and does not currently work on Python 3.
		* Not needed unless you don't have python 2.
	- don't create a virtual environment (pyaudio doesn't work with it)
	- install the [google cloud sdk](https://cloud.google.com/sdk)
		* ./google-cloud-sdk/install.sh OR .\google-cloud-sdk\install.bat
		* ./google-cloud-sdk/bin/gcloud init
	- pip install google-cloud-speech
+ Text to Speech
	- pip install pyttsx3
		* https://pyttsx3.readthedocs.io/en/latest/
	- pip install gtts
		* brew install mpg321

[auth code console](https://console.cloud.google.com/apis/credentials?project=turnkey-lacing-201318)

### CURRENT:

+ folder of current work...

### ARCHIVE:

+ assistants: generic (unfinished) and google specific demos of a speech rec./tts system loop.
	- copy of googleAuth2.json here
	- ggts_speech.mp3 is a side effect of the speech generation
+ speechRecognition:
	- copy of googleAuth2.json here
	- live speech with pocketsphinx (awful)
	- speech recognition CMUsphinx (okay)
	- google_speech (great, $$$)
	- async (not yet working)
+ textToSpeech:
	- google text to speech and python text to speech testers
	- ggts_speech.mp3 is a side effect of the speech generation
