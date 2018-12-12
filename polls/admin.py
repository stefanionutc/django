from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('pub_date', 'question_text')
    search_fields = ['question_text']
    list_display = ('qid', 'pub_date', 'was_published_recently', 'older_than_30_days')
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


class PollsAdmin(admin.ModelAdmin):
    list_display = ('id', 'choice_text', 'votes', 'question_id')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, PollsAdmin)
