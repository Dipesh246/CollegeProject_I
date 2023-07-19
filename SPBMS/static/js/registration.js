const firstNameInput = document.getElementById('first-name');
const lastNameInput = document.getElementById('last-name');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirm-password');
const passwordRequirements = document.getElementById('password-requirements');
const registerButton = document.getElementById('register-button');



firstNameInput.addEventListener('input', updateUsername);
lastNameInput.addEventListener('input', updateUsername);
passwordInput.addEventListener('input', updatePasswordRequirements);
confirmPasswordInput.addEventListener('input', checkPasswordMatch);

        
function updateUsername() {
    const firstName = firstNameInput.value.trim().toLowerCase();
    const lastName = lastNameInput.value.trim().toLowerCase();
    const generatedUsername = `${firstName}.${lastName}`;

           
    checkUniqueUsername(generatedUsername)
        .then(isUnique => {
            if (isUnique) {
                usernameInput.value = generatedUsername;
            } else {
                const randomNumber = Math.floor(Math.random() * 1000);
                const uniqueUsername = `${generatedUsername}${randomNumber}`;
                usernameInput.value = uniqueUsername;
            }
        });
    }
           
function checkUniqueUsername(username) {
    return fetch(`/checkunique/?username=${username}`)
        .then(response => response.json())
        .then(data => data.is_unique);
}
function checkPasswordMatch() {
    const password = passwordInput.value;
    const confirmPassword = confirmPasswordInput.value;

    const uppercaseRegex = /[A-Z]/;
    const lowercaseRegex = /[a-z]/;
    const numberRegex = /[0-9]/;

    if (password === confirmPassword) {
        
        confirmPasswordInput.setCustomValidity('');
        registerButton.disabled = false;
    }
    else{
        confirmPasswordInput.setCustomValidity('Passwords do not match');
        registerButton.disabled = true;
    }
    confirmPasswordInput.reportValidity();
}
function updatePasswordRequirements() {
    const password = passwordInput.value;
    const uppercaseRegex = /[A-Z]/;
    const lowercaseRegex = /[a-z]/;
    const numberRegex = /[0-9]/;

    if (password.length === 0) {
        passwordRequirements.textContent = '';
        registerButton.disabled = false;
    } else if (
        uppercaseRegex.test(password) &&
        lowercaseRegex.test(password) &&
        numberRegex.test(password)
    ) {
        passwordRequirements.textContent = 'Password meets the requirements.';
        passwordRequirements.style.color = 'green';
        registerButton.disabled = false;
    } else {
        passwordRequirements.textContent = 'Password must contain at least one capital letter, one character, and one number.';
        passwordRequirements.style.color = 'red';
        registerButton.disabled = true;
    }
}



updateUsername();