import React from "react";
import axios from "../api/axiosInstance";

export default class Usuarios extends React.Component {
  state = {
    usuarios: [],
  };


  componentDidMount() {
    const url = `api/users/?page_number=1`;
    axios
      .get(url)
      .then((result) => {
        console.log("Users");
        console.log(result);
      })
      .catch(console.log);
    console.log("DidMount");
  }

  render() {
    return <div>Usuarios</div>;
  }
}
