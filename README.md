🎼 Orchestra

Docs

Note: Orchestra is an alpha release, so expect sharp edges and bugs.

🧩 What is Orchestra?

Orchestra is a single, unified data platform that makes it easy to collect instrumentation and performance data from your LLMs, track and run models and experiments, and deploy your LLM models faster, with higher performance

We provide open-source infrastrure for LLM instrumentation and experimentation. Implement in two lines of code to add analytics and insights to help you improve the quality of your large language models (LLMs).

We also provide managed instances and a web dashboard for tracking and improving the performance of all your models and prompts, all in one place.

Check out the Getting Started guide to learn how to use Orchestra.

Call the Orchestra object with the LLM API call as the first argument and add any additional arguments to the LLM API call as the remaining arguments.

import openai

# Wrap the OpenAI API call with the `orchestra` object to track the prompt, generation, and associated metadata
output = orchestra(
    openai.Completion.create,
    engine="text-davinci-003",
    max_tokens=1024,
    temperature=0.3
)