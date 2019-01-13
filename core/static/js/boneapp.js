function saveInput() {
    var input = document.getElementById("userInput").value;
    if (input == "egregious") {
    	document.getElementById("userInput").style.border="3.5px solid #85e085";
    	document.getElementById("check").style.text = "New Word";
    }
    else {
    	document.getElementById("userInput").style.border="3.5px solid #ff4d4d";
    	text.style.display("wrong");
    }
}