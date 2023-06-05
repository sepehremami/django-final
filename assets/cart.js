import Cookies from 'js-cookie';


window.onload = function () {
    let cart = getCart();
    displayCart(cart);
}


function getCart() {
    let cartData = JSON.parse(Cookies.get("cart") || "[]");
    return cartData;
}

function displayCart(cart) {
    // Iterate over items in the shopping cart and display them on the page.
    for (let i = 0; i < cart.length; i++) {
        let itemHTML = `
        <div class="card cart-item">
          <span class="item item-name">نام کالا: ${cart[i].name}</span>
          <span class="item item-quantity">تعداد: ${cart[i].quantity}x </span>
          <span class="item item-price">قیمت کل: ${(cart[i].price * cart[i].quantity).toFixed(2)}</span>
        </div>`;
        document.getElementById("shopping-cart").innerHTML += itemHTML;
    }
}


document.getElementById('order-btn').addEventListener('click', function(e){
    e.preventDefault();
})