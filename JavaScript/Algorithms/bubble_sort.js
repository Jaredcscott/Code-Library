/*
 *@Author Jared Scott ☯
 *This script is an implementation of the bubble sort algorithm for an array of integer values 
 *Passing an array of integers into this function will cause the array to be sorted in place (The input array is augmented) 
 */

function bubbleSort(Int_Array){
    //Main scan through items in the array 
    for(let i = 0; i < Int_Array.length; i++){
        //Secondary scan for comparison 
        for(let j = 0; j < Int_Array.length - i - 1; j++){
            //Comparing the two values from the scans 
            if(Int_Array[j + 1] < Int_Array[j]){
                //Swapping if needed 
                [Int_Array[j + 1],Int_Array[j]] = [Int_Array[j],Int_Array[j + 1]]
            }
        }
    };
    //The array has been sorted in place (the array has been altered)  
    return Int_Array;
};

console.log("Sorting the array of integers using a bubble sort. . .");
console.log("The array has been sorted: " + bubbleSort([5,3,8,4,6]));