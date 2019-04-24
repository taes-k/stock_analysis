# React Boilerplate  
본 프로젝트는 React + Webpack + Babel + Redux 기반의 프로젝트를 시작함에 있어서 간편하게 사용할 수 있는 초기 프로젝트 모델 공유용으로 제작되었다.  

## 개발환경
- Node 10.15.3
- Webpack 4.30.0
- Babel 7.4.3
- React 16.8.6
- Redux 4.0.7

## 패키지 구성
```c
node_modules/
src/
ㄴ index.js
ㄴ index.css
ㄴ App.js
ㄴ client
  ㄴ Root.js : react-router, redux store 설정
ㄴ page
  ㄴ index.js : page 통합 export
  ㄴ Home.js
  ㄴ Home.css
  ㄴ Todo.js
  ㄴ Todo.css
ㄴ components : componenet
  ㄴ TodoComponent.js
ㄴ store : redux store module
  ㄴ modules     
    ㄴ index.js
    ㄴ todo.js
ㄴ template
  ㄴ index.html      
.babelrc : babel 설정파일
package-lock.json   
package.json
webpack.config.js : webpack 설정파일
```

## 렌더링 과정

`src/index.js`  

`src/client/Root.js`  

`src/App.js`  

`src/page/Home.js`  

`src/components/TodoComponent.js`  

## script
`npm run start` : react 시작  
`npm run build` : build 

