import React, { Component } from "react";
import SearchBar from "../searchBar/SearchBar"
import './Head.css';

class Head extends Component{
    render (){
        return (
            <div className="header">
                <div className="header-container">
                    <div className="logo-container">
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