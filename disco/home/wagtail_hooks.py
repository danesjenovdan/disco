from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Speaker, ProgrammeDay, Registered, Individual, Organisation, IndividualByOrganisation


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


class RegisteredAdmin(ModelAdmin):
    model = Registered
    menu_icon = "pilcrow"
    menu_order = 200
    add_to_admin_menu = True


class IndividualAdmin(ModelAdmin):
    model = Individual
    menu_icon = "pilcrow"
    menu_order = 200
    add_to_admin_menu = True


class OrganisationAdmin(ModelAdmin):
    model = Organisation
    menu_icon = "pilcrow"
    menu_order = 200
    add_to_admin_menu = True


class IndividualByOrganisationAdmin(ModelAdmin):
    model = IndividualByOrganisation
    menu_icon = "pilcrow"
    menu_order = 200
    add_to_admin_menu = True


modeladmin_register(SpeakerAdmin)
modeladmin_register(ProgrammeDayAdmin)
modeladmin_register(RegisteredAdmin)
modeladmin_register(IndividualAdmin)
modeladmin_register(OrganisationAdmin)
modeladmin_register(IndividualByOrganisationAdmin)
