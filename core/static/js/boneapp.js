// function newWord() {
// 	document.getElementById("result1").style.display = "none";
// 	document.getElementById("result2").style.display = "none";
// 	document.getElementById("check").innerText= "Generate";
// 	document.getElementById("check").setAttribute("onClick", "javascript: saveInput();");
// 	document.getElementById("actualWord").innerText= "K ER N AH L";
// }

function saveInput() {
			if (document.getElementById("check").innerHTML == "New Phrase!") {

    	document.getElementById("result1").innerHTML= "A Screwdriver";
    	document.getElementById("result2").innerHTML= "Ask Rude Arrive Her";
    }
	
    var input = document.getElementById("userInput").value;
    document.getElementById("result1").style.visibility = "visible";
    document.getElementById("result2").style.visibility = "visible";
    document.getElementById("check").innerText= "New Phrase!";
    document.getElementById("userInput").value = '';
    	// document.getElementById("userInput").style.border="3.5px solid #ff4d4d";
    	// document.getElementById("correct").style.display = "none";
    	// document.getElementById("incorrect").style.display = "block";
}
	

function madGab() {
	var input = document.getElementById("userInput").value;
	document.getElementById("userInput").value = '';
	document.getElementById("reveal").style.display = "block";
	 $.ajax({
    url: '/getPhrase?phrase='+input,
    type: 'GET',
    contentType: "application/json",
    // data: {
    //     phrase: input
    // },
    success: function(data) {
        console.log(data);
        document.getElementById("result1").innerHTML= input;
        document.getElementById("result2").innerHTML= data;
        document.getElementById("result1").style.visibility = "hidden";
    	document.getElementById("result2").style.visibility = "visible";
    }
  });
}

function reveal() {
	document.getElementById("reveal").style.display = "none";
	document.getElementById("result1").style.visibility = "visible";
}