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
    let id = Cookies.get('id')
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


const a = true
if (a) {
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
      const value = document.getElementById('cart-value');
      let quantity = value.value;
      console.log(quantity);
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
    let newItem = { name: itemName, price: parseFloat(itemPrice), quantity: parseInt(itemQuantity) };
    cartData.push(newItem);
    showNotification(`${itemName} has been added to your shopping-cart.`);
  }

  // Store updated shopping car data back into cookie 
  Cookies.set("cart", JSON.stringify(cartData));
}

function showNotification(message) {
  // Create notification element and append it somewhere on page where user can see it.
  const notificationElm = document.getElementById('notification');
  notificationElm.style.display = 'block'
  notificationElm.classList.add('notification');
  notificationElm.textContent = message;

  // document.body.appendChild(notificationElm);

  setTimeout(() => {
    // Remove notification after some time
    // document.body.removeChild(notificationElm)
    notificationElm.style.display = 'none'
  }, 3000)

}

document.querySelectorAll('.add-to-cart').forEach(button => {
  button.addEventListener('click', async (e) => {

    const subproductId = button.dataset.subproductId;
    const subproductPrice = button.dataset.subproductPrice;
    const body = { order: 1, product: subproductId, count: 1 }
    addToCart(subproductId, subproductPrice, 1);
  })
});




function getCart() {
  let cartData = JSON.parse(getCookie("cart") || "[]");
  return cartData;
}

function displayCart(cart) {
  // Iterate over items in the shopping cart and display them on the page.
  for (let i = 0; i < cart.length; i++) {
    let itemHTML = `
      <div class="cart-item">
        <span class="item-name">${cart[i].name}</span>
        <span class="item-quantity">${cart[i].quantity} x </span>
        <span class="item-price">$${(cart[i].price * cart[i].quantity).toFixed(2)}</span>
      </div>`;
    document.getElementById("shopping-cart").innerHTML += itemHTML;
  }
}


function saveCartToDatabase() {
  // Retrieve saved shopping-cart data from cookies
  let cartData = JSON.parse(getCookie("cart") || "[]");

  // Send POST request to server with updated cart data, then remove cookie if successful.
  axios.post('/cart/add-to-cart', { items: cartData })
    .then(response => {
      console.log('Successfully saved shopping cart:', response.data);
      deleteCookie('cart');
    })
    .catch(error => {
      console.error('Error while saving shopping cart:', error.response.data);
    });
}

const makeOrder = document.getElementById('order-btn');
if (makeOrder) {
  makeOrder.addEventListener('click', function (e) {
    e.preventDefault();
    console.log('man')
    djangoClient.apiClient.get('/order')


  })
}
export default DjangoClient;


