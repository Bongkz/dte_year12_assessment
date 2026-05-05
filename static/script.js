document.addEventListener('DOMContentLoaded', () => {
    const toast = document.getElementById('cart-toast');
    const forms = document.querySelectorAll('.add-to-cart-form');

    if (!toast || forms.length === 0) {
        return;
    }

    function showToast(message, error = false) {
        toast.textContent = message;
        toast.style.background = error ? '#c0392b' : '#28a745';
        toast.style.opacity = '1';
        toast.style.transform = 'translateY(0)';
        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateY(10px)';
        }, 2200);
    }

    forms.forEach(form => {
        form.addEventListener('submit', async (event) => {
            event.preventDefault();
            const formData = new FormData(form);

            try {
                const response = await fetch(form.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'Accept': 'application/json'
                    }
                });
                const data = await response.json();
                if (response.ok && data.success) {
                    showToast(data.message || 'Item Added to Cart');
                } else {
                    showToast(data.message || 'Failed to add item', true);
                }
            } catch (error) {
                showToast('Error adding item', true);
            }
        });
    });
});
