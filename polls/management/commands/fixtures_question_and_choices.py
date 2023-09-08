from django.core.management import BaseCommand

from polls.scrpits import script_fixtures_questions_and_choices


class Command(BaseCommand):
    def handle(self, *args, **options):
        script_fixtures_questions_and_choices()
