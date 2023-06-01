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
            div.classList.add("col")

            let p1 = document.createElement('p');
            p1.textContent = `شهر: ${city}`;

            let p2 = document.createElement('p');
            p2.textContent = `کدپستی: ${zip_code}`;

            let p3 = document.createElement('p');
            p3.textContent = `پیش‌فرض: ${is_default ? 'Yes' : 'No'}`

            let label = document.createElement("label");
            label.setAttribute("for", id);
            let input = document.createElement("input");
            input.type = "checkbox";
            input.id = id;
            if (is_default) { /* If this is default record then check it*/
                input.checked = true;
            }
            label.appendChild(input);
            /* Add text node next to the checkbox */
            const labelText = document.createTextNode(`پیش‌فرض`);
            label.appendChild(labelText);
            div.appendChild(p1);
            div.appendChild(p2);
            div.appendChild(label)


            addressList.appendChild(div);
            count++;


        }
    })
    if (response.length > 3) {
        const showMoreBtnDiv = document.createElement("div");

        const showMoreBtn = document.createElement("button");
        showMoreBtn.innerText = "Show More";

        showMoreBtn.onclick = () => {
            for (let i = count; i < response.length; i++) {
                const { id, city, zip_code, is_default } = response[i];
                let div = document.createElement('div');
                div.classList.add("col")
                let p1 = document.createElement('p');
                p1.textContent = `شهر: ${city}`;
                let p2 = document.createElement('p');
                p2.textContent = `کدپستی: ${zip_code}`;
                let p3 = document.createElement('p');
                p3.textContent = `پیش‌فرض: ${is_default ? 'Yes' : 'No'}`
                // Append all created elements to parent div element
                let label = document.createElement("label")
                label.setAttribute("for", id);
                let input = document.createElement("input")
                input.type = "checkbox";
                input.id = id;
                if (is_default) {
                    input.checked = true;
                }
                label.appendChild(input);
                const labelText = document.createTextNode(`پیش‌فرض`);
                label.appendChild(labelText);

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


