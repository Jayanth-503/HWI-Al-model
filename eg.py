import getpass
import os

# setx ANTHROPIC_API_KEY "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"



# os.environ["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"] = getpass.getpass()

# from langchain_anthropic import ChatAnthropic

# model = ChatAnthropic(model="anthropic.claude-3-sonnet-20240229-v1:0")
# print("working")

import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,
    system="You are a world-class poet. Respond only with short poems.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Why is the ocean salty?"
                }
            ]
        }
    ]
)
print(message.content)
