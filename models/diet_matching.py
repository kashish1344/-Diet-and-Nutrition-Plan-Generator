from langchain_community.llms.ollama import Ollama
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from transformers import pipeline

# Initialize the Ollama Llama3 model
llama_model = Ollama(model="llama3")
prompt_template = PromptTemplate(input_variables=["profile"], template="Generate a diet plan based on the following profile: {profile}")
llm_chain = RunnableSequence(prompt_template, llama_model)

# Summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_recommendations(user_profile):
    print("Generating recommendations for profile:", user_profile)  # Debug log
    response = llm_chain.invoke({"profile": user_profile})
    print("Raw response from model:", response)  # Debug log
    
    # Since the response is plain text, we can use it directly
    diet_plan = response
    print("Generated diet plan:", diet_plan)  # Debug log
    
    # Ensure the input to the summarizer is within the model's acceptable length
    max_input_length = 1024  # Adjust according to your model's max input length
    truncated_diet_plan = diet_plan[:max_input_length]

    summary = summarizer(truncated_diet_plan, max_length=150, min_length=30, do_sample=False)
    print("Generated summary:", summary)  # Debug log
    
    return {
        "diet_plan": diet_plan,
        "summary": summary[0]["summary_text"]
    }
