import config from './config.js';
import Cookies from 'js-cookie';
import jwt_decode from 'jwt-decode';

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
  console.log(authToken)
  const decoded = jwt_decode(authToken);
  Cookies.set('id', decoded.id);
  if (authToken) {
    headers['Authorization'] = `Bearer ${authToken}`;
  }
  else {
    alert('Session expired! Please login again!');
  }
  config['headers'] = headers;
  return config;
};
const a = true
// cart functionality
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
      console.log(this);
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

document.querySelectorAll('.add-to-cart').forEach(button => {
  button.addEventListener('click', async () => {
    const subproductId = button.dataset.subproductId;
    const response = await fetch(config.apiURL+'/api/add-to-cart/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ subproduct: subproductId, quantity: 1 }),
    });

    if (response.ok) {
      // Handle successful addition to cart, e.g., show a message or update cart count
    } else {
      // Handle error, e.g., show an error message
    }
  });
});


export default DjangoClient;


