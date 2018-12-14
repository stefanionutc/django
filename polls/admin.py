from django.contrib import admin

from .models import Question, Choice, Person, Group, Membership, Blog, Author, Entry


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


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'shirt_size')


class GroupAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('id', 'name', 'get_members')

    def get_members(self, obj):
        return ", ".join([p.name for p in obj.members.all()])


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'person', 'group', 'date_joined', 'invite_reason')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')


class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'headline', 'pub_date', 'mod_date', 'get_authors')

    def get_authors(self, obj):
        return ', '.join([x.name for x in obj.authors.all()])


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, PollsAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Entry, EntryAdmin)
