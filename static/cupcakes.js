const BASE_URL = 'http://localhost:5000/api';

function createHTML(cupcake) {
    <div data-cupcake-id = '${cupcake.id}'>
        <li>
            ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
            <button class = 'delete-button'>Delete</button>
        </li>

        <img class = 'Cupcake-img'
        src = '${cupcake.image}'></img>
    </div>
}

async function showInitialCupcakes() {
    const response = await axios.get('${BASE_URL}/cupcakes');

    for (let cupcakeData of response.data.cupcakes) {
        let newCupcake = $(genereateCupcakeHTML(cupcakeData));
        $('#cupcakes-list').append(newCupcake);
}


$('#new-cupcake-form').on('submit', async function (evt) {
    evt.preventDefault();
    let flavor = $('#form-flavor').val();
    let rating = $('#form-rating').val();
    let size = $('#form-size').val();
    let image = $('#form-image').val();

    const newCupcakeResponse = await axios.post('${BASE_URL}/cupcakes',
    flavor,rating,size,image)
});

    let newCupcake = $(genereateCupcakeHTML(newCupcakeREsponse.data.cupcake));
    $('#cupcakes-list').append(newCupcake);
    $('#new-cupcake-form').trigger('reset');
};

$('#cupcakes-list').on('click', 'delete-button', async function(evt) {
    evt.preventDefault();
    let $cupcake = $(evt.target).closest('div');
    let cupcakeId = $cupcake.attr('data-cupcake-id');

    await axios.delete('$BASE_URL/cupcakes/${cupcakeId}');
    $cupcake.remove();
});

$(showInitialCupcakes);
