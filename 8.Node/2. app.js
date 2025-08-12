// from flask import Flask
const express = require('express') 

// app = Flask(__name__)
const app = express() 

// @app.route('/')
// def index():
//     return 'hello, world from flask'
app.get('/', (req, res) => {
    res.send('hello, world from node.js')
})

// app.run()
app.listen(3000, () => {
    console.log('서버가 준비 되었음...');
});

// python app.py
// node app.js

// react
// npm install create-react-app -> ??
// npm install -g create-react-app -> 내 글로벌에 설치 / 무거움..
// npx create-react-app my-app -> 한번만
