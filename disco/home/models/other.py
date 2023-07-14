from django.db import models
from wagtail import blocks
from wagtail.fields import StreamField


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


def get_speakers():
    try:
        return [(speaker.id, speaker.name) for speaker in Speaker.objects.all()]
    except:
        return []


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
    

class Registered(models.Model):
    registered_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    email = models.URLField()
    country = models.TextField(choices=[
        ("slovenia", "Slovenia"),
        ("italy", "Italy"),
        ("croatia", "Croatia")
    ])
    registration_fee = models.IntegerField(null=True, blank=True)


class Individual(Registered):
    applied_for_scholarship = models.BooleanField(default=False)
    previously_supported = models.TextField(blank=True)
    scholarship_motivation = models.TextField(blank=True)
    has_paid = models.BooleanField(default=False)
    scholarship_granted = models.BooleanField(default=False)
    scholarship_denied = models.BooleanField(default=False)


class Organisation(Registered):
    address = models.TextField()
    vat_id = models.TextField()
    vat_registered = models.BooleanField(default=False)
    has_paid = models.BooleanField(default=False)


class IndividualByOrganisation(models.Model):
    name = models.TextField()
    email = models.URLField()
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name="+")