import Cropper from 'cropperjs';

class CropperWidget {
    constructor(container, options = {}) {
        this.container = container;
        this.options = options;
        this.modal = container.querySelector('[data-cropper-modal]');
        this.preview = container.querySelector('.preview');
        this.input = container.querySelector('input[type="file"]');
        this.cropButton = container.querySelector('[data-crop-button]');
        this.image = container.querySelector('[data-cropper-image]');
        this.closeButton = container.querySelector('[data-close-modal]');
        this.cropper = null;
        this.contentType = 'image/jpeg'
        this.quality = 0.8

        this._bindEvents();
    }

    _bindEvents() {
        this.input.addEventListener('change', this._onFileChange.bind(this));
        this.cropButton.addEventListener('click', this._onCrop.bind(this));
        this.closeButton.addEventListener('click', () => this._toggleModal(false));
    }

    _onFileChange(e) {
        const file = e.target.files[0];
        if (!file) return;
        this.image.src = URL.createObjectURL(file);
        this._toggleModal(true);
        this.image.onload = () => {
            if (this.cropper) this.cropper.destroy();
            this.cropper = new Cropper(this.image, {
                aspectRatio: this.options.aspectRatio || 1,
                viewMode: 1,
                ...this.options.cropperOptions,
            });
        };
    }

    _onCrop() {
        this.cropper.getCroppedCanvas().toBlob((blob) => {
            const previewURL = URL.createObjectURL(blob);
            this.preview.src = previewURL;
            this.preview.classList.remove('hidden');

            if (this.options.onCrop) {
                this.options.onCrop(blob);
            }

            this._toggleModal(false);
        }, this.contentType, this.quality);
    }

    _toggleModal(show) {
        this.modal.classList.toggle('hidden', !show);
        this.modal.classList.toggle('flex', show);
    }
}

window.CropperWidget = CropperWidget;