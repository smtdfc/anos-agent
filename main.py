from core import AnosAgent,get_llm_model


agent = AnosAgent(
  get_llm_model('google','gemini-2.5-flash')
)

while True:
  prompt = input('You: ')
  print('Agent: ',agent.prompt(prompt))