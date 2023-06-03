import Cookies from "js-cookie";
import jwt_decode from "jwt-decode";
import config from "./config";
const login = document.getElementById('login');
console.log(login)
const routes = {
    "loggedIn": "/user/profile/",
    "notLoggedIn": "/user/login/"
}

const authCookie = Cookies.get('access');
console.log(authCookie)
if (authCookie) {

    const decoded = jwt_decode(authCookie)
    console.log(decoded)
    if (decoded) {
        console.log('hello')
        login.href = config.apiURL + routes.loggedIn
    }

} else {
    login.href = config.apiURL + '/user/login/'
}
