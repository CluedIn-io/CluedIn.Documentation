document.addEventListener('DOMContentLoaded', () => {
  const selector = document.getElementById('docs-version');
  if (!selector) return;

  const currentPrefix = selector.dataset.currentPrefix || '';
  if (currentPrefix) {
    // Older articles and homepage cards may have hard-coded root-relative links.
    document.querySelectorAll('.main-content [href^="/"]').forEach((link) => {
      const path = link.getAttribute('href');
      if (!path.startsWith('//') && !path.startsWith(currentPrefix + '/')) {
        link.setAttribute('href', currentPrefix + path);
      }
    });
  }

  selector.addEventListener('change', async () => {
    const targetPrefix = selector.value;
    const currentPath = window.location.pathname;
    const relativePath = currentPrefix && currentPath.startsWith(currentPrefix + '/')
      ? currentPath.slice(currentPrefix.length + 1)
      : currentPath.replace(/^\//, '');
    const targetPath = targetPrefix + relativePath;

    try {
      const response = await fetch(targetPath, { method: 'HEAD', redirect: 'follow' });
      if (response.ok && new URL(response.url).pathname !== '/404.html') {
        window.location.assign(targetPath + window.location.search + window.location.hash);
        return;
      }
    } catch (_) {
      // A missing or inaccessible article should still allow switching versions.
    }
    window.location.assign(targetPrefix);
  });
});
