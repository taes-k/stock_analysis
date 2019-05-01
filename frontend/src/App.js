import React, { Component } from "react";
import { Route } from "react-router-dom";
import { Home, Search, Company } from "./pages";

class App extends Component{
    render (){
        return (
            <div>
                <Route exact path="/" component={Home}/>
                <Route path="/search/:text" component={Search}/>
                <Route path="/company/:id" component={Company}/>
            </div>
        );
    }
};

export default App;