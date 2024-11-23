$(document).ready(function() {
    // Функція для завантаження турів з бекенду
    function loadTours() {
        $.ajax({
            url: 'http://127.0.0.1:8000/api/tours/',  // Вказуємо правильний шлях до вашого API
            method: 'GET',
            success: function(response) {
                $('#tour-list').empty();  // Очищаємо поточний список турів
                response.forEach(function(tour) {
                    $('#tour-list').append(`
                        <div class="tour">
                            <h3><a href="/tours/${tour.id}">${tour.name}</a></h3>
                            <p>${tour.description}</p>
                            <p>Ціна: ${tour.price}</p>
                        </div>
                    `);
                });
            },
            error: function(error) {
                console.error('Помилка при отриманні турів', error);
            }
        });
    }

    // Завантажуємо тури при завантаженні сторінки
    loadTours();

    // Кнопка "На головну"
    $("#home-btn").click(function() {
        window.location.href = '/';  // Переадресація на головну сторінку
    });
});
