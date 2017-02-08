var Bitly = (function () {
    var x_login,
        x_apiKey,
        format = 'json',
        apiUrl = "http://api.bit.ly/v3/shorten?",
        callbackHandler,
        e,
        head = document.getElementsByTagName("head")[0];

   function constructUrl (longUrl) {
        var q = "";
        
        if (x_login && x_apiKey) {
            q += "login=" + x_login + "&apiKey=" + x_apiKey + "&";
        }
        
        q += "longUrl=" + encodeURIComponent(longUrl) + "&format=json&callback=Bitly.callback";
        
        return apiUrl + q;
    }
    
    return {
        setLogin: function (login) {
            x_login = login || "";
            return this;
        },
        
        setKey: function (apiKey) {
            x_apiKey = apiKey || "";
            return this;
        },

       setCallback: function (fn) {
            if (typeof fn !== 'function') {
                throw new Error("Bitly: callback must be a function.");
            }

           callbackHandler = fn;

           return this;
        },

       shorten: function (longUrl) {
            e = document.createElement("script");
            e.src = constructUrl(longUrl);
                
            head.appendChild(e);
        },
        
        // TODO
        expand: function (shortUrl) {
        },

       // TODO
        validate: function () {
        },

       callback: function (response) {
            callbackHandler(response);
        }
    };
}());