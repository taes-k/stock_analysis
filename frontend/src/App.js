import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import News from './News'

class App extends Component {
  render() {
    return (
      <div className="App">
        <News />
        <News title="수출 7조원 달성" contents="2019년 04월 19일 수출이 7조원이 달성했습니다."/>
        <News title="KBO 홈런왕" contents="KIA 나지완 200홈런-LG 김민성 100홈런 달성"/>
      </div>
    );
  }
}

export default App;
