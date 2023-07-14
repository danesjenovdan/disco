from django.db import models
from django.shortcuts import render

from wagtail import blocks
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock

from .other import ProgrammeDay, Speaker


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
    speaker = models.ForeignKey(Speaker, null=True, blank=True, on_delete=models.SET_NULL, related_name="+")

    content_panels = Page.content_panels + [
        FieldPanel("short_description"),
        FieldPanel("speaker"),
        FieldPanel("image"),
        FieldPanel("body"),
    ]


class NewsListPage(Page):

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context["news"] = NewsPage.objects.live().child_of(self).order_by("-first_published_at")

        return context


class HomePage(Page):
    parent_page_types = []


class NewHomePage(Page):
    # hero section
    subtitle = models.TextField()
    intro_text = models.TextField()
    # speakers
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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context["programme"] = ProgrammeDay.objects.all().order_by("date")
        context["speakers"] = Speaker.objects.filter(exposed=True)

        try:
            news_list = NewsListPage.objects.first()
            exposed_news = NewsPage.objects.live().child_of(news_list).order_by("-first_published_at")[:4]
        except:
            news_list = None
            exposed_news = None

        try:
            speakers_and_programme_page = SpeakersAndProgrammePage.objects.first()
        except:
            speakers_and_programme_page = None

        try:
            location_page = LocationPage.objects.first()
        except:
            location_page = None
        
        context["news_list"] = news_list
        context["exposed_news"] = exposed_news
        context["speakers_and_programme_page"] = speakers_and_programme_page
        context["location_page"] = location_page

        return context


class SpeakersAndProgrammePage(Page):

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context["programme"] = ProgrammeDay.objects.all().order_by("date")
        context["speakers"] = Speaker.objects.all()

        return context


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


# class ThankYouForRegistrationPage(Page):
#     pass


class NewsletterSignupPage(Page):
    pass

