import React, { Component } from "react";
import { connect } from 'react-redux';
import axios from "axios";
import { newsActionCreators } from "../../store/modules/News";
import { companyActionCreators } from "../../store/modules/Company";
import { searchedCompanyActionCreators } from "../../store/modules/SearchedCompany";

import Head from "../include/head/Head";
import Foot from "../include/foot/Foot";
import CompanyComponent from "../../components/CompanyComponent";
import NewsComponent from "../../components/NewsComponent";

import "./Search.css"

class Search extends Component{
    constructor(props){
        super(props);
        this.state = {
            searchFlag : false,
            newsFlag : false,
        }
    }

    componentDidMount(){
        this.getCompany();
        this.props.deleteNews()
        this.getNews();
    }

    componentDidUpdate(prevProps, prevState) {
        if(prevProps.match.params.text != this.props.match.params.text){
            this.getCompany();
            this.props.deleteNews()
            this.getNews();
        }else{

            window.scrollTo(0, 0)
        }
    }

    getCompany = () => {

        this.setState({
            searchFlag : false
        })
        return axios.get('http://45.119.146.58/company/',{
        // return axios.get('http://127.0.0.1:8000/company/',{
            params:{
                name: this.props.match.params.text,
            }
        })
        .then((response)=>{
            let result = response.data;
            if(result.return_code == 200){
                this.props.addSearchedCompany(result)
                this.setState({
                    searchFlag : true
                })
            }else {
                let data = {
                    name : "",
                    code : "",
                    current_price : 0,
                    change_price : 0,
                    chamge_percent : 0,
                    market : "",
                    total_price : 0,
                    total_stock : 0,
                    trade_count : 0,
                    yesterday_price : 0,
                    max_price : 0,
                    min_price : 0,
                    start_price : 0,
                    year_max_price : 0,
                    year_min_price : 0,
                    date:""
                }
                this.props.addSearchedCompany(data)
                this.setState({
                    searchFlag : false
                })
            }
        })
        .catch((error)=>{
            console.log("ERROR : "+error)
        })
    }

    getNews(){

        this.setState({
            newsFlag : true   
        })
        return axios.get('http://45.119.146.58/news/search/',{
        // return axios.get('http://127.0.0.1:8000/news/search/',{
            params:{
                text: this.props.match.params.text,
            }
        })
        .then((response)=>{
            let result = response.data.res
            let companyData = []
            this.props.addNewsInit()
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
            this.setState({
                newsFlag : false 
            })
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
                    axios.get('http://45.119.146.58/company/',{
                    // axios.get('http://127.0.0.1:8000/company/',{
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
                        <div className={"company-search "+(this.state.searchFlag?"find":"")}>
                            <p>상장사 <span>'{ this.props.match.params.text }'</span> 정보</p>
                            <CompanyComponent/>
                        </div>
                        <div>
                            <p><span>'{ this.props.match.params.text }'</span> 키워드 관련뉴스 검색 결과</p>
                            <NewsComponent />
                            <div className="pre-loader-container">
                                <img className={"pre-loader "+(this.state.newsFlag ? "on" : "off")}></img>
                            </div>
                        </div>
                    </div>
                </div>
                <Foot />
            </div>
        );
    }
}

let mapDispatchToProps = (dispatch) => {
    return {
        addNewsInit: () => dispatch(newsActionCreators.addNewsInit()),
        addNews: (data) => dispatch(newsActionCreators.addNews(data)),
        deleteNews: () => dispatch(newsActionCreators.deleteNews()),
        addCompany: (data) => dispatch(companyActionCreators.addCompany(data)),
        addSearchedCompany: (data) => dispatch(searchedCompanyActionCreators.addSearchedCompany(data))
    }
}

export default connect(undefined,mapDispatchToProps)(Search); 