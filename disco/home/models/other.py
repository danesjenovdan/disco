from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from django_countries.fields import CountryField

from home.mautic_api import MauticApi

mautic_api = MauticApi()


class ProgrammeDay(models.Model):
    title = models.TextField()
    location = models.TextField()
    location_url = models.URLField(blank=True)
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
            ("time", blocks.CharBlock(required=False)),
            ("panels_list", blocks.StreamBlock([
                ("panel", blocks.StructBlock([
                    ("text", blocks.RichTextBlock(required=False)),
                    ("speakers", blocks.ListBlock(blocks.StructBlock([
                        ("name", blocks.CharBlock(required=False)),
                        ("image", ImageChooserBlock(required=False)), 
                        ("link", blocks.PageChooserBlock(required=False)),
                        ("organisation", blocks.CharBlock(required=False)),
                        ("title", blocks.CharBlock(required=False)),
                        ("description", blocks.RichTextBlock(required=False))
                    ])))                    
                ]))
            ], use_json_field=True))
        ]))
    ], use_json_field=True, null=True, blank=True)

    def __str__(self):
        return self.title


class Registered(models.Model):
    registered_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    email = models.EmailField(
        unique=True,
        error_messages={'unique': "You have already registered for the conference using this email address. Please use an alternative address."}
    )
    organisation_name = models.TextField(blank=True)
    country = CountryField(blank_label="")
    has_paid = models.BooleanField(default=False)
    registration_fee = models.IntegerField(null=True, blank=True, choices=[
        (50, "€50 plus VAT (€54.75 total)"),
        (25, "€25 plus VAT or €27.38 in total (for those unable to afford the standard fee)"),
        (75, "€75 plus VAT or €82.13 in total (for those who want to support participants with subsidised fee)")
    ])
    mautic_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save_to_mautic(self, tags):
        print('skip save to mautic', settings.DEBUG)
        if not settings.DEBUG:
            response, response_status = mautic_api.createContact(email=self.email, tags=tags)
            if response_status == 200:
                self.mautic_id = response['contact']['id']
                self.save()
                mautic_api.addContactToASegment(segment_id=settings.REGISTRATION_SEGMENT, contact_id=self.mautic_id)


class Individual(Registered):
    applied_for_scholarship = models.BooleanField(default=False)
    previously_supported = models.TextField(blank=True)
    scholarship_motivation = models.TextField(blank=True)
    scholarship_granted = models.BooleanField(default=False)
    scholarship_denied = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__per_save_scholarship_granted = self.scholarship_granted
        self.__per_save_scholarship_denied = self.scholarship_denied
        self.__per_save_has_paid = self.has_paid

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.has_paid and not self.__per_save_has_paid:
            if not settings.DEBUG:
                mautic_api.addContactToASegment(segment_id=settings.REGISTERED_SEGMENT, contact_id=self.mautic_id)
                mautic_api.addContactToASegment(segment_id=settings.PAID_SEGMENT, contact_id=self.mautic_id)
            self.__per_save_has_paid = self.has_paid

        if self.scholarship_granted and not self.__per_save_scholarship_granted:
            if not settings.DEBUG:
                # mautic_api.addTagToContact(self.mautic_id, 'disco-scholarship-granted')
                mautic_api.createContact(email=self.email, tags=['disco-scholarship-granted'])
                mautic_api.addContactToASegment(segment_id=settings.SCHOLARSHIP_SEGMENT, contact_id=self.mautic_id)
            else:
                print('Adding tag to contact', self.mautic_id, 'disco-scholarship-granted')
            self.__per_save_scholarship_granted = self.scholarship_granted

        if self.scholarship_denied and not self.__per_save_scholarship_denied:
            if not settings.DEBUG:
                # mautic_api.addTagToContact(self.mautic_id, 'disco-scholarship-denied')
                mautic_api.createContact(email=self.email, tags=['disco-scholarship-denied'])
                mautic_api.addContactToASegment(segment_id=settings.SCHOLARSHIP_SEGMENT, contact_id=self.mautic_id)
            else:
                print('Adding tag to contact', self.mautic_id, 'disco-scholarship-denied')
            self.__per_save_scholarship_denied = self.scholarship_denied


class Organisation(Registered):
    address = models.TextField()
    vat_id = models.TextField(blank=True, null=True)
    vat_registered = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__per_save_has_paid = self.has_paid

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.has_paid and not self.__per_save_has_paid:
            mautic_api.addContactToASegment(segment_id=settings.PAID_SEGMENT, contact_id=self.mautic_id)
            for individual in self.individuals.all():
                individual.save_to_mautic_as_participant()
            self.__per_save_has_paid = self.has_paid

    def __str__(self):
        return self.organisation_name


class IndividualByOrganisation(models.Model):
    name = models.TextField()
    email = models.EmailField(null=True, blank=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name="individuals")
    mautic_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save_to_mautic_as_participant(self):
        response, response_status = mautic_api.createContact(
            email=self.email,
            tags=['disco-group-participant']
        )
        if response_status == 200:
            self.mautic_id = response['contact']['id']
            self.save()
            if not settings.DEBUG:
                mautic_api.addContactToASegment(segment_id=settings.REGISTERED_SEGMENT, contact_id=self.mautic_id)


class RegisteredSpeaker(models.Model):
    name = models.TextField()
    affiliation = models.TextField()
    email = models.EmailField()
    country = CountryField(blank_label="")
    project = models.TextField()
    project_relevancy = models.TextField()
    project_benefit = models.TextField()
    travel_subsidy = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# signals

@receiver(post_save, sender=Individual)
def after_individual_save(sender, instance, created, **kwargs):
    if created:
        if instance.applied_for_scholarship:
            instance.save_to_mautic(['disco-scolarship-request'])
        else:
            instance.save_to_mautic(['disco-paid-request'])



@receiver(post_save, sender=Organisation)
def after_group_save(sender, instance, created, **kwargs):
    # create empty municipality for user
    if created:
        instance.save_to_mautic(['disco-group-paid-request'])
