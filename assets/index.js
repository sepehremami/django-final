import config from './config.js';
import Cookies from 'js-cookie';
import jwt_decode from 'jwt-decode';
import axios from 'axios';

class DjangoClient {
  constructor(overrides) {
    this.config = {
      ...config,
      ...overrides,
    };
    this.apiClient = this.getApiClient(this.config);
  }

  getApiClient(config) {
    const initialConfig = {
      baseURL: `${config.apiURL}`,
    };
    const client = axios.create(initialConfig);
    client.interceptors.request.use(CookieInterceptor);
    return client;
  }

  getClientAddresses = () => {
    return new Promise((resolve, reject) => {
      this.apiClient.get('/user/api/address/')
        .then(response => {
          resolve(response.data)
        })
        .catch((error) => {
          console.log(error);
          reject(error)
        })
    })
  }

  setDefaultAddress(id) {
    console.log('hello')
    return new Promise((resolve, reject) => {
      this.apiClient.patch(`/user/api/address/${id}/`, { "is_default": "true" })
        .then(response => {
          resolve(response.data)
        })
        .catch((error) => {
          console.log(error);
          reject(error)
        })
    })
  }

  getClientInfo() {
    const id = Cookies.get('id');
    return new Promise((resolve, reject) => {
      this.apiClient.get(`user/api/profile/${id}/`)
        .then(response => {
          resolve(response.data)
        })
        .catch((error) => {
          console.log(error);
          reject(error)
        })

    })
  }
}

function CookieInterceptor(config) {
  const headers = {};
  const authToken = Cookies.get('access');
  const decoded = jwt_decode(authToken);
  const id = decoded.id;
  Cookies.set('id', id)

  if (authToken) {
    if (isTokenExpired(decoded)) {
      console.log(decoded)

    }
    headers['Authorization'] = `Bearer ${authToken}`;
  }
  else {
    alert('Session expired! Please login again!');
  }
  config['headers'] = headers;
  return config;
};

function isTokenExpired(token) {
  const currentTime = Date.now() / 1000
  return token.exp < currentTime
}


const djangoClient = new DjangoClient(config);


// cart functionality


const imgs = document.querySelectorAll('.img-select a');
const imgBtns = [...imgs];
let imgId = 1;

imgBtns.forEach((imgItem) => {
  imgItem.addEventListener('click', (event) => {
    event.preventDefault();
    imgId = imgItem.dataset.id;
    slideImage();
  });
});

function slideImage() {
  const displayWidth = document.querySelector('.img-showcase img:first-child').clientWidth;

  document.querySelector('.img-showcase').style.transform = `translateX(${(imgId - 1) * displayWidth}px)`;
}

window.addEventListener('resize', slideImage);


const cartBtn = document.getElementById('cart-button')
if (cartBtn) {
  cartBtn.addEventListener('click', function (e) {
    e.preventDefault()
    const url = window.location.href;
    let productId = url.slice(-2, -1);
    console.log('p', productId)
    let shoppingCart = Cookies.get('shoppingCart');

    if (!shoppingCart) {
      const cart = `[{${productId} : ${quantity}}]`
      const cartJson = JSON.stringify(cart)
      console.log(cartJson)
      Cookies.set('shoppingCart', cartJson);
    } else {
      console.log(shoppingCart)
    }
    const cookie = Cookies.get('shoppingCart');
    const data = JSON.parse(cookie);
    console.log(data)

  });
}

function addToCart(itemName, itemPrice, itemQuantity) {
  // Get existing cart data from cookie or create empty array if none is found
  let cartData = JSON.parse(Cookies.get("cart") || "[]");

  // Check if item already exists in the shopping cart
  let existingItemIndex = -1;
  for (let i = 0; i < cartData.length; i++) {
    if (cartData[i].name === itemName) {
      existingItemIndex = i;
      break;
    }
  }

  // If item exists, update its quantity. Otherwise, add it to the shopping cart.
  if (existingItemIndex >= 0) {
    cartData[existingItemIndex].quantity += parseInt(itemQuantity);
    showNotification(`${itemQuantity} ${itemName}(s) have been added to your shopping-cart.`);

  } else {
    let newItem = { product_id: itemName, price: parseFloat(itemPrice), quantity: parseInt(itemQuantity) };
    cartData.push(newItem);
    showNotification(`${itemName} has been added to your shopping-cart.`);
  }

  Cookies.set("cart", JSON.stringify(cartData));
}

function showNotification(message) {
  const notificationElm = document.getElementById('notification');
  notificationElm.style.display = 'block'
  notificationElm.classList.add('notification');
  notificationElm.textContent = message;

  setTimeout(() => {
    notificationElm.style.display = 'none'
  }, 3000)

}


const makeOrder = document.getElementById('order-btn');
if (makeOrder) {
  makeOrder.addEventListener('click', function (e) {
    e.preventDefault();
    const cartData = Cookies.get('cart');
    const cartJSON = JSON.parse(cartData);
    const cartjava = JSON.stringify(cartJSON)
    console.log(cartjava)
    console.log(cartJSON)
    djangoClient.apiClient.post('cart/api/make-order/', cartJSON)
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
  })
}


export default DjangoClient;


