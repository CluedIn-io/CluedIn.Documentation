function redirect() {
  // this code runs on 404 page, i.e. the URL does not exist
  const pathname = window.location.pathname;

  // TODO: here comes any logic to redirect to the correct page
  // add it here if you removed a page from the site and want to add a redirect
  
  // if the URL is reaching the old docs site,
  // do nothing - the request would not end here id the page existed
  if (pathname.toLowerCase().indexOf('versions/3.2.3') > -1) {
      return;
  }

  // othewise, let's assume that there is a page in the old docs site,
  // but a user didn't add a /versions/3.2.3/ part to the URL
  const supposedLocation = `https://documentation.cluedin.net/versions/3.2.3${pathname}`;

  // we fetch the supposed old docs page location...
  fetch(supposedLocation)
      .then(response => {
          // ...and if the request is successful...
          if (!response.ok) {
              return;
          }
          // ...and if current URL equals the supposed location...
          if (window.location.href === supposedLocation.toLowerCase()) {
              return;
          }

          // ...then redirect the user to the supposed location
          window.location.href = supposedLocation;
      });
}

redirect();