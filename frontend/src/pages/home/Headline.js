import React, { Component } from "react";
import { connect } from 'react-redux';

class Headline extends Component{

    constructor(props){
        super(props);
        this.state = {
            news:[],
            companyDic:{}
        }
        // this.state = {
        //     url : "",
        //     title : "",
        //     contents : "",
        //     date : "",
        //     profile : "",
        //     positivie : 0,
        //     keyword : [],
        //     company : [],
        //     companyDic : {}
        // }
    }

    render (){
        const companies = []
        const defaultCompanyInfo = this.props.companyDic["000000"]
        this.props.news[0][0].company.forEach(el => {
            let companyInfo = (this.props.companyDic[el.code]==undefined?defaultCompanyInfo:this.props.companyDic[el.code])
            companies.push(<CompanyCard name={el.name} code={el.code} info={companyInfo}/>)
        });

        return (
            <div className="headline-container" style={{backgroundImage: `url(${this.props.profile})`}}>
                <div className="black-background" ></div>
                <div className="contents-background">
                    <div className="headline-top">
                        <div className="title">
                            {this.props.news[0][0].title}
                        </div>
                        <div className="date">
                            {this.props.news[0][0].date}
                        </div>
                    </div>
                    <div className="headline-middle">
                        <div className="contents">
                            {this.props.news[0][0].contents}
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

const CompanyCard = (props) => {
    console.log("PROOOPPPSS",props)
    return (
        <div className="card">
            <div className="title">
                <span>{props.name}</span> 
                <span className="company-id"> &nbsp;{props.code}</span>
            </div>
            <div className="market"> {props.info.market}</div>
            <div className="info current"> ₩ {props.info.current_price.toLocaleString(navigator.language, { minimumFractionDigits: 0 })} ({props.info.change_percent}%)</div>
            <div className="info total">
                <strong>시총</strong> : {props.info.total_price}<br/>
                <strong>거래량</strong> : {props.info.trade_count.toLocaleString(navigator.language, { minimumFractionDigits: 0 })}
            </div>
        </div>
    )
}

// const mapStateToProps = (state) => (
//     {
//     url : state.newsReducer.news[0].url,
//     title : state.newsReducer.news[0].title,
//     contents : state.newsReducer.news[0].contents,
//     date : state.newsReducer.news[0].date,
//     profile : state.newsReducer.news[0].profile,
//     positivie : state.newsReducer.news[0].positivie,
//     keyword : state.newsReducer.news[0].keyword,
//     company : state.newsReducer.news[0].company,
//     companyDic : state.companyReducer.company,
// });

const mapStateToProps = (state) => (
    {
        news : Array(state.newsReducer.news),
        companyDic : state.companyReducer.company
    });

export default connect(mapStateToProps)(Headline);