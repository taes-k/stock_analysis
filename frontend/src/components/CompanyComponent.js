import React, { Component } from 'react';
import { connect } from 'react-redux';
import StockGraph from "../pages/search/StockGraph";

class CompanyComponent extends Component{

    render (){
        return (
            <div className="company-container">
                <div className="contents-background">
                    <div className="company-left">
                        <div className="company-top">
                            <div className="row">
                                <div className="title">
                                    {this.props.companyData.name}<span class="code">{this.props.companyData.code}</span>
                                </div>
                                <div className="date">
                                    {this.props.companyData.date}
                                </div>
                            </div>
                            <div className="row">
                                <div className={"current "+(this.props.companyData.change_price>0?"up":"down")}>
                                    {this.props.companyData.current_price.toLocaleString(navigator.language, { minimumFractionDigits: 0 })} ₩ 
                                    <span className="change">  {this.props.companyData.change_price.toLocaleString(navigator.language, { minimumFractionDigits: 0 })} ({this.props.companyData.change_percent} %)</span><img class={"arrow "+(this.props.companyData.change_price>0?"up":"down")}></img>
                                </div>
                            </div>
                            <div className="row">
                                <div className="market">{this.props.companyData.market}</div>
                            </div>
                            <div className="row">
                                <div className="total-info">
                                    <div className="title">시가총액</div>
                                    <div className="contents">{this.props.companyData.total_price}</div>
                                </div>
                                <div className="total-info">
                                    <div className="title">상장주식수</div>
                                    <div className="contents">{this.props.companyData.total_stock.toLocaleString(navigator.language, { minimumFractionDigits: 0 })}</div>
                                </div>
                                <div className="total-info">
                                    <div className="title">거래량</div>
                                    <div className="contents">{this.props.companyData.trade_count.toLocaleString(navigator.language, { minimumFractionDigits: 0 })}</div>
                                </div>
                            </div>
                        </div>
                        <div class="company-bottom">
                            <div className="row">
                                <div className="detail-info">
                                    <div className="title">전일종가</div>
                                    <div className="contents">{this.props.companyData.yesterday_price.toLocaleString(navigator.language, { minimumFractionDigits: 0 })}</div>
                                </div>
                                <div className="detail-info">
                                    <div className="title">최고</div>
                                    <div className="contents">{this.props.companyData.max_price.toLocaleString(navigator.language, { minimumFractionDigits: 0 })}</div>
                                </div>
                                <div className="detail-info">
                                    <div className="title">최저</div>
                                    <div className="contents">{this.props.companyData.min_price.toLocaleString(navigator.language, { minimumFractionDigits: 0 })}</div>
                                </div>
                            </div>
                            <div className="row">
                                <div className="detail-info">
                                    <div className="title">금일시가</div>
                                    <div className="contents">{this.props.companyData.start_price.toLocaleString(navigator.language, { minimumFractionDigits: 0 })}</div>
                                </div>
                                <div className="detail-info">
                                    <div className="title">1년최고</div>
                                    <div className="contents">{this.props.companyData.year_max_price.toLocaleString(navigator.language, { minimumFractionDigits: 0 })}</div>
                                </div>
                                <div className="detail-info">
                                    <div className="title">1년최저</div>
                                    <div className="contents">{this.props.companyData.year_min_price.toLocaleString(navigator.language, { minimumFractionDigits: 0 })}</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="company-right">
                        <StockGraph companyData={this.props.companyData}></StockGraph>
                    </div>
                </div>
            </div>
        );
    }
};

const mapStateToProps = (state) => (
    {
        companyData : state.searchedCompanyReducer.company
    });
    
export default connect(mapStateToProps)(CompanyComponent);