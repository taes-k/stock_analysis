//Type
const ADD_NEWS = "ADD_NEWS"
const DEL_NEWS = "DEL_NEWS"

//Action
function addNews(value){
    return{
        type: ADD_NEWS,
        data: {
            url : value.url,
            title : value.title,
            contents : value.contents,
            date : value.date,
            profile : value.profile,
            positivie : value.positive,
            keyword : value.keyword,
            company : value.company
        }
    }
}

function deleteNews(){
    return{
        type: DEL_NEWS
    }
}

//State
const initTodoCountState = {
    news :[
        {
         url : "",
         title : "",
         contents : "",
         date : "",
         profile : "",
         positivie : 0,
         keyword : [],
         company : []
        }
    ],
    count : 0
}

//Reducer
function newsReducer(state = initTodoCountState, action) {
    switch (action.type) {
    case ADD_NEWS:
        console.log(state)
        let newsArr = state.news;
        if(state.count == 0){
            let newArr = []
            newArr.push(action.data);
            newsArr = newArr
        }else
            newsArr.push(action.data) 

        return Object.assign({}, state, {
            news: newsArr,
            count: state.count+1
        });
    case DEL_NEWS:
        return Object.assign({}, state, {
            news: [],
            count: 0
        });
    default:
        return state;
    }
}


// Export
const newsActionCreators = {
    addNews,
    deleteNews
};
export { newsActionCreators };  // action export
export default newsReducer;     // reducer export