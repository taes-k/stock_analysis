import React, { Component } from "react";
import './Home.css';
import Head from "../include/Head"
import Foot from "../include/Foot"

import Headline from "./Headline"
import Newsline from "./Newsline"

class Home extends Component{
    render (){
        return (
            <div className="home">
                <Head />
                <div className="container">
                    <div className="home-container">
                        <Headline />
                        <Newsline />
                    </div>
                </div>
                <Foot />
            </div>
        );
    }
};

export default Home;