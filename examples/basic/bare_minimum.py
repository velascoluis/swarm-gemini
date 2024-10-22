from swarm import Swarm, Agent

client = Swarm(
    llm_provider="vertexai",
    project_id="YOUR_PROJECT_ID",
    location="YOUR_LOCATION",
)

agent = Agent(
    name="Agent",
    instructions="You are a helpful agent.",
)

messages = [{"role": "user", "content": "Hi!"}]
response = client.run(agent=agent, messages=messages)

print(response.messages[-1]["content"])
