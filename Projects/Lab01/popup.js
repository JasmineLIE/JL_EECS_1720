

window.addEventListener('load', (event) => {
    //Initialization////////////////////////////////////////////////////
    chrome.storage.sync.get(['configuration'], function(configuration) {
        setUI(configuration["configuration"]);
    });

    ////////////////////////////////////////////////////////////////////

    //Events////////////////////////////////////////////////////////////

    //Checkbox events//////////////////////


    document.getElementById("colorUrlCheckBox").addEventListener("change", event =>{
        changeConfig("colorUrl", event.target.checked);
    });

  

  

    document.getElementById("imagesCheckBox").addEventListener("change", event =>{
        changeConfig("images", event.target.checked);
    });

;

    //Color Selection /////
    document.getElementById("adBackgroundColorSelection").addEventListener("change", event =>{
        changeConfig("adBackgroundColor", event.target.value);
    });






    //Radio events/////////
    var classname = document.getElementsByClassName("adsDisplay");

    for (var i = 0; i < classname.length; i++) {
        classname[i].addEventListener('change', setAdSettings, false);
    }

    function setAdSettings(){
        changeConfig("adsDisplay", this.value);
    }

    ///////////////////////

    //Functions////////////////////////////////////////////////////////////

    function setUI(configuration){
    
        document.getElementById("colorUrlCheckBox").checked = configuration.colorUrl;
        document.getElementById("removeEmojisCheckBox").checked = configuration.removeEmojis;

        document.getElementById("imagesCheckBox").checked = configuration.images;
       
        document.getElementById("adBackgroundColorSelection").value  = configuration.adBackgroundColor;


        var classname = document.getElementsByClassName("adsDisplay");

        for (var i = 0; i < classname.length; i++) {
            if(classname[i].value == configuration.adsDisplay){
                classname[i].checked = true;
            }
        }
    }

    function changeConfig(key, value){
        chrome.storage.sync.get(['configuration'], function(configuration) {
            configuration["configuration"][key] = value;

            chrome.storage.sync.set({'configuration': configuration["configuration"]}, function(){});

            sendToProgramJS(configuration);
        });
    }

    function sendToProgramJS(payload){
        chrome.tabs.query({currentWindow: true, active: true}, function (tabs){
            chrome.tabs.sendMessage(tabs[0].id, payload);
        });
    }

    //////////////////////////////////////////////////////////////////////
});
