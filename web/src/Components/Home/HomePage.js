import React from "react";

export default class HomePage extends React.Component {
    state = {
        usuarios: [],
    };

    removeToken = () => {
        localStorage.removeItem('sm-key');
    }

    render() {
        return (
            <div>
                <div>Home Page</div>
                <div>
                    <a href="" onClick={this.removeToken}>Salir</a>
                </div>
            </div>
        )
    }

}
