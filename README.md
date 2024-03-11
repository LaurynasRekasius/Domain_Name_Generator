# Domain Name Generator

## Goal:
- Create LLM based solution that suggests domain names by the user-provided business description

## Tasks:

✅ 1. Evaluate prompt engineering techniques.
  - [Results]

✅ 2. Create a small dataset and evaluate the fine-tuning approach with open-source LLMs.
  - [Synthetic data creation](https://github.com/LaurynasRekasius/Domain_Name_Generator/blob/main/notebooks/Synthetic_Data_Generation_Mistral.ipynb)
  - [Fine-Tuning](https://github.com/LaurynasRekasius/Domain_Name_Generator/blob/main/notebooks/LLM_Fine_Tuning.ipynb)

✅ 3. Deploy the fine-tuned model.
  - Models on HF:
    - [Mistral 7B](https://huggingface.co/Soaky/Mistral_dn_fix)
    - [Phi-2](https://huggingface.co/Soaky/phi_2_dn)



## Short projection description:

For this task I decided to focus on Phi-2 and Mistral-7B models as open-source models with permisiv license for commercial usage and demonstrating strong performance in their respective sizes. 

First step was to evaluate prompt engineering techniques and their showed pretty good results. However, to reduce the token usage and even more increase model reliability to produce JSON responses I proceeded with fine-tuning.

JSON output was considered important for me to make sure easy data digestion by domain team down the line. Also, I decide to generate domain names without prefix or suffix. My assumption is that domain team will need to validate which domain endings are available for suggested names. Also this reduces the need of extra token usage.

Fine-tuning results let us achieve ability to use much shorter prompts and higher JSON response output reliability. Considering there were no significant differences between 3B and 7B parameter model for deployment I decided to move with smaller model.

For fast and easy usage model was deployed to HF endpoint with extra gurdrails to make sure output is always valid JSON format


## Further recommendations for Domain Team:
  - API can be accessed:
    - Input - business description as string
    - Output - JSON : {'names': ['gloweco', 'naturasphere', 'purelygreen', 'ethicalessence', 'planetbeauty']}
  - Each suggested name needs to be checked for domain availability before being displayed to user
  - Evaluate response times and required needs for parrarel requests so that optimal deployment solution could be choosen.

