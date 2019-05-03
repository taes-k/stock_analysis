import React, { Component } from 'react';
import { connect } from 'react-redux';

class NewsComponent extends Component{
    constructor(props){
        super(props);
        this.state = {
            news:[]
        }
    }
    getNewssss(){

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

const NewslineCard = (props) => {
    let act = <div>hello</div>
    let companies = []
    props.data.company.forEach((el,idx)=>{
        companies.push(<Companies data={el}/>)
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
            {props.data.name}
        </div>
)};

const mapStateToProps = ({ news }) => (
{
    news : Array(news.news)
});

export default connect(mapStateToProps)(NewsComponent);