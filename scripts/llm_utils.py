from transformers import AutoTokenizer, AutoModelForCausalLM
from config import Config

cfg = Config()
tokenizer = AutoTokenizer.from_pretrained(cfg.huggingface_model)
model = AutoModelForCausalLM.from_pretrained(cfg.huggingface_model)

def create_chat_completion(messages, temperature=0.36, max_tokens=0)->str:
    inputs = tokenizer(messages[0]["content"], return_tensors='pt')
    output = model.generate(input_ids=inputs['input_ids'], max_length=1024, temperature=temperature, do_sample=True, top_p=0.9, top_k=50)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

inputs = tokenizer(messages[0]["content"], return_tensors="pt")
outputs = model.generate(
    inputs["input_ids"],
    do_sample=True,
    max_length=1024,
    temperature=temperature,
    num_beams=5,
    num_return_sequences=1,
)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
return response


"""
from llama_cpp import Llama
from config import Config

cfg = Config()
llm = Llama(model_path=cfg.smart_llm_model, n_ctx=2048, embedding=True)

def create_chat_completion(messages, model=None, temperature=0.36, max_tokens=0)->str:
    response = llm(messages[0]["content"], stop=["Q:", "### Human:"], echo=False, temperature=temperature, max_tokens=max_tokens)
    return response["choices"][0]["text"]
"""
