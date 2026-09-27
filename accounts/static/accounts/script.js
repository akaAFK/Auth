const tabs = document.querySelectorAll(".tab");
const forms = document.querySelectorAll(".auth-form");


tabs.forEach(tab => {

    tab.addEventListener("click", () => {
        const target = tab.dataset.tab;
        tabs.forEach(item => {
            item.classList.remove("active");
        });

        forms.forEach(form => {
            form.classList.remove("active");
        });

        tab.classList.add("active");

        document
            .getElementById(target)
            .classList.add("active");

    });

});