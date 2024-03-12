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



## Prompt Engineering
Initial tests with prompt engineering yielded promising results. However, to enhance the accuracy and format consistency of the model's outputs, I proceeded with fine-tuning.

## Fine-Tuning and Data Generation
I generated a synthetic dataset focused on concise business descriptions (up to 500 characters), aiming for output in a structured JSON format. This decision was driven by the need for straightforward integration with the domain team's processes and minimizing token usage. The fine-tuning process prioritized producing domain names in a simplified format (lowercase, without prefixes/suffixes), considering the domain team's subsequent validation process.

## Model Comparison and Selection
The fine-tuning significantly improved output reliability. While Phi-2 showed improvement with extended prompts, Mistral-7B consistently delivered more appropriate suggestions suitable as domain names, with fewer edge cases. Consequently, I selected Mistral-7B for deployment.

## Deployment
The model was deployed as a Gradio app on Hugging Face Spaces, providing a practical and cost-effective solution for immediate use, with the flexibility to migrate to alternative hosting solutions as necessary.

## Recommendations for the Domain Team

  API Usage:
  - Input: Business description in string format, ideally under 500 characters, without paragraphs or special characters.
  - Output: A JSON-formatted string, e.g.:
    
         {"names": ["gloweco", "naturasphere", "purelygreen", "ethicalessence", "planetbeauty"]}
    
Validation: Each suggested name should be verified for domain availability before presenting to user.

Performance Considerations: Assess response times and the ability to handle concurrent requests to ensure the chosen deployment solution meets demand effectively.

