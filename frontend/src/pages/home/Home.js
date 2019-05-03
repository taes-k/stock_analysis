import React, { Component } from "react";
import { connect } from 'react-redux';
import axios from "axios"
import { actionCreators } from "../../store/modules/News";

import Head from "../include/head/Head"
import Foot from "../include/foot/Foot"
import Headline from "./Headline"
import NewsComponent from "../../components/NewsComponent";

import './Home.css';

class Home extends Component{
    constructor(props){
        super(props);
        this.state = {
            news:[]
        }
    }
    componentDidMount(){
        this.getNews()
            .then((result) => {
                this.state.news.forEach(el => {
                    this.props.addNews(el)
                });
            });
    }
    getNews(){
        return axios.get('http://127.0.0.1:8000/news/',{
            params:{
                page: 0,
            }
        })
        .then((response)=>{
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

    render (){
        return (
            <div className="home">
                <Head />
                <div className="container">
                    <div className="home-container">
                        <Headline />
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
        addNews: (data) => dispatch(actionCreators.addNews(data))
    }
}

export default connect(undefined,mapDispatchToProps)(Home); 