from polls.utilities import generate_fixture_question_datas, create_question, create_choice


def script_fixtures_questions_and_choices():
    for question_datas in generate_fixture_question_datas(10, 3):
        question = create_question(question_datas["question_text"], question_datas['pub_date'],
                                   question_datas['author'])
        for choice in question_datas["choices"]:
            create_choice(choice["choice_text"], question.id)
