# 🎼 Orchestra

Docs

Note: Orchestra is an alpha release, so expect sharp edges and bugs.

## 🧩 What is Orchestra?

Orchestra is a single, unified data platform that makes it easy to collect instrumentation and performance data from your LLMs, track and run models and experiments, and deploy your LLM models faster, with higher performance

We provide open-source infrastrure for LLM instrumentation and experimentation. Implement in two lines of code to add analytics and insights to help you improve the quality of your large language models (LLMs).

We also provide managed instances and a web dashboard for tracking and improving the performance of all your models and prompts, all in one place.

## Quick Install
pip install orchestra-ai

Check out the Getting Started guide to learn how to use Orchestra.

Call the Orchestra object with the LLM API call as the first argument and add any additional arguments to the LLM API call as the remaining arguments.

## Getting started
```python
import openai
import orchestra


orchestra.api_key = "sk-..."

# list prompts
prompts = orchestra.Prompts.list()

# print the first prompt
print(prompts.data[0].id)
print(prompts.data[0].template)
print(prompts.data[0].input_variables)

# Create a new prompt with one input variable
one_input_prompt = orchestra.Prompts.create(input_variables=["name"], template="Your name is {name}. Tell me a joke using {name}.")

# Preview prompt with variable name
one_input_prompt.format(name="Jason")
# -> "Your name is Jason. Tell me a joke using Jason."


orchestrate = orchestra.Orchestrate.from_prompt(one_input_prompt)

Wrap the OpenAI API call with the `orchestrate` object to track the prompt, generation, and associated metadata

output = orchestrate(
    openai.Completion.create,
    engine="text-davinci-003",
    max_tokens=1024,
    temperature=0.3,
    input={
        "name": "Jason"
    }
)
# -> "Why did Jason throw his clock out the window? Because he wanted to see time fly!"
```