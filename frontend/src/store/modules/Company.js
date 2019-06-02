//Type
const ADD_COMPANY = "ADD_COMPANY"

//Action
function addCompany(value){
    return{
        type: ADD_COMPANY,
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
            yesterday_price: value.yesterday_price
        }
    }
}

//State
const initState = {
    company :{
        '000000':
        {
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
            yesterday_price: 0
        }
    },
    count : 0
}

//Reducer
function companyReducer(state = initState, action) {
    switch (action.type) {
    case ADD_COMPANY:
        let companyDic = state.company;
        companyDic[action.data.code] = action.data

        return Object.assign({}, state, {
            company: companyDic,
            count: state.count+1
        });
    default:
        return state;
    }
}


// Export
const companyActionCreators = {
    addCompany
};
export { companyActionCreators };  // action export
export default companyReducer;     // reducer export