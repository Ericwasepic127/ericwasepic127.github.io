// ==UserScript==
// @name         Developer Mode
// @namespace    https://ericwasepic127.github.io
// @version      1.0.0
// @description  try to take over the world!
// @author       Ericwasepic127
// @run-at       document-end
// @match        https://*/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    (function () { var script = document.createElement('script'); script.src="//cdn.jsdelivr.net/npm/eruda"; document.body.appendChild(script); script.onload = function () { eruda.init() } })();

})();
