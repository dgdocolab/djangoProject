from datetime import datetime, timedelta
from django.test import TestCase
from django.core.exceptions import ValidationError
from polls.models import Question, Choice
from polls.utilities import is_valid_string, is_valid_author, create_question, is_valid_question, is_valid_date, \
    compare_datetime_a_greater_than_datetime_b


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

    def test_is_valid_date_return_false_with_wrong_parameter_type(self):
        parameter = "ehehe"
        self.assertFalse(is_valid_date(parameter))

    def test_is_valid_date_return_true_with_right_parameter(self):
        parameter = datetime.now()
        self.assertTrue(is_valid_date(parameter))

    # COMPARE_DATETIME_A_GREATER_THAN_DATETIME_B
    def test_compare_datetime_a_greater_than_datetime_b_raise_error_with_wrong_parameter_type_1(self):
        wrong_parameter = "test"
        second_parameter = datetime.now()
        with self.assertRaises(ValidationError):
            compare_datetime_a_greater_than_datetime_b(wrong_parameter, second_parameter)

    def test_compare_datetime_a_greater_than_datetime_b_raise_error_with_wrong_parameter_type_2(self):
        first_parameter = datetime.now()
        wrong_parameter = "test"
        with self.assertRaises(ValidationError):
            compare_datetime_a_greater_than_datetime_b(first_parameter, wrong_parameter)

    def test_compare_datetime_a_greater_than_datetime_b_return_true_with_a_greater_than_b(self):
        dta = datetime.now() + timedelta(days=2)
        dtb = datetime.now()
        self.assertTrue(compare_datetime_a_greater_than_datetime_b(dta, dtb))

    def test_compare_datetime_a_greater_than_datetime_b_return_false_with_a_lower_than_b(self):
        dta = datetime.now() + timedelta(days=2)
        dtb = datetime.now()
        self.assertFalse(compare_datetime_a_greater_than_datetime_b(dtb, dta))

    def test_create_question(self):
        pass


"""
script devtest , print pour verifier ( toute les questions)
def (test_ + nom parlant + signature et courte)


"""
