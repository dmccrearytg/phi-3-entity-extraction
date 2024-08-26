from huggingface_hub import InferenceClient

client = InferenceClient(
    "microsoft/Phi-3-mini-4k-instruct",
    token="hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
)

for message in client.chat_completion(
	messages=[{"role": "user", "content": "What is the capital of France?"}],
	max_tokens=500,
	stream=True,
):
    print(message.choices[0].delta.content, end="")
