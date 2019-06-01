import React, { Component } from 'react';
import StockGraph from "../pages/search/StockGraph";

class CompanyComponent extends Component{
    props = {
        name : "",
        code : "",

    }

    render (){

        return (
            <div className="company-container">
                <div className="contents-background">
                    <div className="company-left">
                        <div className="company-top">
                            <div className="row">
                                <div className="title">
                                    삼성전자<span class="code">00593</span>
                                </div>
                                <div className="date">
                                    20190505
                                </div>
                            </div>
                            <div className="row">
                                <div className="current">
                                     45,300 ₩ 
                                    <span className="change"> -600 (1.31%)</span><img class="arrow up"></img>
                                </div>
                            </div>
                        </div>
                        <div class="company-bottom">
                            <div className="row">
                                <div className="detail_info">
                                    <div className="title">최고</div>
                                    <div className="contents">46,050</div>
                                </div>
                                <div className="detail_info">
                                    <div className="title">최고</div>
                                    <div className="contents">46,050</div>
                                </div>
                                <div className="detail_info">
                                    <div className="title">최고</div>
                                    <div className="contents">46,050</div>
                                </div>
                            </div>
                            <div className="row">
                                <div className="detail_info">
                                    <div className="title">최고</div>
                                    <div className="contents">46,050</div>
                                </div>
                                <div className="detail_info">
                                    <div className="title">최고</div>
                                    <div className="contents">46,050</div>
                                </div>
                                <div className="detail_info">
                                    <div className="title">최고</div>
                                    <div className="contents">46,050</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="company-right">
                        <StockGraph></StockGraph>
                    </div>
                </div>
            </div>
        );
    }
};

export default CompanyComponent;