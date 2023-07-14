from django.db import models

from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)

from wagtail.admin.panels import (
    FieldPanel,
)

@register_setting(icon="cog")
class MetaSettings(BaseGenericSetting):
    show_scholarship_option = models.BooleanField(default=True)
    
    panels = [
        FieldPanel("show_scholarship_option")
    ]

    class Meta:
        verbose_name = "Scholarship settings"