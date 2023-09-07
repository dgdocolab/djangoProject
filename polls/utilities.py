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
    if 0 < len(question_to_test) < 150:
        return True
    return False


def is_valid_date(date_to_test):
    """
    This function check the date parameter is not empty, and the type. Return false if not
    :param date_to_test:
    :return:
    """
    if not isinstance(date_to_test, datetime.date):
        if 0 < len(date_to_test):
            return True
    # raise ValidationError("date_to_test must be a datetime. [not a datetime] : " + str(type(date_to_test)) + "]")
    return False


def create_question(text, date, author=None):
    # TODO : DAVID : check date with type, author and text with length.
    # TODO : DAVID : add test.
    # TODO : DAVID : Add a description.
    if is_valid_string(text):
        if author is not None and is_valid_author(author):
            return Question.objects.create(question_text=text, pub_date=date, author=author)
        elif author is not None and not is_valid_author(author):
            raise ValidationError('The author parameter is empty.')
        else:
            return Question.objects.create(question_text=text, pub_date=date)
    raise ValidationError("Some parameter may be wrong.")
