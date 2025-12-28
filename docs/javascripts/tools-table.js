document.addEventListener("DOMContentLoaded", () => {
  const triggers = document.querySelectorAll(".js-tool-popup-trigger");

  function positionPopup(popup) {
    const wrapper = document.querySelector(".tools-table-wrapper");
    if (!wrapper) return;

    const wrapRect = wrapper.getBoundingClientRect();
    const popRect = popup.getBoundingClientRect();

    let shiftX = 0;

    if (popRect.right > wrapRect.right) {
      shiftX = wrapRect.right - popRect.right - 8;
    }

    if (popRect.left + shiftX < wrapRect.left) {
      shiftX = wrapRect.left - popRect.left + 8;
    }

    popup.style.transform = `translateX(${shiftX}px)`;
  }

  triggers.forEach((btn) => {
    const popupId = btn.dataset.popupId;
    const popup = document.getElementById(popupId);
    if (!popup) return;

    const closeBtn = popup.querySelector(".js-tool-popup-close");

    const close = () => {
      popup.classList.remove("tool-popup--visible");
      popup.style.transform = "translateX(0)";
    };

    const open = () => {
      popup.classList.add("tool-popup--visible");
      popup.style.transform = "translateX(0)";
      positionPopup(popup);
    };

    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      if (popup.classList.contains("tool-popup--visible")) {
        close();
      } else {
        document
          .querySelectorAll(".tool-popup--visible")
          .forEach((el) => {
            el.classList.remove("tool-popup--visible");
            el.style.transform = "translateX(0)";
          });
        open();
      }
    });

    if (closeBtn) {
      closeBtn.addEventListener("click", (e) => {
        e.stopPropagation();
        close();
      });
    }
  });

  document.addEventListener("click", () => {
    document
      .querySelectorAll(".tool-popup--visible")
      .forEach((el) => {
        el.classList.remove("tool-popup--visible");
        el.style.transform = "translateX(0)";
      });
  });
});
