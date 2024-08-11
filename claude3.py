# -----------------------------------------------
# Setting up Amazon Bedrock with AWS SDK Boto3 🐍️
# -----------------------------------------------

import boto3, json
bedrock_runtime=boto3.client(service_name="bedrock-runtime",
                             aws_access_key_id="AKIAZAI4G2JAX2QLD3BG",
                             aws_secret_access_key="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",
                             region_name="us-east-1",
                             )
# Model configuration 
model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
model_kwargs =  {
    "max_tokens": 2048, "temperature": 0.1,
    "top_k": 250, "top_p": 1, "stop_sequences": ["\n\nHuman"],
}
# Input configuration

prompt = "Act as a Shakespeare and write a poem on Genertaive AI"
body = {
    "anthropic_version": "bedrock-2023-05-31",
    "system": "You are a honest and helpful bot.",
    "messages": [
        {"role": "user", "content": [{"type": "text", "text": prompt}]},
    ],
}
body.update(model_kwargs)
# Invoke
response = bedrock_runtime.invoke_model(
    modelId=model_id,
    body=json.dumps(body),
)
# Process and print the response
result = json.loads(response.get("body").read()).get("content", [])[0].get("text", "")
print(result)