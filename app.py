import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.github.ai/inference"
model = "deepseek/DeepSeek-V3-0324"
token = os.environ["GITHUB_TOKEN"]

messages = [
    SystemMessage("You are a helpful assistant. Keep your answers concise.")
]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

print("Chatbot started! Type 'exit', 'quit', or 'bye' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Goodbye!")
        break

    messages.append(UserMessage(user_input))

    response = client.complete(
        messages=messages,
        temperature=1.0,
        top_p=1.0,
        max_tokens=100,
        model="gpt-4o-mini"
    )

    assistant_response = response.choices[0].message.content
    print(f"Assistant: {assistant_response}")
    
    # Store history for multi-turn conversation
    # Note: The client.complete might return a message object that can be added directly or its content needs to be wrapped. 
    # Usually we add the response message to the list.
    messages.append(response.choices[0].message)


