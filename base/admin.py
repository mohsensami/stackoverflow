from django.contrib import admin
from .models import Question, Topic


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'topic')
    prepopulated_fields = {'slug' : ('name',)}


admin.site.register(Topic)
admin.site.register(Question, QuestionAdmin)
