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
            previousFlag : true //무한 스크롤 중복방지 플래그
        }
    }

    componentDidMount(){
        //초기 뉴스 불러오기
        this.getNewsInit()
        //10분 간격 update된 뉴스 불러오기
        this.interval = setInterval(()=> {
            this.getNewsUpdate()
        },300000);
        //무한스크롤, 이전뉴스 불러오기

        window.addEventListener("scroll", this.handleScroll);
    }

    componentWillUnmount() {
        // 언마운트 될때에, 스크롤링 이벤트 제거
        window.removeEventListener("scroll", this.handleScroll);
    }

    handleScroll = () => {
        const { innerHeight } = window;
        const { scrollHeight } = document.body;
        // IE에서는 document.documentElement 를 사용.
        const scrollTop =
          (document.documentElement && document.documentElement.scrollTop) ||
          document.body.scrollTop;
        // 스크롤 하단에서 실행
        if (scrollHeight - innerHeight - scrollTop < 100) {
            this.getPreviousNews()
        }
    };

    //초기 뉴스 불러오기
    getNewsInit = () =>{
        return axios.get('http://45.119.146.58/news/',{
        // return axios.get('http://127.0.0.1:8000/news/',{
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

    //신규 뉴스 불러오기
    getNewsUpdate = () =>{
        var date = new Date(this.props.news[0][0].crawlingDate.replace(' ','T')+"+09:00")
        date.setSeconds(date.getSeconds()+1)
        
        let dateString = date.getFullYear()+"-"+(date.getMonth()+1)+"-"+date.getDate()+" "+date.getHours()+":"+date.getMinutes()+":"+date.getSeconds()
        
        return axios.get('http://45.119.146.58/news/update/',{
        // return axios.get('http://127.0.0.1:8000/news/update/',{
            params:{
                crawlingDate: dateString,
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

                this.props.insertNews(data)
            });
            this.getCompanyInfo(companyData)
        })

        .catch((error)=>{
            console.log("ERROR : "+error)
        })
    }

    //이전 뉴스 불러오기
    getPreviousNews = () =>{
        //무한 스크롤 중복방지 플래그
        if(this.state.previousFlag){

            this.setState({
                previousFlag : false   
            })
            var date = new Date(this.props.news[0][this.props.newsCount-1].crawlingDate.replace(' ','T')+"+09:00")
            date.setSeconds(date.getSeconds()-1)
            
            let dateString = date.getFullYear()+"-"+(date.getMonth()+1)+"-"+date.getDate()+" "+date.getHours()+":"+date.getMinutes()+":"+date.getSeconds()
            
            return axios.get('http://45.119.146.58/news/previous/',{
            // return axios.get('http://127.0.0.1:8000/news/previous/',{
                params:{
                    crawlingDate: dateString,
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
                    previousFlag : true   
                })
            })

            .catch((error)=>{
                console.log("ERROR : "+error)
            })
        }
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

    render (){
        return (
            <div className="home">
                <Head />
                <div className="container">
                    <div className="home-container">
                        <Headline />
                        <NewsComponent />
                        <div className="pre-loader-container">
                            <img className={"pre-loader "+(this.state.previousFlag ? "off" : "on")}></img>
                        </div>
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
    newsCount : state.newsReducer.count,
    companyDic : state.companyReducer.company
});

let mapDispatchToProps = (dispatch) => {
    return {
        addNewsInit: (data) => dispatch(newsActionCreators.addNewsInit()),
        addNews: (data) => dispatch(newsActionCreators.addNews(data)),
        insertNews: (data) => dispatch(newsActionCreators.insertNews(data)),
        addCompany: (data) => dispatch(companyActionCreators.addCompany(data))
    }
}

export default connect(mapStateToProps,mapDispatchToProps)(Home); 