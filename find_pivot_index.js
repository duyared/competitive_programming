/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    for(i=0;i<nums.length;i++){
        sumLeft = 0,sumRight = 0
        for(j=0;j<nums.length;j++){
            if(j < i) { sumLeft += nums[j]}
            else if(j> i) { sumRight += nums[j]}
            else {}
        
        }
    if (sumLeft == sumRight) return i  ;
    }
    return -1;
};
