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
    privacy_policy_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    panels = [
        FieldPanel("show_scholarship_option"),
        FieldPanel("privacy_policy_page"),
    ]

    class Meta:
        verbose_name = "Global site settings"
