import datetime

from django.test import TestCase

from polls.models import Question


# exemple
# question_list = [
#     "Salut ça va ?",
# ]

def create_question(text, date, author=None):
    # check text, date, author
    return Question.objects.create(question_text=text, pub_date=date, author=author)


class DevTest(TestCase):
    pass


class QuestionTest(TestCase):
    # def test_nul_a_chier(self):
    #     question_1 = create_question("bla", datetime.datetime.now().astimezone(), "jean kulowski")
    #     question_2 = create_question("bla 2", datetime.datetime.now().astimezone(), "jean kulowski")
    #     print(Question.objects.all())
    #     print(type(Question.objects.all()))
    #     print(Question.objects.filter(author="jean kulowski"))
    pass


class ChoiceTest(TestCase):
    pass


class UtilitiesTest(TestCase):
    pass


"""
script devtest , print pour verifier ( toute les questions)
def (test_ + nom parlant + signature et courte)


"""
