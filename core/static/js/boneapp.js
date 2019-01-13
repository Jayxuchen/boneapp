function newWord() {
	document.getElementById("incorrect").style.display = "none";
	document.getElementById("correct").style.display = "none";
	document.getElementById("check").innerText= "Check";
	document.getElementById("check").setAttribute("onClick", "javascript: saveInput();");
	document.getElementById("yourWord").innerText= "Your Word: K ER N AH L";
}

function saveInput() {
    var input = document.getElementById("userInput").value;
    document.getElementById("check").innerText= "New Phrase";
    document.getElementById("check").setAttribute("onClick", "javascript: newWord();");
    document.getElementById("result1").style.display = "block";
    document.getElementById("result2").style.display = "block";

    	// document.getElementById("userInput").style.border="3.5px solid #85e085";
    	// document.getElementById("incorrect").style.display = "none";
    	// document.getElementById("correct").style.display = "block";
    	// document.getElementById("userInput").style.border="3.5px solid #ff4d4d";
    	// document.getElementById("correct").style.display = "none";
    	// document.getElementById("incorrect").style.display = "block";
}