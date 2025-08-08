import os
from google import generativeai
from google.generativeai import types

# Configure the API key
generativeai.configure(api_key="AIzaSyDvrKodops4E-M4NB806JmtQUgZfYHfO70")

# Create the model instance
model = generativeai.GenerativeModel("gemini-1.5-flash")  # or "gemini-pro", depending on your access


def generateResponse(prompt, temperature=0.3):
    try:
        response = model.generate_content(
        prompt,
        generation_config={"temperature": temperature}
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"
    
def reinforcementLearningActivity():
    print("\nREINFORCEMENT LEARNING ACTIVITY")

    prompt = input("Enter a prompt for the AI model: ")

    initialResponse = generateResponse(prompt)
    print(f"Initial AI response: {initialResponse}")

    rating = int(input("Rate the response from 1 (bad) to 10 (best)"))
    feedback = input("Provide feedback for the improvement")

    improvedResponse = f"{initialResponse} (Improved with your feedback:) {improvedResponse}"
    print(f"Improved AI response: {improvedResponse}")

    print("\nReflection")
    print("1. How did the model's response improve with feedback?")
    print("2. How does reinforcement learning help AI improve its performance over time?")

def roleBasedPromptActivity():
    print("\nROLE BASED PROMPTS ACTIVITY")

    category = input("Enter a category (eg: science, math, etc)")
    item = input(f"Enter a specific {category} topic (like photosynthesis for science)")

    teacherPrompt = f"You are a teacher. Explain {item} in simple terms."
    expertPrompt = f"You are an expert in {category}. Explain {item} in a detailed, technical matter."

    teacherResponse = generateResponse(teacherPrompt)
    expertResponse = generateResponse(expertPrompt)

    print(f"\nTeacher's response: {teacherResponse}")
    print(f"\nTeacher's response: {expertResponse}")

    print("\nReflection")
    print("1. How did the Ai's response differ between the teacher and the expert's perspectives?")
    print("2. How does role based prompts help tailor AI responses for different contexts?")

def runActivity():
    print("\nAI learning activity")

    activityChoice = input("What actvity would you like to run? 1. Reinforcement learning or 2. Role based prompts")

    if activityChoice == "1":
        reinforcementLearningActivity()
    elif activityChoice == "2":
        roleBasedPromptActivity()
    else:
        print("Invalid choice. Choose either 1 or 2.")

if __name__ == "__main__":
    runActivity()