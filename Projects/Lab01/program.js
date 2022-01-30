//Check if this is actually the Google search engine and not some other google site.
function isSearch() {
    const classname = document.getElementsByClassName("RNNXgb"); //Class present on one of the divs of the Google search bar.
  
    if (classname != undefined && classname != null)
      return true;
    else
      return false;
  }
  
  //Get URL od current page.
  const url = window.location.href;
  
  //Only run on Google domain.
  if (url.includes(".google.") && isSearch()) {
    //Initialization///////////////////////////////////////////////////////////
  
    let configuration = {
    "themeDisplay": 
    "tumbleweed", //"oldBlues", "limeChild", "rebel", "lilac"
    "removeUrl" : 
    false, 
    "removeArrow" : 
    false, 
    "moveUrl": 
    false
  };
  
  //Store defaults if nothing is stored.
  chrome.storage.sync.get(['configuration'], function(storedConfiguration) {
    if ('configuration' in storedConfiguration)
    configuration = storedConfiguration;
    else
    chrome.storage.sync.set( {
    'configuration': 
      configuration
    }
    , function() {
    }
    );
  
    modifySearchResults(configuration["configuration"]);
  }
  );
  }
  
  
  ////////////////////////////////////////////////////////////////////////
  
  
  //Receive data from popup.js////////////////////////////////////////////
  
  chrome.runtime.onMessage.addListener(receivedMessage);
  
  function receivedMessage(message, sender, response) {
    modifySearchResults(message["configuration"]);
  }
  
  /////////////////////////////////////////////////////////////////////////
  
  
  //Main Function//////////////////////////////////////////////////////////
  
  function modifySearchResults(configuration) {
    //Remove Url////////////////////////////////////////////////////////
    if (configuration.removeUrl) {
      //Remove url and icon.
      removeElements(".TbwUpd", 0);
      //Remove url and icon on the litle pages thingy that appears.
      removeElements(".qdrjAc", 0);
  
      //Decrease distance between results.
      decreaseResultDistance("TbwUpd"); //Normal results.
    }
  
  
    //Remove arrows at the end of urls////////////////////////////////////
    if (configuration.removeArrow || configuration.removeUrl || configuration.moveUrl) {
      //Remove arrow.
      removeElements(".B6fmyf", 0);
      //Remove arrow from ad.
      removeElements(".e1ycic", 0);
      //Remove 3 dots if present instaed of arrow.
      removeElements(".D6lY4c", 0);
      removeElements(".rIbAWc", 0);
    }
  
  
  
  
  
    //Move Url////////////////////////////////////////////////////////////////
    if (configuration.moveUrl) {
      cutPasteUrl();
      cutPasteUrlPagesThingy();
  
      //Decrease distance between results.
      decreaseResultDistance("TbwUpd"); //Normal results.
    }
  
  
    //MoveUrl////////////////////////////////////////////////////////////////
    if (configuration.moveUrl && (configuration.adsDisplay != "remove")) {
      cutPasteUrlAds();
  
      //Decrease distance between results.
      decreaseResultDistance("sA5rQ"); //Ads
      decreaseResultDistance("TbwUpd"); //Normal results.
    }
  
  
    if (configuration.themeDisplay == "tumbleweed" || configuration.themeDisplay == "oldBlues" || configuration.display == "limeChild") {
      var footer = document.querySelector('footer')
    } 
    if (configuration.themeDisplay == "tumbleweed") {
  
      document.documentElement.style.setProperty('--text', '#FFC300');
      document.documentElement.style.setProperty('--bg', '#ff9100');
      document.documentElement.style.setProperty('--stroke', '#A75E00 ');
    } 
    if (configuration.themeDisplay == "oldBlues") {
      document.documentElement.style.setProperty('--text', '#00FFE8');
      document.documentElement.style.setProperty('--bg', '#0082FF');
      document.documentElement.style.setProperty('--stroke', '#0039BB ');
    } 
    if (configuration.themeDisplay == "limeChild") {
  
      document.documentElement.style.setProperty('--text', '#B5FF00 ');
      document.documentElement.style.setProperty('--bg', '#1DA000 ');
      document.documentElement.style.setProperty('--stroke', '#009143 ');
    } 
    if (configuration.themeDisplay == "rebel") {
  
      document.documentElement.style.setProperty('--text', '#ff4929');
      document.documentElement.style.setProperty('--bg', '#940700');
      document.documentElement.style.setProperty('--stroke', '#7d0800');
    } 
    if (configuration.themeDisplay == "lilac") {
  
      document.documentElement.style.setProperty('--text', '#e49cff ');
      document.documentElement.style.setProperty('--bg', '#c300ff');
      document.documentElement.style.setProperty('--stroke', '#5900b3');
    }
  }
  
  ////////////////////////////////////////////////////////////////////////////////
  
  
  
  //Search results modification functions/////////////////////////////////////////
  
  
  
  function cutPasteUrl() {
    let elements = document.getElementsByClassName("TbwUpd");
    let elementsArrow = document.getElementsByClassName("eFM0qc");
  
    //Set elements to flex to always push url under title.
    for (let i = 0; i < elements.length; i++) {
      elements[i].style.display = "flex";
    }
  
    let elementsG = document.getElementsByClassName("g");
    //Decrese margin.
    for (let i = 0; i < elementsG.length; i++) {
      elementsG[i].style.margin = "0px 0px 20px 0px";
    }
  
    //Remove <br>.
    for (let i = 0; i < elements.length; i++) {
      let brTags = elements[i].parentNode.getElementsByTagName("BR");
      for (berTag of brTags) {
        berTag.parentNode.removeChild(berTag);
      }
    }
  
    //Insert url into new position.
    for (let i = 0; i < elements.length; i++) {
      if (!elements[i].className.includes("NJjxre")) {
        let element = elements[i]; //Get url element.
        let parentElement = element.parentNode.parentNode; //Get parent element
  
        //Get the element before which the url has to be inserted.
        insertBeforeElement = parentElement.childNodes[0];
  
        //insert element in new position.
        insertAfter(element, insertBeforeElement); //parentElement.insertBefore(element, insertBeforeElement);
      }
    }
  
    //Remove elements.
    for (let i = 0; elements.length > i; i++) {
      if (elements[i].className.includes("NJjxre")) {
        //Remove element.
        elements[i].parentNode.removeChild(elements[i]);
        i--;
      }
    }
  }
  
  function cutPasteUrlAds() {
    let elements = document.getElementsByClassName("ads-visurl");
  
    for (let i = 0; i < elements.length; i++) {
      if (!elements[i].className.includes("NJjxre")) {
        let element = elements[i]; //Get url element.
        let parentElement = element.parentNode.parentNode; //Get parent element
  
        //Get the element before which the url has to be inserted.
        insertBeforeElement = parentElement.childNodes[0];
  
        //insert element in new position.
        insertAfter(element, insertBeforeElement); //parentElement.insertBefore(element, insertBeforeElement);
      }
    }
  }
  
  function cutPasteUrlPagesThingy() {
    let elements = document.getElementsByClassName("qdrjAc");
    let elementsConst = [];
  
    for (let i = 0; i < elements.length; i++) {
      elementsConst.push(elements[i].getAttribute('class'));
    }
  
    for (let i = 0; i < elements.length; i++) {
      //if(!elementsConst[i].includes("qks8td")){
      let element = elements[i];
      let parentElement = element.parentNode.parentNode.parentNode;
  
      elements[i].parentNode.removeChild(elements[i]);
  
      insertBeforeElement = parentElement.childNodes[1]
  
        parentElement.insertBefore(element, insertBeforeElement);
      //}
    }
  }
  
  function decreaseResultDistance(className) {
    elements = document.getElementsByClassName(className);
  
    for (let i = 0; i < elements.length; i++) {
      br = elements[i].parentNode.getElementsByTagName('br');
      if (br.length != 0)
        br[0].parentNode.removeChild(br[0]);
    }
  }
  
  ////////////////////////////////////////////////////////////////////////////////
  
  
  
  //Utils/////////////////////////////////////////////////////////////////////////
  
  function removeElements(name, parentNum) {
    if (name[0] == '.') {
      name = name.replace('.', '');
      const elements = document.getElementsByClassName(name);
  
      for (let i = 0; i < elements.length; i++) {
        let node = getParentNode(elements[i], parentNum);
        node.style.display = 'none';
      }
    } else if (name[0] == '#') {
      name = name.replace('#', '');
  
      const element = document.getElementById(name);
  
      if (element != null)
        getParentNode(element, parentNum).style.display = 'none';
    } else {
      throw "Undefined element!";
    }
  }
  
  function getParentNode(element, parentNum) {
    let parent = element;
  
    for (let i = 0; parentNum > i; i++)
      parent = parent.parentNode
  
        return parent;
  }
  
  function ApplyToClass(className, delegate) {
    let elements = document.getElementsByClassName(className);
  
    for (let i = 0; i < elements.length; i++)
      delegate(elements[i]);
  }
  
  function forEachDoThis(listOfElementLists, delegate) {
    for (let elementList of listOfElementLists) {
      for (element of elementList) {
        delegate(element);
      }
    }
  }
  
  function insertAfter(newNode, referenceNode) {
    referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
  }
  
  /////////////////////////////////////////////////////////////////////////////////
  