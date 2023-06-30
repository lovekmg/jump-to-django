from django.contrib import admin
from .models import Question
from .models import Answer

# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ["subject", "content"]
    list_display = ["subject", "create_date"]
    # fields = ['subject', 'create_date']   # 추가 및 변경 페이지에 적용할 필드
    # actions_on_top = False
    # actions_on_bottom = True
    date_hierarchy = "create_date"


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
