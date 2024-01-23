document.body.addEventListener(
  "click",
  function (evt) {
    if (evt.target.className === "card") {
      var hrefValue = evt.target.getAttribute("href");
      if (hrefValue) {
        window.location = hrefValue;
      }
    }
    const findClosest = evt.target.closest(".card");

    if (findClosest) {
      var hrefValue = findClosest.getAttribute("href");
      if (hrefValue) {
        window.location = hrefValue;
      }
    }
  },
  false
);
