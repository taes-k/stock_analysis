import React, { Component } from "react";
import { connect } from 'react-redux';
import axios from "axios";
import { newsActionCreators } from "../../store/modules/News";

import Head from "../include/head/Head";
import Foot from "../include/foot/Foot";
import CompanyComponent from "../../components/CompanyComponent";
import NewsComponent from "../../components/NewsComponent";

import "./Search.css"

class Search extends Component{
    constructor(props){
        super(props);
    }

    componentDidMount(){
        this.props.deleteNews()
        this.getNews()
            .then((result) => {
                this.state.news.forEach(el => {
                    this.props.addNews(el)
                });
            });
    }

    getNews(){
        return axios.get('http://45.119.146.58/news/search/',{
        //return axios.get('http://127.0.0.1:8000/news/search/',{
            params:{
                text: this.props.match.params.text,
            }
        })
        .then((response)=>{
            console.log("search result : ",response)
            let result = response.data.res;
            let newsData = [];
            result.forEach(el => {
                let data = {
                    url : el._source.url,
                    title : el._source.title,
                    contents : el._source.contents,
                    date : el._source.date,
                    profile : el._source.profile,
                    positive : el._source.positive,
                    keyword : el._source.keyword,
                    company : el._source.company
                };
                newsData.push(data);
            });
            this.setState({
               news:newsData     
            })
        })
        .catch((error)=>{
            console.log("ERROR : "+error)
        })
    }

    render(){
        return(
            <div className="search">
                <Head />
                <div className="container">
                    <div className="search-container">
                        <p><span>'{ this.props.match.params.text }'</span> 기업 검색 결과</p>
                        <CompanyComponent/>
                        <p><span>'{ this.props.match.params.text }'</span> 키워드 관련뉴스 검색 결과</p>
                        <NewsComponent />
                    </div>
                </div>
                <Foot />
            </div>
        );
    }
}

let mapDispatchToProps = (dispatch) => {
    return {
        addNews: (data) => dispatch(newsActionCreators.addNews(data)),
        deleteNews: () => dispatch(newsActionCreators.deleteNews())
    }
}

export default connect(undefined,mapDispatchToProps)(Search); 