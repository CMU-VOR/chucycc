function submitMapForm(input) {
    $('#input-field').val(input);
    $('#mapform').submit();
}

var recognizer = new webkitSpeechRecognition();
recognizer.lang = "en";
recognizer.continuous = true;
recognizer.onresult = function(event) {
    if (event.results.length > 0) {
        var result = event.results[event.results.length-1];
        if(result.isFinal) {
        	var text = result[0].transcript;
            console.log(text);
            $('.input').val(text);
            $('#inputform').submit();
        }
    }  
};

function audiobutton() {
	recognizer.start();
}
