import React, { Component } from "react";
import {Link} from 'react-router-dom';

class SearchBar extends Component{
    state = {
        text: ''
    }
   
    searchEnterPress = (event) =>{
        var code = event.keyCode || event.which;
        if(code == 13){
            this.searchClick();
        }
    }
    searchClick = () =>{
        searchLink.click();
    }
    searchChange = (e) =>{
        this.setState({
            text: "/search/"+e.target.value
        })
    }
    render() {
        return (         
            <div className="search-container">
                <input onKeyPress={this.searchEnterPress} onChange={this.searchChange}></input>
                <Link id="searchLink" to={this.state.text}>
                    <button onClick={this.searchClick}></button>
                </Link>
            </div>
        );
    }
}

export default SearchBar;