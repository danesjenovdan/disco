from django.db import models

from wagtail import blocks
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock


### MODELS

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
    ], use_json_field=True, blank=True, max_num=3)

    def __str__(self):
        return self.name


class ProgrammeDay(models.Model):
    title = models.TextField()
    location = models.TextField()
    available_for = models.TextField()
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    description = models.TextField()
    date = models.DateField()
    timeslots = StreamField([
        ("timeslot", blocks.StructBlock([
            ("time", blocks.CharBlock()),
            ("panels_list", blocks.StreamBlock([
                ("panel", blocks.StructBlock([
                    ("name", blocks.CharBlock()),
                    ("speaker_page", blocks.PageChooserBlock(page_type="home.NewsPage", required=False)),
                    ("description", blocks.TextBlock(required=False)),
                ]))
            ], use_json_field=True))
        ]))
    ], use_json_field=True)

    def __str__(self):
        return self.title
    

def get_speakers():
    return [(speaker.id, speaker.name) for speaker in Speaker.objects.all()]


### PAGES

class NewsListPage(Page):

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context["news"] = NewsPage.objects.live()

        return context


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


class HomePage(Page):
    parent_page_types = []


class NewHomePage(Page):
    # hero section
    subtitle = models.TextField()
    intro_text = models.TextField()
    # speakers
    exposed_speakers = StreamField([
        ("speaker", blocks.ChoiceBlock(choices=get_speakers()))
    ], use_json_field=True, null=True, blank=True)
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
                FieldPanel("exposed_speakers"),
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

        context["exposed_news"] = NewsPage.objects.live()
        context["programme"] = ProgrammeDay.objects.all()
        context["speakers"] = Speaker.objects.filter(id__in=[speaker.value for speaker in self.exposed_speakers])

        return context


class SpeakersAndProgrammePage(Page):

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context["programme"] = ProgrammeDay.objects.all()
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


class RegistrationPage(Page):
    show_scholarship_option = models.BooleanField(default=True)

    content_panels = Page.content_panels + [
        FieldPanel("show_scholarship_option"),
    ]


class ThankYouForRegistrationPage(Page):
    pass


class NewsletterSignupPage(Page):
    pass

