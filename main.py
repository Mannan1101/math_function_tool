from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled, function_tool
from openai import AsyncOpenAI
from decouple import config 
import asyncio

set_tracing_disabled(True)

gemini_api_key = config("GEMINI_API_KEY")
gemini_base_url = config("GEMINI_BASE_URL")
gemini_model_name = config("GEMINI_MODEL_NAME")

gemini_client = AsyncOpenAI(api_key=str(gemini_api_key), base_url=str(gemini_base_url))                        
gemini_model = OpenAIChatCompletionsModel(openai_client=gemini_client, model=str(gemini_model_name))

@function_tool

async def add (a: int , b: int) -> int:
       """Add two numbers"""
       return a + b


math_agent = Agent(
    name="gemini_agent",
    instructions="You are a helpful assistant that can perform math addition.",
    tools=[add],
    model=gemini_model
)

async def main():
 prompt = input("Enter your prompt: ")
 result = await Runner.run(math_agent, prompt)
 print(result.final_output)


if __name__ == "__main__":
 asyncio.run(main())