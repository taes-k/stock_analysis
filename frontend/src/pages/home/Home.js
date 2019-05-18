import React, { Component } from "react";
import { connect } from 'react-redux';
import axios from "axios"
import { newsActionCreators } from "../../store/modules/News";
import { companyActionCreators } from "../../store/modules/Company";

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
        //뉴스 불러오기
        this.getNews()
            .then((result) => {
                this.state.news.forEach(el => {
                    this.props.addNews(el)
                });
                //회사정보 불러오기
                this.getCompanyInfo()
            });
    }
    getNews(){
        return axios.get('http://45.119.146.58/news/',{
            params:{
                page: 0,
            }
        })
        .then((response)=>{
            let result = response.data.res
            let newsData = []
            let companyData = []

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
                companyData.push(el._source.company)
            });
            console.log("newsData",newsData)
            this.setState({
                news:newsData,
                company:companyData     
            })
        })

        .catch((error)=>{
            console.log("ERROR : "+error)
        })
    }

    getCompanyInfo(){
        return new Promise(() =>{
            this.state.company.forEach(companyArrEl => {
                console.log("companyEl.code",companyArrEl)
                companyArrEl.forEach(companyEl => {
                    // axios.get('http://13.209.47.27:8000/company/',{
                    //     params:{
                    //         company: companyEl.code,
                    //     }
                    // })
                    // .then(res => {
                    //     this.props.addCompany(res.data)
                    // })
                    // .catch((error)=>{
                    //     console.log("ERROR 222: "+error)
                    // })
                })
                
            })
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
        addNews: (data) => dispatch(newsActionCreators.addNews(data)),
        addCompany: (data) => dispatch(companyActionCreators.addCompany(data))
    }
}

export default connect(undefined,mapDispatchToProps)(Home); 