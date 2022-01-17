/*
 *@Author Jared Scott ☯
 *This script is an implementation of the selection sort algorithm for sorting integer arrays 
 */
 
function swap(array, idx1, idx2) {
	//Swaps the values at the given indices 
    var temp = array[idx1];
    array[idx1] = array[idx2];
    array[idx2] = temp;
}

function selectionSort(array, item_count) {
    var i, j, index;
    for (i = 0; i < item_count-1; i++)
    {
        //Scan through the array and find the minimum element 
        index = i;
        for (j = i + 1; j < item_count; j++) {
            if (array[j] < array[index])
                index = j;
		}
        //Once the smallest element has been found swap with current position
        swap(array,index, i);
    }
}

var array = [52,22,68,95,12,4,75,23,74];
selectionSort(array, array.length);
console.log("Sorted array: " + array);