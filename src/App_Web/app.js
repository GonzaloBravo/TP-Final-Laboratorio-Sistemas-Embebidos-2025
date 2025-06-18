document.addEventListener("DOMContentLoaded", function () {
    const links = document.querySelectorAll(".presentacion__comidas__link");

    links.forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault(); // Evita que el enlace abra la página directamente

            const mesa = document.getElementById("mesa").value;
            if (!mesa) {
                alert("Por favor, ingrese su número de mesa");
                return;
            }

            const comida = this.getAttribute("href").split("/").pop().replace(".html", "");

            // Datos a enviar
            const pedido = {
                mesa: parseInt(mesa),
                comida: comida
            };

            // Enviar los datos a la computadora principal
            fetch("http://192.XXX.X.XXX:5000/orden", { // Cambia la IP por la de la computadora principal
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(pedido)
            })
            .then(response => response.json())
            .then(data => {
                alert("Pedido enviado!");
                window.location.href = this.getAttribute("href"); // Redirigir a la página de la comida
            })
            .catch(error => {
                alert("Error al enviar el pedido");
                console.error("Error:", error);
            });
        });
    });
    
});
