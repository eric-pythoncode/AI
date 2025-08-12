import os
from google import generativeai
from google.generativeai import types
apiKey = "AIzaSyDvrKodops4E-M4NB806JmtQUgZfYHfO70"
generativeai.configure(api_key="AIzaSyDvrKodops4E-M4NB806JmtQUgZfYHfO70")
model = generativeai.GenerativeModel("gemini-1.5-flash")

def generateResponse(prompt, temperature=.3):
    try:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        configParams = types.GenerateContentConfig(temperature=temperature)
        response = model.generate_content(
        prompt,
        generation_config={"temperature": temperature}
        )
        
    except Exception as e:
        return f"Error: {e}"
    
def biasMitigationActivity():
    print("\nBIAS MITIGATION ACTIVITY")

    prompt = input("Enter a prompt to explore bias (eg: Describe the ideal doctor)")

    modifiedPrompt = input("Modify the prompt to make it more neutral (eg: describe the qualities of a doctor)")

    modifiedResponse = generateResponse(modifiedPrompt)
    print(f"\nModified AI response - Neutral: {modifiedResponse}")

def tokenLimitActivity():
    print("\nToken Limit Activity")

    longPrompt = input("Enter a long prompt - more than 300 words, like a detailed story")
    longResponse = generateResponse(longPrompt)
    print(f"Response: {longResponse}")

    shortPrompt = input("Enter a short prompt - like a small story")
    shortResponse = generateResponse(shortPrompt)
    print(f"Response: {shortResponse}")

def runActivity():
    print("\nAI learning activity")

    activityChoice = input("What activity would you like to do - 1. Bias mitigation or 2. Token limit activity?")

    if activityChoice == "1":
        biasMitigationActivity()
    elif activityChoice == "2":
        tokenLimitActivity()
    else:
        print("Please type 1 or 2.")

if __name__ == "__main__":
    runActivity()