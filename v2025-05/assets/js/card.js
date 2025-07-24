document.body.addEventListener(
  "click",
  function (evt) {
    if (
      evt.target.className === "card" ||
      evt.target.className === "card-smaller"
    ) {
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
        return;
      }
    }

    const findClosestSmaller = evt.target.closest(".card-smaller");

    if (findClosestSmaller) {
      var hrefValue = findClosestSmaller.getAttribute("href");
      if (hrefValue) {
        window.location = hrefValue;
        return;
      }
    }
  },
  false
);
