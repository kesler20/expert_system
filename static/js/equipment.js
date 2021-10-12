
const primarySectionEL = document.getElementById('section-one');
const secondSectionEL = document.getElementById('section-two');
const tertiarySectionEL = document.getElementById('section-three');
const fourthSectionEL = document.getElementById('section-four');
const fifthSectionEL = document.getElementById('section-five');

function onAddDeleteEquipment(e) {
    const button = e.target;
    const secondarySection = document.getElementById('secondary-section');

    if (e.target.tagName === 'BUTTON') {
        if (button.textContent == 'Delete Equipment') {
            const main = secondarySection.parentNode;
            main.removeChild(secondarySection);
        } else if (button.textContent == 'Add Equipment') {
            alert('console')
            const hr = document.createElement('hr');
            const secondarySection = document.createElement('div');
            secondarySection.setAttribute('id', 'secondary-section');
            const anchor = document.createElement('a');
            anchor.classList('general-btns');
            const addEquipment = document.createElement('button');
            const deleteEquipment = document.createElement('button');
            addEquipment.textContent == 'Add Equipment'
            deleteEquipment.textContent == 'Delete Equipment'
            anchor.appendChild(addEquipment);
            anchor.appendChild(deleteEquipment);
            secondarySection.appendChild(hr);
            secondarySection.appendChild(anchor);
        }
    };
};

primarySectionEL.addEventListener("click", onAddDeleteEquipment);


