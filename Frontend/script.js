const benchList = document.getElementById('benchList');
const fetchBtn = document.querySelector('.fetch-btn');
const userInput = document.querySelector('.user-input');

fetchBtn.addEventListener('click', ()=> clickFunction(userInput.value));

var list;

function testFunc(input){
    list = input
    console.log(list.bench_history);
    benchList.innerHTML = list.bench_history.join('<br />');
}

fetch('http://127.0.0.1:8000/bench_history/smoer')
    .then(data => data.json())
    .then(data => testFunc(data))

// Function to save data from fetch
function myFunc(data) {
console.log(data.bench_history)   
//benchList.innerHTML = data //.join('\r\n'); // adds it to html site
};

function clickFunction(input){
    fetch('http://127.0.0.1:8000/'+input)
    .then(data => data.json())
    .then(data => myFunc(data))
}



function fetchData(input){
    fetch('http://127.0.0.1:8000/'+input)
    .then(data => data.json())
    .then(success => myFunc(success))
}




// fetch data
/*fetch('http://127.0.0.1:8000/bench-list/')
    .then(data => data.json())
    .then(success => myFunc(success)); */