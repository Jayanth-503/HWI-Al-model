connecting to vm(IP address and pem file will be shared separately)
1. Open GitBash or PowerShell
2. Enter the command - ssh -i <pem-file> ubuntu@<ip>

Model ids
model name - Llama 3 8B Instruct
model_id - meta.llama3-8b-instruct-v1:0

model name - Claude 3 Sonnet
model_id - anthropic.claude-3-sonnet-20240229-v1:0

model name - Titan Multimodal Embeddings G1
model_id - amazon.titan-embed-image-v1

model name - Titan Text Embeddings V2
model_id - amazon.titan-embed-text-v2:0

model name - SDXL 1.0
model_id - stability.stable-diffusion-x1-v1


code examples(use boto3)
https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-runtime.html
https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples

