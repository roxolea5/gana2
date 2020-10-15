import axios from "axios";
import { config } from "./Components/config"

let host = "";
let port = 5000;
if (process.env.NODE_ENV === "development") {
  host = config.api_url_axios;
  port = config.api_port;
} else {
  if (process.env.NODE_ENV === "production") {
    host = config.api_url_axios_PROD;
    port = config.api_port_PROD;
  }
}
let BASE_URI = `${host}:${port}/`;

console.log("BASE_URI");
console.log(BASE_URI);

const client = axios.create({
  baseURL: BASE_URI,
  json: true
});

class APIClient {
  constructor(token) {
    this.accessToken = token;
  }

  check() {
    return this.perform('post', '/api/check');
  }

  async perform(method, resource) {
    console.log("Performing axios request to: ", resource);
    console.log("Auth: ", `Bearer ${this.accessToken}`)
    return client({
      method,
      url: resource,
      // data,
      headers: {
        Authorization: `Bearer ${this.accessToken}`
      }
    }).then(resp => {
      console.log("then=> resp.data: ");
      console.log(resp.data);
      return resp.data ? resp.data : [];
    }).catch(err => {
      console.error("** Axios Instance Error: Server not available")
      console.log(err);
    })
  }

}
export default APIClient;
