from config import Config
from transformers import AutoModelForCausalLM, AutoTokenizer

cfg = Config()


def call_ai_function(function, args, description, model_path=None):
    """Call an AI function"""
    if model_path is None:
        model_path = cfg.smart_llm_model
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)
    # For each arg, if any are None, convert to "None":
    args = [str(arg) if arg is not None else "None" for arg in args]
    # parse args to comma seperated string
    args = ", ".join(args)
    messages = [
        {
            "role": "system",
            "content": f"You are now the following python function: ```# {description}\n{function}```\n\nOnly respond with your `return` value.",
        },
        {"role": "user", "content": args},
    ]

    response = create_chat_completion(
        model=model, tokenizer=tokenizer, messages=messages, temperature=0
    )

    return response




"""
from llm_utils import create_chat_completion
# This is a magic function that can do anything with no-code. See
# https://github.com/Torantulino/AI-Functions for more info.
def call_ai_function(function, args, description, model=None):
    """Call an AI function"""
    if model is None:
        model = cfg.smart_llm_model
    # For each arg, if any are None, convert to "None":
    args = [str(arg) if arg is not None else "None" for arg in args]
    # parse args to comma seperated string
    args = ", ".join(args)
    messages = [
        {
            "role": "system",
            "content": f"You are now the following python function: ```# {description}\n{function}```\n\nOnly respond with your `return` value.",
        },
        {"role": "user", "content": args},
    ]

    response = create_chat_completion(
        model=model, messages=messages, temperature=0
    )

    return response
"""
