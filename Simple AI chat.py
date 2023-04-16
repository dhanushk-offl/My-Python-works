#Simple AI Based chat box using random
#Coded by: Dhanush K
import random

# Define some lists of possible responses
greetings = ['Hello!', 'Hi there!', 'Hey!', 'Greetings!']
hobbies = ['What are your hobbies?', 'Do you have any hobbies?', 'What do you like to do for fun?']
gender = ['Are you male or female?', 'What gender do you identify as?', 'Do you have a gender?']
age = ['How old are you?', 'When were you born?', 'What is your age?']
jokes = ['Why did the chicken cross the road? To get to the other side!', 'Why did the tomato turn red? Because it saw the salad dressing!', 'Why did the coffee file a police report? It got mugged!']
funny_questions = ['What do you call a fake noodle? An impasta!', 'Why do we tell actors to "break a leg?" Because every play has a cast!', 'Why do seagulls fly over the sea? Because if they flew over the bay, they would be bagels!']

# Define a function to generate a random response from a list of possible responses
def generate_response(options):
    return random.choice(options)

# Define the main chat loop
while True:
    # Get input from the user
    user_input = input('You: ')

    # Process the input and generate a response
    if 'hello' in user_input.lower() or 'hi' in user_input.lower() or 'hey' in user_input.lower() or 'greetings' in user_input.lower():
        response = generate_response(greetings)
    elif 'hobby' in user_input.lower() or 'hobbies' in user_input.lower() or 'fun' in user_input.lower():
        response = generate_response(hobbies)
    elif 'gender' in user_input.lower() or 'male' in user_input.lower() or 'female' in user_input.lower():
        response = generate_response(gender)
    elif 'age' in user_input.lower() or 'born' in user_input.lower():
        response = generate_response(age)
    elif 'joke' in user_input.lower():
        response = generate_response(jokes)
    elif '?' in user_input:
        response = generate_response(funny_questions)
    else:
        response = "I'm sorry, I don't understand."

    # Print the response
    print('AI: ' + response)

