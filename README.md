# Auto-Local-GPT: An Autonomous Multi-LLM Project

The major goal of this project is to be able to easily load your own AI model and let it run autonomously in a loop with goals you set for it, and to do this basic function without requiring an API key or an account at some website.  The focus is for boad compatability with AI models and ease of use.

Reasons why this project matters:
 - You would like to use your own LLM that is pre-trained on a custom dataset
 - You want to use an AI model offline, without being tied to an internet API
 - You require a LLM that is more task orientated and less politically correct,
   such as with White Hat or Red Team security testing
 - You're bored and just happen to have super powerful hardware sitting around

This project is more for a group of folks with a lot of CPU power, rediculious amounts of RAM, and a lot of time for the AI model to process.  



## Supported Models
---
Since this uses [llama.cpp](https://github.com/ggerganov/llama.cpp) under the hood it should work with all models they support. As of writing this is 
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

Overall the Vicuna model performed much better than the original LLama model in terms of answering in the required JSON format and how much sense the answers make. I just couldn't get it to stop starting every answer with ### ASSISTANT.
I am very curious to hear how well others models perform. The 7B models seemed have problems with grasping what's asked of them in the prompt, but I tried very little in this direction since the inference speed didn't seem to be much faster for me.

### Inference Speed
The biggest problem at the moment is indeed inference speed. As the agent is self prompting a lot, a few seconds of infernce that are acceptable in a chatbot scenario become minutes and more. 
Testing things like different prompts etc is a pain under these conditions. 

## Discussion
Fell free to add your thoughts and experiences in the [discussion](https://github.com/rhohndorf/Auto-Llama-cpp/discussions) area. What models did you try? How well did they work ou for you? 

## Future Plans
---
1. Try to keep in step with upstream projects
2. Use Hugging Face transformers and some logic that optomizes for various models i.e., gpt-j and gpt-neox
3. Search for LLMs and devise a menu to select which model to load
4. Add GPU Support via GPTQ
5. Improve Prompts
6. Remove external API support (This is supposed to be completely self-contained agent)
7. Add support for [Open Assistent](https://github.com/LAION-AI/Open-Assistant) models
