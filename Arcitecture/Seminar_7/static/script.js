(async function f() {
    async function fetchAndRender() {
        const path = window.location.pathname.split("/");
        const page = path[path.length - 1] || "main";
        try {
            const response = await fetch(`/get-page-html/${page}`);
            if (response.ok) {
                document.getElementById("main-page").innerHTML = await response.text();
            } else {
                console.error("Error response");
            }
        } catch (error) {
            console.error("Error response", error);
        }
    }
    document.querySelectorAll(".menu-link").forEach(function (element) {
        element.addEventListener("click", async function (event) {
            event.preventDefault();
            history.pushState(null, null, element.id !== "main" ? `/${element.id}`: "/");

            await fetchAndRender();
        });
    });

    window.onpopstate = fetchAndRender;
    await fetchAndRender();
})();
