from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


for question in question_data: # Looping through each question in the data
    question_text = question["text"] # Using the key from the dictionary
    question_ans = question["answer"]
    new_question = Question(question_text, question_ans) # Creating new questions
    question_bank.append(new_question) # Adding the question to the empty array

quiz = QuizBrain(question_bank) # Making the quiz object

while quiz.still_has_questions():
    quiz.next_question(question_bank)

# After completing the quiz
print("You've completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")