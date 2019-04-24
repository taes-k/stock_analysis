import React, { Component } from "react";
import './Home.css';
import Todo from "../components/TodoComponent"

class Home extends Component{
    render (){
        return (
            <div className="Home">
                <p>React Home</p>

                <Todo text="Webpack 설치"/>
                <Todo text="Babel 설치"/>
                <Todo text="React 설치"/>
                <Todo text="Redux 설치"/>
            </div>
        );
    }
};

export default Home;