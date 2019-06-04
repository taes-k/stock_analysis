import React, { Component } from "react";
import './Foot.css';

class Foot extends Component{
    render (){
        return (
            <div className="footer">
                <div className="footer-container">
                    <div className="info">
                        <span >Taes.k @2019</span>
                    </div>
                    <div className="link">
                        <img class="homepage" onClick={()=>window.open("https://taes-k.github.io/")}></img>

                        <img class="git" onClick={()=>window.open("https://github.com/taes-k")}></img>


                    </div>
                </div>
            </div>
        );
    }
};

export default Foot;