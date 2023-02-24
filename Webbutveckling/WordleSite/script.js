var words = [
    "HELLO",
    "WORLD",
    "JAVASCRIPT",
    "COMPUTER",
    "PROGRAM",
    "ENGINEERING",
    "SCIENCE",
    "MATHEMATICS",
    "STATISTICS",
    "ALGORITHMS"
  ];
  
  var word = words[Math.floor(Math.random() * words.length)];
  var guesses = [];
  var maxGuesses = 5;
  var guessesLeft = maxGuesses;
  var circles = [];
  
  function createCircle(x, y) {
    var colors = ["red", "orange", "yellow", "green", "blue", "purple"];
    var colorIndex = guessesLeft - 1;
    var circle = document.createElement("div");
    circle.classList.add("guess-row");
    circle.style.backgroundColor = colors[colorIndex];
    circle.innerHTML = maxGuesses - guessesLeft + 1;
    document.getElementsByClassName("guesses-container")[0].appendChild(circle);
    circles.push(circle);
  }
  
  function createLetterContainer(letter) {
    var letterContainer = document.createElement("div");
    letterContainer.classList.add("letter-container");
    letterContainer.innerHTML = letter;
    document.getElementsByClassName("word-container")[0].appendChild(letterContainer);
  }
  
  function setup() {
    for (var i = 0; i < word.length; i++) {
      guesses.push("_");
      createLetterContainer(guesses[i]);
    }
    for (var i = 0; i < maxGuesses; i++) {
      createCircle(0, 0);
    }
  }
  
  function updateGuesses(letter) {
    var correct = false;
    for (var i = 0; i < word.length; i++) {
      if (word[i] === letter) {
        guesses[i] = letter;
        document.getElementsByClassName("letter-container")[i].innerHTML = letter;
        correct = true;
      }
    }
    if (!correct) {
      guessesLeft--;
      if (guessesLeft === 0) {
        for (var i = 0; i < circles.length; i++) {
          circles[i].classList.add("red");
        }
        alert("You lose! The word was " + word);
        return false;
      } else {
        circles[guessesLeft].classList.add("red");
      }
    }
    if (guesses.join("") === word) {
      alert("You win!");
      return false;
    }
    return true;
  }
  
  function onKeyPress(event) {
    if (event.keyCode >= 65 && event.keyCode <= 90) {
      var letter = String.fromCharCode(event.keyCode);
      if (updateGuesses(letter)) {
        var input = document.createElement("input");
        input.type = "text";
        input.maxLength = 1;
        input.style.fontSize = "24px";
        input.style.width = "40px";
        input.style.height = "40px";
        input.style.textAlign = "center";
        input.style.margin = "10px";
        input.onkeypress = onKeyPress;
        document.getElementsByClassName("input-container")[0].appendChild(input);
        input.focus();
      }
    }
  }
  
  var input = document.createElement("input");
  input.type = "text";
  input.maxLength = 1;
  input.style.fontSize = "24px";
  input.style.width = "40px";
  input.style.height = "40px";
  input.style.textAlign = "center";
  input.style.margin = "10px";
  input.onkeypress = onKeyPress;
  document.getElementsByClassName("input-container")[0].appendChild(input);
  
  setup();
  