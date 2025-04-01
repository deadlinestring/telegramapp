document.addEventListener("DOMContentLoaded", function () {
    const restaurants = [
        { name: "Пиццерия Mario", id: 1 },
        { name: "Суши-бар Tokyo", id: 2 },
        { name: "Стейкхаус Texas", id: 3 }
    ];

    const list = document.getElementById("restaurants");

    restaurants.forEach(restaurant => {
        let li = document.createElement("li");
        li.textContent = restaurant.name;
        li.onclick = function() {
            alert("Открываем меню " + restaurant.name);
        };
        list.appendChild(li);
    });
});
