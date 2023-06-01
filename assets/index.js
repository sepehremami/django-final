import config from './config.js';
import Cookies from 'js-cookie';


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
  };
}

function CookieInterceptor(config) {
  const headers = {};
  const authToken = Cookies.get('access');
  if (authToken) {
    headers['Authorization'] = `Bearer ${authToken}`;
  }
  else {
    alert('Session expired! Please login again!');
  }
  config['headers'] = headers;
  return config;
};

export default DjangoClient;