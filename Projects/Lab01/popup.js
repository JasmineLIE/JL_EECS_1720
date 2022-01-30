

window.addEventListener('load', (event) => {
    //Initialization////////////////////////////////////////////////////
    chrome.storage.sync.get(['configuration'], function(configuration) {
      setUI(configuration["configuration"]);
    }
    );
  
    ////////////////////////////////////////////////////////////////////
  
    //Events////////////////////////////////////////////////////////////
  
    //Checkbox events//////////////////////
  
    document.getElementById("removeUrlCheckBox").addEventListener("change", event => {
      changeConfig("removeUrl", event.target.checked);
    }
    );
  
    document.getElementById("removeArrowCheckBox").addEventListener("change", event => {
      changeConfig("removeArrow", event.target.checked);
    }
    );
  
    document.getElementById("moveCheckBox").addEventListener("change", event => {
      changeConfig("moveUrl", event.target.checked);
    }
    );
  
  
  
    //Button///////////////
    document.getElementById("defaultSettings").addEventListener("click", restoreDefaultConfig);
  
    function restoreDefaultConfig() {
      const defaultConfiguration = {
      "configuration":
      {
      "themeDisplay": 
        "tumbleweed", 
        "removeUrl": 
        false, 
        "removeArrow": 
        false, 
        "moveUrl": 
        false
      }
    }
  
    sendToProgramJS(defaultConfiguration);
  
    setUI(defaultConfiguration["configuration"]);
  
    chrome.storage.sync.set( {
    'configuration': 
      defaultConfiguration["configuration"]
    }
    , function() {
    }
    );
  }
  
  ///////////////////////
  
  //Radio events/////////
  var classname = document.getElementsByClassName("themeDisplay");
  
  for (var i = 0; i < classname.length; i++) {
    classname[i].addEventListener('change', setThemeSettings, false);
  }
  
  function setThemeSettings() {
    changeConfig("themeDisplay", this.value);
  }
  
  ///////////////////////
  
  //Functions////////////////////////////////////////////////////////////
  
  function setUI(configuration) {
    document.getElementById("removeUrlCheckBox").checked = configuration.removeUrl;
    document.getElementById("removeArrowCheckBox").checked = configuration.removeArrow;
    document.getElementById("moveCheckBox").checked = configuration.moveUrl;
  
  
  
    var classname = document.getElementsByClassName("themeDisplay");
  
    for (var i = 0; i < classname.length; i++) {
      if (classname[i].value == configuration.themeDisplay) {
        classname[i].checked = true;
      }
    }
  }
  
  function changeConfig(key, value) {
    chrome.storage.sync.get(['configuration'], function(configuration) {
      configuration["configuration"][key] = value;
  
      chrome.storage.sync.set( {
      'configuration': 
        configuration["configuration"]
      }
      , function() {
      }
      );
  
      sendToProgramJS(configuration);
    }
    );
  }
  
  function sendToProgramJS(payload) {
    chrome.tabs.query( {
    currentWindow: 
    true, active: 
      true
    }
    , function (tabs) {
      chrome.tabs.sendMessage(tabs[0].id, payload);
    }
    );
  }
  
  //////////////////////////////////////////////////////////////////////
  });
  