import os
from typing import Optional

# External Dependencies:
import boto3,json
from botocore.config import Config

bedrock_boto3 = boto3.client(service_name="bedrock-runtime",
                             aws_access_key_id="AKIAZAI4G2JAX2QLD3BG",
                             aws_secret_access_key="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",
                             region_name="us-east-1",
                             )

model_id ="amazon.titan-embed-text-v2:0"
accept = "application/json"
content_type = "application/json"
text="abc"
dimensions=256
normalize=True

body = json.dumps({
            "inputText": text,
            "dimensions": dimensions,
            "normalize": normalize
        })

response = bedrock_boto3.invoke_model(
    body=body, modelId=model_id, accept=accept, contentType=content_type
)

response_body = json.loads(response.get('body').read())

response_body['embedding']