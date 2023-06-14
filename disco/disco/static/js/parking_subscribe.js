(async () => {
  const form = document.querySelector("#subscribe-form");
  const email = form.querySelector('input[type="email"]');
  const check = form.querySelector("#subscribe-check");
  const submit = form.querySelector('button[type="submit"]');

  const segment_id = 29;

  form.addEventListener("submit", async (event) => {
    if (email.value && check.checked) {
      email.disabled = true;
      check.disabled = true;
      submit.disabled = true;

      try {
        const response = await fetch(
          "https://podpri.lb.djnd.si/api/subscribe/",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              email: email.value,
              segment_id,
            }),
          }
        );
        if (response.ok) {
          const data = await response.json();
          if (data.msg == "mail sent") {
            form.insertAdjacentHTML(
              "afterbegin",
              `<div class="alert alert-primary" role="alert">
                Thank you!<br>
                We sent you an email with a confirmation link.
              </div>`
            );
            return;
          }
        }
        form.insertAdjacentHTML(
          "afterbegin",
          `<div class="alert alert-primary" role="alert">
             Something went wrong.<br>
             Please try again later.
           </div>`
        );
      } catch (error) {
        console.error(error);
        form.insertAdjacentHTML(
          "afterbegin",
          `<div class="alert alert-primary" role="alert">
             Something went wrong.<br>
             Please try again later.
           </div>`
        );
      }
    }
  });
})();
