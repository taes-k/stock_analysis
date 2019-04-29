import React, { Component } from "react";
import { connect } from 'react-redux';

class Headline extends Component{

    constructor(props){
        super(props);
        this.state = {
            url : "",
            title : "",
            contents : "",
            date : "",
            profile : "",
            positivie : 0,
            keyword : [],
            company : []
        }
    }

    render (){
        const companies = []
        this.props.company.forEach(el => {
            companies.push(<CompanyCard name={el.name}/>)
        });

        return (
            <div className="headline-container" style={{backgroundImage: `url(${this.props.profile})`}}>
                <div className="black-background" ></div>
                <div className="contents-background">
                    <div className="headline-top">
                        <div className="title">
                            {this.props.title}
                        </div>
                        <div className="date">
                            {this.props.date}
                        </div>
                    </div>
                    <div className="headline-middle">
                        <div className="contents">
                            {this.props.contents}
                        </div>
                    </div>
                    <div className="headline-bottom">
                        <div className="companies">
                            {companies}
                        </div>
                    </div>
                </div>
            </div>
        );
    }


};

const CompanyCard = (props) => (
    <div className="card">
        <div className="title">
            <span>{props.name}</span> 
            <span className="company-id"> 012345</span>
        </div>
        <div className="info">▼19,000</div>
        <div className="info">▲19,000</div>
    </div>
);

const mapStateToProps = ({ news }) => (
    {
    url : news.news[0].url,
    title : news.news[0].title,
    contents : news.news[0].contents,
    date : new Date(news.news[0].date).toLocaleString(),
    profile : news.news[0].profile,
    positivie : news.news[0].positivie,
    keyword : news.news[0].keyword,
    company : news.news[0].company,
});

export default connect(mapStateToProps)(Headline);