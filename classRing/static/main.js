const flasher = document.getElementById("flash-block");
const flash_btn = document.getElementById("flash-close-btn");
function close_flash() {
  flasher.remove();
  flash_btn.remove();
}
if (flasher.children.length <= 1) {
  close_flash();
}
