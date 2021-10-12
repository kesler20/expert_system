

const primarySectionEL = document.getElementById('primary-chemicals');
const secondarySectionEL = document.getElementById('general-btns-hazid');
const tertiarySectionEL = document.getElementById('section-2-handling-and-storage');
 

function onEditSection(e) {
    
    const button = e.target;
    button.classList.add('btn');
    const anchor = button.parentNode;
    const generalSection = anchor.parentNode;
    const input = document.createElement('input');

    if (e.target.tagName === 'BUTTON') {
        
        if (button.textContent === 'Delete') {
            generalSection.removeChild(anchor);

        } else if (button.textContent === 'Edit') {
            const span = anchor.firstElementChid;
            console.log(span);

            input.type = 'text';
            input.value = 'Enter title to replace';
            input.setAttribute('id', 'main-title');
            anchor.insertBefore(input, span); 
            button.textContent = 'Save';
            button.classList.add('btn');
            button.classList.add('save');
        } else if (button.textContent === 'Save') {
            
            const alcohols = document.getElementById('alcohols')// cahnge the id 
            document.getElementById('alcohols').remove()
            const newAnchor = document.createElement('a');
            const strong = document.createElement('strong');
            const h1 = document.createElement('h1');
            const editButton = document.createElement('button');
            editButton.classList.add('btn');
            
            const buttonSection = button.parentNode
            buttonSection.removeChild(button)
            

            const deleteButton = document.createElement('button');
            deleteButton.classList.add('btn');
            const mainBody = document.getElementById('primary-chemicals');
            
            mainBody.appendChild(newAnchor);
            newAnchor.classList.add('section');
            newAnchor.appendChild(h1);
            newAnchor.appendChild(editButton);
            newAnchor.appendChild(deleteButton);
            h1.appendChild(strong);

            const inputField = document.getElementById('main-title').value;
            strong.textContent = inputField;
            strong.setAttribute('id', 'alcohols')
            document.getElementById('main-title').remove()
            editButton.textContent = 'Edit';
            deleteButton.textContent = 'Delete'; // the one above deletes the add chemical button ythe one just created deletes the title
        } else if (button.textContent === 'Add Chemicals') {

            const generalSection = button.parentNode;
            const secondSectionChemicals = document.getElementById('secondary-chemicals')
            const h2 = document.createElement('h2');
            const hr = document.createElement('hr');

            h2.textContent = document.getElementById('alcohols').textContent;
            secondSectionChemicals.appendChild(hr);
            secondSectionChemicals.appendChild(h2);
            secondSectionChemicals.appendChild(hr);
        }
    }
};

/*
<div id="acids">
  <a class=section>
    <h1 id='title-acids'><strong>Acids</strong></h1>
    <button type="button" class="navbar-toggler-edit" title="edit" >edit</button>
    <button type="button" class="navbar-toggler-delete" title="remove">remove</button>
  </a>
</div>

*/

function onEditSecondSection(e) {
    
    const button = e.target;
    const anchor = button.parentNode;
    button.classList.add('btn');
    if (e.target.tagName === 'BUTTON') {

        const input1 = document.createElement('input');
        const input2 = document.createElement('input');
        const input3 = document.createElement('input');
        
        if (button.textContent === 'Edit') {
            alert('console');
            button.textContent = 'Save';
            button.classList.add('btn');
            const tableBody = document.getElementById('table-body');
            tableBody.parentNode.removeChild(tableBody);

            input1.type = 'text';
            input2.type = 'text';
            input3.type = 'text';

            input1.setAttribute('id', 'colmn1')
            input2.setAttribute('id', 'colmn2')
            input3.setAttribute('id', 'colmn3')

            anchor.appendChild(input1);
            anchor.appendChild(input2);
            anchor.appendChild(input3);
            anchor.appendChild(button);

        } else if (button.textContent === 'Save' || button.textContent === 'Submit') {
            
            const tableBody = document.createElement('tbody');
            const table = document.getElementById('table-id')

            
            const firstRow = document.createElement('tr');
            const secondRow = document.createElement('tr');
            const thirdRow = document.createElement('tr');

            const hazardStatement = document.createElement('td');
            hazardStatement.textContent = document.getElementById('colmn1').value;
            const hazardClassCategory = document.createElement('td');
            hazardClassCategory.textContent = document.getElementById('colmn2').value;	
            const precautionaryMeasures = document.createElement('td');
            precautionaryMeasures.textContent = document.getElementById('colmn3').value;

            firstRow.appendChild(hazardStatement);
            firstRow.appendChild(hazardClassCategory);
            firstRow.appendChild(precautionaryMeasures);

            secondRow.appendChild(hazardStatement);
            secondRow.appendChild(hazardClassCategory);
            secondRow.appendChild(precautionaryMeasures);

            thirdRow.appendChild(hazardStatement);
            thirdRow.appendChild(hazardClassCategory);
            thirdRow.appendChild(precautionaryMeasures);

            tableBody.appendChild(firstRow);
            tableBody.appendChild(secondRow);
            tableBody.appendChild(thirdRow);
            
            table.classList.add('table');
            table.classList.add('table-striped');
            table.classList.add('table-hover');
            table.appendChild(tableBody).

            button.textContent = 'Submit';
            button.classList.add('btn');
        }
    }
};

/*
    <tbody id='table-body'>
    <tr>
        <td>Highly flammable liquid and vapour</td>
        <td>Flam. Liq. 2</td>
        <td>Keep away from open flames and hot surfaces. No smoking.</td>
    </tr>
    <tr>
        <td>Causes serious eye damage</td>
        <td>Eye Dam. 1</td>
        <td>Wear protective gloves and eye protection.</td>
    </tr>
    <tr>
        <td>May cause drowsiness or dizziness</td>
        <td>STOT SE 3</td>
        <td>Keep container tightly closed.</td>
    </tr>
    </tbody>
*/

function onEditTertiarySection(e) {
    
    const button = e.target;
    const anchor = button.parentNode;

    if (e.target.tagName === 'BUTTON') {
        
        if (button.textContent === 'Edit') {
            alert('console');
            button.textContent = 'Save';
            const input = document.createElement('input');

            input.type = 'text';
            input.setAttribute('id', 'input-list')
            anchor.appendChild(input);

            anchor.appendChild(button);

        } else if (button.textContent === 'Save' || button.textContent === 'Submit') {
            
            const ul = document.createElement('ul');
            const li = document.createElement('li');

            li.textContent = document.getElementById('input-list').value;

            ul.appendChild(li)
            tertiarySectionEL.appendChild(ul)
            button.textContent = 'Submit';
        }
    }
};
/*
    <ul>
        <li>Eye protection: Use safety goggles with side protection.</li>
        <li>Skin protection: Wear suitable chemical protection gloves (tested according to EN 374).</li>
        <li>Respiratory protection: Necessary at aerosol or mist formation.</li>
        <li>Other protection measures: Flame-retardant protective clothing.</li>
    </ul>
*/


// change save submit transition coulkd not add pseudo ::marker no tertiary section
primarySectionEL.addEventListener("click", onEditSection);
secondarySectionEL.addEventListener("click", onEditSecondSection);
tertiarySectionEL.addEventListener("click", onEditTertiarySection);
