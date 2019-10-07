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