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

import DjangoClient from './index';
import config from './config';
import Swal from 'sweetalert2';

const djangoClient = new DjangoClient(config)
let successMessage = document.getElementById('success');
const AddToCartBtn = document.querySelector('#cartButton');
AddToCartBtn.addEventListener('click', (e) => {
  e.preventDefault()

  // let loadingMessage = document.getElementById('')

  inputCarts.forEach((inputCarts, i) => {

    var formData = new FormData();
    var productId = inputCarts.getAttribute('data-subproduct-id');
    var count = inputCarts.value;
    
    if (count != 0 ){
    formData.append('product', productId)
    formData.append('count', count)
    djangoClient.apiClient.post(config.apiURL + '/cart/api/order-item/', formData)
      .then(res => { 
        Swal.fire({
          title: 'موفق!',
          text: 'به سبد خرید اضافه شد! ',
          icon: 'success',
          confirmButtonColor: '#3085d6',
          confirmButtonText: 'خب'
        }).then((result) => {
            // Do something after the user clicks on the confirmation button (if needed).
        });

       })
      .catch(err => { 

        Swal.fire({
          title: '',
          text: 'لطفا برای اضافه به سبد خرید وارد شوید',
          icon: 'info',
          showCancelButton: false,
          confirmButtonColor: '#3085d6',
          confirmButtonText: 'وارد شوید!',
        }).then((result) => {
            if (result.isConfirmed) {
                window.location.href = `${config.apiURL}/accounts/login/`;
            }
        });
      })
    }
  })

})
