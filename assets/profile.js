import DjangoClient from './index';
import config from './config';
import Cookies from 'js-cookie';
import axios from 'axios';
import { Profiler } from 'react';
import { cond } from 'lodash';
import Swal from 'sweetalert2';


window.onload = function () {
    djangoClient.apiClient.get(config.apiURL + '/user/login')
        .then(res => console.log('logged in. /profile.js'))
        .catch(err => console.log('error logging in. /profile.js'))

}
const djangoClient = new DjangoClient(config);

async function injectData(address) {
    // console.log(address)
    const { id, city, province, receiver, zip_code, is_default } = address;
    // console.log(is_default)

    const injects = `
    <th scope="col">${city}</th>
    <th scope="col">${province}</th>
    <th scope="col">${zip_code}</th>
    <th scope="col">${receiver}</th>

    <th scope="col">
        <input type="checkbox" data-address-id="${id}"  ${is_default ? 'checked' : ''}>
    </th>

    <th scope="col">
        <input class="delete selectAddress" type="checkbox" data-address-id="${id}">
    </th>
    `
    return injects
}


const container = document.querySelector('#addressTable');
const loadingMessage = document.querySelector('#loading-message');
const successAlert = document.querySelector('#success-alert');


container.addEventListener('click', async (event) => {
    if (event.target.tagName === 'INPUT' &&
        event.target.type === 'checkbox' &&
        !event.target.classList.contains('delete')) {


        const clickedCheckbox = event.target;
        const selfid = clickedCheckbox.dataset.addressId;

        container.querySelectorAll('input[type="checkbox"]').forEach((otherCheckbox) => {
            if (otherCheckbox !== clickedCheckbox) {
                otherCheckbox.checked = false;
            }
            const parent = clickedCheckbox.parentNode;

            loadingMessage.style = 'block';
        });

        djangoClient.setDefaultAddress(selfid)
            .then(response => {

                Swal.fire({
                    icon: 'success',

                    text: 'با موفقیت تغییر کرد'
                })
            })
            .catch(error => {
                console.log(error);
            })
            .finally(() => loadingMessage.style.display = 'none',
                // successAlert.style.display = 'none',
                loadingMessage.style.display = 'none')
    }
});



djangoClient.getClientAddresses()
    .then(response => {
        // console.log(response)
        const addressList = document.getElementById('address-holder'); // Get reference to DOM element where we will append our created elements.
        let count = 0;
        response.forEach(address => {
            if (count < 3) {
                const { id, city, province, receiver, zip_code, is_default } = address;

                // the new one
                const addressTable = document.getElementById('addressTable')
                const addressBody = document.getElementById('addressTableBody')

                const trEle = document.createElement('tr')
                trEle.id = `tr-${id}`
                injectData(address).then(
                    (value) => {
                        // console.log(value)
                        trEle.innerHTML = value
                    },
                    (error) => { console.log(error) }
                )
                // console.log(injectDataSon)
                addressBody.appendChild(trEle)

                // end of the new
                count++;

            }
        })
        if (response.length > 3) {
            const showMoreBtnDiv = document.createElement("div");
            showMoreBtnDiv.style.textAlign = 'center'
            const showMoreBtn = document.createElement("button");
            showMoreBtn.innerText = "بیشتر";
            showMoreBtn.style['margin'] = '2px'
            showMoreBtn.style['padding'] = '2px'

            showMoreBtn.onclick = () => {
                showMoreBtn.style.display = 'none';
                for (let i = count; i < response.length; i++) {
                    const { id, city, province, receiver, zip_code, is_default } = response[i];

                    const addressBody = document.getElementById('addressTableBody')

                    const trEle = document.createElement('tr')
                    trEle.id = `tr-${id}`

                    injectData(response[i]).then(
                        (value) => {
                            // console.log(value)
                            trEle.innerHTML = value

                        },
                        (error) => { console.log(error) }
                    )
                    // console.log(injectDataSon)
                    addressBody.appendChild(trEle)


                }
            }
            addressTable.appendChild(showMoreBtn);
        }
    })



djangoClient.getClientInfo().then(response => {

    const phoneNumber = document.getElementById('phone_number');
    phoneNumber.innerText = `${response.phone_number}`;

    const email = document.getElementById('email');
    email.innerText = response.email

})
    .catch(error => {
        console.log(error)
    })



document.getElementById('test-btn').addEventListener('click', function (e) {
    e.preventDefault();
    console.log('deleted');
    Cookies.remove('access');
    window.location.assign('/accounts/login/')
})


const addressProvince = document.getElementById('addressProvince');
const addressReciever = document.getElementById('addressReciever');
const addressCity = document.getElementById('addressCity');
const addressZipcode = document.getElementById('addressZipcode');
const addressPhone = document.getElementById('addressPhone');
const addressAddress = document.getElementById('addressAddress');
// const addressDefault = document.getElementById('addressDefault');
const addressSubmit = document.getElementById('addressSubmit');
const userId = Cookies.get('id');
const addressHolder = document.getElementById('address-holder')
const addressForm = document.getElementById('addressForm')

