let profilDropdownList = document.querySelector(".profile-dropdown-list");
let btn = document.querySelector(".profile-dropdown-btn");

const toggle = () => profilDropdownList.classList.toggle('active');

window.addEventListener("click", function (e) {
    if (!btn.contains(e.target)) profilDropdownList.classList.remove("active");
});