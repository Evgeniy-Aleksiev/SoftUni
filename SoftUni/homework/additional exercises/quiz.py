from Question import Question

print('Hello. My name is Mario')
name = input('What is your first name? ')
last_name = input('What is your last name? ')
print(f'Hello {name} {last_name}, do you like games? Because we are going to play a game')
answer1 = input('yes/no: ').lower()
print()
if answer1 == 'yes':
    print(f'Nice {name}, me too.')
elif answer1 == 'no':
    print(f'Dont worry you gonna love this game, its for relax!')

print(f'Ok, {name}. Nice to meet you, my name is Mario im coming from MSI Laptop')
answer2 = input('Where are you coming from? ')

question_prompts = [
    "What color are tomatoes?\n(a) Red\n(b) Green\n(c) Yellow"
    "Where are seven Rila lakes?\n(a) Vitosha mountain\n(b) Pirin mountain\n(c) Rila"
    "The capital of Bulgaria is?\n(a) Pernik\n(b) Plovdiv\n(c) Sofia"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You got {score} / {len(questions)} correct.")


run_test(questions)