addressSubmit.addEventListener('click', (e) => {
    e.preventDefault()
    console.log(
        userId,
        addressProvince.value,
        addressCity.value,
        addressZipcode.value,
        addressPhone.value,
        addressAddress.value,
        // addressDefault.checked
    )

    const formData = new FormData();

    formData.append('user', userId)
    formData.append('receiver', addressReciever.value)
    formData.append('province', addressProvince.value)
    formData.append('city', addressCity.value)
    formData.append('zip_code', addressZipcode.value)
    formData.append('phone', addressPhone.value)
    formData.append('addr', addressAddress.value)
    // formData.append('is_default', addressDefault.checked)

    djangoClient.apiClient.post(config.apiURL + '/user/api/address/', formData)
        .then(res => {
            const addressTable = document.getElementById('addressTable')
            const addressBody = document.getElementById('addressTableBody')

            const trEle = document.createElement('tr')
            injectData(res.data).then(
                (value) => {
                    // console.log(value)
                    trEle.innerHTML = value
                },
                (error) => { console.log(error) }
            )
            // console.log(injectDataSon)
            addressBody.appendChild(trEle)

            // end of the new

            addressForm.reset()

        })
        .catch(err => { console.log(err) })
})



const profilEdit = document.getElementById('profileEdit');

profilEdit.addEventListener('click', (e) => {
    e.preventDefault();
    const formData = new FormData();
    const alphone = document.getElementById('phone_number');
    const alusername = document.getElementById('username');
    const alemail = document.getElementById('email');


    const username = document.getElementById('id_username').value;
    const email = document.getElementById('id_email').value;
    const phone = document.getElementById('id_phone').value;


    console.log(username, phone, email)

    if (username !== alusername) {
        formData.append('username', username)
        console.log('username')
    }

    console.log(alphone.innerText)

    if (phone !== alphone) {
        formData.append('phone_number', phone)
        console.log(alphone.innerText)
    }

    if (email !== alemail) {
        formData.append('email', email)
        console.log(alemail.innerText)
    }

    djangoClient.apiClient.patch(config.apiURL + `/user/api/profile/${userId}/`, formData)
        .then((res) => {
            alphone.innerText = phone
        })
        .catch((err) => console.log(err))
})





function validateForm() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm-password").value;

    if (password != confirmPassword) {
        alert("Passwords do not match.");
        return false;
    }

    // If passwords match, allow form submission to proceed.
    return true;
}

document.getElementById('editModalBtn').addEventListener('click', (e) => {
    let choise = $('input.selectAddress:checked').map(function () {
        return this.dataset.addressId;
    }).get();

    if (choise.length > 1) {
        Swal.fire({
            icon: 'warning',
            text: 'برای ویرایش فقط باید یک آدرس انتخاب کنید'
        }
        )
    } else if (choise.length === 0) {
        Swal.fire({
            icon: 'warning',
            text: 'برای ویرایش باید حداقل یک آدرس انتخاب کنید'
        }
        )
    } else {
        $('#exampleModal').modal("show");
        console.log(choise)
        djangoClient.apiClient.get(`${config.apiURL}/user/api/address/${choise}`)
            .then(res => {
                console.log(res)
                const modalReciever = document.getElementById('modalReceiver');
                const modalProvince = document.getElementById('modalProvince');
                const modalCity = document.getElementById('modalCity');
                const modalZipcode = document.getElementById('modalZipcode');
                const modalPhone = document.getElementById('modalPhone');
                const modalAddress = document.getElementById('modalAddress');
                modalReciever.value = res.data.receiver
                modalProvince.value = res.data.province
                modalCity.value = res.data.city
                modalZipcode.value = res.data.zip_code
                modalPhone.value = res.data.phone
                modalAddress.value = res.data.addr
                $(document).ready(function () {
                    $('#modalFormEdit').submit(function (e) {
                        e.preventDefault();
                        console.log(this)

                        let formData = $(this).serialize();


                        djangoClient.apiClient.put(`${config.apiURL}/user/api/address/${choise[0]}/`, formData)
                            .then(response => {

                                Swal.fire({
                                    icon: 'success',
                                    text: 'آدرس با موفقیت بروز شد'
                                })

                                const trEle = document.createElement('tr')
                                injectData(response.data).then(
                                    (value) => {
                                        // console.log(value)
                                        trEle.innerHTML = value
                                    },
                                    (error) => { console.log(error) })

                                $(`#tr-${response.data.id}`).replaceWith(trEle)


                            })
                            .catch(error => {
                                console.log(error, error.status)

                            });
                    });
                });

            })
            .catch(err => { console.log(err) })
    }



})


document.getElementById('deleteModalBtn').addEventListener('click', (e) => {
    let choise = $('input.selectAddress:checked').map(function () {
        return this.dataset.addressId;
    }).get();
    console.log(choise)

    choise.forEach((id, i) => {
        djangoClient.apiClient.delete(`${config.apiURL}/user/api/address/${id}`)
            .then(res => {
                console.log(res)
                $(`#tr-${id}`).remove()

            })
            .catch(err => {
                console.log(err)

            })
    })

})