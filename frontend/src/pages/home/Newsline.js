import React, { Component } from "react";
import { connect } from 'react-redux';

class Newsline extends Component{

    constructor(props){
        super(props);
        this.state = {
            news:[]
        }
    }

    render (){

        const newscard = []

        this.props.news[0].forEach((el,idx) => {
            newscard.push( <NewslineCard key={idx} data={el}/> )
        });

        return (
            <div className="newsline-container">
                {newscard}
            </div>
        );
    }
};


const NewslineCard = (props) => (
    <div className="newsline-box" style={{backgroundImage: `url(${props.data.profile})`}}>
        <div className="black-background" ></div>
        <div className="contents-background">
            <div className="newsline-top">
                <div className="title">
                    {props.data.title}
                </div>
                <div className="date">
                    {props.data.date}
                </div>
            </div>
            <div className="headline-middle">
                <div className="contents">
                </div>
            </div>
            <div className="headline-bottom">
                <div className="companies">
                </div>
            </div>
        </div>
    </div>
);

const mapStateToProps = ({ news }) => (
{
    news : Array(news.news)
});

export default connect(mapStateToProps)(Newsline);