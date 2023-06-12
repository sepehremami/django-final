
import axios from 'axios';
import config from './config.js';
import Cookies from 'js-cookie';
import DjangoClient from './index.js';


const djangoClient = new DjangoClient(config);
document.getElementById("submitBtn").addEventListener("click", (e) => {
    e.preventDefault();
    var formData = new FormData();
    const username = document.getElementById('username');
    const password = document.getElementById('password');

    formData.append('username', username.value);
    formData.append('password', password.value);


    axios.post(`${config.apiURL}/user/api/token/obtain/`, formData)
        .then(function (response) {
            console.log(response)
            if (response.status === 200) {

                Cookies.set('access', response.data.token);
                console.log(this)
                djangoClient.apiClient.get(config.apiURL+'/user/login/')
                .then(res=> {console.log(res)})
                .catch(err=>{console.log(err)})

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

function toggleOTP(e){
    e.preventDefault();
    $('#logreg-forms .form-signin').toggle();
    $('#logreg-froms .form-otp').toggle();
}

$(() => {
    // Login Register Form
    $('#logreg-forms #forgot_pswd').click(toggleResetPswd);
    $('#logreg-forms #cancel_reset').click(toggleResetPswd);
    $('#logreg-forms #btn-signup').click(toggleSignUp);
    $('#logreg-forms #cancel_signup').click(toggleSignUp);
    $('#logreg-forms #otp-enter').click(toggleOTP)
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


const registerBtn = document.getElementById('registerButton');
registerBtn.addEventListener('click', function(e) {
    e.preventDefault();
    var formData = new FormData();

    const username = document.getElementById('user-email');
    const password = document.getElementById('user-pass');
    console.log(username)
    formData.append('username', username.value);
    formData.append('password', password.value);

    axios.post(config.apiURL + '/user/api/register/',  formData)
    .then(res => {
        console.log(res)
        if (res.status===201){
            window.location.assign(config.apiURL + '/accounts/login/')
        }
    })
    .catch ( err => {
        console.log(err)
    })
})