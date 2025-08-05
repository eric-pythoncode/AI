from transformers import GPT2LMHeadModel, GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
def getResponse(prompt, max_length = 50):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

questionPrompt = "What are the benefits of exercise?"
print(f'Question prompt response: {getResponse(questionPrompt)}\n')

commandPrompt = "List five benefits of an exercise"
print(f"Command Prompt Response: {getResponse(commandPrompt)}")
