from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item['question'], item['correct_answer']))


q_brain = QuizBrain(question_bank)

while q_brain.still_has_question():
    q_brain.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {q_brain.score}/{q_brain.question_number}")
