(() => {
  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".spinning-banner").forEach((banner) => {
      const content = banner.querySelector(".spinning-content");
      if (!content) {
        return;
      }

      let originalText = "";
      if (content.hasAttribute("original-text")) {
        originalText = content.getAttribute("original-text");
      } else {
        content.setAttribute("original-text", content.textContent);
        originalText = content.textContent;
      }
      originalText = originalText.trim() + "&nbsp;";

      const factor = Math.ceil(window.innerWidth / content.offsetWidth);
      content.innerHTML = originalText.repeat(factor);

      const clone = content.parentElement.cloneNode(true);
      clone.classList.add("spinning-clone");
      banner.appendChild(clone);
    });
  });
})();
