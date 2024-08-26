import os
from huggingface_hub import InferenceClient

# Read the Hugging Face token from an environment variable
hf_token = os.getenv("HF_API_TOKEN")

# Initialize the InferenceClient with the token
client = InferenceClient(
    "microsoft/Phi-3-mini-4k-instruct",
    token=hf_token,
)

# Perform the chat completion
for message in client.chat_completion(
    messages=[{"role": "user", "content": "What are the key entities and entity types in this text:  The University of Minnesota Department of Computer Science is hosting a seminar on generative AI next Monday, August 26th at 2pm in room CS-547.?"}],
    max_tokens=500,
    stream=True,
):
    print(message.choices[0].delta.content, end="")
