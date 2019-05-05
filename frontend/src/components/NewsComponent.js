import React, { Component } from 'react';
import { connect } from 'react-redux';

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
    console.log("COMDIC :::: ",props.companyDic)
    props.data.company.forEach((el,idx)=>{
        let companyInfo = (props.companyDic[el.code]==undefined?defaultCompanyInfo:props.companyDic[el.code])
        companies.push(<Companies data={el} info={companyInfo} />)
    })
    return(
        <div className="newsline-box">
            <div className="newsline-top" style={{backgroundImage: `url(${props.data.profile})`}}>
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
        <div className="company">
            <div class="name">{props.data.name}</div>
            <div class="code">{props.info.code}</div>
            <div class="percent">({props.info.change_percent}%)</div>
            <div class="price">₩ {props.info.current_price.toLocaleString(navigator.language, { minimumFractionDigits: 0 })}</div>
            
        </div>
)};

const mapStateToProps = (state) => (
{
    news : Array(state.newsReducer.news),
    companyDic : state.companyReducer.company
});

export default connect(mapStateToProps)(NewsComponent);