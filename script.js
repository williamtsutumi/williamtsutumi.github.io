let json = {"28/03/24": 5,"12/03/24": 6,"29/02/24": 3,"28/02/24": 15,"27/02/24": 5,"24/02/24": 5,"23/02/24": 15,"21/02/24": 3,"20/02/24": 1,"19/02/24": 6,"18/02/24": 7,"16/02/24": 4,"15/02/24": 4,"13/02/24": 4,"30/01/24": 7,"28/01/24": 9,"26/01/24": 13,"25/01/24": 12,"24/01/24": 10,"23/01/24": 16,"22/01/24": 5,"21/01/24": 4,"20/01/24": 2,"18/01/24": 4,"17/01/24": 9,"16/01/24": 15,"15/01/24": 14,"14/01/24": 14,"13/01/24": 8,"06/01/24": 3,"05/01/24": 2,"02/01/24": 8,"11/12/23": 4,"05/12/23": 7,"04/12/23": 5,"03/12/23": 1,"02/12/23": 15,"01/12/23": 4,"30/11/23": 3,"28/11/23": 4,"26/11/23": 12,"25/11/23": 8,"24/11/23": 5,"23/11/23": 2,"19/11/23": 4,"13/11/23": 1,"01/11/23": 1,"29/10/23": 7,"28/10/23": 5,"27/10/23": 1,"31/08/23": 5,"24/08/23": 3,"05/08/23": 25,"04/08/23": 2,"02/08/23": 14,"24/07/23": 8,"23/07/23": 23,"22/07/23": 15,"18/07/23": 23,"15/07/23": 17,"11/07/23": 4,"10/07/23": 4,"09/07/23": 9,"08/07/23": 7,"07/07/23": 10,"04/07/23": 1,"01/07/23": 8,"30/06/23": 1,"03/02/23": 12,"01/02/23": 1,"27/01/23": 6,"12/12/22": 1,"05/12/22": 1,"04/12/22": 5,"29/11/22": 1,"27/10/22": 4,"10/10/22": 7,"04/10/22": 2,"26/09/22": 1,"23/09/22": 3,"22/09/22": 3,"21/09/22": 5,"17/09/22": 12,"13/09/22": 1,"12/09/22": 4,"10/09/22": 4,"09/09/22": 3,"01/09/22": 2,"31/08/22": 2};

const formatter = new Intl.DateTimeFormat('pt-BR', { day: '2-digit', month: '2-digit', year: '2-digit' });
const numCols = 53;
const numLins = 7;

const codeforcesColor1 = 'MidnightBlue';
const codeforcesColor2 = 'blue';
const codeforcesColor3 = 'rgb(59, 129, 203)';

window.onload = function () {
    let table = document.getElementById("calendar");
    let dayOfWeek = new Date().getDay();
    let currDate = new Date();
    for (let i = dayOfWeek; i >= 0; i--) {
        setDayActivity(table.rows[i].cells[numCols-1], currDate);
        currDate.setTime(currDate.getTime() - 86400000);
    }

    for (let j = numCols-2; j >= 0; j--) {
        for (let i = 6; i >= 0; i--) {
            setDayActivity(table.rows[i].cells[j], currDate);
            currDate.setTime(currDate.getTime() - 86400000);
        }
    }
    
    for (let i = 0; i < dayOfWeek; i++) { table.rows[i].cells[0].style.visibility = 'hidden'; }
    for (let i = dayOfWeek+1; i < numLins; i++) { table.rows[i].cells[52].style.visibility = 'hidden'; }
}

function setDayActivity(cell, date) {
    let dateStr = formatter.format(date);
    
    if (!json.hasOwnProperty(dateStr)) {
        cell.getElementsByTagName('span')[0].innerHTML = 'no activity on ' + dateStr;
        return;
    }

    if (json[dateStr] <= 3) { cell.style.backgroundColor = codeforcesColor1; }
    else if (json[dateStr] <= 6) { cell.style.backgroundColor = codeforcesColor2; }
    else { cell.style.backgroundColor = codeforcesColor3; }

    cell.getElementsByTagName('span')[0].innerHTML = json[dateStr] + ' activities on ' + dateStr;
}