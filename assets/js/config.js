/*
 * Firma Plus — form routing configuration.
 *
 * Each form on the site has a data-form="<key>" attribute. When an endpoint is
 * set below (Zoho Forms, Zoho CRM Web-to-Lead, Formspree, etc.), the form is
 * POSTed there and the visitor is sent to /merci.html.
 * While an endpoint is empty, the site falls back to opening the visitor's
 * email client with a pre-filled message addressed to the right office.
 */
window.FIRMA_CONFIG = {
  endpoints: {
    "devenir-client": "",   // full intake form (devenir-client.html)
    "rappel": "",           // callback request (home page, service pages)
    "contact": "",          // general contact (contact.html)
    "carrieres": "",        // job application with CV (carrieres.html)
    "infolettre": ""        // newsletter signup (footer)
  },
  // Office routing used by the mailto fallback and passed as a hidden field.
  offices: {
    "montreal-saguenay": { label: "Montréal / Saguenay", email: "cpa@firmaplus.ca" },
    "saint-eustache":    { label: "Saint-Eustache (Rive-Nord)", email: "inforn@firmaplus.ca" }
  },
  defaultEmail: "cpa@firmaplus.ca"
};
