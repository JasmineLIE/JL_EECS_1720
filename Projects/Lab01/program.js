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

if(configuration.themeDisplay == "tumbleweed" || configuration.themeDisplay == "oldBlues" || configuration.themeDisplay == "limeChild") {
    let bgElement = document.getElementsByTagName("html body");

  
    }
}
 

//Utils/////////////////////////////////////////////////////////////////////////

function removeElements(name, parentNum){
    if(name[0] == '.'){
        name = name.replace('.', '');
        const elements = document.getElementsByClassName(name);

        for (let i = 0; i < elements.length; i++){
            let node = getParentNode(elements[i], parentNum);
            node.style.display = 'none';
        }
    }else if(name[0] == '#'){
        name = name.replace('#', '');

        const element = document.getElementById(name);

        if(element != null)
            getParentNode(element, parentNum).style.display = 'none';
    }else{
        throw "Undefined element!";
    }
}

function getParentNode(element, parentNum){
    let parent = element;

    for(let i = 0; parentNum > i; i++)
        parent = parent.parentNode

    return parent;
}

function ApplyToClass(className, delegate){
    let elements = document.getElementsByClassName(className);

    for (let i = 0; i < elements.length; i++)
        delegate(elements[i]);
}

function forEachDoThis(listOfElementLists, delegate){
    for(let elementList of listOfElementLists){
        for(element of elementList){
            delegate(element);
        }
    }
}

function insertAfter(newNode, referenceNode) {
    referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
}

/////////////////////////////////////////////////////////////////////////////////
