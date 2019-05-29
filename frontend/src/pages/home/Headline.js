import React, { Component } from "react";
import { connect } from 'react-redux';
import {Link} from 'react-router-dom';

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
            companies.push(<CompanyCard name={el.name} code={el.code} info={companyInfo} positive={this.props.news[0][0].positive}/>)
        });

        return (
            <div className="headline-container" style={{backgroundImage: `url(${this.props.news[0][0].profile})`}}>
                <div className="black-background" ></div>
                <div className={"positive-status "+(this.props.news[0][0].positive>0 ? "up" : "down")}></div>
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
                        <div className="more" onClick={()=>window.open(this.props.news[0][0].url)} >더보기</div>
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
    return (
        <div className={"card "+(props.positive>0 ? "up" : "down")}>
            <div className="title">
                <img className={"arrow "+(props.positive>0 ? "up" : "down")}></img>
                <Link className={"name "+(props.positive>0 ? "up" : "down")} to={"/search/"+(props.name)}>
                    <span >{props.name}</span>
                </Link>
                <span className="company-id"> &nbsp;{props.code}</span>
            </div>
            <div className={"info current "+(props.info.change_percent>0 ? "up" : "down")}>
                <strong>₩ {props.info.current_price.toLocaleString(navigator.language, { minimumFractionDigits: 0 })} </strong>
                <span>( {props.info.change_percent}% )</span></div>
            <div className="info capitalization">
                <strong className="title">시총</strong>
                <span className="contents">{props.info.total_price}</span>
            </div>
            <div className="info volume">
                <strong>거래량</strong>
                <span>{props.info.trade_count.toLocaleString(navigator.language, { minimumFractionDigits: 0 })}</span>
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