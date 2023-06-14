import Cookies from "js-cookie";
import jwt_decode from "jwt-decode";
import config from "./config";


async function authToken() {
    const token = Cookies.get('access');
    const decoded = jwt_decode(token)
    return decoded
}


const login = document.getElementById('login');
const cartURL = document.getElementById('cart');
const shoppingCart = document.getElementById('shopping-cart');

const routes = {
    "loggedIn": "/user/profile/",
    "notLoggedIn": "/accounts/login/"
}

const authCookie = Cookies.get('access');
if (authCookie) {
    const decoded = jwt_decode(authCookie)
    const expire = (decoded.exp * 1000 ) - Date.now();
    console.log(expire)

    if (decoded.exp < Date.now() / 1000) {
        Cookies.remove('access'); // Delete expired token immediately
        
    } else  {
        setTimeout( ()=> {
            Cookies.remove('access')
        }, 500000 )

        login.href = config.apiURL + routes.loggedIn + decoded.id
        // cartURL.href = config.apiURL + '/cart/detail/' 
        console.log
    }

} else {
    login.href = config.apiURL + routes.notLoggedIn
}
