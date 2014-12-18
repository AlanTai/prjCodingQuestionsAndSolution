/*
<div id="main">Current Color (solution 1)</div>
<button id="button">Rainbow Time 1!</button>


<br/>
<div id="debounce_before">Current Color (Debounce: Before Action)</div>
<br/>
<div id="debounce_after">Current Color (Debounce: After Action)</div>
*/


var colorAry = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];
var colorIndex = 0;
var colorIndexDebounceBefore = 0;
var colorIndexDebounceAfter = 0;

var new_throttle;
$("#button").click(function() {
    if(new_throttle === undefined){
    new_throttle = new myThrottle(changeBackgroundColor, changeBackgroundColorDebounceBefore, changeBackgroundColorDebounceAfter, 1000);
    }
    new_throttle.startThrottle();
});

function changeBackgroundColor(){
    $("#main").css({'background-color' : colorAry[colorIndex]});
    colorIndex++;
    colorIndex = colorIndex % 7;
}

function changeBackgroundColorDebounceBefore(){
    $("#debounce_before").css({'background-color' : colorAry[colorIndexDebounceBefore]});
    colorIndexDebounceBefore++;
    colorIndexDebounceBefore = colorIndexDebounceBefore % 7;
}

function changeBackgroundColorDebounceAfter(){
    $("#debounce_after").css({'background-color' : colorAry[colorIndexDebounceAfter]});
    colorIndexDebounceAfter++;
    colorIndexDebounceAfter = colorIndexDebounceAfter % 7;
}


// refatoring throttle
var myThrottle = function(callbackThrottle, callbackDebounceBefore, callbackDebounceAfter, timeSpan){
    this.callbackThrottle = callbackThrottle;
    this.callbackDebounceBefore = callbackDebounceBefore;
    this.callbackDebounceAfter = callbackDebounceAfter;
    this.timeSpan = timeSpan;
    
    this.actionAry = [];
    this.isThrottleStarted = false;
    this.timeoutAction;
}

myThrottle.prototype = {
    startThrottle : function(){
        this.actionAry.push(this.callbackThrottle);
        // console.log(this.isThrottleStarted);
        if(!this.isThrottleStarted){
            this.isThrottleStarted = true;
            this.doAction();
            // console.log(this.isThrottleStarted);
            // debounce (before)
            this.callbackDebounceBefore();
        }
    },
    
    doAction : function(){
        if(this.actionAry.length > 0){
            var action = this.actionAry.shift();
            action(); // change background color
            this.timeoutAction = setTimeout(this.doAction.bind(this), this.timeSpan);
        }
        else{
            this.isThrottleStarted=false;
            clearTimeout(this.timeoutAction);
            
            // debounce (after)
            this.callbackDebounceAfter();
        }
    }
}
