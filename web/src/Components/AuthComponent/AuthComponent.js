import React from "react";
import axios from "axios";
import { Button, Form, FormGroup, Row, Col } from "react-bootstrap";

import "bootstrap/dist/css/bootstrap.min.css";

import FacebookLoginButton from "../General/FacebookLoginComponent/FacebookLoginComponent"
import "./AuthComponent.css";
import { config } from "../../Components/config"

export default class AuthComponent extends React.Component {
  state = {
    username: '',
    password: '',
  };

  componentDidMount() {
  }

  doLogin = () => {
    let data = new FormData();
    data.append("username", this.state.username);
    data.append("password", this.state.password);
    let httpPrefix = "http";
    if (config.using_ssl === true) {
      httpPrefix = "https";
    }
    const url = `${httpPrefix}://${config.api_url}:${config.api_port}/login`;
    axios
      .post(url, data)
      .then((result) => {
        if (result.status === 401) {
          console.log("Usuario o contraseña incorrectos");
        } else {
          if (result.status === 200) {
            localStorage.setItem("sm-key", result.data.access_token);
            window.location.href = "/";
          }
        }
      })
      .catch(err => {
        console.log(err);
      });
  }

  handleLogin = (e) => {
    e.preventDefault();
    this.doLogin();
  }

  onUsernameChange = (e) => {
    this.setState({
      username: e.target.value
    })
  }

  onPasswordChange = (e) => {
    this.setState({
      password: e.target.value
    })
  }

  render() {
    return (
      <Form className="login-form" onSubmit={this.handleLogin}>
        <h1>
          <span className="font-weight-bold">Sommelier</span>.com
        </h1>
        <h2 className="text-center">Iniciar sesi&oacute;n</h2>
        <FormGroup>
          <Form.Label>Email</Form.Label>
          <Form.Control type="email" placeholder="Email" value={this.state.username} onChange={this.onUsernameChange} />
        </FormGroup>
        <FormGroup>
          <Form.Label>Contraseña</Form.Label>
          <Form.Control type="password" placeholder="Contraseña" value={this.state.password} onChange={this.onPasswordChange} />
        </FormGroup>
        <Button variant="primary" className="btn-block" type="submit">
          Entrar
        </Button>
        <div className="text-center pt-3 pb-3">O con alguna de las siguientes opciones</div>
        <div>
          <Row>
            <Col lg={3} className="text-center"></Col>
            <Col lg={6} className="text-center">
              <FacebookLoginButton />
            </Col>
            <Col lg={3} className="text-center"></Col>
          </Row>
        </div>
        <div className="text-center pt-3 pb-3">
          <a href="/sign-up">Registrarse</a>
          <span className="p-2">|</span>
          <a href="/sign-up">Olvid&eacute; mi contraseña</a>
        </div>
      </Form>

    );
  }
}