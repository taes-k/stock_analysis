import React, { Component } from 'react';

class News extends Component {
  state = {
    like: 0,
    news:{
      title: '제목',
      contents: '내용',
    }
  }

  likeIncrease = () => {
    this.setState({
      like: this.state.like + 1
    });
  }

  componentDidMount(){
    this.setState({
      news:{
        title: this.props.title,
        contents: this.props.contents
      }
    })
  }

  componentDidUpdate(prevProps, prevState){
     console.log("STATE Change : ",prevState)
  }

  render() {
    return (
      <div className="News">

        <div class="Title">
          {this.state.news.title}
        </div>
        <div class="Contents">
          {this.state.news.contents}
        </div>


        <div>Like :{this.state.like}</div>
        <button onClick={this.likeIncrease}>Like</button>
      </div>
    );
  }
}

export default News;
