# Define a base User class with common attributes for Student, Teacher, and Parent
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Create a Student class, inheriting from User
class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id

# Create a Teacher class, inheriting from User
class Teacher(User):
    def __init__(self, name, email, teacher_id):
        super().__init__(name, email)
        self.teacher_id = teacher_id

# Create a Parent class, inheriting from User
class Parent(User):
    def __init__(self, name, email, child_name):
        super().__init__(name, email)
        self.child_name = child_name

# Define a Quiz class to manage quizzes
class Quiz:
    def __init__(self, quiz_id, title):
        self.quiz_id = quiz_id
        self.title = title
        self.questions = []  # List to store quiz questions
        self.participants = {}  # Dictionary to store participants and their answers

    # Add a question to the quiz
    def add_question(self, question, options, correct_option):
        self.questions.append({
            'question': question,
            'options': options,
            'correct_option': correct_option
        })

    # Invite a participant to the quiz
    def invite_participant(self, user):
        self.participants[user.email] = {'user': user, 'answers': []}

    # Submit an answer to a quiz question
    def submit_answer(self, user, question_idx, answer_idx):
        if user.email in self.participants:
            if 0 <= question_idx < len(self.questions) and 0 <= answer_idx < len(self.questions[question_idx]['options']):
                self.participants[user.email]['answers'].append((question_idx, answer_idx))
                return True
        return False

    # Calculate the score of a participant in the quiz
    def calculate_score(self, user):
        if user.email in self.participants:
            score = 0
            for question_idx, answer_idx in self.participants[user.email]['answers']:
                if self.questions[question_idx]['correct_option'] == answer_idx:
                    score += 1
            return score
        return 0

# Define a QuizManagementSystem class to manage multiple quizzes
class QuizManagementSystem:
    def __init__(self):
        self.quizzes = {}  # Dictionary to store quizzes

    # Create a new quiz
    def create_quiz(self, quiz_id, title):
        quiz = Quiz(quiz_id, title)
        self.quizzes[quiz_id] = quiz
        return quiz

    # Add a participant to a quiz
    def add_participant_to_quiz(self, quiz_id, user):
        if quiz_id in self.quizzes:
            self.quizzes[quiz_id].invite_participant(user)
            return True
        return False

    # Submit an answer to a quiz question
    def submit_quiz_answer(self, quiz_id, user, question_idx, answer_idx):
        if quiz_id in self.quizzes:
            return self.quizzes[quiz_id].submit_answer(user, question_idx, answer_idx)
        return False

    # Get the quiz results for a participant
    def get_quiz_results(self, quiz_id, user):
        if quiz_id in self.quizzes:
            return self.quizzes[quiz_id].calculate_score(user)
        return 0

# Sample usage of the Quiz Management System
if __name__ == "__main__":
    # Instantiate users
    student1 = Student("Amardeep", "amardeepnigam32@gmail.com", "S12345")
    teacher1 = Teacher("Vivek", "vivek@gamail.com", "T98765")
    parent1 = Parent("Amit", "amit@gmail.com", "Alice")

    # Create Quiz Management System
    qms = QuizManagementSystem()

    # Create a quiz
    quiz1 = qms.create_quiz("Q001", "Math Quiz")

    # Add questions to the quiz
    quiz1.add_question("What is 8 - 4?", ["3", "4", "5"], 1)
    quiz1.add_question("What is 6 x 4?", ["18", "21", "24"], 1)

    # Invite participants to the quiz
    qms.add_participant_to_quiz("Q001", student1)
    qms.add_participant_to_quiz("Q001", teacher1)

    # Participants submit answers
    qms.submit_quiz_answer("Q001", student1, 0, 1)  # Student's answer to the first question
    qms.submit_quiz_answer("Q001", teacher1, 1, 1)  # Teacher's answer to the first question

    # Get quiz results
    student1_score = qms.get_quiz_results("Q001", student1)
    teacher1_score = qms.get_quiz_results("Q001", teacher1)

    print(f"Student1's score: {student1_score}")
    print(f"Teacher1's score: {teacher1_score}")
