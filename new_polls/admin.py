from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['quest_text']}),
        ('Date information', {'fields': ['pub_data'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('quest_text', 'pub_data', 'was_published_recently')
    list_filter = ['pub_data']
    search_fields = ['quest_text']


admin.site.register(Question, QuestionAdmin)