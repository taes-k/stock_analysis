import React, { Component } from 'react';
import { connect } from 'react-redux';
import {Link} from 'react-router-dom';

class NewsComponent extends Component{
    constructor(props){
        super(props);
        this.state = {
            news:[],
            companyDic:{}
        }
    }

    render (){
        const newscard = []
        this.props.news[0].forEach((el,idx) => {
            newscard.push( <NewslineCard key={idx} data={el} companyDic={this.props.companyDic}/> )
        });

        return (
            <div className="newsline-container">
                {newscard}
            </div>
        );
    }
};

const NewslineCard = (props) => {
    let companies = []
    const defaultCompanyInfo = props.companyDic["000000"]
    props.data.company.forEach((el,idx)=>{
        let companyInfo = (props.companyDic[el.code]==undefined?defaultCompanyInfo:props.companyDic[el.code])
        companies.push(<Companies data={el} info={companyInfo} positive={props.data.positive}/>)
    })
    return(
        <div className={"newsline-box "+(props.data.positive>0 ? "up" : "down")}>
            <div className="newsline-top" style={{backgroundImage: `url(${props.data.profile})`}}  onClick={()=>window.open(props.data.url)}>
                <div className="black-background" ></div>
                <div className="contents-background">
                    <div className="title">
                        {props.data.title}
                    </div>
                    <div className="date">
                        {props.data.date}
                    </div>
                </div>
            </div>
            <div className="newsline-bottom">
                <div className="company-list">
                        {companies}
                </div>
            </div>
        </div>
    )
};

 const Companies = (props) => {
    
    return(        
    <Link to={"/search/"+(props.data.name)}>
        <div className={"company "+(props.positive>0 ? "up" : "down")} onClick={()=> props.history.push('/serach/YG')} >
            <div class="arrow">
                <img class={"arrow "+(props.positive>0 ? "up" : "down")}></img>
            </div>
            <div class="name">{props.data.name}</div>
            <div class="code">{props.info.code}</div>
            <div class={"percent "+(props.info.change_percent>0 ? "up" : (props.info.change_percent==0 ? "" : "down"))}>({props.info.change_percent}%)</div>
            <div class={"price "+(props.info.change_percent>0 ? "up" : (props.info.change_percent==0 ? "" : "down"))}>₩ {props.info.current_price.toLocaleString(navigator.language, { minimumFractionDigits: 0 })}</div>
        </div>
    </Link>
)};

const mapStateToProps = (state) => (
{
    news : Array(state.newsReducer.news),
    companyDic : state.companyReducer.company
});

export default connect(mapStateToProps)(NewsComponent);