// Made by @Ericwasepic127
// Usage:
// <p id="statusBox">JavaScript is disabled in this browser. Please enable or ensure your browser supports JavaScript</p>
// <script src="https://ericwasepic127.github.io/run.js"></script>

const status = document.getElememtById("statusBox");
if (typeof WebAssembly === "object" && typeof WebAssembly.instantiate === "function") {
    status.remove();
} else {
    status.innerHTML = "WebAssembly is disabled in this browser. Please enable or ensure your browser supports WebAssembly";
}
