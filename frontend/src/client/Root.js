import React, { Component } from "react";
import { BrowserRouter } from 'react-router-dom';
import { Provider } from 'react-redux';
import { createStore } from 'redux';
import rootReducer from '../store/modules';
import App from '../App';

const store = createStore(rootReducer);
console.log(store.getState());

const Root = () =>{
    return(
        <Provider store={store}>
            <BrowserRouter>
                <App/>
            </BrowserRouter>
        </Provider>
    );
}


export default Root;