import React, { Component } from "react";
import { connect } from 'react-redux';
import axios from "axios";
import { newsActionCreators } from "../../store/modules/News";
import { companyActionCreators } from "../../store/modules/Company";

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
        this.getNews();
    }

    getCompany(){
        //return axios.get('http://45.119.146.58/company/name/',{
        return axios.get('http://127.0.0.1:8000/company/name/',{
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

    getNews(){
        //return axios.get('http://45.119.146.58/news/search/',{
        return axios.get('http://127.0.0.1:8000/news/search/',{
            params:{
                text: this.props.match.params.text,
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

    //회사정보 불러오기
    getCompanyInfo(companyData){
        return new Promise(() =>{
            companyData.forEach(companyArrEl => {
                companyArrEl.forEach(companyEl => {
                    //axios.get('http://45.119.146.58/company/',{
                    axios.get('http://127.0.0.1:8000/company/',{
                        params:{
                            code: companyEl.code,
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

    render(){
        return(
            <div className="search">
                <Head />
                <div className="container">
                    <div className="search-container">
                        <p>상장사 <span>'{ this.props.match.params.text }'</span> 정보</p>
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
        deleteNews: () => dispatch(newsActionCreators.deleteNews()),
        addCompany: (data) => dispatch(companyActionCreators.addCompany(data))
    }
}

export default connect(undefined,mapDispatchToProps)(Search); 