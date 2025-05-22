# -SPEECH-RECOGNITION-SYSTEM


*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: HASHMI SYED FAHAD

*INTERN ID*: CT08DL815

*DOMAIN*: ARTIFICIAL INTELLIGENCE

*DURATION*: 8 WEEEKS

*MENTOR*: NEELA SANTOSH



## Description :

## Project Overview :-


I’m a student diving deeper into natural language processing, and speech-to-text-transcriber is my latest project—a Python script that converts WAV audio files into text using Google Speech Recognition via the speech_recognition library. After tackling challenges with LSTM models that churned out gibberish like “musensiblet” and navigating memory limits on my laptop (~1025 MB), I wanted to explore speech processing as a new frontier. This script takes a WAV file, like a recorded lecture or podcast snippet, and transcribes it into readable text, handling errors gracefully. It’s another step in my journey to build portfolio-worthy tools for AI internship applications, showcasing my growth in coding and problem-solving.


## What It Does :-

This script transcribes WAV audio files into text using Google’s Speech Recognition API. It includes features to ensure reliability: it validates that the input is a WAV file, adjusts for ambient noise to improve accuracy, and catches errors like unintelligible audio or API failures. The script is lightweight, requiring minimal memory compared to my previous projects like BART summarization, and outputs the transcription to the console. It’s perfect for tasks like transcribing short audio clips, such as interviews or voice memos, making it a practical tool for students, researchers, or content creators.


## Lesson Learned :-

This project enabled me to explore NLP concepts that extend beyond text generation operations in both my GPT-2  script and summarization models like BART. My experience with speech-to-text technology introduced me to audio  processing which presented a new difficulty because LSTM models struggled with incorrect spellings and required extended training periods.  The implementation of speech_recognition brought me relief since I could obtain precise transcriptions through Google’s  API without needing to create models from the ground up. The audio-specific challenges which include noise reduction through  recognizer.adjust_for_ambient_noise() led to enhanced results in transcribing noisy recordings.

My memory management experience  in this project proved to be simpler than when I worked with BART or GPT-2.  The speech_recognition library showed excellent performance by functioning within my ~1025 MB memory boundary which  contrasts with the 1-2 GB requirements of Transformers models. The handling of WAV file sizes demanded  close attention since large files could create system strain which is why I limited my activities to short audio clips  such as converted_audio_16k.wav. The implementation of error handling systems brought a significant victory to  my work because the script now remained stable despite file absences and API problems while my LSTM scripts used  to fail because of missing files.

API dependencies became a fundamental learning point during this project. Whenever Google Speech Recognition operates it needs an  active internet connection, and I mastered the process of managing RequestError cases during network failures. When I  documented the script installation process alongside meaningful code explanations I expanded my understanding of usability principles to better prepare for  my upcoming internships. Through audio transcription I discovered the practical applications of NLP which enable the transformation of  lectures into notes and interviews into articles. My experience with audio transcription has inspired me to develop upcoming projects  that will provide additional audio format support while creating a graphical user interface for enhanced accessibility.


## Requirements:-

speechrecognition>=3.8.1




## Setup and Usage :-



Install Dependencies: Install the required library using requirements.txt:

```
pip install -r requirements.txt
```


Prepare Audio: Ensure your audio file is in WAV format, sampled at 16kHz (e.g., converted_audio_16k.wav). Use tools like Audacity to convert if needed.


Clone and Run:

```
git clone https://github.com/your-username/speech-to-text-transcriber.git
cd speech-to-text-transcriber
python transcribe_audio.py

```

  
Customize: Edit audio_file in transcribe_audio.py with your WAV file path, or import transcribe_audio:

```
from transcribe_audio import transcribe_audio
print(transcribe_audio("your_audio.wav"))

```

## Notes:-

-Audio Requirements: WAV files, 16kHz sample rate for best results.



-Internet: Requires connectivity for Google Speech Recognition API.



-Future Plans: Support more formats, add live microphone input.


## OUTPUT:-


