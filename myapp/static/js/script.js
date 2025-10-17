// Quick View Functionality
document.querySelectorAll(".quick-view").forEach(btn => {
    btn.addEventListener("click", function() {
        document.getElementById("modalTitle").textContent = this.dataset.title;
        document.getElementById("modalPrice").textContent = this.dataset.price;
        document.getElementById("modalImg").src = this.dataset.img;
        new bootstrap.Modal(document.getElementById("quickViewModal")).show();
    });
});

// Add to Cart Functionality
let cartCount = 0;
document.querySelectorAll(".add-to-cart").forEach(btn => {
    btn.addEventListener("click", function() {
        cartCount++;
        document.getElementById("cartCount").textContent = cartCount;
    });
});
