#!/usr/bin/node
$(document).ready(function(){
    $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data){
        $('DIV#character').text(data.name);
    })
});
