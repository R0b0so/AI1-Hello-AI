print("Hello I am an AI chatbot. What is your name?")

name = input()

print("hello ", name, " nice to meet you.")
print("How are you feeling (Good\Bad)")

mood = input().lower()
 
if mood == "bad":
    print("I'm sorry to hear that.")
elif mood == "good":
    print("That's good to hear.")
else:
    print("I understand it's hard to put your feelings into words.")