$(document).ready(function(){
    console.log("Script loaded."); // Debugging message

    $('#btn_translate').click(function(){
        console.log("Translate button clicked."); // Debugging message

        const languageCode = $('#language_code').val();
        console.log("Language code:", languageCode); // Debugging message

        const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
        console.log("API URL:", apiUrl); // Debugging message
        
        $.get(apiUrl, { lang: languageCode }, function(data){
            console.log("API Response:", data); // Debugging message
            $('#hello').text(data.hello);
        });
    });
});
