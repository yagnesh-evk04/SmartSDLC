import os
import re
from dotenv import load_dotenv
from ibm_watsonx_ai.foundation_models import ModelInference

# Load env variables
load_dotenv()

api_key = os.getenv("IBMs_API_KEY")
project_id = os.getenv("IBM_PROJECT_ID")
base_url = os.getenv("IBM_BASE_URL")
model_id = os.getenv("IBM_MODEL_ID")

def truncate_prompt(prompt, max_words=1500):
    words = prompt.split()
    return ' '.join(words[-max_words:]) if len(words) > max_words else prompt

def ask_ibm(prompt: str) -> str:
    try:
        model = ModelInference(
            model_id=model_id,
            credentials={"apikey": api_key, "url": base_url},
            project_id=project_id
        )
        prompt = truncate_prompt(prompt)
        response = model.generate_text(
            prompt=prompt,
            params={
                "max_new_tokens": 300,
                "temperature": 0.7,
                "top_p": 0.9,
                "decoding_method": "sample",
                "stop_sequences": ["<|endoftext|>", "User:"]
            }
        )

        if isinstance(response, dict) and 'generated_text' in response:
            result = response['generated_text']
        else:
            result = str(response)

        return re.split(r'\bUser:|\bAssistant:', result)[0].strip()

    except Exception as e:
        return f"Error: {str(e)}"


# Specific prompt functions
def ai_requirements_analysis(project_input):
    prompt = f"""You are a software requirements analyst. Analyze the following project and extract key features and a priority level.

Project Idea: {project_input}
Respond in JSON with 'features' (list) and 'priority' (Low, Medium, High)."""
    return ask_ibm(prompt)

def ai_design_suggestion(features_str):
    prompt = f"""You are a software architect. Based on these features: {features_str}, suggest a suitable software architecture.

Include frontend, backend, database, and hosting. Respond in JSON format."""
    return ask_ibm(prompt)

def auto_code_generator(design_str):
    prompt = f"""You are a smart code generator. Based on this design for a project to help college students manage their daily study schedule, generate a relevant code summary.

Design:
{design_str}

Respond with relevant code structure and implementation outline only for that use case (not e-commerce)."""
    return ask_ibm(prompt)


def smart_test_automation(design):
    prompt = f"""
You are an AI test engineer. Write 3 test cases for a {design}.
Return a result summary at the end

"""

    return ask_ibm(prompt)


def smart_deployment(design):
    prompt = f"""
You are an AI deployment engineer. explain how to deploy for {design}.
return the result in neat format.
"""
    return ask_ibm(prompt)

def predictive_maintenance(design):
    prompt = f"You are a system maintenance AI. Predict future issues or confirm stability for project {design}.return the result in neat format."
    return ask_ibm(prompt)

def extract_json_from_codeblock(text):
    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()
    return text
