import datetime

from django.core.exceptions import ValidationError

from polls.models import Question


def is_valid_string(string_to_test):
    """
    This function raise an error if the parameter is not a string, or True.
    :param string_to_test:
    :return: Boolean
    """
    if not isinstance(string_to_test, str):
        raise ValidationError("string_to_test must be a string. [not a string : " + str(type(string_to_test)) + "]")
    return True


def is_valid_author(author_to_test):
    """
    This function check the author parameter is a valid string and not empty or > 150. Return False if not.
    :param author_to_test:
    :return: Boolean
    """
    if is_valid_string(author_to_test):
        if 0 < len(author_to_test) < 150:
            return True
    return False


def is_valid_question(question_to_test):
    """
    This function check the question parameter is not empty and not > 200 char. Return False if not
    :param question_to_test:
    :return: Boolean
    """
    if 0 < len(question_to_test) < 150 and isinstance(question_to_test, str):
        return True
    else:
        return False


def is_valid_date(date_to_test):
    """
    This function check the date parameter is not empty, and the type. Return false if not
    :param date_to_test:
    :return: Boolean
    """
    if isinstance(date_to_test, datetime.datetime):
        return True
    return False


# def compare_datetime_a_greater_than_datetime_b(datetime_a, datetime_b):
#     if is_valid_date(datetime_a):
#         if is_valid_date(datetime_b):
#             if datetime_a > datetime_b:
#                 return True
#             return False
#         return False
#     return False


def create_question(text, date, author=None):
    """
    This function create and return a question with a text, a date and an optional author.
    """
    # TODO : DAVID : add test. ok
    if is_valid_string(text) and 0 < len(text) < 200 and is_valid_date(date):
        if author is None:
            return Question.objects.create(question_text=text, pub_date=date)
        else:
            if is_valid_author(author):
                return Question.objects.create(question_text=text, pub_date=date, author=author)
            else:
                raise ValidationError("Author need to be a string")
    else:
        raise ValidationError("Question need to be a string / between 0 and 200 characters ")
