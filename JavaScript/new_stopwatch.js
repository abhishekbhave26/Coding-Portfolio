var h1 = document.getElementsByTagName('h1')[0],
    start = document.getElementById('start'),
    stop = document.getElementById('stop'),
    clear = document.getElementById('clear'),
    seconds = 0, minutes = 0, hours = 0,
    t;


function add() 
    {
    seconds++;
    if (seconds >= 60) {
        seconds = 0;
        minutes++;
        if (minutes >= 60) {
            minutes = 0;
            hours++;
        }
    }
    
    h1.textContent = (hours ? (hours > 9 ? hours : "0" + hours) : "00") + ":" + (minutes ? (minutes > 9 ? minutes : "0" + minutes) : "00") + ":" + (seconds > 9 ? seconds : "0" + seconds);

    timer();
    }


function timer() 
{
    t = setTimeout(add, 1000);
    
}



/* Start button */
start.onclick = function()
{
    timer();
    var table = document.getElementById("myTable");
    var row = table.insertRow(i);
    var cell1 = row.insertCell(t);
    

          // creating all cells
          for (var i = 0; i < 1; i++) 
          {
            // creates a table row
            var row = document.createElement("tr");

            
            // Create a <td> element and a text node, make the text
              // node the contents of the <td>, and put the <td> at
              // the end of the table row
              var cell = document.createElement("td");
              var cellText1 = document.createTextNode("Start Time is ");
              var cellText2 = document.createTextNode("Stop Time is ");
              var cellText3 = document.createTextNode("Time is ");
              cell.appendChild(cellText1);
              row.appendChild(cell);
              cell.appendChild(cellText2);
              row.appendChild(cell);
              cell.appendChild(cellText3);
              row.appendChild(cell);
              
            

            // add the row to the end of the table body
            tblBody.appendChild(row);
          }

          
    
    
    
}
/* Stop button */
stop.onclick = function() 
{
    clearTimeout(t);
    
    var cell2 = row.insertCell(1);
    
    
}

/* Clear button */
clear.onclick = function() 
{
    h1.textContent = "00:00:00";
    seconds = 0; minutes = 0; hours = 0;
    var cells3=stop-start;
    var cell3 =row.insertCell(2);
}

var start,stop;
var time;
            
                student = 
                {
                    start_time:   j,
                    stop_time: j,
                    time:  j,
                };
                
                cell1.innerHTML = student.start,
                cell2.innerHTML = student.stop,
                cell3.innerHTML = student.time;
            
            