# ncg-firp — firmaplus.ca

Static rebuild of **firmaplus.ca** (Firma Plus, firme comptable pour PME), replacing the WordPress / JupiterX site. Same structure as the Kerson Wallaw rebuild: utility bar, mega-menus, services and industries, credentials-driven team, Perspectives (insights), and lead-generation forms on every key page. Hosted on GitHub Pages; no build step is needed to serve it.

## Structure

| Path | Content |
|---|---|
| `index.html` | Home: hero and key figures, services, sectors, process, why Firma Plus and callback form, partners, offices, latest insights |
| `services/` | Services overview plus 6 service pages (with FAQ schema and callback form) |
| `secteurs/` | Sectors overview plus 6 sector pages |
| `equipe/` | Partners with bios, full team with an office filter |
| `bureaux/` | Both offices, each with its own team list |
| `perspectives/` | Insights index (topic filter) plus 6 articles |
| `devenir-client/` | Full intake form (lead generation) |
| `contact/`, `carrieres/`, `a-propos/` | Contact, careers (CV upload), about |
| `merci/`, `404.html`, `conditions-dutilisation/`, `confidentialite/` | Utility and legal pages |
| `a-propos/montreal-jonquiere/`, `a-propos/st-eustache/` | Redirects from the old WordPress URLs |
| `assets/` | CSS, JS, logo, images |
| `_build/` | `content.py` (all text and data) and `build.py` (page generator) |

## Editing

All content lives in `_build/content.py`. After editing, regenerate:

```
python3 _build/build.py
```

Commit the generated HTML along with the change.

## Forms

Every form posts through `assets/js/config.js`. While an endpoint there is empty, submitting opens the visitor's email client with a pre-filled message to the chosen office (`cpa@firmaplus.ca` or `inforn@firmaplus.ca`). Paste a Zoho Forms / Zoho CRM Web-to-Lead URL into `endpoints` to capture submissions directly. Successful posts redirect to `/merci/`.

Forms: `devenir-client` (intake), `rappel` (callback, on most pages), `contact`, `carrieres` (CV upload; needs an endpoint to receive files), `infolettre` (footer).

## Images to add

Team cards show initials until a portrait is added. Drop each photo in with the name below and it appears without any code change.

| Image | Path |
|---|---|
| Original logo (replace the SVG redraw, or keep it) | `assets/img/logo.svg` |
| Nicolas Lessard | `assets/img/equipe/nicolas-lessard.jpg` |
| Jérome Thibeault | `assets/img/equipe/jerome-thibeault.jpg` |
| Yannick P-Michel | `assets/img/equipe/yannick-p-michel.jpg` |
| Christophe Gingras | `assets/img/equipe/christophe-gingras.jpg` |
| Jessica Gingras | `assets/img/equipe/jessica-gingras.jpg` |
| Cathy Thibeault | `assets/img/equipe/cathy-thibeault.jpg` |
| Marie-Pierre Charron-Ligez | `assets/img/equipe/marie-pierre-charron-ligez.jpg` |
| Hadja Fatou Barry | `assets/img/equipe/hadja-fatou-barry.jpg` |
| Marie-Claude Fontaine | `assets/img/equipe/marie-claude-fontaine.jpg` |
| Patrick Royer | `assets/img/equipe/patrick-royer.jpg` |
| Roxanne Mongeau | `assets/img/equipe/roxanne-mongeau.jpg` |
| Noémie Girard-Tremblay | `assets/img/equipe/noemie-girard-tremblay.jpg` |
| Myriam Perreault | `assets/img/equipe/myriam-perreault.jpg` |
| Jessica Brassard-Samson | `assets/img/equipe/jessica-brassard-samson.jpg` |
| Tessa Haudecoeur | `assets/img/equipe/tessa-haudecoeur.jpg` |
| Manon Perreault | `assets/img/equipe/manon-perreault.jpg` |
| Nancy Charbonneau | `assets/img/equipe/nancy-charbonneau.jpg` |
| Stéphanie Groulx | `assets/img/equipe/stephanie-groulx.jpg` |
| Émilie Rose | `assets/img/equipe/emilie-rose.jpg` |
| Nancy-Lee Chevanelle | `assets/img/equipe/nancy-lee-chevanelle.jpg` |
| Arnold Nguessan | `assets/img/equipe/arnold-nguessan.jpg` |
| Fhami Aouani | `assets/img/equipe/fhami-aouani.jpg` |
| Osama Habshy | `assets/img/equipe/osama-habshy.jpg` |
| Isabelle Gagnon | `assets/img/equipe/isabelle-gagnon.jpg` |
| Anik Champagne | `assets/img/equipe/anik-champagne.jpg` |
| Wafa Ben Akacha | `assets/img/equipe/wafa-ben-akacha.jpg` |
| Fabiola Beauchemin | `assets/img/equipe/fabiola-beauchemin.jpg` |
| Khadija Ait Ben Ouissaden | `assets/img/equipe/khadija-ait-ben-ouissaden.jpg` |
| Chantal Longtin | `assets/img/equipe/chantal-longtin.jpg` |
| Liliana Aguiar | `assets/img/equipe/liliana-aguiar.jpg` |
| Félix Nadeau | `assets/img/equipe/felix-nadeau.jpg` |
| Claude Nadeau | `assets/img/equipe/claude-nadeau.jpg` |

