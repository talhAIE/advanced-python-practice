from asyncio.locks import _ContextManagerMixin
from email import message
import json

with open("bonusExamples/questions.json","r") as file:
    content=json.load(file)


for question in content:
    print(f"Question: {question['question_text']}")
    for index,option in enumerate(question['alternatives']):
        print(f"{index+1}. {option}")
    user_choice=int(input("Enter your choice: "))
    question['user_choice']=user_choice

score=0

for index , question in enumerate(content):
    if question['user_choice']==question['correct_answer']:
        score+=1
        result="Correct Answer"
    else:
        result="Wrong Answer"
    
    message=f"{index+1}. {question['question_text']}\nYour Answer: {question['user_choice']}\nCorrect Answer: {question['correct_answer']}\n{result}"
    print(message)

print(f"Your score is {score}/{len(content)}")