import axios from 'axios';
import Cookies from 'js-cookie';
import DjangoClient from '.';
import config from './config';



const prices = document.querySelectorAll('#price-of-subpro');
console.log(prices)

let total = 0;
prices.forEach(function (price) {
  const priceValue = parseInt(price.textContent.match(/\d+/)[0]);

  total += priceValue;
});


const counts = document.querySelectorAll('input#form1');
console.log(counts)

counts.forEach(function (count) {
  const countValue = count.value;

  console.log(countValue);
});


const djangoClient = new DjangoClient(config);


let incrBtn = document.querySelectorAll('.increase');
let decrBtn = document.querySelectorAll('.decrease');
let inputCarts = document.querySelectorAll('.product-detail-cart-count')

incrBtn.forEach(function (Btn, i) {
  Btn.addEventListener('click', function (e) {

    e.preventDefault()
    let value = parseInt(inputCarts[i].value);
    value += 1
    inputCarts[i].value = value
  })
})

decrBtn.forEach(function (Btn, i) {
  Btn.addEventListener('click', function (e) {
    e.preventDefault()

    var innerValue = parseInt(inputCarts[i].value);
    console.log(innerValue)
    if (innerValue != 0) {
      let value = parseInt(inputCarts[i].value);
      value -= 1
      inputCarts[i].value = value
    }
  })
})


document.getElementById('buy').addEventListener('click', (e) => {
  e.preventDefault();
  inputCarts.forEach((inputCart, i) => {

    let formData = new FormData();
    let productId = inputCart.getAttribute('data-subproduct-id');
    let count = inputCart.value;
    let orderID = inputCart.getAttribute('data-order-item');
    console.log(orderID)
    const userId = Cookies.get('id')


    if (count != 0) {
      formData.append('product', productId)
      formData.append('count', count)
      djangoClient.apiClient.patch(config.apiURL + `/cart/api/order-item/${orderID}/`, formData)
        .then(res => {
          console.log(res)
          window.location.assign(`${config.apiURL}/user/order/${userId}`)

        })
        .catch(err => {
          console.log(err)

        })
    }
  })
})

function reduceByPercent(x, percent, maximum) {
  console.log(x, percent, maximum)
  let maxReduction = x * (percent/100);
  console.log(maxReduction)
  let reduction = Math.min(maxReduction, maximum);
  console.log(reduction)
  return x - reduction;
}

document.getElementById('discount').addEventListener('click', (e)=> {
  e.preventDefault();
  const discountCode = document.getElementById('discount_code')
  const price = document.getElementById('totalPrice');

  djangoClient.apiClient.get(`${config.apiURL}/cart/api/discount-validate/${discountCode.value}`)
  .then(res=> {
    console.log(res)
    const {discount_value, maximum_discount_amount} = res.data;
    const disPrice = reduceByPercent(price.innerText, discount_value, maximum_discount_amount);
    console.log(disPrice)
    price.style.textDecoration = 'line-through';
    let span = document.createElement('span')
    span.innerText = disPrice;
    price.parentElement.append(span)

  })
  .catch(err => {
    console.log(err)
  })
  

})