from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
    readonly_fields = ["created_at", "updated_at"]


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    readonly_fields = ["created_at", "updated_at"]


admin.site.register(Question, QuestionAdmin)
