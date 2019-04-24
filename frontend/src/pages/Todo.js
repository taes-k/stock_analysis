import React, { Component } from "react";

class Todo extends Component{
    render (){
        return (
            <div className="Todo">
                <p>Todo : { this.props.match.params.title }</p>
            </div>
        );
    }
};

export default Todo;