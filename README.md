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

# Create a new prompt and add to your account's prompts, with one input variable
new_prompt = orchestra.Prompts.create(input_variables=["name"], template="Your name is {name}. Tell me a joke using {name}.")

# Preview prompt with variable name
new_prompt.format(name="Jason")
# -> "Your name is Jason. Tell me a joke using Jason."

# Edit an existing prompt
updated_prompt = orchestra.Prompts.update(new_prompt.id, input_variables=["name", "age"], template="Your name is {name}. You are {age} years old, Tell me a joke using {name}, that a {age} year old would find funny.")

# Create a tracking event named "Joke generated." on your account. Wraps the OpenAI API call 
# and tracks every instance this prompt is triggered, along with the corresponding output, and associated metadata

orchestration = orchestra.Ochestration.create("Joke generated.", 
    action=openai.Completion.create,
    prompt=updated_prompt, 
    engine="text-davinci-003",
    max_tokens=1024,
    temperature=0.3
)

# Run this Orchestration with the input variables
output = orchestration.play(
    input={
        "name": "Jason",
        "age": 24
    }
)

# output.choices[0].text
# -> "Why did Jason throw his clock out the window? Because he wanted to see time fly!"

# score generated output completion (-1.0 to -1.0)
orchestra.Reward.score_output(output.id, -1)

# Update the prompt
iterated_prompt = orchestra.Prompts.update(updated_prompt.id, input_variables=["topic", "age"], template="Tell me a joke about {topic}, that a {age} year old would find funny.")

# Update the orchestration with the new prompt
orchestration.update_prompt(iterated_prompt)

# Run this prompt with the new prompt 
output = orchestration.play(
    input={
        "topic": "coffee",
        "age": 24
    }
)

# output.choices[0].text
# -> "Why don't you ever tell secrets to coffee? Because it always spills the beans and keeps you up all night!"

# score generated output completion (-1.0 to -1.0)
orchestra.Reward.score_output(output.id, 1)
```