import getpass
import os

if not os.environ.get("GROQ_API_KEY"):
	os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")
from langchain.chat_models import init_chat_model

model = init_chat_model("llama3-8b-8192", model_provider="groq")

from langchain_core.messages import HumanMessage, SystemMessage
messages = [
	SystemMessage("Translate the following from English into Italian"),
	HumanMessage("hi!"),
]

model.invoke(messages)

model.invoke("Hello")
model.invoke([{"role": "user", "content": "Hello"}])
model.invoke([HumanMessage("Hello")])

from langchain_core.prompts import ChatPromptTemplate
system_template = "Translate the following from English into {language}"
prompt_template = ChatPromptTemplate.from_messages(
	[("system", system_template), ("user","{text}")]
)

prompt = prompt_template.invoke({"language":"Italian", "text":"hi!"})

prompt

prompt.to_messages()

response = model.invoke(prompt)
print(response.content)
