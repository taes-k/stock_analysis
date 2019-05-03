import React, { Component } from 'react';
import { connect } from 'react-redux';

class CompanyComponent extends Component{
    state = {
        name : "",
        code : "",

    }

    render (){

        return (
            <div className="company-container">
                <div className="black-background" ></div>
                <div className="contents-background">
                    <div className="company-top">
                        <div className="title">
                            {this.props.title}
                        </div>
                        <div className="date">
                            {this.props.date}
                        </div>
                    </div>
                    <div className="company-middle">
                        <div className="contents">
                            {this.props.contents}
                        </div>
                    </div>
                    <div className="company-bottom">
                        <div className="companies">
                        </div>
                    </div>
                </div>
            </div>
        );
    }
};

export default CompanyComponent;