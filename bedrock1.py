import os
from llama_index.embeddings.bedrock import BedrockEmbedding
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.bedrock import Bedrock
import json
import filetype
llm = Bedrock(
    model="meta.llama3-8b-instruct-v1:0",
    aws_access_key_id=os.getenv("AWS_ID"),
    aws_secret_access_key=os.getenv("AWS_KEY"),
    region_name="us-east-1"
)
embed_model = BedrockEmbedding(region_name="us-east-1",aws_access_key_id=os.getenv("AWS_ID"),
    aws_secret_access_key=os.getenv("AWS_KEY"))
# aws ec2 instance those were switcehd off
Settings.embed_model=embed_model
Settings.llm = llm

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

def is_pdf(path_to_file):
    return filetype.guess(path_to_file).mime == 'application/pdf'

def is_json(path_to_file):
    return filetype.guess(path_to_file).mime == 'application/json'

def is_mp3(path_to_file):
    return (filetype.guess(path_to_file).mime == 'audio/wav')

def is_csv(path_to_file):
    return (filetype.guess(path_to_file).mime == 'text/csv')

# we get input from user like pdf or audio or csv 
if is_mp3(path):
    #
    print("ge")
    
elif is_pdf(path):
    #
    documents = SimpleDirectoryReader(
    input_files=[".\\WM17S.pdf"]
    ).load_data()
    index = VectorStoreIndex.from_documents(documents)
    query = "Act as doctor and provide me the detailed health analysis in english"
    query_engine = index.as_query_engine(llm=llm)
    answer = query_engine.query(query)
elif is_csv(path):
    #
    print("po")
else:
    print("no valid input")
documents = SimpleDirectoryReader(
    input_files=[".\\WM17S.pdf"]
).load_data()
index = VectorStoreIndex.from_documents(documents)
query = "Act as doctor and provide me the detailed health analysis in english"
query_engine = index.as_query_engine(llm=llm)
answer = query_engine.query(query)
print(answer)

