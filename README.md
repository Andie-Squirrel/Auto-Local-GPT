# Auto-Local-GPT: An Autonomous Multi-LLM Project

The primary goal of this project is to enable users to easily load their own AI models and run them autonomously in a loop with goals they set, without requiring an API key or an account on some website. The focus is on compatibility with a broad range of AI models and ease of use.

This project should be considered UNSTABLE for the moment.  Keep in mind that this project is in its infancy and barely working, and sometimes not at all.  Hugging Face transformers are being added right now, as well as updates to the current LLaMA/Alpaca-based compatibility.

Reasons why this project matters:

- You want to use your own LLM that is pre-trained or fine-tuned on a custom dataset
- You want to use an AI model offline, without being tied to an internet API
- You want to use an LLM that is more task-oriented and less politically correct,
  such as with White Hat or Red Team security testing
- You are bored and have powerful hardware just sitting around.

This project is more geared towards folks with a lot of CPU power, a ridiculous amount of RAM, and a lot of time for the AI model to process. Inevitably, someone out there will try to run this on their old Intel i3 with 8GB of RAM, but they are not likely to have success. If they somehow do, it will be several hours of 100% CPU use to give a large response from a small LLM.

The minimum recommended hardware for the project is:
- A modern high-end CPU with at least 16 threads
- At least 64GB of RAM

Development for this project is happening on 2 Dell PowerEdge rack servers:

R820:
- 4x Xeon 12 core processors, 96 threads total
- 768 GB of RAM

R810:
- 4x Xeon 10 core processors, 80 threads total
- 256 GB of RAM

Even with these servers, there is sometimes wait time of up to 20 minutes for a medium-sized response. With code that is not yet integrated into this project, using the R810 with 256 GB of RAM, it usually cannot run larger than a 30B sized LLM, and the largest without running out of RAM is a 65B Int4 [TianXxx/llama-65b-int4](https://huggingface.co/TianXxx/llama-65b-int4).  On the R820 with 768GB of RAM, it can comfortably run [facebook/galactica-120b](https://huggingface.co/facebook/galactica-120b), and can barely run [bigscience/bloomz](https://huggingface.co/bigscience/bloomz) with special settings.

## Supported Models
---
Hugging Face transformers are being added as a first priority and will happen soon.


Currently, this uses [llama.cpp](https://github.com/ggerganov/llama.cpp), it should work with all models they support, including:
* LLaMA
* Alpaca
* GPT4All
* Chinese LLaMA / Alpaca
* Vigogne (French)
* Vicuna
* Koala

## Model Performance (the experience so far)
---

### Response Quality
So far I have tried 
* Vicuna-13b-4BIT 
* LLama-13B-4BIT

Overall, the Vicuna model outperformed the original LLama model in terms of answering in the required JSON format and the comprehensibility of its answers. However, the Vicuna model has a tendency to start every answer with ### ASSISTANT. Further testing with other models is necessary to determine their performance.

### Inference Speed
The most significant issue at the moment is inference speed. As the agent is self-prompting, a few seconds of inference that are acceptable in a chatbot scenario become minutes and more. This makes testing things like different prompts difficult under these conditions.

## Discussion
Please feel free to share your thoughts and experiences in the [discussion](https://github.com/InvalidAdmin/Auto-Local-GPT/discussions) area. What models did you try? How well did they work for you?

## Future Plans
---
1. Keep in step with upstream projects
2. Use Hugging Face transformers and some logic that optimizes for various models, such as gpt-j and gpt-neox
3. Search for LLMs and devise a menu to select which model to load
4. Add GPU support via GPTQ
5. Improve prompts
6. Remove external API support (this is meant to be a completely self-contained agent)
7. Add support for [Open Assistent](https://github.com/LAION-AI/Open-Assistant) models

## History

2023/4/18 Forked this from [rhohndorf/Auto-Llama-cpp](https://github.com/rhohndorf/Auto-Llama-cpp)

Auto-Local-GPT is a fork of [rhohndorf/Auto-Llama-cpp](https://github.com/rhohndorf/Auto-Llama-cpp), which is a fork of [Significant-Gravitas/Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT).
