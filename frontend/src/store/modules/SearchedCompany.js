//Type
const ADD_SEARCHED_COMPANY = "ADD_SEARCHED_COMPANY"

//Action
function addSearchedCompany(value){
    return{
        type: ADD_SEARCHED_COMPANY,
        data: {
            change_percent: value.change_percent,
            change_price: value.change_price,
            code: value.code,
            current_price: value.current_price,
            market: value.market,
            max_price: value.max_price,
            min_price: value.min_price,
            name: value.name,
            total_price: value.total_price,
            total_stock: value.total_stock,
            trade_count: value.trade_count,
            yesterday_price: value.yesterday_price,
            start_price: value.start_price,
            year_max_price: value.year_max_price,
            year_min_price: value.year_min_price
        }
    }
}

//State
const initState = {
    company :{
        change_percent: 0,
        change_price: 0,
        code: "000000",
        current_price: 0,
        market: "코스피",
        max_price: 0,
        min_price: 0,
        name: "",
        total_price: 0,
        total_stock: 0,
        trade_count: 0,
        yesterday_price: 0,
        start_price: 0,
        year_max_price: 0,
        year_min_price: 0
    },
    count : 0
}

//Reducer
function searchedCompanyReducer(state = initState, action) {
    switch (action.type) {
    case ADD_SEARCHED_COMPANY:
        return Object.assign({}, state, {
            company: action.data,
        });
    default:
        return state;
    }
}


// Export
const searchedCompanyActionCreators = {
    addSearchedCompany
};
export { searchedCompanyActionCreators };  // action export
export default searchedCompanyReducer;     // reducer export