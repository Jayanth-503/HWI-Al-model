import filetype

def is_pdf(path_to_file):
    return filetype.guess(path_to_file).mime == 'application/pdf'

def is_json(path_to_file):
    return filetype.guess(path_to_file).mime == 'application/json'

def is_mp3(path_to_file):
    return (filetype.guess(path_to_file).mime == 'audio/mpeg')

def is_csv(path_to_file):
    return (filetype.guess(path_to_file).mime == 'text/csv')

print(is_pdf(".//file_example_MP3_1MG.mp3"))
print(is_mp3(".//file_example_MP3_1MG.mp3"))

# from google.cloud import speech_v1p1beta1 as speech
# import io

# def transcribe_audio_with_google(audio_file_path):
#     client = speech.SpeechClient()

#     with io.open(audio_file_path, "rb") as audio_file:
#         content = audio_file.read()

#     audio = speech.RecognitionAudio(content=content)
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=16000,
#         language_code="en-US",
#     )

#     response = client.recognize(config=config, audio=audio)
#     return " ".join([result.alternatives[0].transcript for result in response.results])




from llama_index.core import VectorStoreIndex
# from llama_hub.assemblyai.base import AssemblyAIAudioTranscriptReader

# reader = AssemblyAIAudioTranscriptReader(file_path=audio_file)

# Example usage
audio_file_path = "Recording112.wav"
import speech_recognition as sr

def transcribe_audio_speech_recognition(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

# Example usage
reader = transcribe_audio_speech_recognition(audio_file_path)


# reader = transcribe_audio_with_google(audio_file)
docs = reader.load_data()

# docs[0].metadata = {}

index = VectorStoreIndex.from_documents(docs)
query_engine = index.as_query_engine()
response = query_engine.query("What is a runner's knee?")
