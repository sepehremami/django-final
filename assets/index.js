import config from './config.js';



console.log(config.apiURL)

axios.get(config.apiURL)
    .then((response)=> {
        console.log(response)
    })
    .catch((error)=> {
        console.log(error)
    })