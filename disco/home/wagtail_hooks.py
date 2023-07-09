from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Speaker, ProgrammeDay


class SpeakerAdmin(ModelAdmin):
    model = Speaker
    menu_icon = "pilcrow"
    menu_order = 200
    add_to_admin_menu = True
    # list_display = ('title', 'author')
    # list_filter = ('author',)
    # search_fields = ('title', 'author')


class ProgrammeDayAdmin(ModelAdmin):
    model = ProgrammeDay
    menu_icon = "pilcrow"
    menu_order = 200
    add_to_admin_menu = True


modeladmin_register(SpeakerAdmin)
modeladmin_register(ProgrammeDayAdmin)
