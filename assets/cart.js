import axios from 'axios';
import Cookies from 'js-cookie';
import DjangoClient from '.';
import config from './config';



function getCart() {
  let cartData = JSON.parse(Cookies.get("cart") || "[]");
  return cartData;
}


function displayCart(cart) {
  // Clear previous items before iterating over new ones.
  document.getElementById("shopping-cart").innerHTML = "";

  // Iterate over items in the shopping cart and display them on the page.
  for (let i = 0; i < cart.length; i++) {
    let itemHTML = `
        <div class="card cart-item">
          <span class="item item-name">نام کالا: ${cart[i].name}</span>
          <span class="item item-quantity">تعداد: ${cart[i].quantity}x </span>
          <span class="item item-price">قیمت کل: ${(cart[i].price * cart[i].quantity).toFixed(2)}</span>
          <button class="btn btn-danger delete-cart-item" data-index="${i}">حذف</button>
          <button class="btn btn-danger remove-item-btn" data-index="${i}">کاهش تعداد</button>
        </div>`;
    document.getElementById("shopping-cart").innerHTML += itemHTML;
  }

  // Add event listeners to all Delete buttons with 'delete-cart-item' class.
  const deleteButtons = document.querySelectorAll('.delete-cart-item');
  for (let j = 0; j < deleteButtons.length; j++) {
    deleteButtons[j].addEventListener('click', function (event) {
      const indexToDelete = parseInt(this.getAttribute('data-index'));
      console.log(`Deleting Item at Index: ${indexToDelete}`);

      // Remove corresponding object from cartData array
      const cartData = getCart();
      cartData.splice(indexToDelete, 1);
      Cookies.set('cart', JSON.stringify(cartData));

      // Update the view by re-displaying the shopping cart with updated data
      displayCart(getCart());
    });
  }
  const removeButtons = document.querySelectorAll('.remove-item-btn');
  for (let j = 0; j < removeButtons.length; j++) {
    removeButtons[j].addEventListener('click', function (event) {
      const indexToRemove = parseInt(this.getAttribute('data-index'));
      console.log(`Removing Item at Index: ${indexToRemove}`);

      // Decrement quantity of corresponding object in cartData array by 1 (if not already 0)
      const cartData = getCart();
      if (cartData[indexToRemove].quantity > 1) {
        cartData[indexToRemove].quantity--;
        Cookies.set('cart', JSON.stringify(cartData));

        // Update view by re-displaying shopping cart with updated data
        displayCart(getCart());
      }
    });
  }
}




// Call displayCart() once to show initial shopping cart contents.


displayCart(getCart());


const prices = document.querySelectorAll('#price-of-subpro');
console.log(prices)  

let total = 0;
prices.forEach(function(price) {
    // Extract number from text content of each p tag using regex
    const priceValue = parseInt(price.textContent.match(/\d+/)[0]);
    
    // Add extracted number to total
    total += priceValue;
});


const totalPrice = document.getElementById('total-price');
console.log(totalPrice)
totalPrice.innerText = total
console.log(total);

const counts  = document.querySelectorAll('input#form1');
console.log(counts)

counts.forEach(function(count) {
  // Extract number from text content of each p tag using regex
  const countValue = count.value;
  
  // Add extracted number to total
  console.log(countValue);
});


const djangoClient = new DjangoClient(config);

document.getElementById('buy').addEventListener('click', (e) => {
  e.preventDefault();
  const id = document.getElementById('order_id');
  djangoClient.apiClient.patch(config.apiURL + `/cart/api/order/${id.value}/`, {'order_status':1})
  .then(res=> {
    window.location.assign(config.apiURL+'/user/profile/')
  })
  .catch(err=>{
    console.log(err)
  })
  
})
