import { combineReducers } from 'redux';
import newsReducer from './News';
import companyReducer from './Company'

//통합 리듀서 모듈
export default combineReducers({
    newsReducer,
    companyReducer
});