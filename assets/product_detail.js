let incrBtn = document.querySelectorAll('.increase');
let decrBtn = document.querySelectorAll('.decrease');
let inputCarts = document.querySelectorAll('.product-detail-cart-count')

incrBtn.forEach(function(Btn, i){
  Btn.addEventListener('click', function(e){

    e.preventDefault()
    let value = parseInt(inputCarts[i].value);
    value += 1
    inputCarts[i].value = value
  })
})

decrBtn.forEach(function(Btn, i){
    Btn.addEventListener('click', function(e){
        e.preventDefault()
        
        innerValue = parseInt(inputCarts[i].value);
        console.log(innerValue)
        if (innerValue != 0){
            let value = parseInt(inputCarts[i].value);
            value -= 1
            inputCarts[i].value = value
        }
    })
})

import DjangoClient from './index';
import config from './config';

const djangoClient = new DjangoClient(config)

const AddToCartBtn = document.querySelectorAll('.add-to-cart');
AddToCartBtn.forEach((cartBtn, i)=> {
  cartBtn.addEventListener('click', (e)=> {
    e.preventDefault()
    var formData = new FormData();

    var productId = cartBtn.getAttribute('data-subproduct-id');
    var count = inputCarts[i].value;
    console.log('helo')
    formData.append('product', productId)
    formData.append('count', count)
    djangoClient.apiClient.post(config.apiURL+'/cart/api/order-item/', formData)
    .then(res=> { console.log(res)})
    .catch(err => {console.log(err)})
  })
})
