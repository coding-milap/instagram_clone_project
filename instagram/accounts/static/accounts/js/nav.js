btn = document.getElementById('btn-1');
btn2 = document.getElementById('btn-2')

click_counter = 0
function hello(){
    click_counter = click_counter + 1;
    card = document.getElementById('card-1');

    if (click_counter % 2 == 0)
    {
        card.style.display = "none";
    }
    else{
        card.style.display = "block";
    }

    
}

function moon()
{
    click_counter = click_counter + 1;
    body = document.getElementsByName('body')
    
    if (click_counter % 2 == 0)
    {
        body.style.backgroundColor = "white";
    }
    else{
        body.style.backgroundColor = "black";
    }

}