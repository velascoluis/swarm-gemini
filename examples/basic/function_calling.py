from swarm import Swarm, Agent

client = Swarm(
    llm_provider="vertexai",
    project_id="YOUR_PROJECT_ID",
    location="YOUR_LOCATION",
)


def get_weather(location) -> str:
    return "{'temp':67, 'unit':'F'}"


agent = Agent(
    name="Agent",
    instructions="You are a helpful agent.",
    functions=[get_weather],
)

messages = [{"role": "user", "content": "What's the weather in NYC?"}]

response = client.run(agent=agent, messages=messages)
print(response.messages[-1]["content"])
