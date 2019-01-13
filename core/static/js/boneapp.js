function saveInput() {
    var input = document.getElementById("userInput").value;
    document.getElementById("check").innerText= "New Word";
    if (input == "egregious") {
    	document.getElementById("userInput").style.border="3.5px solid #85e085";
    	document.getElementById("incorrect").style.display = "none";
    	document.getElementById("correct").style.display = "block";
    }
    else {
    	document.getElementById("userInput").style.border="3.5px solid #ff4d4d";
    	document.getElementById("correct").style.display = "none";
    	document.getElementById("incorrect").style.display = "block";
    }
}