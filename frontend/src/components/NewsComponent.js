import React, { Component } from 'react';
import { connect } from 'react-redux';
import news from '../store/modules/News';
import { actionCreators } from '../store/modules/News';
import { Link } from 'react-router-dom';

class TodoComponent extends Component{
constructor(props) {
    super(props);
    this.state = {
        text: props.text,
        link: "/todo/"+props.text,
    }
    this.deleteTodoList = this.deleteTodoList.bind(this);
}
deleteTodoList (){
    this.setState({
        text: "",
        link: ""
    });
    this.props.delTodo()
}

render() {
    return(
        <div className="todo">
            <div className="text">
                <Link to={this.state.link}>{ this.state.text }</Link>
            </div>
            <button onClick={this.deleteTodoList}>Delete</button>
        </div>
        );
    }
}

let mapDispatchToProps = (dispatch) => {
    return {
        delTodo: () => dispatch(actionCreators.subTodoCount(-1))
    }
}

export default connect(undefined,mapDispatchToProps)(TodoComponent);