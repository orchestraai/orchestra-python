🎼 Orchestra
Discord Twitter

Orchestra is an open-source Javascript package for LLM instrumentation. It allows users to add structure and type, validate and correct the outputs of large language models (LLMs).

Docs

Note: Orchestra is an alpha release, so expect sharp edges and bugs.

🧩 What is Orchestra?
Orchestra is a Javascript package that lets a user add structure, type and quality guarantees to the outputs of large language models (LLMs). Orchestra:

does validation of LLM outputs (including semantic validation such as checking for bias in generated text, checking for bugs in generated code, etc.)
takes corrective actions (e.g. reasking LLM) when validation fails,
enforces structure and type guarantees (e.g. JSON).
🚒 Under the hood
Orchestra provides a format (.orch) for enforcing a specification on an LLM output, and a lightweight wrapper around LLM API calls to implement this spec.

orch (Orchestra markup Language) files for specifying structure and type information, validators and corrective actions over LLM outputs.
gd.Orchestra wraps around LLM API calls to structure, validate and correct the outputs.

Check out the Getting Started guide to learn how to use Orchestra.

📜 ORCH spec
At the heart of Orchestra is the orch spec. orch is intended to be a language-agnostic, human-readable format for specifying structure and type information, validators and corrective actions over LLM outputs.

orch is a flavor of XML that lets users specify:

the expected structure and types of the LLM output (e.g. JSON)
the quality criteria for the output to be considered valid (e.g. generated text should be bias-free, generated code should be bug-free)
and corrective actions to be taken if the output is invalid (e.g. reask the LLM, filter out the invalid output, etc.)
To learn more about the ORCH spec and the design decisions behind it, check out the docs. To learn how to write your own ORCH spec, check out this link.

📦 Installation
npm install orchestra-sdk
📍 Roadmap
 Adding more examples, new use cases and domains
 Adding integrations with langchain, gpt-index, minichain, manifest
 Expanding validators offering
 More compilers from .orch -> LLM prompt (e.g. .orch -> TypeScript)
 Informative logging
 Improving reasking logic
 A guardrails.js implementation
 VSCode extension for .orch files
 Next version of .orch format
 Add more LLM providers
🚀 Getting Started
Let's go through an example where we ask an LLM to explain what a "bank run" is in a tweet, and generate URL links to relevant news articles. We'll generate a .orch spec for this and then use Orchestra to enforce it. You can see more examples in the docs.

📝 Creating a ORCH spec
We create a ORCH spec to describe the expected structure and types of the LLM output, the quality criteria for the output to be considered valid, and corrective actions to be taken if the output is invalid.

Specifically, we use ORCH to

Request the LLM to generate an object with two fields: explanation and follow_up_url.
For the explanation field, ensure the max length of the generated string should be between 200 and 280 characters.
If the explanation is not of valid length, reask the LLM.
For the follow_up_url field, the URL should be reachable.
If the URL is not reachable, we will filter it out of the response.
<orch version="0.1">
<output>
    <object name="bank_run" format="length: 2">
        <string
            name="explanation"
            description="A paragraph about what a bank run is."
            format="length: 200 280"
            on-fail-length="reask"
        />
        <url
            name="follow_up_url"
            description="A web URL where I can read more about bank runs."
            format="valid-url"
            on-fail-valid-url="filter"
        />
    </object>
</output>

<prompt>
Explain what a bank run is in a tweet.

@xml_prefix_prompt

{output_schema}

@json_suffix_prompt_v2_wo_none
</prompt>
</orch>
We specify our quality criteria (generated length, URL reachability) in the format fields of the ORCH spec below. We reask if explanation is not valid, and filter the follow_up_url if it is not valid.

🛠️ Using Orchestra to enforce the ORCH spec
Next, we'll use the ORCH spec to create a Orchestra object. The Orchestra object will wrap the LLM API call and enforce the ORCH spec on its output.

import orchestra-sdk as gd

orchestra = gd.Orchestra.from_orch(f.name)
The Orchestra object compiles the ORCH specification and adds it to the prompt. (Right now this is a passthrough operation, more compilers are planned to find the best way to express the spec in a prompt.)

Here's what the prompt looks like after the ORCH spec is compiled and added to it.

Explain what a bank run is in a tweet.

Given below is XML that describes the information to extract from this document and the tags to extract it into.

<output>
    <object name="bank_run" format="length: 2">
        <string name="explanation" description="A paragraph about what a bank run is." format="length: 200 280" on-fail-length="reask" />
        <url name="follow_up_url" description="A web URL where I can read more about bank runs." required="true" format="valid-url" on-fail-valid-url="filter" />
    </object>
</output>

ONLY return a valid JSON object (no other text is necessary). The JSON MUST conform to the XML format, including any types and format requests e.g. requests for lists, objects and specific types. Be correct and concise.

JSON Output:
Call the Orchestra object with the LLM API call as the first argument and add any additional arguments to the LLM API call as the remaining arguments.

import openai

# Wrap the OpenAI API call with the `orchestra` object
raw_llm_output, validated_output = orchestra(
    openai.Completion.create,
    engine="text-davinci-003",
    max_tokens=1024,
    temperature=0.3
)

print(validated_output)
{
    'bank_run': {
        'explanation': 'A bank run is when a large number of people withdraw their deposits from a bank due to concerns about its solvency. This can cause a financial crisis if the bank is unable to meet the demand for withdrawals.',
        'follow_up_url': 'https://www.investopedia.com/terms/b/bankrun.asp'
    }
}
