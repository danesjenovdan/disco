from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.forms import formset_factory


from .forms import IndividualForm, OrganisationForm, IndividualByOrganisationForm
from .models import Individual, Organisation, IndividualByOrganisation


class ConfirmEmailView(TemplateView):
    template_name = "home/confirm_email_view.html"


class RegistrationSuccessfulView(TemplateView):
    template_name = "home/thank_you_for_registration_page.html"


class RegistrationView(TemplateView):
    template_name = "home/registration_view.html"

    def get(self, request, *args, **kwargs):
        individual_form = IndividualForm(prefix="individual")
        organisation_form = OrganisationForm(prefix="organisation")

        IndividualByOrganisationFormSet = formset_factory(IndividualByOrganisationForm, extra=1)
        formset = IndividualByOrganisationFormSet()
        
        return render(request, self.template_name, {
            "individual_form": individual_form,
            "organisation_form": organisation_form,
            "formset": formset
        })
    
    def post(self, request):
        individual_form = IndividualForm(request.POST, prefix="individual")
        organisation_form = OrganisationForm(request.POST, prefix="organisation")

        IndividualByOrganisationFormSet = formset_factory(IndividualByOrganisationForm)
        participants_formset = IndividualByOrganisationFormSet(request.POST)

        print("NEW REGISTRATION")

        # registration as individual
        if individual_form.is_valid():
            print("Individual form is valid")

            name = individual_form.cleaned_data["name"]
            email = individual_form.cleaned_data["email"]
            organisation_name = individual_form.cleaned_data["organisation_name"]
            country = individual_form.cleaned_data["country"]
            registration_fee = individual_form.cleaned_data["registration_fee"]
            applied_for_scholarship = individual_form.cleaned_data["applied_for_scholarship"]
            previously_supported = individual_form.cleaned_data["previously_supported"]
            scholarship_motivation = individual_form.cleaned_data["scholarship_motivation"]

            individual = Individual(
                name=name,
                email=email,
                country=country,
                registration_fee=registration_fee,
                organisation_name=organisation_name,
                applied_for_scholarship=applied_for_scholarship,
                previously_supported=previously_supported,
                scholarship_motivation=scholarship_motivation
            )

            individual.save()
            print("Successfuly created individual: ", individual)

            # TODO: subscribe to newsletter maybe
            newsletter = individual_form.cleaned_data["newsletter"]
            if newsletter:
                print("Subscribe to newsletter")

            return redirect("thank-you-for-registration")
        
        # organisation as individual
        elif organisation_form.is_valid():
            print("organisation form is valid")

            organisation_name = organisation_form.cleaned_data["organisation_name"]
            name = organisation_form.cleaned_data["name"]
            email = organisation_form.cleaned_data["email"]
            address = organisation_form.cleaned_data["address"]
            vat_id = organisation_form.cleaned_data["vat_id"]
            vat_registered = organisation_form.cleaned_data["vat_registered"]
            country = organisation_form.cleaned_data["country"]
            registration_fee = organisation_form.cleaned_data["registration_fee"]
            also_attending = organisation_form.cleaned_data["also_attending"]

            organisation = Organisation(
                organisation_name=organisation_name,
                name=name,
                email=email,
                address=address,
                vat_id=vat_id,
                vat_registered=vat_registered,
                country=country,
                registration_fee=registration_fee,
            )

            organisation.save()

            # save participants
            if participants_formset.is_valid():
                for participant in participants_formset.cleaned_data:
                    print(participant)
                    if participant.get("name") and participant.get("email"):
                        individual = IndividualByOrganisation(
                            name=participant["name"],
                            email=participant["email"],
                            organisation=organisation
                        )
                        individual.save()
            else:
                print("Participants not valid")

            if also_attending:
                individual = IndividualByOrganisation(
                    name=name,
                    email=email,
                    organisation=organisation
                )
                individual.save()

            print("Successfuly created organisation", organisation)

            # TODO: subscribe to newsletter maybe
            newsletter = organisation_form.cleaned_data["newsletter"]
            if newsletter:
                print("Subscribe to newsletter")

            return redirect("thank-you-for-registration")
        
        else:
            print("No form is valid")

            if "individual-form" in request.POST:
                submitted_form = "individual"
            else: 
                submitted_form = "organisation"

            return render(request, self.template_name, {
                "individual_form": individual_form,
                "organisation_form": organisation_form,
                "submitted_form": submitted_form
            })
