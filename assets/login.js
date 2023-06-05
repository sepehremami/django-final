
import axios from 'axios';
import config from './config.js';
import Cookies from 'js-cookie';

document.getElementById("submitBtn").addEventListener("click", (e) => {
    e.preventDefault();
    var formData = new FormData();
    const username = document.getElementById('username');
    const password = document.getElementById('password');
    const otpCode = document.getElementById('otp');

    formData.append('username', username.value);
    formData.append('password', password.value);
    formData.append('otp_code', otpCode.value);


    axios.post(`${config.apiURL}/user/api/token/obtain/`, formData)
        .then(function (response) {
            if (response.status === 200) {

                Cookies.set('access', response.data.token);
                window.location.assign(config.apiURL + '/user/profile/')
            }
        })

        .catch(function (error) {
            console.log(error);
        });

    let token = document.cookie.split(';');

});



function toggleResetPswd(e) {
    e.preventDefault();
    $('#logreg-forms .form-signin').toggle() // display:block or none
    $('#logreg-forms .form-reset').toggle() // display:block or none
}

function toggleSignUp(e) {
    e.preventDefault();
    $('#logreg-forms .form-signin').toggle(); // display:block or none
    $('#logreg-forms .form-signup').toggle(); // display:block or none
}

$(() => {
    // Login Register Form
    $('#logreg-forms #forgot_pswd').click(toggleResetPswd);
    $('#logreg-forms #cancel_reset').click(toggleResetPswd);
    $('#logreg-forms #btn-signup').click(toggleSignUp);
    $('#logreg-forms #cancel_signup').click(toggleSignUp);
})

const unauth = document.getElementById("danger");




const otpButton = document.querySelector('.otp-button');
otpButton.addEventListener('click', (event) => {
    let timeLeft = 60;

    // Disable button and change text to show remaining time
    otpButton.disabled = true;

    const intervalId = setInterval(() => {
        if (timeLeft > 0) {
            otpButton.textContent = `ارسال مجدد (${timeLeft} ثانیه باقی‌مانده)`;
            timeLeft--;
        } else {
            clearInterval(intervalId);
            otpButton.textContent = 'ارسال';
            otpButton.disabled = false;
        }
    }, 1000); // Update every one second

    var formData = new FormData();
    const username = document.getElementById('username');
    const password = document.getElementById('password');
    formData.append('username', username.value);
    formData.append('password', password.value);

    axios.post(`${config.apiURL}/user/otp/`, formData)
        .then(response => {
            console.log(response)
        })
        .catch(error => {
            console.log(error)
        })

    event.preventDefault(); // Prevent default form submission
});