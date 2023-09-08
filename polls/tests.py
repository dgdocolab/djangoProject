from datetime import datetime, timedelta
from django.test import TestCase
from django.core.exceptions import ValidationError
from polls.models import Question, Choice
from polls.utilities import is_valid_type_string, is_valid_author, create_question, is_valid_question, \
    is_valid_type_date, \
    compare_datetime_a_greater_than_datetime_b, generate_fixture_question_datas, create_choice


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


#
# def boucler_questions(create_boucle_question, n):
#     nombre = 0
#     while nombre < n:
#         create_boucle_question()
#         nombre += 1


# def create_choice(text):
#     if text is None or type(text) != type(text):
#         raise ValidationError(
#             "(choice) is not a text / is empty",
#         )
#     else:
#         return Choice.objects.create(choice_text=text)


class DevTest(TestCase):
    def test_joker(self):
        print(create_question("test", datetime.now().astimezone(), ""))


class QuestionTest(TestCase):
    pass


class ChoiceTest(TestCase):
    pass


class UtilitiesTest(TestCase):
    questions = {
        "1": "How are u",
        "2": "How old are u",
        "3": "What are u doing",
        "4": "What's ur favorite sports",
        "5": "What do you think about me",
        "6": "Where do you lives",
        "7": "What's ur name",
        "8": "When is ur birthday",
        "9": "What's the wether like ",
        "10": "What's ur favorite game"
    }

    authors = {
        "1": "Jean",
        "2": "Patrick",
        "3": "Laurent",
        "4": "Enzo",
    }

    choices = {
        "1": "I'm fine ",
        "2": "I'm tired",
        "3": "I'm mad",
        "4": "I'm 20",
        "5": "I'm 25",
        "6": "I'm 15",
        "7": "I'm playing videos games",
        "8": "I'm playing guitar",
        "9": "I'm sleeping right now",
        "10": "Judo",
        "11": "MMA",
        "12": "cool",
        "13": "amazing",
        "14": "paris",
        "15": "LA",
        "16": "Patrick",
        "17": "William",
        "18": "Ahmed",
        "19": "2001",
        "20": "1950",
        "21": "2008",
        "22": "good",
        "23": "hot",
        "24": "cold",
        "25": "Valorant",
        "26": "Smite",
        "27": "Hunt Showdown ",
    }

    # IS_VALID_STRING
    def test_is_valid_string(self):
        parameter = "hello"
        self.assertTrue(is_valid_type_string(parameter))

    # IS_VALID_STRING
    def test_is_valid_string_raise_error_with_wrong_parameter_type(self):
        parameter = 1
        with self.assertRaises(ValidationError):
            is_valid_type_string(parameter)

    # IS_VALID_STRING
    def test_is_valid_string_raise_error_with_none_parameter(self):
        wrong_parameter = None
        with self.assertRaises(ValidationError):
            is_valid_type_string(wrong_parameter)

    # IS_VALID_AUTHOR
    def test_is_valid_author(self):
        parameter = "Jean Martin"
        self.assertTrue(is_valid_author(parameter))

    # IS_VALID_AUTHOR
    def test_is_valid_author_raise_error_with_wrong_parameter_type(self):
        wrong_parameter = 1
        with self.assertRaises(ValidationError):
            is_valid_author(wrong_parameter)

    # IS_VALID_AUTHOR
    def test_is_valid_author_return_false_with_empty_string(self):
        empty_parameter = ""
        self.assertFalse(is_valid_author(empty_parameter))

    # IS_VALID_AUTHOR
    def test_is_valid_author_return_false_with_more_than_150_char(self):
        lenght_parameter = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis p"
        self.assertFalse(is_valid_author(lenght_parameter))

    # IS_VALID_QUESTION
    def test_is_valid_question_return_false_with_more_than_200_char(self):
        lenght_parameter = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec qu"
        self.assertFalse(is_valid_question(lenght_parameter))

    # IS_VALID_DATE
    def test_is_valid_date_return_false_with_wrong_parameter_type(self):
        parameter = "ehehe"
        self.assertFalse(is_valid_type_date(parameter))

    # IS_VALID_DATE
    def test_is_valid_date_return_true_with_right_parameter(self):
        parameter = datetime.now()
        self.assertTrue(is_valid_type_date(parameter))

    # COMPARE_DATETIME_A_GREATER_THAN_DATETIME_B
    def test_compare_datetime_a_greater_than_datetime_b_raise_error_with_wrong_parameter_type_1(self):
        wrong_parameter = "test"
        second_parameter = datetime.now()
        with self.assertRaises(ValidationError):
            compare_datetime_a_greater_than_datetime_b(wrong_parameter, second_parameter)

    # COMPARE_DATETIME_A_GREATER_THAN_DATETIME_B
    def test_compare_datetime_a_greater_than_datetime_b_raise_error_with_wrong_parameter_type_2(self):
        first_parameter = datetime.now()
        wrong_parameter = "test"
        with self.assertRaises(ValidationError):
            compare_datetime_a_greater_than_datetime_b(first_parameter, wrong_parameter)

    # COMPARE_DATETIME_A_GREATER_THAN_DATETIME_B
    def test_compare_datetime_a_greater_than_datetime_b_return_true_with_a_greater_than_b(self):
        dta = datetime.now() + timedelta(days=2)
        dtb = datetime.now()
        self.assertTrue(compare_datetime_a_greater_than_datetime_b(dta, dtb))

    # COMPARE_DATETIME_A_GREATER_THAN_DATETIME_B
    def test_compare_datetime_a_greater_than_datetime_b_return_false_with_a_lower_than_b(self):
        dta = datetime.now() + timedelta(days=2)
        dtb = datetime.now()
        self.assertFalse(compare_datetime_a_greater_than_datetime_b(dtb, dta))

    # CREATE_QUESTION
    def test_create_question(self):
        text = self.questions["7"]
        datetime_b = datetime.now() - timedelta(days=2)
        author = self.authors["2"]
        self.assertTrue(create_question(text, datetime_b, author))

    # LOOP_QUESTION
    # def test_loop_question(self):
    #     parameter = "Votre question est ? "
    #     datetime_b = datetime.now() - timedelta(days=2)
    #     author = "Votre nom est ?  "
    #     self.assertTrue(loop_question(parameter, datetime_b, author))

    def test_questions(self):
        print(self.questions["8"], self.questions["1"])

    def test_create_choice(self):
        print(self.choices["9"])

    def test_joker(self):
        for question_datas in generate_fixture_question_datas(3, 3):
            question = create_question(question_datas["question_text"], question_datas['pub_date'],
                                       question_datas['author'])
            for choice in question_datas["choices"]:
                create_choice(choice["choice_text"], question.id)
        print(Question.objects.all().count())
        print(Choice.objects.all().count())


"""
script devtest , print pour verifier ( toute les questions)
def (test_ + nom parlant + signature et courte)
"""
