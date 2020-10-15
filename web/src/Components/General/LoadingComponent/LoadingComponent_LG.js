import React from "react";
import { Spinner } from "react-bootstrap";

import "./LoadingComponent.css"

// when the SM, MD and LG size be defined, Loading Component will be for all 3 sizes
// Component can be SM, MD and LD, but CSS Style will be only ONE

export default class LoadingComponentLG extends React.Component {
    state = {
        usuarios: [],
    };

    render() {
        return (
            <div className="div-parent text-center">
                <div className="div-on-spinner-lg"></div>
                <Spinner className="loading-component-lg align-top" animation="grow" size="lg" />
            </div>
        )
    }

}