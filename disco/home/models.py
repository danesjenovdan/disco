from django.db import models

from wagtail import blocks
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock


### PAGES

class HomePage(Page):
    parent_page_types = []


class NewHomePage(Page):
    # hero section
    subtitle = models.TextField()
    intro_text = models.TextField()
    # speakers
    # exposed_speakers = models.StreamField([
    #     speaker = 
    # ])
    show_tba = models.BooleanField(default=False)
    # scholarship
    scholarship_title = models.TextField()
    scholarship_description = models.TextField()
    # about
    about = StreamField([
        ("paragraph", blocks.StructBlock([
            ("text", blocks.TextBlock(required=False)),
            ("image", ImageChooserBlock(required=False)),
            ("positioning", blocks.ChoiceBlock(choices=[
                ("image-left", "Image on the left, text on the right"),
                ("image-right", "Text on the left, image on the right"),
                ("no-image", "Only text"),
                ("just-image", "Only image"),
            ], default="no-image"))
        ]))
    ], use_json_field=True)
    # organized by
    organized_by_title = models.TextField()
    organized_by_text = models.TextField()
    # sponsored by
    sponsored_by = StreamField([
        ("logo", blocks.StructBlock([
            ("image", ImageChooserBlock()),
            ("link", blocks.URLBlock(required=False))
        ]))
    ], use_json_field=True, blank=True, null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("subtitle"),
                FieldPanel("intro_text"),
            ],
            heading="Hero"
        ),
        MultiFieldPanel(
            [
                # FieldPanel("exposed_speakers"),
                FieldPanel("show_tba"),
            ],
            heading="Speakers"
        ),
        MultiFieldPanel(
            [
                FieldPanel("scholarship_title"),
                FieldPanel("scholarship_description"),
            ],
            heading="Scholarship"
        ),
        MultiFieldPanel(
            [
                FieldPanel("about"),
            ],
            heading="About"
        ),
        MultiFieldPanel(
            [
                FieldPanel("organized_by_title"),
                FieldPanel("organized_by_text"),
            ],
            heading="Organized by"
        ),
        MultiFieldPanel(
            [
                FieldPanel("sponsored_by"),
            ],
            heading="Sponsored by"
        ),
    ]


class SpeakersAndProgrammePage(Page):
    pass


class LocationPage(Page):
    description = RichTextField()
    accommodation_description = models.TextField()
    accommodation_options = StreamField([
        ("accommodation", blocks.StructBlock([
            ("title", blocks.TextBlock()),
            ("short_description", blocks.TextBlock()),
            ("image", ImageChooserBlock()),
            ("link", blocks.URLBlock()),
        ]))
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("accommodation_description"),
        FieldPanel("accommodation_options"),
    ]


class NewsListPage(Page):
    pass


class NewsPage(Page):
    short_description = models.TextField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    body = RichTextField()
    # speaker

    content_panels = Page.content_panels + [
        FieldPanel("short_description"),
        FieldPanel("image"),
        FieldPanel("body"),
    ]


class RegistrationPage(Page):
    show_scholarship_option = models.BooleanField(default=True)

    content_panels = Page.content_panels + [
        FieldPanel("show_scholarship_option"),
    ]


class ThankYouForRegistrationPage(Page):
    pass


class NewsletterSignupPage(Page):
    pass

