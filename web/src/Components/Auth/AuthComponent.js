import React from "react";
import axios from "axios"; // usamos axios directamente por ser el login

export default class Login extends React.Component {
  state = {
    isLoading: true,
    username: "",
    password: "",
  };

  handleLogin = (e) => {
    e.preventDefault();
    this.login();
  };

  handleUsernameChange = (e) => {
    let username = e.target.value;
    this.setState({
      username,
    });
  };

  handlePasswordChange = (e) => {
    let password = e.target.value;
    this.setState({
      password,
    });
  };

  login = () => {
    let url = `http://127.0.0.1:5000/login`;
    let data = new FormData();
    data.append("username", this.state.username);
    data.append("password", this.state.password);
    axios
      .post(url, data)
      .then((result) => {
        console.log("OK!");
        console.log(result);
      })
      .catch((err) => {
        // 1``console.err("Servidor no disponible")
        console.log(err);
      });
  };

  render() {
    return (
      <div>
        <form>
          <label>Username:</label>
          <input
            type="name"
            value={this.state.username}
            onChange={this.handleUsernameChange}
          />
          <label>Password:</label>
          <input
            type="password"
            value={this.state.password}
            onChange={this.handlePasswordChange}
          />
          <input type="submit" value="Login" onClick={this.handleLogin} />
        </form>
      </div>
    );
  }
}
