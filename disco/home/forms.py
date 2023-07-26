from django import forms
from django.core.exceptions import ValidationError
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField

from .models import Individual, Organisation, IndividualByOrganisation, RegisteredSpeaker


# class RegisterTypeForm(forms.Form):
#     register_type = forms.ChoiceField(widget=forms.RadioSelect(), choices=[
#         ("individual", "Individual"), 
#         ("organisation", "Organisation")
#     ], required=True)


class IndividualForm(forms.ModelForm):
    scholarship_checkbox = forms.BooleanField(required=False)
    newsletter = forms.BooleanField(required=False)

    class Meta:
        model = Individual
        fields = ["name", "email", "organisation_name", "country", "registration_fee", "applied_for_scholarship", "previously_supported", "scholarship_motivation"]
        widgets = {
            "name": forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.EmailInput(attrs={'class':'form-control'}),
            "organisation_name": forms.TextInput(attrs={'class':'form-control'}),
            "country": CountrySelectWidget(layout='{widget}', attrs={'class':'form-control'}), 
            "registration_fee": forms.RadioSelect(),
            "previously_supported": forms.Textarea(attrs={'class':'form-control'}),
            "scholarship_motivation": forms.Textarea(attrs={'class':'form-control'})
        }
    

    def clean(self):
        super().clean()

        applied_for_scholarship = self.cleaned_data.get("applied_for_scholarship")

        if applied_for_scholarship:
            previously_supported = self.cleaned_data.get("previously_supported")
            scholarship_motivation = self.cleaned_data.get("scholarship_motivation")
            scholarship_checkbox = self.cleaned_data.get("scholarship_checkbox")

            if not previously_supported:
                msg = "This field should not be empty."
                self.add_error("previously_supported", msg)
            
            if not scholarship_motivation:
                msg = "This field should not be empty."
                self.add_error("scholarship_motivation", msg)

            if not scholarship_checkbox:
                msg = "This checkbox is required."
                self.add_error("scholarship_checkbox", msg)

            self.cleaned_data["registration_fee"] = None
            
        else:
            self.cleaned_data["previously_supported"] = ""
            self.cleaned_data["scholarship_motivation"] = ""

        return self.cleaned_data


class OrganisationForm(forms.ModelForm):
    organisation_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    also_attending = forms.BooleanField(required=False)
    newsletter = forms.BooleanField(required=False)

    class Meta:
        model = Organisation
        fields = ["organisation_name", "name", "email", "address", "vat_id", "vat_registered", "country", "registration_fee"]
        widgets = {
            "name": forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.EmailInput(attrs={'class':'form-control'}),
            "address": forms.TextInput(attrs={'class':'form-control'}),
            "vat_id": forms.TextInput(attrs={'class':'form-control'}),
            "country": CountrySelectWidget(layout='{widget}', attrs={'class':'form-control'}), 
            "registration_fee": forms.RadioSelect()
        }


class IndividualByOrganisationForm(forms.ModelForm):
    
    class Meta:
        model = IndividualByOrganisation
        fields = ["name", "email"]
        widgets = {
            "name": forms.TextInput(attrs={'class':'form-control mb-3'}),
            "email": forms.EmailInput(attrs={'class':'form-control mb-5'})
        }
        labels = {
            "name": "Participant’s name and surname",
            "email": "Participant’s email address"
        }


class ApplySpeakerForm(forms.ModelForm):
    travel_subsidy = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix

    class Meta:
        model = RegisteredSpeaker
        exclude = []
        widgets = {
            "name": forms.TextInput(attrs={'class':'form-control'}),
            "affiliation": forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.EmailInput(attrs={'class':'form-control'}),
            "country": CountrySelectWidget(layout='{widget}', attrs={'class':'form-control'}),
            "project": forms.Textarea(attrs={'class':'form-control'}),
            "project_relevancy": forms.Textarea(attrs={'class':'form-control'}),
            "project_benefit": forms.Textarea(attrs={'class':'form-control'}),
        }
        labels = {
            "name": "Your name",
            "affiliation": "Your affiliation",
            "email": "Your email",
            "country": "What country are you travelling from?",
            "project": "Describe the project you want to present",
            "project_relevancy": "How is your project relevant to DISCO attendees?",
            "project_benefit": "How can your project benefit from the DISCO community?",
        }