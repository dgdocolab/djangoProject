from datetime import datetime, date, timedelta
from django.test import TestCase
from django.core.exceptions import ValidationError
from polls.models import Question, Choice
from polls.utilities import is_valid_string, is_valid_author, create_question, is_valid_question, is_valid_date


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
def Validation_des_champs(text):
    pass


def boucler_questions(create_boucle_question, n):
    nombre = 0
    while nombre < n:
        create_boucle_question()
        nombre += 1


def create_choice(text):
    if text is None or type(text) != type(text):
        raise ValidationError(
            "(choice) is not a text / is empty",
        )
    else:
        return Choice.objects.create(choice_text=text)


class DevTest(TestCase):
    def test_joker(self):
        print(create_question("test", datetime.now().astimezone(), ""))


class QuestionTest(TestCase):
    pass


class ChoiceTest(TestCase):
    def test_choice_essaie(self):
        choice = create_choice(text="ca vas")
        print(choice)


class UtilitiesTest(TestCase):
    # IS_VALID_STRING
    def test_is_valid_string(self):
        parameter = "hello"
        self.assertTrue(is_valid_string(parameter))

    def test_is_valid_string_raise_error_with_wrong_parameter_type(self):
        parameter = 1
        with self.assertRaises(ValidationError):
            is_valid_string(parameter)

    def test_is_valid_string_raise_error_with_none_parameter(self):
        wrong_parameter = None
        with self.assertRaises(ValidationError):
            is_valid_string(wrong_parameter)

    # IS_VALID_AUTHOR
    def test_is_valid_author(self):
        parameter = "Jean Martin"
        self.assertTrue(is_valid_author(parameter))

    def test_is_valid_author_raise_error_with_wrong_parameter_type(self):
        wrong_parameter = 1
        with self.assertRaises(ValidationError):
            is_valid_author(wrong_parameter)

    def test_is_valid_author_return_false_with_empty_string(self):
        empty_parameter = ""
        self.assertFalse(is_valid_author(empty_parameter))

    def test_is_valid_author_return_false_with_more_than_150_char(self):
        lenght_parameter = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis p"
        self.assertFalse(is_valid_author(lenght_parameter))

    def test_is_valid_question_return_false_with_more_than_200_char(self):
        lenght_parameter = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec qu"
        self.assertFalse(is_valid_question(lenght_parameter))


    def test_is_valid_date_return_false_with_empty_date(self):
        empty_parameter = ""
        self.assertFalse(is_valid_date(empty_parameter))

    def test_is_valid_date_return_false_with_wrong_parameter_type(self):
        empty_parameter = "salut toi"
        self.assertFalse(is_valid_date(empty_parameter))

"""
script devtest , print pour verifier ( toute les questions)
def (test_ + nom parlant + signature et courte)


"""
