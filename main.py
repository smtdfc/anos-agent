from ai import AnosAgent,get_llm_model
from getpass import getpass
from dotenv import load_dotenv
import os
import os

load_dotenv()

os.environ["GOOGLE_API_KEY"] = getpass("Your API key: ")

agent = AnosAgent(
  get_llm_model('google','gemini-2.5-flash')
)

while True:
  prompt = input('You: ')
  print('Agent: ',agent.prompt(prompt))