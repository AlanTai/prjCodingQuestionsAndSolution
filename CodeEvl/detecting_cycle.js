function myFunction(){
    var str = "2 0 6 3 1 6 3 1 6 3 1";
    var res = str.split(" ");
    var resStr = res.toString();
    var newResStr = "," + resStr.toString() + ",";
    var maxStrLength = Math.floor(res.length / 2);
    var isFound = false;
    for (var ith = maxStrLength; ith > 0 ; ith--){
        for (var jth = 0; jth + ith <= res.length; jth++){
            var subAry = res.slice(jth, jth + ith);
            var strPattern, result;
            
            
            var isSingleChar = true;
            for (var kth = 0; kth < subAry.length ; kth ++){
                if(subAry[0] !== subAry[kth]){
                    isSingleChar = false;
                };
            }
            
            if(isSingleChar){
                console.log(subAry[0]);
                isFound = true;
                break;
            }
            
                
            if (subAry.length === 1){
                  strPattern = "," + subAry.toString() + ",";
            }
            else{
                strPattern = subAry.toString();
            }
            
            var re = new RegExp(strPattern, "g");
            var found = newResStr.match(re);
            result = strPattern.replace(/,/g, " ");
            
            
            
            if (found.length > 1){
                console.log(result);
                isFound = true;
                break;
            }
        }
        
        if(isFound){
            break;
        }
    }
    
    alert("done");
}

myFunction();