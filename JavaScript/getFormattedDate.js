/*
  @Author Jared Scott 
  This function uses the Date object to generate a string representation of the current date to the second
*/
function getFormattedDate() {
	  //Instantiating a date object 
    var date = new Date();
	  //Generating various time values from date object 
    var month = date.getMonth() + 1;
    var day = date.getDate();
    var hour = date.getHours();
    var min = date.getMinutes();
    var sec = date.getSeconds();
	  //Formatting strings
    month = (month < 10 ? "0" : "") + month;
    day = (day < 10 ? "0" : "") + day;
    hour = (hour < 10 ? "0" : "") + hour;
    min = (min < 10 ? "0" : "") + min;
    sec = (sec < 10 ? "0" : "") + sec;
	  //Combining various elements into a single date string. 
    var dateStr = date.getFullYear() + "-" + month + "-" + day + " " +  hour + ":" + min + ":" + sec;
    return dateStr;
}
