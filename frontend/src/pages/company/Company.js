import React, { Component } from "react";
import { connect } from 'react-redux';

class Company extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return(
            <div></div>
        )
    }
}

let mapDispatchToProps = (dispatch) => {
    return {
        addNews: (data) => dispatch(actionCreators.addNews(data))
    }
}

export default connect(undefined,mapDispatchToProps)(Company); 