//Type
const ADD_TODO_COUNT = "ADD_TODO_COUNT"
const SUB_TODO_COUNT = "SUB_TODO_COUNT"

//Action
function addTodoCount(value){
    return{
        type: ADD_TODO_COUNT,
        diff: value
    }
}

function subTodoCount(value){
    return{
        type: SUB_TODO_COUNT,
        val: value
    }
}

//State
const initTodoCountState = {
    count : 0
}

//Reducer
function reducer(state = initTodoCountState, action) {
    switch (action.type) {
    case ADD_TODO_COUNT:
    case SUB_TODO_COUNT:
        console.log(state)
        return Object.assign({}, state, {
            count: state.count + action.val
        });
    default:
        return state;
    }
}


// Export
const actionCreators = {
    addTodoCount,
    subTodoCount
};
export { actionCreators };  // action export
export default reducer;     // reducer export