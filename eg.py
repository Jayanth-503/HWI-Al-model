import getpass
import os


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
