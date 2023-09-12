from django.contrib import admin
from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from admin_extra_buttons.utils import HttpResponseRedirectToReferrer
from django.core.management import call_command
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .models import Choice, Question


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'votes',)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
    readonly_fields = ["created_at", "updated_at"]


class QuestionAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    inlines = [ChoiceInline]
    readonly_fields = ["created_at", "updated_at"]
    model = Question
    list_display = ("question_text", "pub_date", "author",)
    list_filter = ("author",)

    # @button(permission=lambda request, obj: request.user.is_superuser,
    #         html_attrs={'style': 'background-color:var(--button-bg)'},
    #         label='Reset All Votes',
    #         change_form=True
    #         )
    # def reset_votes(self, request):
    #     # votes = []
    #     # qs = Question.objects.all()
    #     # for choice in qs:
    #     #     for vote in choice:
    #     #         votes.append(vote.votes)
    #     # votes.clear()
    #     # print("hello")
    #     return HttpResponseRedirectToReferrer(request)

    @button(html_attrs={'style': 'background-color:#DC6C6C;color:white'})
    def confirm(self, request):
        def _action(request):
            qs = Question.objects.all()
            for question in qs:
                choices = list(question.choice_set.all())
                for choice in choices:
                    choice.votes = 0
                    choice.save()

        return confirm_action(self, request, _action, "Confirm reset",
                              "Successfully executed", )


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
