function dragElement(target) {
  if (typeof target === 'string') target = document.querySelector(target);
  if (!target) return;

  const el = target;
  const handle = el.querySelector('.title-bar') || el;

  const parent = el.offsetParent || el.parentElement;
  if (parent && getComputedStyle(parent).position === 'static') {
    parent.style.position = 'relative';
  }
  if (getComputedStyle(el).position === 'static') {
    el.style.position = 'absolute';
  }

  if (!el.style.left && !el.style.top) {
    const rect = el.getBoundingClientRect();
    const parentRect = (el.offsetParent || document.documentElement).getBoundingClientRect();
    el.style.left = (rect.left - parentRect.left) + 'px';
    el.style.top  = (rect.top  - parentRect.top)  + 'px';
  }

  let startX = 0, startY = 0, origLeft = 0, origTop = 0, activeId = null;

  function onPointerDown(e) {
    if (e.pointerType === 'mouse' && e.button !== 0) return;
    e.preventDefault();
    try { handle.setPointerCapture(e.pointerId); } catch (err) {}
    activeId = e.pointerId;
    startX = e.clientX; startY = e.clientY;
    origLeft = parseFloat(el.style.left) || 0;
    origTop  = parseFloat(el.style.top)  || 0;
    document.addEventListener('pointermove', onPointerMove);
    document.addEventListener('pointerup', onPointerUp);
    document.addEventListener('pointercancel', onPointerUp);
  }

  function onPointerMove(e) {
    if (e.pointerId !== activeId) return;
    const dx = e.clientX - startX;
    const dy = e.clientY - startY;
    el.style.left = (origLeft + dx) + 'px';
    el.style.top  = (origTop  + dy) + 'px';
  }

  function onPointerUp(e) {
    if (e.pointerId === activeId) {
      try { handle.releasePointerCapture(e.pointerId); } catch (err) {}
      activeId = null;
    }
    document.removeEventListener('pointermove', onPointerMove);
    document.removeEventListener('pointerup', onPointerUp);
    document.removeEventListener('pointercancel', onPointerUp);
  }

  handle.addEventListener('pointerdown', onPointerDown);
}

document.addEventListener('DOMContentLoaded', function () {
  const win = document.querySelector('#weatherWindow');
  if (win) dragElement(win);
});

window.dragElement = dragElement;
