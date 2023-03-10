from django.contrib import admin

from todolist.goals.models import GoalCategory, GoalComment, Goal


class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'updated')
    search_fields = ('title', 'user')


class GoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'description', 'status', 'priority', 'due_date', 'created', 'updated')
    search_fields = ('title', 'user')


class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ('goal', 'user', 'text', 'created', 'updated')
    search_fields = ('title', 'user')


admin.site.register(GoalCategory, GoalCategoryAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(GoalComment, GoalCommentAdmin)
