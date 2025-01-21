function selectVehicle(button, type) {
            // Remove selected class from all vehicle buttons
            document.querySelectorAll('.vehicle-btn').forEach(btn => {
                btn.classList.remove('selected');
            });
            // Add selected class to clicked button
            button.classList.add('selected');
        }

        // Add stop functionality
        document.querySelector('.add-stop-btn').addEventListener('click', function() {
            const input = document.createElement('input');
            input.type = 'text';
            input.className = 'input-field';
            input.placeholder = 'Destino';

            // Insert before the add stop button
            this.parentNode.insertBefore(input, this);
        });