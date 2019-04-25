import React, { Component } from "react";
import News from "../../components/NewsComponent";

class Newsline extends Component{
    render (){
        return (
            <div className="newsline-container">
                <div>
                    <div className="title">
                        [속보] 미세먼지 경보단계 
                    </div>
                    <div className="contents">
                        4월 30일 북서쪽에서 불어온 미세먼지로 인해 전국이 까만 하늘로 뒤덮힐 예정입니다. 외출에 각별히 유의해주시고 ...
                    </div>
                    <div className="companies">
                        웅진
                    </div>
                </div>
            </div>
        );
    }
};
1
export default Newsline;