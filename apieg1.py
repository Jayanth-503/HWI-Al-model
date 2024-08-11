from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# from llama_cpp import Llama
from llama_index.embeddings.bedrock import BedrockEmbedding
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.bedrock import Bedrock
import json
import filetype

llm = Bedrock(
    model="meta.llama3-8b-instruct-v1:0",
    aws_access_key_id="AKIAZAI4G2JAX2QLD3BG",
    aws_secret_access_key="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",
    region_name="us-east-1"
)
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# llm = Llama(model_path="./models/7B/ggml-model-Q4_0.bin")

class InferenceRequest(BaseModel):
    prompt: str

@app.post("/complete")
def perform_inference(request: InferenceRequest):
    output = llm(
        request.prompt,
        max_tokens=48,
        stop=["Q:", "\n"],
        echo=True,
    )
    return {"data": output}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)