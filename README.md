# Domain Name Generator

## Goal:
Develop and deploy an API endpoint that leverages LLM to generate domain name suggestions based on descriptions of businesses provided by users.

## Tasks:

✅ 1. Review LLMs and evaluate prompt engineering techniques & fine-tuning:
  - [Results](https://github.com/LaurynasRekasius/Domain_Name_Generator/blob/main/notebooks/LLMs_Overview.ipynb)

✅ 2. Create a small dataset and fine-tune open-source LLMs:
  - [Synthetic data creation](https://github.com/LaurynasRekasius/Domain_Name_Generator/blob/main/notebooks/Synthetic_Data_Generation_Mistral.ipynb)
  - [Fine-Tuning](https://github.com/LaurynasRekasius/Domain_Name_Generator/blob/main/notebooks/LLM_Fine_Tuning.ipynb)

✅ 3. Deploy the fine-tuned models to HF:
  - [Mistral 7B](https://huggingface.co/Soaky/Mistral_dn_V3)
  - [Phi-2](https://huggingface.co/Soaky/phi_2_dn_v3)

✅ 4. Deploy API endpoint:
  - [HuggingFace Space](https://huggingface.co/spaces/Soaky/DN)
  - [Notebook with API testing](https://github.com/LaurynasRekasius/Domain_Name_Generator/blob/main/notebooks/API_Endpoint.ipynb)



## Project Overview
This analysis reviews two open-source LLMs:
  - Phi-2
  - Mistal-7B

### Prompt Engineering
Initial tests with prompt engineering yielded promising results. I tried basic prompts which yielded very bad results. More advanced one-shot and few-shot prompts managed to yield pretty good results for these small models. However, to enhance the accuracy and format consistency of the model's outputs, I proceeded with fine-tuning.

### Fine-Tuning and Data Generation
To generate data faster I used Mistral API. The mix of Mistral 7b and Mixtral 8x7B models were used to generate all the required data. Synthetic dataset focused on concise business descriptions (up to 500 characters), aiming for output in a structured JSON format. This decision was driven by the need for straightforward integration with the domain team's processes and minimizing token usage. The fine-tuning process prioritized producing domain names in a simplified format (lowercase, without prefixes/suffixes), considering the domain team's subsequent validation process.

### Model Comparison and Selection
The fine-tuning significantly improved output reliability. While Phi-2 showed improvement with extended prompts, Mistral-7B consistently delivered more appropriate suggestions suitable as domain names, with fewer edge cases and shorter prompts. Consequently, I selected Mistral-7B for deployment.

![Performance Chart](https://github.com/LaurynasRekasius/Domain_Name_Generator/assets/13908912/9c30f211-0558-4205-a68d-92f5c802233a)

Here performance was mainly measured based on the ability to consistently produce JSON output. When the best model was identified extra refinement was done to ensure the content inside the JSON is also what makes sense and in consistently good format.

### Deployment
The model was deployed as a Gradio app on Hugging Face Spaces, providing a practical and cost-effective solution for immediate use, with the flexibility to migrate to alternative hosting solutions as necessary. This deployment has extra guardrails to ensure consistent output and was tested for 350 consecutive requests and produced 100% expected and correct output.

### Recommendations for the Domain Team

  API Usage:
  - Input: Business description in string format, ideally under 500 characters, without paragraphs or special characters.
  - Output: A JSON-formatted string, e.g.:
    
         {"names": ["gloweco", "naturasphere", "purelygreen", "ethicalessence", "planetbeauty"]}
    
Validation: Each suggested name should be verified for domain availability before presenting it to the user.

Performance Considerations: Assess response times and the ability to handle concurrent requests to ensure the chosen deployment solution meets demand effectively.

Further improvements:
- Model feedback loop implementation for continuous improvements. Collect real business descriptions and domain names users picked to refine recommendations.

- Multilingual support could be the next step in making this tool more widely available. 

