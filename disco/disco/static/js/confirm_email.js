(async () => {
  document.addEventListener("DOMContentLoaded", async () => {
    const searchParams = new URLSearchParams(window.location.search);
    const email = searchParams.get("email");
    const token = searchParams.get("token");

    if (!email || !token) {
      window.location.replace("/");
    }

    const fullsizeContent = document.querySelector(".fullsize-content");
    const loaderContainer = document.querySelector(".loader-container");
    const thankYou = document.querySelector(".thank-you");

    const segment_id = 29;

    const apiSearchParams = new URLSearchParams({ email, token });
    const url = `https://podpri.lb.djnd.si/api/segments/${segment_id}/contact/?${apiSearchParams}`;

    try {
      const response = await fetch(url, { method: "POST" });
      if (response.ok) {
        loaderContainer.classList.add("d-none");
        thankYou.classList.remove("d-none");
        return;
      }

      loaderContainer.classList.add("d-none");
      fullsizeContent.insertAdjacentHTML(
        "afterbegin",
        `<div class="alert alert-primary" role="alert">
           Something went wrong.<br>
           Please try again later.
         </div>`
      );
    } catch (error) {
      console.log(error);
      loaderContainer.classList.add("d-none");
      fullsizeContent.insertAdjacentHTML(
        "afterbegin",
        `<div class="alert alert-primary" role="alert">
           Something went wrong.<br>
           Please try again later.
         </div>`
      );
    }
  });
})();
