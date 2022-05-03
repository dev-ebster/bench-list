
const rosterGridContainer = document.querySelector('.roster-grid-container');
const hiddenDiv = document.querySelector('.hiddenDiv');
const rightSide = document.querySelector('.right-side');

let hunters =[];
let priests =[];
let shamans =[];
let paladins =[];
let warlocks =[];
let warriors =[];
let rogues =[];
let druids =[];
let mages =[];



//fetch('http://127.0.0.1:8000/players')
//.then(response => response.json())
//.then(data => loopThrough(data))




fetch('http://127.0.0.1:8000/players')
.then(response => response.json())
.then(data => consoleCheck(data))

fetch('http://127.0.0.1:8000/bench-list')
.then(response => response.json())
.then(data => addBench(data))




function consoleCheck(input){
    input.forEach(element => {
        // create elems
        const boks = document.createElement('div');
        const img = document.createElement('img');
        const nameP = document.createElement('p');
        const hidden = document.createElement('div');
        const statsDiv = document.createElement('div');
        const statName = document.createElement('p');
        const statClass = document.createElement('p');
        const statSpec = document.createElement('p');
        const statRole = document.createElement('p');
        const statRank = document.createElement('p');
        const logLink = document.createElement('a');

        // add classes
        hidden.classList.add('hiddenDiv');
        hidden.classList.add('hide');
        boks.classList.add('player-grid-elem');

        // add html
        nameP.innerText = element.name
        img.src = "./icons/"+element.class+".png";
        statName.innerText =  "Name: "+element.name
        statClass.innerText = "Class: "+element.class
        statSpec.innerText = "Spec: "+element.spec
        statRole.innerText = "Role: "+element.role
        statRank.innerText = "Rank: "+element.rank
        logLink.innerText = "Warcraft logs"
        logLink.href = "https://classic.warcraftlogs.com/character/eu/mirage-raceway/"+element.name
        logLink.target = "_blank";

        // append to document.
        statsDiv.appendChild(statName);
        statsDiv.appendChild(statClass);
        statsDiv.appendChild(statSpec);
        statsDiv.appendChild(statRole);
        statsDiv.appendChild(statRank);
        statsDiv.appendChild(logLink);
        hidden.appendChild(statsDiv);
        boks.appendChild(nameP);
        boks.appendChild(img);
        boks.appendChild(hidden);
        rosterGridContainer.appendChild(boks);
     
    });
    function toggle(e){
        e.currentTarget.lastChild.classList.toggle('hide');
    }
   const playerGridElems = document.querySelectorAll('.player-grid-elem');
    for (let i=0; i < playerGridElems.length; i++){
        playerGridElems[i].addEventListener('click', toggle)
    } 
}

function addBench(input){

    // ---------- Get player names into class arrays ----------//

    fetch('http://127.0.0.1:8000/players')
    .then(response => response.json())
    .then(data => testCheck(data))
  
    
    function testCheck(input){
        input.forEach(elem => {
            //console.log(elem.class)
            if(elem.class == "hunter"){
                hunters.push(elem.name);
            }
            if(elem.class == "priest"){
                priests.push(elem.name);
            }
            if(elem.class == "shaman"){
                shamans.push(elem.name);
            }
            if(elem.class == "paladin"){
                paladins.push(elem.name);
            }
            if(elem.class == "warlock"){
                warlocks.push(elem.name);
            }
            if(elem.class == "warrior"){
                warriors.push(elem.name);
            }
            if(elem.class == "rogue"){
                rogues.push(elem.name);
            }
            if(elem.class == "druid"){
                druids.push(elem.name);
            }
            if(elem.class == "mage"){
                mages.push(elem.name);
            }
            if(warlocks.includes('metrognome')){
                console.log('nub');
            }
        });
    
    }

   
    

    const benchListDiv = document.createElement('div');
    benchListDiv.classList.add('bench-list-div')
   
    input.forEach(element =>{
        if(hunters.includes(element)){
            console.log('hunter')
        }
        //console.log(element); 
        const listItemBtn = document.createElement('button'); 
        listItemBtn.classList.add('bench-btn');
        listItemBtn.innerText = element
        listItemBtn.classList.add(element)
        benchListDiv.appendChild(listItemBtn);         
    }); 

    rightSide.appendChild(benchListDiv);


    function benchPlayer(e){
        console.log(e.target.innerText);
        const data = { username: 'example' };
        fetch('http://127.0.0.1:8000/bench/'+e.target.innerText, {
            method: 'POST', // or 'PUT'
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });

    }
    
    const benchBtns = document.querySelectorAll('.bench-btn');
        for (let i=0; i < benchBtns.length; i++){
            benchBtns[i].addEventListener('click', benchPlayer)
        }
    
    /*const listItems = document.querySelectorAll('.listItem');
        for (let i=0; i < listItems.length; i++){
         listItems[i].addEventListener('click', loli)
        }*/
    

}




