function displayCover() {
    let input = document.getElementById('cover');
    let preview = document.getElementById('cover_preview');

    if (input.files && input.files[0]) {
        let reader = new FileReader();

        reader.onload = (event) => {
            preview.src = event.target.result;
        }

        reader.readAsDataURL(input.files[0]);
    }
}

function manageActorsFields() {
    let actorsDiv = document.getElementById('actors');

    let actors = actorsDiv.querySelectorAll('input');

    if (!Array.from(actors).some((actor) => actor.value === '')) {
        let newActor = document.createElement('input');
        newActor.setAttribute('type', 'text');
        newActor.setAttribute('name', 'actor_' + (actors.length + 1));

        actorsDiv.appendChild(newActor);

        newActor.addEventListener('input', manageActorsFields);

        actors[actors.length - 1].required = true;
    }
    else {
        if (actors.length >= 2 && actors[actors.length - 1].value === '' && actors[actors.length - 2].value === '') {
            actorsDiv.removeChild(actors[actors.length - 1]);

            if (actors.length > 2) {
                actors[actors.length - 2].required = false;
            }

            manageActorsFields();
        }
    }
}

window.onload = () => {
    document
        .getElementById('cover')
        .addEventListener('change', displayCover);

    document
        .getElementById('actors')
        .querySelectorAll('input')
        .forEach((actor) => 
            actor.addEventListener('input', manageActorsFields)
        );
}