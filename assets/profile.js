import DjangoClient from './index';
import config from './config';



const djangoClient = new DjangoClient(config);
djangoClient.getClientAddresses().then(response => {
    console.log(response)
    const addressList = document.getElementById('address-holder'); // Get reference to DOM element where we will append our created elements.
    let count = 0;
    response.forEach(address => {
        if (count < 3) {

            const { id, city, zip_code, is_default } = address;

            let div = document.createElement('div');
            div.classList.add("d-flex")
            div.classList.add("m-2")
            div.style.justifyContent = 'space-between'


            let p1 = document.createElement('p');
            p1.textContent = `شهر: ${city}`;
            p1.id = 'flexbox-item'

            let p2 = document.createElement('p');
            p2.textContent = `کدپستی: ${zip_code}`;
            p2.id = 'flexbox-item'


            let p3 = document.createElement('p');
            p3.textContent = `پیش‌فرض: ${is_default ? 'Yes' : 'No'}`

            let label = document.createElement("label");
            label.setAttribute("for", id);
            label.id = 'flexbox-item';
            let input = document.createElement("input");
            input.type = "checkbox";
            input.id = id;
            if (is_default) { /* If this is default record then check it*/
                input.checked = true;
            }

            label.appendChild(input);
            div.appendChild(p1);
            div.appendChild(p2);
            div.appendChild(label)

            addressList.appendChild(div);
            count++;


        }
    })
    if (response.length > 3) {
        const showMoreBtnDiv = document.createElement("div");
        showMoreBtnDiv.style.textAlign= 'center'
        const showMoreBtn = document.createElement("button");
        showMoreBtn.innerText = "بیشتر";
        showMoreBtn.style['margin'] = '2px'
        showMoreBtn.style['padding'] = '2px'

        showMoreBtn.onclick = () => {
            for (let i = count; i < response.length; i++) {
                const { id, city, zip_code, is_default } = response[i];

                let div = document.createElement('div');
                div.classList.add("d-flex")
                div.style.justifyContent = 'space-between'
                div.classList.add("m-2")

                let p1 = document.createElement('p');
                p1.textContent = `شهر: ${city}`;
                p1.id = 'flexbox-item'

                let p2 = document.createElement('p');
                p2.textContent = `کدپستی: ${zip_code}`;
                p2.id = 'flexbox-item'

                let p3 = document.createElement('p');
                p3.textContent = `پیش‌فرض: ${is_default ? 'Yes' : 'No'}`

                let label = document.createElement("label")
                label.id = 'flexbox-item'
                let input = document.createElement("input")
                label.setAttribute("for", id);
                input.type = "checkbox";
                input.id = id;
                if (is_default) {
                    input.checked = true;
                }

                label.appendChild(input);

                div.appendChild(p1);
                div.appendChild(p2);
                // div.appendChild(p3);
                div.appendChild(label);
                addressList.appendChild(div);

            }
            showMoreBtnDiv.style.display = "none";

        }
        showMoreBtnDiv.appendChild(showMoreBtn);
        addressList.after(showMoreBtnDiv);
    }
});


const container = document.querySelector('#address-holder');
const loadingMessage = document.querySelector('#loading-message');
const successAlert = document.querySelector('#success-alert');

container.addEventListener('click', (event) => {
    // Check if clicked element is a checkbox input field
    if (event.target.tagName === 'INPUT' && event.target.type === 'checkbox') {
        const clickedCheckbox = event.target;
        // Get all other checkbox inputs in this container and uncheck them
        container.querySelectorAll('input[type="checkbox"]').forEach((otherCheckbox) => {
            if (otherCheckbox !== clickedCheckbox) { // Skip current checkbox
                otherCheckbox.checked = false;
            }

            const parent = clickedCheckbox.parentNode;
            const selfid = parent.htmlFor;
            console.log(parent)
            console.log(selfid)

            console.log(selfid)

            loadingMessage.style = 'block';

            djangoClient.setDefaultAddress(selfid)
                .then(response => {

                    successAlert.style.display = 'block';

                    setTimeout(() => {
                        successAlert.style.display = 'none';
                    }, 3000);
                })
                .catch(error => {
                    console.log(error);
                })
                .finally(() => loadingMessage.style.display = 'none')


        });
    }
});