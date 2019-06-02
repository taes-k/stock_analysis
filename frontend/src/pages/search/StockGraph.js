import React, { Component } from 'react';
import ReactHighcharts from 'react-highcharts';

class StockGraph extends Component {
    constructor(props){
        super(props);
        this.state = {
            chartConfig : {
            }
        }
    }
    static getDerivedStateFromProps = (nextProps, prevState) => {

        return{
            chartConfig : {
                chart:{
                    height:340,
                    style: {
                        fontFamily: '"Spoqa Han Sans", "Roboto", "Spoqa Han Sans JP", "Sans-serif"'
                    }
                },
                title: {
                    text: ''
                },
                subtitle: {
                    text: ''
                },
                xAxis:{
                    labels:{
                        style: {
                            color: '#adb5bd',
                            fontSize: '12px',
                            fontWeight: 'bold'
                        }
                    },
                    categories: (nextProps.companyData.change_price>0?['전일종가','금일시가','최고가','최저가','현재가']:['전일종가','금일시가','최저가','최고가','현재가']),
                    tickWidth: 0,
                },
                yAxis: {
                    title: {
                        text: ''
                    },
                    labels:{
                        style: {
                            color: '#adb5bd',
                            fontSize: '12px',
                            fontWeight: 'bold'
                        },
                        formatter: function () {
                            return this.value.toLocaleString(navigator.language, { minimumFractionDigits: 0 });
                        } 
                    }
                },
                legend: {
                    enabled:false
                },
                plotOptions: {
                    series: {
                        label: {
                            dataLabels: {
                                enabled: true
                            },
                            enableMouseTracking: false
                        },
                    }
                },
                series: [{
                    name: 'stock_price',
                    data: (nextProps.companyData.change_price>0?[nextProps.companyData.yesterday_price, nextProps.companyData.start_price, nextProps.companyData.max_price, nextProps.companyData.min_price, nextProps.companyData.current_price]:[nextProps.companyData.yesterday_price, nextProps.companyData.start_price, nextProps.companyData.min_price, nextProps.companyData.max_price, nextProps.companyData.current_price]),
                    color: (nextProps.companyData.change_price>0?'#f03e3e':'#228be6'),
                    lineWidth:4,
                    marker:{
                        radius:0
                    }
                }],
                responsive: {
                    rules: [{
                        condition: {
                            maxWidth: 500
                        },
                        chartOptions: {
                            legend: {
                                layout: 'horizontal',
                                align: 'center',
                                verticalAlign: 'bottom'
                            }
                        }
                    }]
            
                }
            }
        }
    }

    render() {
        return (
            <div>
                <ReactHighcharts config={this.state.chartConfig}></ReactHighcharts>
            </div>
        );
    }
}
 
export default StockGraph;