## Stock photos

`assets/img/photos/` holds 19 photos from Unsplash, used under the [Unsplash License](https://unsplash.com/license) (free commercial use, no attribution required). Each file is named after its use (`hero-montreal.jpg`, `construction.jpg`, etc.). Source IDs, for reference or replacement:

| File | Unsplash image |
|---|---|
| hero-montreal | photo-1470181942237-78ce33fec141 |
| montreal-soir | photo-1770488767269-9200cca087fa |
| vieux-montreal | photo-1767290444122-5230a7fefef7 |
| equipe-reunion | photo-1758518730083-4c12527b6742 |
| equipe-bureau | photo-1758518731706-be5d5230e5a5 |
| conseil-table | photo-1714974528737-3e6c7e4d11af |
| signature | photo-1562564055-71e051d33c19 |
| analyse | photo-1758519289074-9de36003622b |
| calculatrice | photo-1709880945165-d2208c6ad2ec |
| paie | photo-1772588627373-729b0f47e5bb |
| graphiques | photo-1707157284454-553ef0a4ed0d |
| commerce | photo-1556740758-90de374c12ad |
| proprietaire | photo-1764173039192-2bbd508d5211 |
| construction | photo-1742112125567-3e8967bad60f |
| immobilier | photo-1624204386084-dd8c05e32226 |
| manufacturier | photo-1581091212991-8891c7d4bd9b |
| demarrage | photo-1522071820081-009f0129c71c |
| services-pro | photo-1551836022-4c4c79ecde51 |
| architecte | photo-1503387762-592deb58ef4e |

To swap one, replace the file under the same name. Keep landscape images about 1200 px wide (1920 px for the hero).

## Open items for Firma Plus to confirm

- Street addresses for Montréal and Jonquière (only Saint-Eustache is published).
- Sectors (`secteurs/`) were proposed from the current services. Validate or replace them.
- The 6 Perspectives articles are new drafts dated 2026-09 to 2026-11. Review before publishing.
- Privacy officer name (Loi 25) in `confidentialite/`. Have both legal pages validated.
- The "1 business day" callback promise used on the forms.
- Team titles: Cathy Thibeault is listed as "Directrice ressources humaines" on one old page and "Directrice du développement humain" on another. The rebuild uses the latter. Typos from the old site were corrected.

## GitHub Pages and DNS

Settings → Pages → Deploy from branch → `main` / root. Custom domain `firmaplus.ca`, then Enforce HTTPS once the certificate is issued. **Turn Pages on first, then change DNS.**

```
@    A     185.199.108.153 / 185.199.109.153 / 185.199.110.153 / 185.199.111.153
@    AAAA  2606:50c0:8000::153 / 8001::153 / 8002::153 / 8003::153
www  CNAME adamnormand.github.io
```

Remove the old A/CNAME records on `@` and `www`. Don't touch MX, SPF, DKIM or other TXT records.
