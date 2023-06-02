
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

    console.log(otpCode, otpCode.value)
    console.log('entering')

    axios.post(`${config.apiURL}/user/api/token/obtain/`, formData)
        .then(function (response) {
            console.log(response)
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

document.getElementById("registerButton").addEventListener("click", (e) => {
    e.preventDefault();
    var formData = new FormData();
    const username = document.getElementById('username');
    const password = document.getElementById('password');
    formData.append('username', username.value);
    formData.append('password', password.value);

    const config1 = {
        headers: {
            "AUTHORIZATION": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkZW50aWZpZXIiOiJub2xpbWF4IiwiZXhwIjoxNjg1MjE0OTcwLCJpYXQiOjE2ODUyMTEzNzAuMzY5MDY3LCJ1c2VybmFtZSI6Im5vbGltYXgiLCJwaG9uZV9udW1iZXIiOm51bGx9.0fDcSGUJz6k_NPbWt6m72wxtwpvBg3OZHMU7m8le6Pg"
        }
    };

    axios.post(
        'http://127.0.0.1:8000/user/token/obtain/', formData
    )
        .then(function (response) {
            console.log(response);

        })
        .catch(function (error) {
            console.log(error);
        });

    let form2 = document.forms[1];
    form.submit();
    // console.log(form)
    console.log('salam')
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