import datetime
from random import random

from django.core.exceptions import ValidationError

from polls.models import Question, Choice


############## CHECK TYPE ##############

def is_valid_type_int(int_to_test):
    """
    This return false if the parameter is not an int, or True.
    :param int_to_test:
    :return: Boolean
    """
    if isinstance(int_to_test, int):
        return True
    return False


def is_valid_type_string(string_to_test):
    """
    This return false if the parameter is not a string, or True.
    :param string_to_test:
    :return: Boolean
    """
    if isinstance(string_to_test, str):
        return True
    return False


def is_valid_type_date(date_to_test):
    """
    This function check the date parameter is not empty, and the type. Return false if not
    :param date_to_test:
    :return: Boolean
    """
    if isinstance(date_to_test, datetime.datetime):
        return True
    return False


############## VARIOUS CHECK ##############

def is_valid_author(author_to_test):
    """
    This function check the author parameter is a valid string and not empty or > 150. Return False if not.
    :param author_to_test:
    :return: Boolean
    """
    if is_valid_type_string(author_to_test):
        if 0 < len(author_to_test) < 150:
            return True
    return False


def is_valid_question(question_to_test):
    """
    This function check the question parameter is not empty and not > 200 char. Return False if not
    :param question_to_test:
    :return: Boolean
    """
    if 0 < len(question_to_test) < 150 and is_valid_type_string(question_to_test):
        return True
    return False



# COMPARISON FUNCTION

def compare_datetime_a_greater_than_datetime_b(datetime_a, datetime_b):
    if is_valid_type_date(datetime_a) and is_valid_type_date(datetime_b):
        return datetime_a > datetime_b
    raise ValidationError("Les dates doivent être valides")


############## MODEL FUNCTION ##############

def create_question(text, datetime_b, author=None):
    """
    This function create and return a question with a text, a date and an optional author.
    """
    # TODO : DAVID : add test.
    datetime_a = datetime.datetime.now()
    if is_valid_type_string(text) and 0 < len(text) < 200 and is_valid_type_date(
            datetime_b):
        if author is None:
            return Question.objects.create(question_text=text, pub_date=datetime_b)
        else:
            if is_valid_author(author):
                return Question.objects.create(question_text=text, pub_date=datetime_b, author=author)
            else:
                raise ValidationError("Author need to be a string")
    else:
        raise ValidationError("Question need to be a string / between 0 and 200 characters ")


def create_choice(text, question_id):
    # TODO : DAVID : creer un is_valid_choice.
    if is_valid_type_string(text):
        return Choice.objects.create(choice_text=text, question_id=question_id)
    raise ValidationError("The choice need to be a string")


############## DATAS FUNCTION ##############

def generate_fixture_author():
    author_list = [
        "Jean",
        "Louis",
        "Max",
        "Denis"
    ]
    rand = int(random() * 100)
    if rand < 26:
        return author_list[0]
    elif rand < 51:
        return author_list[1]
    elif rand < 76:
        return author_list[2]
    else:
        return author_list[3]


def generate_fixture_choice_datas(quantity):
    choices_list = []
    for i in range(0, quantity):
        choice_text = "c" + str((i + 1))
        choices_list.append({
            "choice_text": choice_text
        })
    return choices_list


def generate_fixture_question_datas(question_quantity, choice_quantity):
    if is_valid_type_int(question_quantity) and is_valid_type_int(choice_quantity):
        question_list = []
        for i in range(0, question_quantity):
            question_text = "q" + str((i + 1))
            pub_date = datetime.datetime.now().astimezone() + datetime.timedelta(hours=i + 1)
            author = generate_fixture_author()
            choices_list = generate_fixture_choice_datas(choice_quantity)
            question_list.append({
                "question_text": question_text,
                "pub_date": pub_date,
                "author": author,
                "choices": choices_list
            })
        return question_list
    raise ValidationError("The type needs to be an integer")