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
    }
    componentDidMount(){
        //초기 뉴스 불러오기
        this.getNewsInit()

        this.interval = setInterval(()=> {
            this.getNewsUpdate()
        },300000);
    }

    getNewsInit(){
        return axios.get('http://45.119.146.58/news/',{
        //return axios.get('http://127.0.0.1:8000/news/',{
            params:{
                page: 0,
            }
        })
        .then((response)=>{
            let result = response.data.res
            let companyData = []
            
            result.forEach(el => {
            
                let data = {
                    url : el._source.url,
                    title : el._source.title,
                    contents : el._source.contents,
                    crawlingDate : el._source.crawling_date,
                    date : el._source.date,
                    profile : el._source.profile,
                    positive : el._source.positive,
                    keyword : el._source.keyword,
                    company : el._source.company
                };
                companyData.push(el._source.company)

                this.props.addNews(data)
            });
            this.getCompanyInfo(companyData)
        })

        .catch((error)=>{
            console.log("ERROR : "+error)
        })
    }

    getNewsUpdate(){
        return axios.get('http://45.119.146.58/news/update',{
        //return axios.get('http://127.0.0.1:8000/news/update',{
            params:{
                crawlingDate: this.props.news[0][0].crawlingDate,
            }
        })
        .then((response)=>{
            let result = response.data.res
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
                companyData.push(el._source.company)

                this.props.addNews(data)
            });
            this.getCompanyInfo(companyData)
        })

        .catch((error)=>{
            console.log("ERROR : "+error)
        })
    }

    getCompanyInfo(companyData){
        return new Promise(() =>{
            companyData.forEach(companyArrEl => {
                console.log("companyEl.code",companyArrEl)
                companyArrEl.forEach(companyEl => {
                    axios.get('http://45.119.146.58/company/',{
                        params:{
                            company: companyEl.code,
                        }
                    })
                    .then(res => {
                        this.props.addCompany(res.data)
                    })
                    .catch((error)=>{
                        console.log("ERROR 222: "+error)
                    })
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
const mapStateToProps = (state) => (
{
    news : Array(state.newsReducer.news),
    companyDic : state.companyReducer.company
});

let mapDispatchToProps = (dispatch) => {
    return {
        addNews: (data) => dispatch(newsActionCreators.addNews(data)),
        addCompany: (data) => dispatch(companyActionCreators.addCompany(data))
    }
}

export default connect(mapStateToProps,mapDispatchToProps)(Home); 