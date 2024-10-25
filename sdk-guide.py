from composio_openai import ComposioToolSet, App, Action
from openai import OpenAI

openai_client = OpenAI()
composio_toolset = ComposioToolSet(entity_id="ram")

tools = composio_toolset.get_tools(actions=[Action.GITHUB_STAR_A_REPOSITORY_FOR_THE_AUTHENTICATED_USER])

task = "Star a repo composiohq/composio on GitHub"

response = openai_client.chat.completions.create(
    model="gpt-4-turbo-preview",
    tools=tools,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": task},
    ],
)

result = composio_toolset.handle_tool_calls(response)
print(result)
