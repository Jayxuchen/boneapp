// function newWord() {
// 	document.getElementById("result1").style.display = "none";
// 	document.getElementById("result2").style.display = "none";
// 	document.getElementById("check").innerText= "Generate";
// 	document.getElementById("check").setAttribute("onClick", "javascript: saveInput();");
// 	document.getElementById("actualWord").innerText= "K ER N AH L";
// }

function saveInput() {
    var input = document.getElementById("userInput").value;
    document.getElementById("check").innerText= "New Phrase!";
    document.getElementById("userInput").value = '';
    //document.getElementById("check").setAttribute("onClick", "javascript: newWord();");
    document.getElementById("result1").style.visibility = "visible";
    document.getElementById("result2").style.visibility = "visible";

    	
    	document.getElementById("result1").innerHTML= "A Screwdriver";
    	document.getElementById("result2").innerHTML= "Ask Rude Arrive Her";

    	// document.getElementById("userInput").style.border="3.5px solid #85e085";
    	// document.getElementById("incorrect").style.display = "none";
    	// document.getElementById("correct").style.display = "block";
    	// document.getElementById("userInput").style.border="3.5px solid #ff4d4d";
    	// document.getElementById("correct").style.display = "none";
    	// document.getElementById("incorrect").style.display = "block";
}