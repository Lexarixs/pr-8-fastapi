fetch("http://127.0.0.1:8000/products/all")
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById("products");

        data.forEach(product => {
            const div = document.createElement("div");
            div.className = "product";
            div.innerHTML = `
                <h3>${product.name}</h3>
                <p>Цена: ${product.price} ₽</p>
                <p>Категория: ${product.category}</p>
            `;
            container.appendChild(div);
        });
    });
