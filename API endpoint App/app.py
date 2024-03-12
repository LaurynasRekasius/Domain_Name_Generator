from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline
import torch

import gradio as gr
import json

# Load in 4-bits to make model faster and reduce memory usage
bnb_config = BitsAndBytesConfig(
   load_in_4bit=True,
   bnb_4bit_quant_type="nf4",
   bnb_4bit_use_double_quant=True,
   bnb_4bit_compute_dtype=torch.bfloat16
)


model = AutoModelForCausalLM.from_pretrained(
    "Soaky/Mistral_dn_V3",
    quantization_config=bnb_config,
    device_map='auto',
    trust_remote_code=True,
    use_cache=False
)

tokenizer = AutoTokenizer.from_pretrained("Soaky/Mistral_dn_V3")

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer = tokenizer,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    pad_token_id = 50256
)


def is_valid_json(json_string):
    try:
        json_object = json.loads(json_string)
        return True
    except ValueError:
        return False

def format_name(name, suffix='.com'):
    """
    Format the name by removing the suffix, spaces, and converting to lowercase.
    """
    cleaned_name = name.replace(suffix, '')  # Remove suffix
    cleaned_name = cleaned_name.replace(' ', '')  # Remove spaces
    cleaned_name = cleaned_name.lower()  # Convert to lowercase
    return cleaned_name

def unify_json_format(json_string):
    try:
        data = json.loads(json_string)
        names = []
        if "names" in data:
            if all(isinstance(item, dict) for item in data["names"]):
                # Process names from dictionaries, format each name
                names = [format_name(item["name"]) for item in data["names"]]
            elif all(isinstance(item, str) for item in data["names"]):
                # Process direct string names, format each name
                names = [format_name(name) for name in data["names"]]
        return json.dumps({"names": names})
    except ValueError:
        return json_string

def generate_response_with_valid_json(message, pipe):
    max_attempts = 5  # Maximum number of attempts to get valid JSON
    for attempt in range(max_attempts):
        system_prompt = "Provide 5 names in JSON format based on description:"
        prompt = f"[INST] {system_prompt} {message} [/INST]"
        
        sequences = pipe(
            prompt,
            max_new_tokens=200,
            temperature=0.1,
            do_sample=True
        )
        
        generated_text = sequences[0]['generated_text']
        # Split the output text to extract the portion after [/INST]
        output_text = generated_text.split("[/INST]")[1].strip() if "[/INST]" in generated_text else ""
        
        # Ensure the JSON format is unified, suffixes are removed, and names are formatted
        unified_output_text = unify_json_format(output_text)
        
        if is_valid_json(unified_output_text):
            return unified_output_text
    return '{"error": "Failed to generate valid JSON after several attempts."}'

def chat_function(message, history):
    # Since the history parameter is not used in generate_response_with_valid_json, we omit it here
    return generate_response_with_valid_json(message, pipe)

# Use gr.ChatInterface to create the chat UI
demo = gr.ChatInterface(fn=chat_function, title="Domain Name Generator", description="This chatbot helps generate domain names based on your business description.")

if __name__ == "__main__":
    demo.launch(share=True)
