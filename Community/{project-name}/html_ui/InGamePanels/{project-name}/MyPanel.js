class MyPanel extends TemplateElement {
    constructor() {
        super(...arguments);
        this.initialize();
    }

    connectedCallback() {
        super.connectedCallback();
        this.initialize();
    }
    
    initialize() {
        if (this.started) {
            return;
        }

        var self = this;

        this.ingameUi = this.querySelector('ingame-ui');

        if (this.ingameUi) {
            this.ingameUi.addEventListener("panelActive", (e) => {
                self.updateImage()
            });

            this.ingameUi.addEventListener("panelInactive", (e) => {
                self.updateImage()
            });

            this.ingameUi.addEventListener("onResizeElement", () => {
                self.updateImage()
            });
        }

        this.started = true;
    }

    disconnectedCallback() {
        super.disconnectedCallback();
    }

    updateImage() {
    }
}

window.customElements.define("my-panel", MyPanel);
checkAutoload();