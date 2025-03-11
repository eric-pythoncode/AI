print("Hello! I am an AI bot. What's your name?")

name = input()

print(f"Nice to meet you, {name}.")

print("How are you doing today?")
mood = input().lower()

if mood == "good":
    print("I'm glad to hear that!")
if mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon")
else:
    print("I understand. Sometimes it's hard to put things into words.")

print(f"It was nice meeting you, {name}. Goodbye.")