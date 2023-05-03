import os, yaml
from langchain.llms.openai import OpenAI
from langchain.requests import RequestsWrapper

from langchain.agents.agent_toolkits.openapi.spec import reduce_openapi_spec
os.environ['OPENAI_API_KEY'] = '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'

from langchain.agents.agent_toolkits.openapi import planner

with open("openai_openapi.yaml", encoding='utf-8') as f:
    raw_openai_api_spec = yaml.load(f, Loader=yaml.Loader)
openai_api_spec = reduce_openapi_spec(raw_openai_api_spec)

with open("klarna_openapi.yaml", encoding='utf-8') as f:
    raw_klarna_api_spec = yaml.load(f, Loader=yaml.Loader)
klarna_api_spec = reduce_openapi_spec(raw_klarna_api_spec)

with open("spotify_openapi.yaml", encoding='utf-8') as f:
    raw_spotify_api_spec = yaml.load(f, Loader=yaml.Loader)
spotify_api_spec = reduce_openapi_spec(raw_spotify_api_spec)


headers = {
    "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
}

llm = OpenAI(model_name="text-davinci-003", temperature=0.0)

openai_requests_wrapper = RequestsWrapper(headers=headers)
openai_agent = planner.create_openapi_agent(openai_api_spec, openai_requests_wrapper, llm)
user_query = "generate a short piece of advice"
openai_agent.run(user_query)
