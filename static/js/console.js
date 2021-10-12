

function addArgument(numberOfArguments,e) {

    const button = e.target;
    btnSectionEL = button.parentNode;

    for (var i = 0; i < numberOfArguments; i++) {
        const input = document.createElement('input');
        const anchor = document.createElement('a');
        const button = document.createElement('button');
        button.textContent = 'Submit';
        button.classList.add('btn');
        button.classList.add('btns');

        anchor.appendChild(input);
        anchor.appendChild(button);
        anchor.classList.add('btn');

        anchor.classList.add('btns');
        btnSectionEL.appendChild(anchor);
    }

    return btnSectionEL;
}

function onClickButton(e) {
    const button = e.target;
    if (e.target.tagName === 'BUTTON') {

    } else if (e.target.tagName === 'P'); {
        const id = button.getAttribute('id');
        
        if (id === '2'); {
            document.getElementById('2').remove()
            btnsection = addArgument(2,e);
            const mainSection = document.getElementById('section-one');
            mainSection.append(btnsection);
            btnsection.setAttribute('id','two')
        };
        
    };
};
// change anchor for a form
const sectionBtn = document.getElementById('section-one');
sectionBtn.addEventListener('click', onClickButton);