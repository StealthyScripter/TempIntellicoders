const submit_button_form = document.getElementById("submit_form_button");
const headline_exprot_button = document.getElementById("export-button");

headline_exprot_button.addEventListener("click", function () {
    console.log("working");
    submit_button_form.click();

});
