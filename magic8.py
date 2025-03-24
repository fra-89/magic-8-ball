import random

# Variables
name = "Joe"  # Replace with any name you prefer
question = "Is this real life?"  # Replace with your question
answer = ""

# Generate a random number between 1 and 9
random_number = random.randint(1, 9)

# Uncomment the line below to see the random number during testing
# print(f"Random number: {random_number}")

# Control flow to determine the answer
if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    answer = "Error"

# Display output
if name:
    print(f"{name} asks: {question}")
else:
    print(f"Question: {question}")

if question:
    print(f"Magic 8-Ball's answer: {answer}")
else:
    print("The Magic 8-Ball cannot provide an answer without a question.")
