/*question 1*/
/*
 * 1. Deduplicate an array of mixed types.
 */
dedup = function(arg){
    var resultAry = [];
    var hasDuplicatedElem = false;
    while (arg.length > 0){
        var elem = arg.shift();
        hasDuplicatedElem = false;
        resultAry.forEach(function(resultElem){
            if(Object.prototype.toString.call(elem) === Object.prototype.toString.call(resultElem)){
                if(Object.prototype.toString.call(elem) === "[object Object]"){
                    if(isEqualDict(elem, resultElem)){
                        hasDuplicatedElem = true;
                    }
                }
                else if (Object.prototype.toString.call(elem) === "[object Array]"){
                    if(JSON.stringify(elem) === JSON.stringify(resultElem)){
                        hasDuplicatedElem = true;
                    }
                }
                else{
                    if(elem === resultElem){
                        hasDuplicatedElem = true;
                    }
                }
            }                        
        });
        if(!hasDuplicatedElem){
            resultAry.push(elem);
        }
    }
    
    return resultAry;
}

function isEqualDict(arg_1, arg_2){
    var keys_1 = Object.keys(arg_1).sort();
    var keys_2 = Object.keys(arg_2).sort();
    if(JSON.stringify(keys_1) !== JSON.stringify(keys_2)){
        return false;
    }else{
        keys_1.forEach(function(key){
            if(arg_1[key] !== arg_2[key]){
                return false;
            }
        });
        return true;
    }
}

// Test
var givenAry = [1, "1", 2, 0, false, true, {b: "a", a: "b"},2, {a: "b", b: "a"}, "true",0, {a: "b"}];
console.log(JSON.stringify(dedup(givenAry)));



/*question 2*/
/*
 * 2. Create a prototype for a dog, which adheres to the interface demonstrated below.
 */
var Dog = function(arg_name, arg_age){
    this.name = arg_name;
    this.age = arg_age;
}

Dog.prototype.bark = function(arg){
    if(arg === undefined){
        console.log(this.name + " barks");
    }else if(!isNaN(arg)){
        for(var ith = 0; ith < arg; ith++){
            console.log(this.name + " barks");
        }
    }
    
    if(typeof(arg) === typeof(this)){
        console.log(this.name + " barks at " + arg.name);
    }
}

Dog.prototype.getAge = function(){
    return this.age;
}

Dog.prototype.haveBirthday = function(){
    this.age++;
}

Dog.prototype.befriend = function(arg){
    if(typeof(arg) !== typeof(this)){
        return false;
    }
    if(this.friends === undefined){
        this.friends = [];        
    }
    if(arg.friends === undefined){
        arg.friends = [];
    }
    this.friends.push(arg.name);
    arg.friends.push(this.name);
}

Dog.prototype.getFriends = function(){
    return this.friends;
}

Dog.prototype.removeFriend = function(arg){
    if((typeof(arg) !== typeof(this)) || this.friends === undefined){
        return false;
    }
    var valIndex = this.friends.indexOf(arg.name);
    if(valIndex !== -1){
        this.friends.splice(valIndex, 1);
    }
}
    
var fido = new Dog("Fido", 6);
fido.bark(7);
fido.haveBirthday();
console.log(fido.getAge());

var princess = new Dog("Princess", 7);
princess.bark(fido);
princess.befriend(fido);
console.log(princess.getFriends());
console.log(fido.getFriends());

princess.removeFriend(fido);
console.log(princess.getFriends());


/*question 3*/
/* 
 * 3. Assuming you have the HTML below and jQuery available, please write the JavaScript that
 *    makes it so that when the button is clicked, the background color of the div changes to
 *    the next color in this array: [“red”, “orange”, “yellow”, “green”, “blue”, “indigo”, “violet”].
 *    After one full cycle through the array, it should begin again at the first color in the array.
 *    However, these color changes should be throttled so that it can only be changed 0.5 seconds
 *    after the last change.

 * Available HTLM:
 *   <div id=”main”></div>
 *   <button id=”button”>Rainbow Time!</button>
 */
var colorAry = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];
var colorIndex = 0;
$("#button").click(function() {
    throttled();    
});

function changeBackgroundColor(){
    $("#main").css({'background-color' : colorAry[colorIndex]});
    colorIndex++;
    colorIndex = colorIndex % 7;
}

// throttle
var timeoutAction;
var startAction=true;
var continueAction=false;
function throttled(){
    if( startAction && !continueAction){
        startAction=false;
        continueAction=true;
        throttledAction()
    }
    else{
        continueAction=true;
    }
}

function throttledAction(){
    if(continueAction){
        changeBackgroundColor();
        continueAction=false;
        timeoutAction=setTimeout(throttledAction,500);
    }
    else{
        startAction=true;
        clearTimeout(timeoutAction);
    }
}