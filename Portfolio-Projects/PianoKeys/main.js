// The keys and notes variables store the piano keys
const keys = ['c-key', 'd-key', 'e-key', 'f-key', 'g-key', 'a-key', 'b-key', 'high-c-key', 'c-sharp-key', 'd-sharp-key', 'f-sharp-key', 'g-sharp-key', 'a-sharp-key'];
const notes = [];
keys.forEach(function(key){
  notes.push(document.getElementById(key));
})

// Write named functions that change the color of the keys below
const keyPlay = (e) => {
    e.target.style.backgroundColor = "green" 
}

// Write a named function with event handler properties
const keyReturn = (e) => {
    e.target.style.backgroundColor = "";
}

// Write a loop that runs the array elements through the function
const this_note = (note) => {
    note.addEventListener("mousedown", keyPlay);
    note.addEventListener("mouseup", keyReturn);
}


notes.forEach(function(note){
    this_note(note)
});


// These variables store the buttons that progress the user through the lyrics
let nextOne = document.getElementById('first-next-line');
let nextTwo = document.getElementById('second-next-line');
let nextThree = document.getElementById('third-next-line');
let startOver = document.getElementById('fourth-next-line');

// This variable stores the '-END' lyric element
let lastLyric = document.getElementById('column-optional');

// These statements are "hiding" all the progress buttons, but the first one
nextTwo.hidden = true;
nextThree.hidden = true;
startOver.hidden= true;

// Write anonymous event handler property and function for the first progress button
nextOne.onclick = function(){
    console.log("clicked")

    nextTwo.hidden = false;
    nextOne.hidden = true;
    document.getElementById('letter-note-five').innerHTML = 'D';   
    document.getElementById('letter-note-six').innerHTML = 'C';   
}

// Write anonymous event handler property and function for the second progress button
nextTwo.onclick = function(){
    console.log("clicked")
    nextThree.hidden = false;
    nextTwo.hidden = true;
    document.getElementById('word-five').innerHTML = 'DEAR';   
    document.getElementById('word-six').innerHTML = 'FRIEND';   
    lastLyric.style.display = "inline-block";
    document.getElementById('letter-note-three').innerHTML = 'G';   
    document.getElementById('letter-note-four').innerHTML = 'E';   
    document.getElementById('letter-note-five').innerHTML = 'C';   
    document.getElementById('letter-note-six').innerHTML = 'B';   
}

// Write anonymous event handler property and function for the third progress button
nextThree.onclick = function(){
    console.log("clicked")
    startOver.hidden= false;        
    nextThree.hidden = true;
    document.getElementById('word-one').innerHTML = 'HAP-';
    document.getElementById('word-two').innerHTML = 'PY';
    document.getElementById('word-three').innerHTML = 'BIRTH';
    document.getElementById('word-four').innerHTML = 'DAY';
    document.getElementById('word-five').innerHTML = 'TO';
    document.getElementById('word-six').innerHTML = 'YOU!';
    lastLyric.style.display = "none";
    document.getElementById('letter-note-one').innerHTML = 'F';
    document.getElementById('letter-note-two').innerHTML = 'F';
    document.getElementById('letter-note-three').innerHTML = 'E';
    document.getElementById('letter-note-four').innerHTML = 'C';
    document.getElementById('letter-note-five').innerHTML = 'D';
    document.getElementById('letter-note-six').innerHTML = 'C';

}


// This is the event handler property and function for the startOver button
startOver.onclick = function() {
    console.log("clicked")
    nextOne.hidden = false;
    startOver.hidden = true;
    document.getElementById('word-one').innerHTML = 'HAP-';
    document.getElementById('letter-note-one').innerHTML = 'G';
    document.getElementById('word-two').innerHTML = 'PY';
    document.getElementById('letter-note-two').innerHTML = 'G';
    document.getElementById('word-three').innerHTML = 'BIRTH-';
    document.getElementById('letter-note-three').innerHTML = 'A';
    document.getElementById('word-four').innerHTML = 'DAY';
    document.getElementById('letter-note-four').innerHTML = 'G';
    document.getElementById('word-five').innerHTML = 'TO';
    document.getElementById('letter-note-five').innerHTML = 'C';
    document.getElementById('word-six').innerHTML = 'YOU!';
    document.getElementById('letter-note-six').innerHTML = 'B';
}