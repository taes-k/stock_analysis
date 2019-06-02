import React, { Component } from "react";
import {Link} from 'react-router-dom';
import SearchBar from "../searchBar/SearchBar"
import './Head.css';

class Head extends Component{
    render (){
        return (
            <div className="header">
                <div className="header-container">
                    <div className="logo-container" onClick={() =>{window.location.href='/'}}>
                        <span className="title">BSN</span>
                        <span className="sub-title">Breaking Stock News</span>
                    </div>
                    <SearchBar />
                </div>
            </div>
        );
    }

};

export default Head;