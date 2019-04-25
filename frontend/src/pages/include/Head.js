import React, { Component } from "react";

import './Head.css';

class Head extends Component{
    render (){
        return (
            <div className="header">
                <div className="header-container">
                    <div>
                        <span className="title">BSN</span>
                        <span className="sub-title">Breaking Stock News</span>
                    </div>
                </div>
            </div>
        );
    }
};
1
export default Head;