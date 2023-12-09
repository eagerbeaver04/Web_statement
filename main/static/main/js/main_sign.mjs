import { setFormValue, resetForm, disableButton, submitSignForm, setRepeatPasswordStatus, validateEmail, validatePassword, matchPassword }
    from "./utils.mjs"

const first_name_id = 'first_name'
const last_name_id = 'last_name'
const password_id = 'password'

const password_repeat_id = "password-repeat"

const sign_in_link_id = 'sign_in_link'
const sign_up_link_id = 'sign_up_link'
const sign_up_form_id = 'sign_up_form'
const sign_in_form_id = 'sign_in_form'
var current_form = sign_in_form_id;

const first_name = document.getElementById(first_name_id);
first_name.oninput = (e) => setFormValue(first_name_id, e.target)

const second_name = document.getElementById(last_name_id);
second_name.oninput = (e) => setFormValue(last_name_id, e.target)

const emails = document.querySelectorAll("input[type=email]");

emails.forEach(email => {
    email.oninput = (e) => setFormValue(email.id, e.target, validateEmail);
});

const passwords = document.querySelectorAll("input[type=password]:not([id=password-repeat])");
const password = document.getElementById(password_id);
const password_repeat = document.getElementById(password_repeat_id);

passwords.forEach(password => {
    password.oninput = (e) => {
        setFormValue(password_id, e.target, validatePassword);
        if (current_form === sign_up_form_id)
            setRepeatPasswordStatus(e.target, password_repeat);
    }

});


password_repeat.oninput = (e) => {
    setFormValue(password_repeat_id, e.target, matchPassword);
    if (current_form === sign_up_form_id)
        setRepeatPasswordStatus(password, password_repeat);
};

export const changeWindow = (form_id) => {
    document.getElementById(current_form).style.display = "none"
    current_form = form_id;
    resetForm(current_form);
    document.getElementById(current_form).style.display = "";
}

const switch_to_sign_in = document.getElementById(sign_in_link_id);
switch_to_sign_in.onclick = (e) => { changeWindow(sign_in_form_id); }

const switch_to_sign_up = document.getElementById(sign_up_link_id);
switch_to_sign_up.onclick = (e) => {
    changeWindow(sign_up_form_id);
}



document.addEventListener('input', function (e) {
    if (e.target.tagName == "INPUT")
        disableButton(current_form);
})

