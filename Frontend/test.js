fetch('http://127.0.0.1:8000/bench_list')
.then(response => response.json())
.then(data => console.log(data))

fetch('http://127.0.0.1:8000/players')
.then(response => response.json())
.then(data => console.log(data))


function fetchBenchHistory(input){
    fetch('http://127.0.0.1:8000/bench_history/'+input)
    .then(data => data.json())
    .then(data => console.log(data))
}

function fetchBenchCount(input){
    fetch('http://127.0.0.1:8000/bench_count/'+input)
    .then(data => data.json())
    .then(data => console.log(data))
}

fetchBenchCount('smoer');
fetchBenchHistory('smoer');


const data = { username: 'example' };

fetch('http://127.0.0.1:8000/bench/smoer', {
  method: 'POST', // or 'PUT'
  headers: {
    'Content-Type': 'application/json',
  },
  body: data,
})
.then(response => response.json())
.then(data => {
  console.log('Success:', data);
})
.catch((error) => {
  console.error('Error:', error);
});
