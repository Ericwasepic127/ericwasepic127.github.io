// src/js/index.js
import { initArrowNavigation, initFocusTrap, initOutsideClick, removeArrowNavigation, removeFocusTrap, removeOutsideClick } from "@t007/utils/hooks/vanilla";
import { bindAllMethods, createEl, isDef, loadResource, uid, parseCSSTime } from "@t007/utils";
var T007_Dialog = class {
  constructor(resolve, { id, closedBy: by, rootElement: root = document.body, scoped = true }) {
    bindAllMethods(this);
    this.resolve = resolve;
    t007.dialogs.set(this.id = id ?? uid("t007_dialog_"), this);
    this.rootElement = root?.isConnected ? root : document.body, this.rootScoped = this.rootElement !== document.body, this.scoped = this.rootScoped && scoped;
    this.rootElement.append(this.dialog = createEl("dialog", { closedBy: by || (this.rootScoped ? "none" : "any"), className: `t007-dialog${this.rootScoped ? " t007-dialog-scoped" : ""}`, id: this.id }), this.rootScoped ? this.backdrop = createEl("div", { className: "t007-dialog-backdrop", id: `${this.id}_backdrop` }) : "");
    this.dialog.addEventListener("cancel", this.cancel);
    initArrowNavigation(this.dialog, { enabled: true, rovingTab: false });
    this.rootScoped && !by && initOutsideClick(this.dialog, { enabled: true, onOutside: this.cancel, root: this.rootElement, scoped: this.scoped });
  }
  show() {
    this.dialog[this.rootScoped ? "show" : "showModal"]();
    initFocusTrap(this.dialog, { enabled: true, root: this.rootElement, scoped: this.scoped });
  }
  remove() {
    removeArrowNavigation(this.dialog), removeFocusTrap(this.dialog), removeOutsideClick(this.dialog);
    this.dialog.open && this.dialog.close(), t007.dialogs.delete(this.id);
    setTimeout(() => (this.dialog.remove(), this.backdrop?.remove()), parseCSSTime(getComputedStyle(this.dialog).transitionDuration || "150ms"));
  }
  confirm(res = true) {
    this.remove(), this.resolve(res instanceof Event ? true : res);
  }
  cancel(res = false) {
    this.remove(), this.resolve(res instanceof Event ? false : res);
  }
};
var T007_Alert_Dialog = class extends T007_Dialog {
  constructor({ message, resolve, options = {} }) {
    super(resolve, options), this.render(message, options);
  }
  render(message, options) {
    this.dialog.innerHTML = `
      <div class="t007-dialog-top-section" tabindex="-1">
        <div class="t007-dialog-question">${message}</div>
      </div>
      <div class="t007-dialog-bottom-section">
        <button type="button" autofocus data-arrow-item class="t007-dialog-confirm-button">${options.confirmText || "OK"}</button>
      </div>
    `;
    this.dialog.querySelector(".t007-dialog-confirm-button").addEventListener("click", this.confirm);
    this.show();
  }
};
var T007_Confirm_Dialog = class extends T007_Dialog {
  constructor({ question, resolve, options = {} }) {
    super(resolve, options), this.render(question, options);
  }
  render(question, options) {
    this.dialog.innerHTML = `
      <div class="t007-dialog-top-section" tabindex="-1">
        <div class="t007-dialog-question">${question}</div>
      </div>
      <div class="t007-dialog-bottom-section">
        <button type="button" autofocus data-arrow-item class="t007-dialog-confirm-button">${options.confirmText || "OK"}</button>
        <button type="button" data-arrow-item class="t007-dialog-cancel-button">${options.cancelText || "Cancel"}</button>
      </div>
    `;
    this.dialog.querySelector(".t007-dialog-confirm-button").addEventListener("click", this.confirm);
    this.dialog.querySelector(".t007-dialog-cancel-button").addEventListener("click", this.cancel);
    this.show();
  }
};
var T007_Prompt_Dialog = class extends T007_Dialog {
  constructor({ question, defaultValue, resolve, options = {} }) {
    super(resolve, options), this.render(question, defaultValue, options);
  }
  async render(question, defaultValue, options) {
    options = { autofocus: true, ...options, value: defaultValue };
    await loadResource(window.T007_INPUT_JS_SRC, "script");
    this.dialog.innerHTML = `
      <form class="t007-input-form" ${t007.field ? "novalidate" : ""}>
        <div class="t007-dialog-top-section" tabindex="-1">
          <div class="t007-dialog-question">${question}</div>
        </div>
        <div class="t007-dialog-bottom-section">
          <button type="submit" data-arrow-item class="t007-dialog-confirm-button">${options.confirmText || "OK"}</button>
          <button type="button" data-arrow-item class="t007-dialog-cancel-button">${options.cancelText || "Cancel"}</button>
        </div>
      </form>
    `;
    (this.form = this.dialog.querySelector("form")).lastElementChild.insertAdjacentElement("beforebegin", t007.field?.(options) || createEl("input", options));
    t007.field ? this.form.onSubmit = this.confirm : this.form.addEventListener("submit", (e) => (e.preventDefault(), this.confirm()));
    this.dialog.querySelector(".t007-dialog-cancel-button").addEventListener("click", this.cancel);
    t007.handleFormValidation?.(this.form);
    this.show();
  }
  show() {
    super.show(), this.form.elements[0]?.select?.();
  }
  confirm() {
    super.confirm(this.form.elements[0]?.value);
  }
  cancel() {
    super.cancel(null);
  }
};
function isActive(id) {
  return isDef(id) ? t007.dialogs.has(id) : t007.dialogs.size > 0;
}
function alert(message, options) {
  return new Promise((resolve) => new T007_Alert_Dialog({ resolve, message, options }));
}
function confirm(question, options) {
  return new Promise((resolve) => new T007_Confirm_Dialog({ resolve, question, options }));
}
function prompt(question, defaultValue, options) {
  return new Promise((resolve) => new T007_Prompt_Dialog({ resolve, question, defaultValue, options }));
}
function dismiss(id, response) {
  if (isDef(id)) return t007.dialogs.get(id)?.cancel(response);
  for (const dialog of t007.dialogs.values()) dialog.cancel(response);
}
if ("undefined" !== typeof window) {
  t007.alert = alert, t007.confirm = confirm, t007.prompt = prompt;
  t007.dialog = { isActive, alert, confirm, prompt, dismiss };
  t007.dialogs = /* @__PURE__ */ new Map();
  loadResource(T007_DIALOG_CSS_SRC), loadResource(window.T007_INPUT_JS_SRC, "script");
  window.Alert ??= t007.alert, window.Confirm ??= t007.confirm, window.Prompt ??= t007.prompt;
  console.log("%cT007 Dialogs attached to window!", "color: darkturquoise");
}
export {
  alert,
  confirm,
  dismiss,
  isActive,
  prompt
};
