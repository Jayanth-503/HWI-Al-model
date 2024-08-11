# Use the native inference API to send a text message to Meta Llama 3.

import boto3
import json

from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client("bedrock-runtime",
                             aws_access_key_id="AKIAZAI4G2JAX2QLD3BG",
                             aws_secret_access_key="vD2RKz4T82zUGwuGaryJSgMLTv8jnl4Qj0dvqgpr",
                             region_name="us-east-1",
                             )
# Set the model ID, e.g., Llama 3 8b Instruct.
model_id = "amazon.titan-embed-text-v2:0"
# model_id = "meta.llama3-8b-instruct-v1:0"

# Define the prompt for the model.
prompt = "Act as a Shakespeare and write a poem on Genertaive AI"

# Embed the prompt in Llama 3's instruction format.
formatted_prompt = f"""
<|begin_of_text|>
<|start_header_id|>user<|end_header_id|>
{prompt}
<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>
"""

# Format the request payload using the model's native structure.
native_request = {
    "prompt": formatted_prompt,
    "max_gen_len": 512,
    "temperature": 0.5,
}

# Convert the native request to JSON.
request = json.dumps(native_request)

try:
    # Invoke the model with the request.
    response = client.invoke_model(modelId=model_id, body=request)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)

# Decode the response body.
model_response = json.loads(response["body"].read())

# Extract and print the response text.
response_text = model_response["generation"]
print(response_text)


