var formValues = {}
var formValidation = {}
let strongPassword = new RegExp('((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{6,}))|((?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])(?=.{8,}))')
const emailRegExp = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/

export const validatePassword = (password) => {
    console.log("Password validation...")
    console.log(password);
    return strongPassword.test(password);
}

export const matchPassword = (repeatedPassword) => {
    return repeatedPassword == formValues.password;
}

export const validateEmail = (email) => {
    return String(email)
        .toLowerCase()
        .match(emailRegExp);
}

export const getValidationStatus = () => {
    return Object.values(formValidation).every((validationStatus) => !!validationStatus)
}

export const setFormValue = (valueKey, target, validator) => {
    formValues[valueKey] = target.value;
    if (validator) {
        formValidation[valueKey] = validator(target.value);
        target.classList.remove('valid', 'invalid');
        target.classList.add(formValidation[valueKey] ? 'valid' : 'invalid');
    }
}

export const setRepeatPasswordStatus = (target, repeat_target) => {
    if (repeat_target.value !== "" || target.value !== "") {
        repeat_target.classList.remove('valid', 'invalid');
        repeat_target.classList.add(target.value == repeat_target.value ? 'valid' : 'invalid');
        formValidation[target.id] = (target.value == repeat_target.value) && strongPassword.test(target.value);
        formValidation[repeat_target.id] = (target.value == repeat_target.value);
    }
}

export const setInputsInFormValues = (current_form) => {
    const inputs = document.querySelectorAll("#" + current_form + " input");
    inputs.forEach((input) => { formValues[input.id] = input.value; });
}

export const resetForm = (new_form) => {
    formValidation = {};
    formValues = {};
    setInputsInFormValues(new_form);
}

export const submitSignForm = (form_id) => {
    if (!getValidationStatus()) {
        console.log("FORM IS INCORRECT");
        return false;
    }
    resetForm(form_id);
    console.log("FORM IS FINE");
    console.log(formValues);
    return true;
}

/*const sign_buttons = document.querySelectorAll("button");
sign_buttons.forEach((button) => {
button.onclick = (e) => { e.preventDefault();
submitSignForm(current_form);
window.location.href = "/personal"
}
})

 */
export const disableButton = (form_id) => {
    const button = document.querySelector("#" + form_id + " button");
    const inputs = document.querySelectorAll("#" + form_id + " input");
    button.disabled = (!getValidationStatus() ||
        Object.values(inputs).some((elem) => !elem.value));
}

