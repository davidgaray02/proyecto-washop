// script.ts

document.addEventListener("DOMContentLoaded", () => {
  const body = document.querySelector('body') as HTMLBodyElement,
    sidebar = body.querySelector('nav') as HTMLElement,
    toggle = body.querySelector(".toggle") as HTMLElement,
    searchBtn = body.querySelector(".search-box") as HTMLElement,
    modeSwitch = body.querySelector(".toggle-switch") as HTMLElement,
    modeText = body.querySelector(".mode-text") as HTMLElement;

  toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
  });

  searchBtn.addEventListener("click", () => {
    sidebar.classList.remove("close");
  });

  modeSwitch.addEventListener("click", () => {
    body.classList.toggle("dark");

    if (body.classList.contains("dark")) {
      modeText.innerText = "Light mode";
    } else {
      modeText.innerText = "Dark mode";
    }
  });
});
