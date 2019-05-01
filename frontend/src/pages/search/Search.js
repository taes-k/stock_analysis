import React, { Component } from "react";
import { connect } from 'react-redux';
import Head from "../include/Head";
import Foot from "../include/Foot";

class Search extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return(
            <div className="search">
                <Head />
                <div className="container">
                    <div className="search-container">
                    { this.props.match.params.text }
                    </div>
                </div>
                <Foot />
            </div>
        );
    }
}

let mapDispatchToProps = (dispatch) => {
    return {
        addNews: (data) => dispatch(actionCreators.addNews(data))
    }
}

export default connect(undefined,mapDispatchToProps)(Search); 