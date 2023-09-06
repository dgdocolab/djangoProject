import datetime

from django.test import TestCase
from django.core.exceptions import ValidationError

from polls.models import Question


# exemple
# question_list = [
#     "Salut ça va ?",
# ]

# def validatortext(value):
#     if value is None or value != type:
#         raise ValidationError(
#             "%(value)s is not a char",
#             params={"value": value},
#         )


def create_question(text, date, author=None):
    # check text, date, author
    if text is None or type(text) != type(text):
        raise ValidationError(
            "(text) is not a text / is empty",
        )
    else:
        return Question.objects.create(question_text=text, pub_date=date, author=author)





class DevTest(TestCase):
    pass


class QuestionTest(TestCase):
    def test_nul_a_chier(self):
        question = create_question(None, datetime.datetime.now().astimezone(), "jean kulowski")
        # create_question("bla 2", datetime.datetime.now().astimezone(), "jean kulowski")
        print(question)
        # print(type(Question.objects.all()))
        # print(Question.objects.filter(author="jean kulowski"))

    pass


class ChoiceTest(TestCase):
    pass


class UtilitiesTest(TestCase):
    pass


"""
script devtest , print pour verifier ( toute les questions)
def (test_ + nom parlant + signature et courte)


"""
