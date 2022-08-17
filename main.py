from cgitb import text
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)
print(question_bank)

brain = QuizBrain(question_bank)
brain.next_question()

while brain.still_has_questions():
    brain.next_question()
