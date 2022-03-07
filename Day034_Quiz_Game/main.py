from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface


parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()['results']

question_bank = []
for item in question_data:
    question_bank.append(Question(item['question'], item['correct_answer']))


q_brain = QuizBrain(question_bank)
quiz_ui = QuizInterface(q_brain)


print("You've completed the quiz.")
print(f"Your final score was: {q_brain.score}/{q_brain.question_number}")
