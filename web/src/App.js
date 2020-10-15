import React from "react";

import { Route } from "react-router-dom"

import APIClient from "./axiosInstance";

import AuthComponent from "./Components/AuthComponent/AuthComponent";
import HomePage from "./Components/Home/HomePage"
import LoadingComponent from "./Components/General/LoadingComponent/LoadingComponent_LG"


export default class App extends React.PureComponent {
    state = {
        isLoading: true,
        isLoggedIn: false,
    };

    async componentDidMount() {

        const smKey = localStorage.getItem("sm-key");

        if (smKey) {
            this.apiClient = new APIClient(smKey);
            this.apiClient.check().then((data) => {
                console.log("Success: Data from Axios instance", data);
            });
        } else {
            this.setState({ isLoading: false })
        }


    }

    render() {
        let { isLoggedIn, isLoading } = { ...this.state };
        let app = <LoadingComponent />;

        if (isLoggedIn === false && !isLoading) {
            app = (<AuthComponent />);
        } else {
            app = (
                <div className="container-fluid">
                    <Route exact path="/" component={HomePage} />
                    <Route exact path="/login" component={AuthComponent} />
                </div>
            );
        }

        return (app)

    }

}
