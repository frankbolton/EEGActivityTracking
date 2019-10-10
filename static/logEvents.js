console.log("success importing the logEvents code");    

var logEvents = function() {
    return {
       neurosteer_log: function(message){
            var request = new XMLHttpRequest();
            request.open('POST', '/ns_logger', true);
            request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
            var postVars = 'msg='+message+"&sec=secret";
            request.send(postVars);
            return false;
       },
        

    };
}();


//Browser detection of focus change from https://dystroy.org/demos/vis-en.html
//and <a href=http://stackoverflow.com/a/19519701/263525>Code here</a>. 
        
// "librairie" de gestion de la visibilité
        //  var visible = vis(); // donne l'état courant
        //  vis(function(){});   // définit un handler pour les changements de visibilité
        var vis = (function(){
            var stateKey, eventKey, keys = {
                hidden: "visibilitychange",
                webkitHidden: "webkitvisibilitychange",
                mozHidden: "mozvisibilitychange",
                msHidden: "msvisibilitychange"
            };
            for (stateKey in keys) {
                if (stateKey in document) {
                    eventKey = keys[stateKey];
                    break;
                }
            }
            return function(c) {
                if (c) {
                    document.addEventListener(eventKey, c);
                    //document.addEventListener("blur", c);
                    //document.addEventListener("focus", c);
                }
                return !document[stateKey];
            }
        })();
        
        vis(function(){
            //document.title = vis() ? 'Visible' : 'Not visible';
            //console.log(new Date, 'visible ?', vis());
            var obj = new Object();
            obj.name = window.location.pathname.substring(1,);
            if(window.location.pathname == "/"){
                obj.name = 'index';
            }
            obj.visible = vis()? '1' : '0';
            logEvents.neurosteer_log(JSON.stringify(obj));
        });
        
        // to set the initial state
        //document.title = vis() ? 'Visible' : 'Not visible';