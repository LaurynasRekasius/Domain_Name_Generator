# Domain Name Generator

## Goal:
- Create LLM based solution that suggests domain names by the user-provided business description and deploy it as an API endpoint

## Tasks:

✅ 1. Review LLMs and evaluate prompt engineering techniques & fine-tuning:
  - [Results]

✅ 2. Create a small dataset and fine-tune open-source LLMs:
  - [Synthetic data creation](https://github.com/LaurynasRekasius/Domain_Name_Generator/blob/main/notebooks/Synthetic_Data_Generation_Mistral.ipynb)
  - [Fine-Tuning](https://github.com/LaurynasRekasius/Domain_Name_Generator/blob/main/notebooks/LLM_Fine_Tuning.ipynb)

✅ 3. Deploy the fine-tuned models to HF:
  - [Mistral 7B](https://huggingface.co/Soaky/Mistral_dn_fix)
  - [Phi-2](https://huggingface.co/Soaky/phi_2_dn)

✅ 4. Deploy API endpoint:
  - [HuggingFace Space](https://huggingface.co/spaces/Soaky/DN)
  - [Notebook with API testing]()



## Short projection implementation description:

For this task, I decided to focus on Phi-2 and Mistral-7B models as open-source models with permissive licenses for commercial usage and demonstrating strong performance in their respective sizes. 

The first step was to evaluate prompt engineering techniques and they showed pretty good results. However, to reduce the token usage and to increase model reliability to produce JSON responses I proceeded with fine-tuning.

The first step for fine-tuning was to generate synthetic data. My goal was to focus on short business descriptions (up to 500 characters) and that model response would be in JSON format. The output format was considered important to ensure easy data digestion by the domain team down the line. Also, I decide to generate domain names without prefixes or suffixes and in lowercase. I assume that the domain team will need to validate which domain endings are available for suggested names. Also, this reduces the need for extra token usage.

The fine-tuned models provided better reliability in the output format. Phi-2 outputs struggled and also benefited from extended prompts with output examples (few-shots prompt). Despite end results looking very similar and consistently producing JSON output further investigation showed that smaller model outputs often can't be used as domain names. Mistal output were much better in this regard and had very few edge cases that could be easily addressed with simple data manipulation operations. Also, it was possible to use the model with a short basic prompt. This let me confidently choose the Mistal-7b fine-tuned model as the option for deployment. 

For fast and easy usage, the model was deployed to the HF spaces as a Gradio app. This made it easy to add extra guardrails to ensure correct JSON output and was a cost-effective solution. Prepared files can be easily deployed to other hosting providers as needed.


## Further recommendations for Domain Team:
  - API can be accessed:
    - Input - business description as in string format without paragraphs or any other special characters. Idealy description should be less than 500 characters.
    - Output - string in a valid JSON format that looks like this:
      
       {'names': ['gloweco', 'naturasphere', 'purelygreen', 'ethicalessence', 'planetbeauty']}
  - Each suggested name needs to be checked for domain availability before being displayed to the user.
  - Evaluate response times and required needs for parallel requests so that optimal deployment solutions can be chosen.

