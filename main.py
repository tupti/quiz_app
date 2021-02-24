import json
import random

class Question:
     def __init__(self, prompt, options: list, answer):
          self.prompt = prompt
          random.shuffle(options)
          self.options = options
          self.answer = answer

questionsData = []
with open('questions.json','r') as json_file:
    questionsData = json.load(json_file)

allQuestions = []
for question in questionsData['questions']:
    allQuestions.append(Question(question['prompt'], question['options'], question['answer']))

def run_quiz(allQuestions):
    score = 0
    for question in allQuestions:
        print(f"{question.prompt}?")
        for i, option in enumerate(question.options, start=1):
            print(f"{i}. {option}")
        answer = input("Your choice: ")
        if question.options[int(answer)-1] == question.answer:
            score+=1
        print("\n")
    print(f"Final score is {score} of {len(allQuestions)}.")

run_quiz(allQuestions)