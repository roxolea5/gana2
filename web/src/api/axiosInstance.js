import axios from "axios";

let host = "";
let port = "";
if (process.env.NODE_ENV === "development") {
  host = "http://127.0.0.1";
  port = "5000";
}

let baseUrl = `${host}:${port}/`;

const axiosInstance = axios.create({ baseURL: baseUrl });

axiosInstance.interceptors.request.use(function (config) {
  let token = "Bearer " + localStorage.getItem("sm-key");

  config.headers = { Authorization: token };

  return config;
});

export default axiosInstance;
