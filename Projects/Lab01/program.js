//Check if this is actually the Google search engine and not some other google site.
function isSearch(){
    const classname = document.getElementsByClassName("RNNXgb"); //Class present on one of the divs of the Google search bar.

    if(classname != undefined && classname != null)
        return true;
    else
        return false;
}

//Get URL od current page.
const url = window.location.href;

//Only run on Google domain.
if(url.includes(".google.") && isSearch()){
    //Initialization///////////////////////////////////////////////////////////
    let configuration = {
      
        "adsDisplay" : "normal", //"remove", "standOut"
        "adBackgroundColor" : "antiquewhite",
        "removeEmojis": false,
       "themeDisplay" : "tumbleweed", //"oldBlues", "limeChild"
        "images": false,
      
    };

      //Store defaults if nothing is stored.
      chrome.storage.sync.get(['configuration'], function(storedConfiguration) {
        if('configuration' in storedConfiguration)
            configuration = storedConfiguration;
        else
            chrome.storage.sync.set({'configuration': configuration}, function(){});

        modifySearchResults(configuration["configuration"]);
    });
}


//Receive data from popup.js////////////////////////////////////////////

chrome.runtime.onMessage.addListener(receivedMessage);

function receivedMessage(message, sender, response){
    modifySearchResults(message["configuration"]);
}

/////////////////////////////////////////////////////////////////////////


//Main Function//////////////////////////////////////////////////////////

function modifySearchResults(configuration){
    //Remove Url////////////////////////////////////////////////////////
    //Images next to/in some search results
    if(configuration.images){
        ApplyToClass("SD80kd", function(element){
            element.style.display = "none";
        });

        ApplyToClass("FxLDp", function(element){
            element.style.padding = "0";
        });
    }

    if(configuration.removeEmojis){
        //Make list of elements to be processed.
        let listOfElementLists = [
            document.getElementsByClassName("LC20lb"),
            document.getElementsByClassName("st"),
            document.getElementsByClassName("cbphWd"),
            document.getElementsByClassName("fl")
        ];
    //For each element take it's inner text replace any emojis with '' and save the new string back into the element.
    forEachDoThis(listOfElementLists, function(element){
        const cleanedString =element.innerText.replace(/([\u2700-\u27BF]|[\uE000-\uF8FF]|\uD83C[\uDC00-\uDFFF]|\uD83D[\uDC00-\uDFFF]|[\u2011-\u26FF]|\uD83E[\uDD10-\uDDFF])/g, '');
        if(element.innerText != cleanedString)
            element.innerText = cleanedString;
    });
}


}