import React, { Component } from "react";
import { Route } from "react-router-dom";
import { Home, Todo } from "./pages";

class App extends Component{
    render (){
        return (
            <div>
                <Route exact path="/" component={Home}/>
                <Route path="/todo/:title" component={Todo}/>
                <Route exact path="/todo" component={Todo}/>
            </div>
        );
    }
};

export default App;