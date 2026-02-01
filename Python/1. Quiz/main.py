from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# n = len(question_data)
# question_bank = []
# for i in range(0, n):
#     q_text = question_data[i]["text"]
#     q_answer = question_data[i]["answer"]
#     new_question = Question(q_text, q_answer)
#     question_bank.append(new_question)

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[1].text, question_bank[1].answer)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final scor is: {quiz.score}/{quiz.question_number}")