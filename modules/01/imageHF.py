# 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
from langchain_community.llms import HuggingFaceHub
from langchain_huggingface import HuggingFaceEndpoint
# Initialize model from Hugging Face Hub
model = HuggingFaceHub(
    repo_id="purplesmartai/pony-v7-base",
    model_kwargs={
        "temperature": 0.7,
        "max_new_tokens": 512
    }
)

# Text prompt (you can describe what you want the model to generate or explain)
prompt = "Describe the content of an image showing a cute cat sitting on a chair in sunlight."

# Run the model
response = model.invoke(prompt)


print("Model Output:\n", response)


# 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-> openai api key  text to image