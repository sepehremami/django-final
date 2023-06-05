import Cookies from "js-cookie";
import jwt_decode from "jwt-decode";
import config from "./config";


const login = document.getElementById('login');
const routes = {
    "loggedIn": "/user/profile/",
    "notLoggedIn": "/user/login/"
}

const authCookie = Cookies.get('access');
if (authCookie) {
    const decoded = jwt_decode(authCookie)
    const expire = (decoded.exp * 1000 ) -Date.now();
    console.log(expire)

    if (decoded.exp < Date.now() / 1000) {
        Cookies.remove('access'); // Delete expired token immediately
        window.location.href = config.apiURL + notLoggedIn;
        
    } else  {
        setTimeout( ()=> {
            Cookies.remove('access')
            window.location.href = config.apiURL + notLoggedIn
        }, 5000 )
        login.href = config.apiURL + routes.loggedIn
    }

} else {
    login.href = config.apiURL + routes.notLoggedIn
}
