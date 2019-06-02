//Type
const ADD_NEWS_INIT = "ADD_NEWS_INIT"
const ADD_NEWS = "ADD_NEWS"
const INSERT_NEWS = "INSERT_NEWS"
const DEL_NEWS = "DEL_NEWS"

//Action
function addNewsInit(){
    return{
        type: ADD_NEWS_INIT
    }
}

function addNews(value){
    return{
        type: ADD_NEWS,
        data: {
            url : value.url,
            title : value.title,
            contents : value.contents,
            crawlingDate : value.crawlingDate,
            date : value.date,
            profile : value.profile,
            positive : value.positive,
            keyword : value.keyword,
            company : value.company
        }
    }
}

function insertNews(value){
    return{
        type: INSERT_NEWS,
        data: {
            url : value.url,
            title : value.title,
            contents : value.contents,
            crawlingDate : value.crawlingDate,
            date : value.date,
            profile : value.profile,
            positive : value.positive,
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
         crawlingDate : "",
         date : "",
         profile : "",
         positive : 0,
         keyword : [],
         company : []
        }
    ],
    count : 0,
    isUpdated : false,
}

//Reducer
function newsReducer(state = initTodoCountState, action) {
    let newsArr = state.news;

    switch (action.type) {
    case ADD_NEWS_INIT:
        return Object.assign({}, state, {
            isUpdated: true
        });
    case ADD_NEWS:
        if(state.count == 0){
            let newArr = []
            newArr.push(action.data);
            newsArr = newArr
        }else
            newsArr.push(action.data) 

        return Object.assign({}, state, {
            news: newsArr,
            count: state.count+1,
            isUpdated: true
        });
        break;
    case INSERT_NEWS:
        newsArr.unshift(action.data)
        return Object.assign({}, state, {
            news: newsArr,
            count: state.count+1,
            isUpdated: true
        });
        break;
    case DEL_NEWS:
        return Object.assign({}, state, {
            news: [],
            count: 0,
            isUpdated: false
        });
    default:
        return state;
    }
}


// Export
const newsActionCreators = {
    addNewsInit,
    addNews,
    insertNews,
    deleteNews
};
export { newsActionCreators };  // action export
export default newsReducer;     // reducer export