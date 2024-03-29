from django.db import models
from django.shortcuts import render

from wagtail import blocks
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock

from .other import ProgrammeDay


class NewsPage(Page):
    short_description = models.TextField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    body = RichTextField(blank=True, null=True)
    gallery_images = StreamField([
        ("image", ImageChooserBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("short_description"),
        FieldPanel("image"),
        FieldPanel("body"),
        FieldPanel("gallery_images"),
    ]


class NewsListPage(Page):

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context["news"] = NewsPage.objects.live().child_of(self).order_by("-first_published_at")

        return context


class Speaker(models.Model):
    name = models.TextField()
    short_description = models.TextField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    social_media = StreamField([
        ("instagram", blocks.URLBlock()),
        ("mastodon", blocks.URLBlock()),
        ("twitter", blocks.URLBlock()),
        ("facebook", blocks.URLBlock()),
        ("website", blocks.URLBlock()),
        ("podcast", blocks.URLBlock()),
        ("linkedin", blocks.URLBlock()),
        ("youtube", blocks.URLBlock()),
        ("tiktok", blocks.URLBlock()),
    ], use_json_field=True, blank=True, max_num=3)
    exposed = models.BooleanField(default=False)
    news_page = models.ForeignKey(NewsPage, null=True, blank=True, on_delete=models.SET_NULL, related_name="+")

    def __str__(self):
        return self.name


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
    # register as speaker
    speaker_application_title = models.TextField(blank=True)
    speaker_application_description = models.TextField(blank=True)
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
    organized_by_text = RichTextField()
    # sponsored by
    sponsored_by = StreamField([
        ("logo", blocks.StructBlock([
            ("image", ImageChooserBlock()),
            ("link", blocks.URLBlock(required=False))
        ]))
    ], use_json_field=True, blank=True, null=True)
    # stream link
    stream_link = models.URLField(blank=True, null=True)
    stream_text = models.TextField(blank=True)

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
                FieldPanel("speaker_application_title"),
                FieldPanel("speaker_application_description"),
            ],
            heading="Application for speakers"
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
        MultiFieldPanel(
            [
                FieldPanel("stream_link"),
                FieldPanel("stream_text"),
            ],
            heading="Livestream"
        )   
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # context["programme"] = ProgrammeDay.objects.all().order_by("date")
        programme = ProgrammeDay.objects.all().order_by("date")
        for day in programme:
            programme_day_page = ProgrammeDayPage.objects.get(programme_day=day)
            day.programme_day_page = programme_day_page

        context["programme"] = programme
        context["speakers"] = Speaker.objects.filter(exposed=True).order_by('?')

        try:
            news_list = NewsListPage.objects.first()
            exposed_news = NewsPage.objects.live().child_of(news_list).order_by("-first_published_at")[:4]
        except:
            news_list = None
            exposed_news = None

        try:
            speakers_page = SpeakersPage.objects.first()
        except:
            speakers_page = None

        try:
            programme_page = ProgrammePage.objects.first()
        except:
            programme_page = None

        try:
            location_page = LocationPage.objects.first()
        except:
            location_page = None

        context["news_list"] = news_list
        context["exposed_news"] = exposed_news
        context["speakers_page"] = speakers_page
        context["programme_page"] = programme_page
        context["location_page"] = location_page

        return context


class SpeakersPage(Page):
    show_speakers = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel("show_speakers"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["speakers"] = Speaker.objects.all().order_by('?')
        return context
    

class ProgrammeDayPage(Page):
    programme_day = models.ForeignKey(ProgrammeDay, on_delete=models.PROTECT, related_name="+")

    content_panels = Page.content_panels + [
        FieldPanel("programme_day"),
    ]


class ProgrammePage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        programme = ProgrammeDay.objects.all().order_by("date")
        for day in programme:
            programme_day_page = ProgrammeDayPage.objects.get(programme_day=day)
            day.programme_day_page = programme_day_page

        context["programme"] = programme

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
