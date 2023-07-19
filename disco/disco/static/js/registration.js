(async () => {
    const scholarship_countries = ["AL", "CZ", "SK", "HU", "HR", "BA", "MK", "RS", "BG", "RO", "SI", "XK"];

    // fields
    const registration_type_individual = document.querySelector("#id_register_type_0");
    const registration_type_organisation = document.querySelector("#id_register_type_1");
    const country_field = document.querySelector("#id_individual-country");

    // form sections
    const individual_form = document.querySelector("#individual_form");
    const organisation_form = document.querySelector("#organisation_form");
    const scholarship_form = document.querySelector("#scholarship-form-section");
    const scholarship_yes_form = document.querySelector("#scholarship-yes-form-section");
    const register_fee_form = document.querySelector("#registration-fee-form-section");
    const participants_form = document.querySelector("#participants-form");

    // buttons
    const add_participants_button = document.querySelector("#add-participant");

    if (registration_type_individual && registration_type_organisation && individual_form && organisation_form) {

        registration_type_individual.addEventListener("change", (event) => {
            if (event.target.checked) {
                individual_form.classList.remove("d-none")
                organisation_form.classList.add("d-none");
            }
        });

        registration_type_organisation.addEventListener("change", (event) => {
            if (event.target.checked) {
                organisation_form.classList.remove("d-none")
                individual_form.classList.add("d-none");
            }
        });
    }

    if (country_field) {
        if (scholarship_countries.includes(country_field.value)) {
            scholarship_form.classList.remove("d-none");
        }

        country_field.addEventListener("change", (event) => {
            console.log("Chosen country", event.target.value)

            if (scholarship_countries.includes(event.target.value)) {
                console.log("Scholarship yes!")
                scholarship_form.classList.remove("d-none");
            } else {
                console.log("Schilarhsip no!")
                scholarship_form.classList.add("d-none");
            }
        });
    }

    if (scholarship_form) {

        const scholarship_field = document.querySelector("#id_individual-applied_for_scholarship");
        scholarship_field.addEventListener("change", (event) => {
            console.log("scholarship chosen", event.target.checked);
            const scholarship_chosen = event.target.checked;
            if (scholarship_chosen) {
                // hide registration fee
                register_fee_form.classList.add("d-none");
                scholarship_yes_form.classList.remove("d-none");
            } else {
                // show registration fee
                register_fee_form.classList.remove("d-none");
                scholarship_yes_form.classList.add("d-none");
            }
        });
    }

    let forms_num = 0;
    let totalForms = document.querySelector("#id_form-TOTAL_FORMS");

    add_participants_button.addEventListener("click", (event) => {
        const existing_form = document.querySelectorAll(".participant")[0];

        if (existing_form.classList.contains("d-none")) {
            existing_form.classList.remove("d-none");
            return;
        }

        let new_form = existing_form.cloneNode(true);
        let formRegex = RegExp(`form-(\\d){1}-`,'g');

        forms_num++;
        new_form.innerHTML = new_form.innerHTML.replace(formRegex, `form-${forms_num}-`);
        participants_form.insertBefore(new_form, add_participants_button);
        totalForms.setAttribute('value', `${forms_num+1}`);
    })

  })();
