document.addEventListener("DOMContentLoaded", function(event) {
    var $leftMenuIcons = document.querySelector('#leftMenuIcons');
    var $leftMenuText = document.querySelector('#leftMenuText');

    var j1 = true;
    var j2 = true;
    var tI;

    function leftMenuOutTimer() {
        setTimeout(() => {
            if (j1 === true && j2 == true) {
                leftMenuText.classList.add('leftMenuOut');
            }
        }, 1000);
    }

    leftMenuIcons.addEventListener('mouseover', () => {
        leftMenuText.classList.remove('leftMenuOut');
        j1 = false;
    });

    leftMenuText.addEventListener('mouseover', ()=>{
        j2= false;
    });

    leftMenuIcons.addEventListener('mouseout', () => { 
        j1 = true;
        tI = leftMenuOutTimer();
        
    
    });

    leftMenuText.addEventListener('mouseout', () => { 
        j2 = true;
        tI = leftMenuOutTimer();
    });
});