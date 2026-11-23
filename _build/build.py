# -*- coding: utf-8 -*-
"""Generates the static Firma Plus site. Run from repo root: python3 _build/build.py"""
import os, sys, html, re, datetime
sys.path.insert(0, os.path.dirname(__file__))
from content import SITE, OFFICES, SERVICES, SECTORS, PARTNERS, STAFF, ARTICLES, ICONS

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BUILT = []
SVC = {s["slug"]: s for s in SERVICES}

def esc(s): return html.escape(s, quote=True)

def icon(name, cls="ico"):
    return f'<span class="{cls}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg></span>'

def initials(n):
    p = [x for x in re.split(r"[\s-]+", n) if x]
    return (p[0][0] + p[-1][0]).upper()

def slugify(n):
    import unicodedata
    n = unicodedata.normalize("NFKD", n).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-")

def fr_date(iso):
    m = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
    d = datetime.date.fromisoformat(iso)
    return f"{d.day} {m[d.month-1]} {d.year}"

SOCIAL = {
    "facebook": '<svg viewBox="0 0 24 24"><path d="M14 8h3V4h-3c-2.8 0-4 1.7-4 4.2V10H7v4h3v8h4v-8h3l1-4h-4V8.6c0-.4.3-.6.6-.6z"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24"><path d="M4 9h4v12H4zM6 3a2 2 0 1 1 0 4 2 2 0 0 1 0-4zm5 6h3.8v1.7h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.6 4.8 6V21h-4v-5.6c0-1.3 0-3-1.9-3s-2.1 1.4-2.1 2.9V21h-4z"/></svg>',
}

# ------------------------------------------------------------------ LAYOUT
def header(r, active):
    svc = "".join(f'<a href="{r}services/{s["slug"]}/"><b>{s["title"]}</b><small>{s["short"]}</small></a>' for s in SERVICES)
    sec = "".join(f'<a href="{r}secteurs/{s["slug"]}/"><b>{s["title"]}</b><small>{s["short"]}</small></a>' for s in SECTORS)
    def cur(k): return ' aria-current="page"' if active == k else ""
    phones = "".join(f'<a href="tel:{p[2]}"><span>{p[0]}</span>{p[1]}</a>' for o in OFFICES for p in o["phones"])
    return f'''<a class="skip" href="#main">Aller au contenu</a>
<div class="util"><div class="wrap">
  <div class="phones">{phones}</div>
  <div class="tools"><a href="mailto:{SITE["email"]}">{SITE["email"]}</a><button class="theme-toggle" type="button" aria-label="Basculer le thème clair ou sombre">Clair / Sombre</button></div>
</div></div>
<header class="site-header"><div class="wrap">
  <a class="logo" href="{r}" aria-label="Firma Plus — accueil"><img src="{r}assets/img/logo.svg" alt="Firma Plus" width="200" height="38"></a>
  <button class="burger" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav class="nav" id="nav" aria-label="Navigation principale">
    <ul>
      <li class="has-mega"><button type="button" aria-expanded="false"{cur("services")}>Services ▾</button>
        <div class="mega">{svc}<a class="all" href="{r}services/">Tous nos services →</a></div></li>
      <li class="has-mega"><button type="button" aria-expanded="false"{cur("secteurs")}>Secteurs ▾</button>
        <div class="mega">{sec}<a class="all" href="{r}secteurs/">Tous les secteurs →</a></div></li>
      <li><a href="{r}equipe/"{cur("equipe")}>Équipe</a></li>
      <li><a href="{r}perspectives/"{cur("perspectives")}>Perspectives</a></li>
      <li><a href="{r}a-propos/"{cur("apropos")}>À propos</a></li>
      <li><a href="{r}contact/"{cur("contact")}>Contact</a></li>
    </ul>
    <a class="btn btn-primary btn-sm" href="{r}devenir-client/">Devenir client</a>
  </nav>
</div></header>'''

def footer(r):
    svc = "".join(f'<li><a href="{r}services/{s["slug"]}/">{s["title"]}</a></li>' for s in SERVICES)
    sec = "".join(f'<li><a href="{r}secteurs/{s["slug"]}/">{s["title"]}</a></li>' for s in SECTORS)
    offices = "".join(
        f'<li><b style="color:#fff">{o["name"]}</b><br>' + "<br>".join(f'<a href="tel:{p[2]}">{p[1]}</a>' for p in o["phones"]) + f'<br><a href="mailto:{o["email"]}">{o["email"]}</a></li>'
        for o in OFFICES)
    return f'''<footer class="site-footer"><div class="wrap">
  <div class="fgrid">
    <div>
      <img class="flogo" src="{r}assets/img/logo.svg" alt="Firma Plus" width="180" height="34">
      <p>Firme comptable pour PME. Vous êtes entrepreneurs, nous sommes comptables.</p>
      <div class="social"><a href="{SITE["facebook"]}" aria-label="Facebook" rel="noopener">{SOCIAL["facebook"]}</a><a href="{SITE["linkedin"]}" aria-label="LinkedIn" rel="noopener">{SOCIAL["linkedin"]}</a></div>
      <h4 style="margin-top:26px">Infolettre</h4>
      <p style="font-size:.82rem">Échéances fiscales et conseils de gestion, une fois par mois.</p>
      <form class="news" data-form="infolettre" data-subject="Inscription à l’infolettre" novalidate>
        <label class="sr" for="nl-email">Courriel</label>
        <input id="nl-email" type="email" name="courriel" placeholder="Votre courriel" required>
        <input type="hidden" name="consentement" value="oui">
        <button class="btn btn-primary btn-sm" type="submit">OK</button>
      </form>
    </div>
    <div><h4>Services</h4><ul>{svc}</ul></div>
    <div><h4>Secteurs</h4><ul>{sec}</ul></div>
    <div><h4>Firme</h4><ul>
      <li><a href="{r}a-propos/">À propos</a></li><li><a href="{r}equipe/">Notre équipe</a></li>
      <li><a href="{r}bureaux/">Nos bureaux</a></li><li><a href="{r}perspectives/">Perspectives</a></li>
      <li><a href="{r}carrieres/">Carrières</a></li><li><a href="{r}devenir-client/">Devenir client</a></li></ul></div>
    <div><h4>Nous joindre</h4><ul>{offices}</ul></div>
  </div>
  <div class="legal"><span>© <span id="year">2026</span> Firma Plus. Tous droits réservés.</span>
    <span><a href="{r}conditions-dutilisation/">Conditions d’utilisation</a> · <a href="{r}confidentialite/">Politique de confidentialité</a></span></div>
</div></footer>
<div class="mcta"><a class="btn btn-outline btn-sm" href="tel:+14388170057">Appeler</a><a class="btn btn-primary btn-sm" href="{r}devenir-client/">Devenir client</a></div>'''

def page(path, title, desc, body, active="", schema=""):
    depth = path.count("/")
    r = "../" * depth
    canonical = "https://" + SITE["domain"] + "/" + (path[:-len("index.html")] if path.endswith("index.html") else path)
    doc = f'''<!doctype html>
<html lang="fr-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canonical}"><meta property="og:locale" content="fr_CA">
<link rel="icon" href="{r}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/site.css">
<script>try{{var t=localStorage.getItem('fp-theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
{schema}
</head>
<body data-root="{r}">
{header(r, active)}
<main id="main">
{body.replace("{root}", r)}
</main>
{footer(r)}
<script src="{r}assets/js/config.js"></script>
<script src="{r}assets/js/site.js"></script>
</body>
</html>
'''
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f: f.write(doc)
    BUILT.append(path)

def hero(kicker, h1, lead, ctas="", crumbs="", small=True, extra="", img=""):
    style = f' style="background-image:url({img})"' if img else ""
    return f'''<section class="hero{" small" if small else ""}"{style}><div class="wrap">
{f'<div class="crumbs">{crumbs}</div>' if crumbs else ""}<span class="kicker">{kicker}</span>
<h1>{h1}</h1>{f'<p class="lead">{lead}</p>' if lead else ""}{f'<div class="ctas">{ctas}</div>' if ctas else ""}{extra}
</div></section>'''

def crumbs(*items):
    return " / ".join(f'<a href="{h}">{t}</a>' if h else t for t, h in items)

def service_options(selected=""):
    o = '<option value="">Choisir…</option>' + "".join(f'<option value="{s["slug"]}"{" selected" if s["slug"]==selected else ""}>{s["title"]}</option>' for s in SERVICES)
    return o + '<option value="autre">Autre / je ne sais pas encore</option>'

def office_options():
    return '<option value="">Peu importe</option>' + "".join(f'<option value="{o["slug"]}">{o["name"]}</option>' for o in OFFICES)

HP = '<div class="hp" aria-hidden="true"><label>Site Web<input name="website" tabindex="-1" autocomplete="off"></label></div>'
CONSENT = '<label class="consent"><input type="checkbox" name="consentement" value="oui" required><span>J’accepte que Firma Plus utilise ces renseignements pour répondre à ma demande, conformément à la <a href="{root}confidentialite/">politique de confidentialité</a>. <span class="req">*</span></span></label>'
MARKETING = '<label class="consent"><input type="checkbox" name="infolettre" value="oui"><span>Je souhaite recevoir l’infolettre de Firma Plus (désabonnement en tout temps).</span></label>'

def callback_form(service=""):
    return f'''<form data-form="rappel" data-subject="Demande de rappel" novalidate>
<h3 style="margin-bottom:6px">Gagnez du temps, parlez à un spécialiste</h3>
<p class="muted" style="font-size:.9rem;margin-bottom:20px">Laissez vos coordonnées : un membre de l’équipe vous rappelle dans un délai d’un jour ouvrable.</p>
<div class="row"><div class="field"><label for="cb-nom">Nom <span class="req">*</span></label><input id="cb-nom" name="nom" autocomplete="name" required></div>
<div class="field"><label for="cb-ent">Entreprise</label><input id="cb-ent" name="entreprise" autocomplete="organization"></div></div>
<div class="row"><div class="field"><label for="cb-tel">Téléphone <span class="req">*</span></label><input id="cb-tel" name="telephone" type="tel" autocomplete="tel" required></div>
<div class="field"><label for="cb-mail">Courriel <span class="req">*</span></label><input id="cb-mail" name="courriel" type="email" autocomplete="email" required></div></div>
<div class="row"><div class="field"><label for="cb-svc">Sujet</label><select id="cb-svc" name="service">{service_options(service)}</select></div>
<div class="field"><label for="cb-bur">Bureau</label><select id="cb-bur" name="bureau">{office_options()}</select></div></div>
<div class="field"><label for="cb-moment">Moment préféré pour le rappel</label><select id="cb-moment" name="moment"><option>En matinée</option><option>En après-midi</option><option>En fin de journée</option><option>Peu importe</option></select></div>
{HP}{CONSENT}
<button class="btn btn-primary" type="submit">Demander un rappel</button>
<p class="form-msg" role="status"></p>
</form>'''

def cta_band(title="Prêt à déléguer votre comptabilité ?", text="Une première consultation pour comprendre vos besoins, sans engagement."):
    return f'''<section><div class="wrap"><div class="cta-band reveal">
<div><h2>{title}</h2><p>{text}</p></div>
<div class="ctas" style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-ghost" href="{{root}}contact/">Nous joindre</a><a class="btn" style="background:#fff;color:var(--navy)" href="{{root}}devenir-client/">Devenir client</a></div>
</div></div></section>'''

def photo(name, alt=""):
    return f'<img src="{{root}}assets/img/photos/{name}.jpg" alt="{esc(alt)}" loading="lazy">'

def media_card(href, s, more):
    return f'<a class="card media reveal" href="{href}"><div class="thumb">{photo(s["img"], s["title"])}</div><div class="cb">{icon(s["icon"])}<h3>{s["title"]}</h3><p>{s["short"]}</p><span class="more">{more} →</span></div></a>'

def svc_card(s, r="{root}"):
    return media_card(f'{r}services/{s["slug"]}/', s, "En savoir plus")

def sec_card(s):
    return media_card(f'{{root}}secteurs/{s["slug"]}/', s, "Voir le secteur")

def post_card(a):
    return f'''<a class="card post reveal" href="{{root}}perspectives/{a["slug"]}/"><div class="cover" style="background-image:url({{root}}assets/img/photos/{a["img"]}.jpg)"><span>{a["cat"]}</span></div>
<div class="meta"><span class="chip">{a["cat"]}</span><time datetime="{a["date"]}">{a["date"]}</time><span>{a["read"]} min</span></div>
<h3>{a["title"]}</h3><p>{a["excerpt"]}</p><span class="more">Lire →</span></a>'''

def member_card(name, cred, role, office, bio="", compact=False):
    slug = slugify(name)
    img = f'<img src="{{root}}assets/img/equipe/{slug}.jpg" alt="{esc(name)}" loading="lazy" onerror="this.remove()">'
    return f'''<div class="member reveal" data-office="{office}"><div class="ph" aria-hidden="true">{initials(name)}{img}</div><div class="bd">
<b>{name}</b>{f'<span class="cred">{cred}</span><br>' if cred else ""}<span class="role">{role}</span>{f'<p>{bio}</p>' if bio and not compact else ""}</div></div>'''

def office_card(o):
    phones = "".join(f'<dt>{p[0]}</dt><dd><a href="tel:{p[2]}">{p[1]}</a></dd>' for p in o["phones"])
    addr = f'<dt>Adresse</dt><dd>{o["address"]}</dd>' if o["address"] else ""
    return f'''<div class="card office media reveal"><div class="thumb">{photo(o["img"], o["name"])}</div><div class="cb">{icon("pin")}<h3>{o["name"]}</h3><span class="muted" style="font-size:.85rem">{o["entity"]}</span>
<p style="margin-top:10px">{o["blurb"]}</p>
<dl>{phones}<dt>Courriel</dt><dd><a href="mailto:{o["email"]}">{o["email"]}</a></dd>{addr}</dl>
<span class="more"><a href="{{root}}bureaux/{o["slug"]}/">Voir le bureau et l’équipe →</a></span></div></div>'''

ORG_SCHEMA = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"AccountingService","name":"Firma Plus","url":"https://firmaplus.ca/","email":"cpa@firmaplus.ca","telephone":"+1-438-817-0057","areaServed":"Québec","sameAs":["https://www.facebook.com/Firmacompta","https://www.linkedin.com/company/firmagestion/"],"department":[{"@type":"AccountingService","name":"Cabinet Firma Plus CPA Inc.","telephone":"+1-438-817-0057"},{"@type":"AccountingService","name":"Cabinet Firma Plus Rive-Nord S.E.N.C.R.L.","telephone":"+1-450-472-2828","address":{"@type":"PostalAddress","streetAddress":"450, rue du Parc, bureau 113","addressLocality":"Saint-Eustache","addressRegion":"QC","postalCode":"J7R 7G6","addressCountry":"CA"}}]}</script>'''

N_PEOPLE = len(PARTNERS) + len(STAFF)
P = "{root}assets/img/photos/"

# ------------------------------------------------------------------ HOME
def build_home():
    stats = f'''<div class="stats">
<div class="stat"><b>3</b><span>points de service</span></div>
<div class="stat"><b>{N_PEOPLE}</b><span>professionnels</span></div>
<div class="stat"><b>20+</b><span>ans d’expérience en financement d’entreprises</span></div>
<div class="stat"><b>6</b><span>services intégrés pour PME</span></div></div>'''
    body = hero("Services comptables pour PME", "Vous êtes entrepreneurs.<br>Nous sommes comptables.",
        "Tenue de livres, paie, prévisions financières, directeur financier fractionné et dossiers de financement : une équipe de CPA et de techniciens qui vous libère de l’administratif pour que vous vous concentriez sur la croissance.",
        '<a class="btn btn-primary" href="{root}devenir-client/">Devenir client</a><a class="btn btn-ghost" href="{root}contact/">Planifier une consultation</a>',
        small=False, img="{root}assets/img/photos/hero-montreal.jpg",
        extra='<div class="tags" style="margin-top:28px"><span>CPA</span><span>Tenue de livres</span><span>Paie</span><span>CFO à la demande</span><span>Déboursés bancaires</span><span>Impôts</span></div>' + stats)
    body += f'''<section><div class="wrap split" style="align-items:center">
<div class="reveal"><span class="kicker">Notre équipe est là pour vous</span><h2>Une firme québécoise au service des PME</h2>
<p class="muted" style="margin-top:16px;font-size:1.05rem">Notre équipe de professionnels vous accompagne avec des solutions comptables personnalisées, innovantes et de haute qualité. Rapides, efficaces et toujours à l’écoute, nous mettons notre savoir-faire au service des PME de Montréal, du Saguenay et de la Rive-Nord pour assurer une gestion financière optimale.</p>
<div class="ctas" style="display:flex;gap:12px;margin-top:26px;flex-wrap:wrap"><a class="btn btn-primary" href="{{root}}equipe/">Découvrez nos experts</a><a class="btn btn-outline" href="{{root}}a-propos/">À propos</a></div></div>
<div class="photo wide reveal">{photo("conseil-table", "Rencontre entre une comptable de Firma Plus et des dirigeants de PME")}<div class="badge"><b>{N_PEOPLE}</b>professionnels dans 3 points de service</div></div>
</div></section>
<section class="alt"><div class="wrap">
<div class="head"><span class="kicker">Nos services</span><h2>Des services personnalisables selon vos besoins</h2>
<p>De la gestion de vos livres à l’accompagnement de vos demandes de financement, notre équipe vous soutient à chaque étape. Vous choisissez la fréquence et l’étendue du mandat.</p></div>
<div class="grid g3">{"".join(svc_card(s) for s in SERVICES)}</div></div></section>'''
    body += f'''<section><div class="wrap">
<div class="head"><span class="kicker">Secteurs</span><h2>Nous connaissons votre réalité</h2>
<p>Chaque secteur a ses enjeux comptables. Nous adaptons nos méthodes, nos rapports et nos échéanciers à la façon dont votre entreprise gagne son argent.</p></div>
<div class="grid g3">{"".join(sec_card(s) for s in SECTORS)}</div></div></section>'''
    body += '''<section class="dark band" style="background-image:url({root}assets/img/photos/equipe-reunion.jpg)"><div class="wrap">
<div class="head"><span class="kicker" style="color:#8ec2f5">Notre façon de travailler</span><h2>Simple à démarrer, rigoureux à chaque mois</h2></div>
<div class="steps">
<div class="step reveal"><h3>Consultation</h3><p>Nous faisons le point sur vos livres, vos échéances et vos objectifs. Sans engagement.</p></div>
<div class="step reveal"><h3>Proposition</h3><p>Un mandat sur mesure : services, fréquence et honoraires établis clairement dès le départ.</p></div>
<div class="step reveal"><h3>Mise en place</h3><p>Accès à vos systèmes, rattrapage s’il y a lieu et processus simple pour nous transmettre vos pièces.</p></div>
<div class="step reveal"><h3>Suivi régulier</h3><p>Livres à jour, remises dans les délais et rapports qui servent vos décisions.</p></div>
</div></div></section>'''
    body += f'''<section><div class="wrap split">
<div class="reveal"><span class="kicker">Pourquoi Firma Plus</span><h2>Rapides, efficaces et toujours à l’écoute</h2>
<p class="muted" style="margin-top:16px">Firma Plus a été fondée pour offrir aux PME des solutions comptables personnalisées, innovantes et de haute qualité, et ce, rapidement. Notre mission : alléger vos charges administratives pour que vous puissiez vous concentrer pleinement sur la croissance de votre entreprise.</p>
<div class="grid g2" style="margin-top:30px">
<div>{icon("shield")}<h3 style="margin:12px 0 6px">Rigueur professionnelle</h3><p class="muted" style="font-size:.93rem">Des CPA encadrent les dossiers, de la tenue de livres à la certification.</p></div>
<div>{icon("clock")}<h3 style="margin:12px 0 6px">Information rapide</h3><p class="muted" style="font-size:.93rem">Des chiffres à jour quand vous en avez besoin, pas trois mois plus tard.</p></div>
<div>{icon("cloud")}<h3 style="margin:12px 0 6px">Technologies actuelles</h3><p class="muted" style="font-size:.93rem">Outils infonuagiques et processus automatisés pour moins de papier et plus de fiabilité.</p></div>
<div>{icon("handshake")}<h3 style="margin:12px 0 6px">Une équipe accessible</h3><p class="muted" style="font-size:.93rem">Un interlocuteur attitré qui connaît votre entreprise et répond à vos questions.</p></div>
</div>
<div class="quote" style="margin-top:36px">En laissant la comptabilité à des experts, j’ai pu me concentrer sur la croissance de l’entreprise. Je recommande cette démarche pour une gestion financière efficace et une croissance durable.<cite>Jérome Thibeault, associé</cite></div>
</div>
<div class="panel sticky reveal">{callback_form()}</div>
</div></section>'''
    body += f'''<section class="alt"><div class="wrap">
<div class="head"><span class="kicker">Nos associés</span><h2>Des associés engagés, une équipe de {N_PEOPLE} professionnels</h2>
<p>CPA, techniciens comptables, spécialistes de la certification et de la paie : une équipe complète, répartie dans nos bureaux de Montréal, du Saguenay et de Saint-Eustache.</p></div>
<div class="team five">{"".join(member_card(p["name"], p["cred"], p["role"], p["office"]) for p in PARTNERS)}</div>
<p style="margin-top:28px"><a class="btn btn-outline" href="{{root}}equipe/">Découvrez nos experts</a></p>
</div></section>'''
    body += f'''<section><div class="wrap">
<div class="head"><span class="kicker">Nos bureaux</span><h2>Trois points de service pour mieux vous servir</h2></div>
<div class="grid g2">{"".join(office_card(o) for o in OFFICES)}</div></div></section>'''
    body += f'''<section class="alt"><div class="wrap">
<div class="head"><span class="kicker">Perspectives</span><h2>Conseils et échéances pour les dirigeants de PME</h2></div>
<div class="grid g3">{"".join(post_card(a) for a in ARTICLES[:3])}</div>
<p style="margin-top:28px"><a class="btn btn-outline" href="{{root}}perspectives/">Toutes les perspectives</a></p></div></section>'''
    body += cta_band()
    page("index.html", "Firme comptable pour PME | Firma Plus", "Firma Plus, firme comptable pour PME à Montréal, au Saguenay et à Saint-Eustache : tenue de livres, paie, prévisions financières, directeur financier fractionné et dossiers de financement.", body, schema=ORG_SCHEMA)

# ------------------------------------------------------------------ SERVICES
def build_services():
    body = hero("Nos services", "Des services comptables complets pour PME",
        "De la gestion de vos livres à l’accompagnement de vos besoins de financement, notre équipe de spécialistes vous soutient à chaque étape.",
        '<a class="btn btn-primary" href="{root}devenir-client/">Devenir client</a><a class="btn btn-ghost" href="{root}contact/">Planifier une consultation</a>',
        crumbs(("Accueil", "{root}"), ("Services", "")), img=P+"equipe-reunion.jpg")
    body += f'<section><div class="wrap"><div class="grid g3">{"".join(svc_card(s) for s in SERVICES)}</div></div></section>'
    body += '''<section class="alt"><div class="wrap split"><div class="reveal"><span class="kicker">Forfaits sur mesure</span><h2>Vous choisissez l’étendue du mandat</h2>
<p class="muted" style="margin-top:14px">Chaque service peut être retenu seul ou combiné aux autres. La plupart de nos clients commencent par la tenue de livres et la paie, puis ajoutent les prévisions ou le directeur financier fractionné à mesure que l’entreprise grandit.</p>
<ul class="check"><li>Fréquence hebdomadaire, mensuelle ou trimestrielle</li><li>Honoraires établis à l’avance</li><li>Rattrapage comptable possible dès le départ</li><li>Un interlocuteur attitré</li></ul></div>
<div class="panel reveal">''' + callback_form() + '</div></div></section>'
    body += cta_band()
    page("services/index.html", "Services comptables pour PME | Firma Plus", "Tenue de livres, service de paie, budget et prévisions, directeur financier fractionné, accompagnement lors de déboursés bancaires, impôts.", body, "services")

    for s in SERVICES:
        faq = "".join(f'<h3>{q}</h3><p>{a}</p>' for q, a in s["faq"])
        secs = [x for x in SECTORS if s["slug"] in x["services"]]
        others = [x for x in SERVICES if x["slug"] != s["slug"]][:3]
        schema = '<script type="application/ld+json">' + __import__("json").dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faq"]]}, ensure_ascii=False) + '</script>'
        body = hero("Service", s["title"], s["short"],
            f'<a class="btn btn-primary" href="{{root}}devenir-client/?service={s["slug"]}">Démarrer</a><a class="btn btn-ghost" href="#rappel">Être rappelé</a>',
            crumbs(("Accueil", "{root}"), ("Services", "{root}services/"), (s["title"], "")), img=P+s["img"]+".jpg")
        body += f'''<section><div class="wrap split">
<div class="prose reveal"><p style="font-size:1.1rem">{s["intro"]}</p>
<h2>Ce que nous faisons pour vous</h2><ul class="check">{"".join(f"<li>{b}</li>" for b in s["bullets"])}</ul>
<p>{s["close"]}</p>
<h2>Pour qui</h2><ul class="check">{"".join(f"<li>{b}</li>" for b in s["for"])}</ul>
<h2>Questions fréquentes</h2>{faq}
{f'<h2>Secteurs où ce service fait la différence</h2><p>' + " · ".join(f'<a href="{{root}}secteurs/{x["slug"]}/">{x["title"]}</a>' for x in secs) + '</p>' if secs else ""}
</div>
<div class="sticky" style="position:sticky;top:110px"><div class="photo wide reveal" style="margin-bottom:22px">{photo(s["img"], s["title"])}</div><div class="panel reveal" id="rappel">{callback_form(s["slug"])}</div></div>
</div></section>
<section class="alt"><div class="wrap"><div class="head"><span class="kicker">Aussi</span><h2>Services complémentaires</h2></div>
<div class="grid g3">{"".join(svc_card(o) for o in others)}</div></div></section>'''
        body += cta_band()
        page(f"services/{s['slug']}/index.html", f"{s['title']} | Firma Plus", s["short"], body, "services", schema)

# ------------------------------------------------------------------ SECTORS
def build_sectors():
    body = hero("Secteurs", "Une comptabilité adaptée à votre secteur",
        "Les chiffres d’un entrepreneur en construction ne se lisent pas comme ceux d’un cabinet de services. Nous adaptons nos méthodes à la façon dont votre entreprise fonctionne.",
        '<a class="btn btn-primary" href="{root}devenir-client/">Devenir client</a>', crumbs(("Accueil", "{root}"), ("Secteurs", "")), img=P+"vieux-montreal.jpg")
    body += f'<section><div class="wrap"><div class="grid g3">{"".join(sec_card(s) for s in SECTORS)}</div></div></section>' + cta_band("Votre secteur n’est pas dans la liste ?", "Nous accompagnons des PME de tous les horizons. Parlons de votre réalité.")
    page("secteurs/index.html", "Secteurs desservis | Firma Plus", "Construction, immobilier, commerce, services professionnels, manufacturier et entreprises en croissance.", body, "secteurs")
    for s in SECTORS:
        body = hero("Secteur", s["title"], s["short"],
            f'<a class="btn btn-primary" href="{{root}}devenir-client/?secteur={s["slug"]}">Parler à un spécialiste</a>',
            crumbs(("Accueil", "{root}"), ("Secteurs", "{root}secteurs/"), (s["title"], "")), img=P+s["img"]+".jpg")
        body += f'''<section><div class="wrap split">
<div class="reveal"><span class="kicker">Vos enjeux</span><h2>Ce que nous voyons dans votre secteur</h2>
<ul class="check" style="margin-top:20px">{"".join(f"<li>{i}</li>" for i in s["issues"])}</ul>
<h2 style="margin-top:46px">Comment nous vous aidons</h2>
<div class="grid g2" style="margin-top:22px">{"".join(svc_card(SVC[x]) for x in s["services"])}</div></div>
<div class="panel sticky reveal">{callback_form()}</div></div></section>'''
        body += cta_band()
        page(f"secteurs/{s['slug']}/index.html", f"Comptable pour {s['title'].lower()} | Firma Plus", s["short"], body, "secteurs")

# ------------------------------------------------------------------ TEAM & OFFICES
def build_team():
    partners = "".join(member_card(p["name"], p["cred"], p["role"], p["office"], p["bio"]) for p in PARTNERS)
    staff = "".join(member_card(n, c, r_, o, compact=True) for n, c, r_, o in STAFF)
    body = hero("Notre équipe", "Notre équipe est là pour vous",
        "Une équipe de professionnels compétents, dynamiques et accessibles, qui met son savoir-faire au service des PME pour assurer une gestion financière optimale.",
        '<a class="btn btn-primary" href="{root}devenir-client/">Travailler avec nous</a><a class="btn btn-ghost" href="{root}carrieres/">Se joindre à l’équipe</a>',
        crumbs(("Accueil", "{root}"), ("Équipe", "")), img=P+"equipe-bureau.jpg")
    body += f'''<section><div class="wrap"><div class="head"><span class="kicker">Associés</span><h2>La direction</h2></div>
<div class="team">{partners}</div></div></section>
<section class="alt"><div class="wrap"><div class="head"><span class="kicker">Professionnels</span><h2>Les personnes qui tiennent vos dossiers</h2></div>
<div class="filters" data-target="#staff" role="group" aria-label="Filtrer par bureau"><button class="on" data-f="all" type="button">Tous</button><button data-f="mtl" type="button">Montréal / Saguenay</button><button data-f="rn" type="button">Saint-Eustache</button></div>
<div class="team compact" id="staff">{staff}</div></div></section>'''
    body += cta_band("Envie de faire partie de l’équipe ?", "Nous recrutons des techniciens comptables et des CPA dans nos trois points de service.").replace("{root}contact/", "{root}carrieres/").replace("Nous joindre", "Carrières")
    page("equipe/index.html", "Notre équipe | Firma Plus", "Associés, CPA, techniciens comptables et spécialistes de la certification de Firma Plus à Montréal, au Saguenay et à Saint-Eustache.", body, "equipe")

    body = hero("Nos bureaux", "Trois points de service, une même rigueur", "Montréal, Saguenay et Saint-Eustache. Rencontrez-nous en personne ou à distance.", "", crumbs(("Accueil", "{root}"), ("Bureaux", "")), img=P+"montreal-soir.jpg")
    body += f'<section><div class="wrap"><div class="grid g2">{"".join(office_card(o) for o in OFFICES)}</div></div></section>' + cta_band()
    page("bureaux/index.html", "Nos bureaux | Firma Plus", "Bureaux de Firma Plus à Montréal, au Saguenay (Jonquière) et à Saint-Eustache.", body)

    for o in OFFICES:
        code = "mtl" if o["slug"] == "montreal-saguenay" else "rn"
        people = [member_card(p["name"], p["cred"], p["role"], p["office"]) for p in PARTNERS if code in p["office"]]
        people += [member_card(n, c, r_, of, compact=True) for n, c, r_, of in STAFF if code in of]
        phones = "".join(f'<dt>{p[0]}</dt><dd><a href="tel:{p[2]}">{p[1]}</a></dd>' for p in o["phones"])
        addr = f'<dt>Adresse</dt><dd>{o["address"]}</dd>' if o["address"] else ""
        body = hero("Bureau", o["name"], o["entity"], f'<a class="btn btn-primary" href="{{root}}devenir-client/?bureau={o["slug"]}">Devenir client</a><a class="btn btn-ghost" href="tel:{o["phones"][0][2]}">Appeler</a>',
            crumbs(("Accueil", "{root}"), ("Bureaux", "{root}bureaux/"), (o["name"], "")), img=P+o["img"]+".jpg")
        body += f'''<section><div class="wrap split"><div class="reveal"><h2>Nous joindre</h2><p class="muted" style="margin-top:12px">{o["blurb"]}</p>
<div class="office"><dl>{phones}<dt>Courriel</dt><dd><a href="mailto:{o["email"]}">{o["email"]}</a></dd>{addr}</dl></div></div>
<div class="panel reveal">{callback_form().replace(f'<option value="{o["slug"]}">', f'<option value="{o["slug"]}" selected>')}</div></div></section>
<section class="alt"><div class="wrap"><div class="head"><h2>L’équipe de {o["name"]}</h2></div><div class="team compact">{"".join(people)}</div></div></section>'''
        page(f"bureaux/{o['slug']}/index.html", f"{o['entity']} — {o['name']} | Firma Plus", f"Coordonnées et équipe du bureau {o['name']} de Firma Plus.", body)

# ------------------------------------------------------------------ INSIGHTS
def build_insights():
    cats = sorted(set(a["cat"] for a in ARTICLES))
    body = hero("Perspectives", "Conseils, échéances et analyses pour les dirigeants de PME",
        "Fiscalité, paie, financement et gestion : ce que nos professionnels voient sur le terrain, expliqué simplement.", "", crumbs(("Accueil", "{root}"), ("Perspectives", "")), img=P+"analyse.jpg")
    body += f'''<section><div class="wrap">
<div class="filters" data-target="#posts" role="group" aria-label="Filtrer par thème"><button class="on" data-f="all" type="button">Tous</button>{"".join(f'<button data-f="{c}" type="button">{c}</button>' for c in cats)}</div>
<div class="grid g3" id="posts">{"".join(post_card(a).replace('class="card post reveal"', f'class="card post reveal" data-office="{a["cat"]}"') for a in ARTICLES)}</div></div></section>'''
    body += cta_band("Recevez nos perspectives chaque mois", "Inscrivez-vous à l’infolettre au bas de cette page, ou parlez directement à un spécialiste.")
    page("perspectives/index.html", "Perspectives | Firma Plus", "Articles et conseils de Firma Plus pour les dirigeants de PME : fiscalité, paie, financement et gestion.", body, "perspectives")
    import json
    for i, a in enumerate(ARTICLES):
        related = [x for x in ARTICLES if x["slug"] != a["slug"]][:3]
        schema = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "datePublished": a["date"], "author": {"@type": "Organization", "name": "Firma Plus"}, "publisher": {"@type": "Organization", "name": "Firma Plus"}, "description": a["excerpt"]}, ensure_ascii=False) + '</script>'
        body = hero(a["cat"], a["title"], a["excerpt"], "", crumbs(("Accueil", "{root}"), ("Perspectives", "{root}perspectives/"), (a["cat"], "")), img=P+a["img"]+".jpg",
            extra=f'<p class="meta" style="color:#c3d2e8;margin-top:18px"><time datetime="{a["date"]}">{a["date"]}</time> · {a["read"]} min de lecture · Firma Plus</p>')
        body += f'''<section><div class="wrap split"><article class="prose reveal">{a["body"]}
<p class="muted" style="font-size:.82rem;margin-top:32px">Cet article est fourni à titre informatif et ne constitue pas un avis professionnel. Les règles fiscales évoluent : consultez un professionnel avant d’agir.</p></article>
<aside class="panel sticky reveal">{callback_form()}</aside></div></section>
<section class="alt"><div class="wrap"><div class="head"><h2>À lire aussi</h2></div><div class="grid g3">{"".join(post_card(x) for x in related)}</div></div></section>'''
        page(f"perspectives/{a['slug']}/index.html", f"{a['title']} | Firma Plus", a["excerpt"], body, "perspectives", schema)

# ------------------------------------------------------------------ OTHER PAGES
def build_about():
    body = hero("À propos", "Nous sommes Firma Plus",
        "Une firme comptable fondée pour fournir aux PME des solutions comptables personnalisées, innovantes et de haute qualité, et ce, rapidement.",
        '<a class="btn btn-primary" href="{root}equipe/">Rencontrer l’équipe</a>', crumbs(("Accueil", "{root}"), ("À propos", "")), img=P+"vieux-montreal.jpg")
    body += f'''<section><div class="wrap split"><div class="prose reveal">
<h2 style="margin-top:0">Notre mission</h2>
<p>Chez Firma Plus, notre mission est d’alléger les charges administratives de nos clients, leur permettant ainsi de se concentrer pleinement sur la croissance de leur entreprise.</p>
<p>Pour ce faire, nous réunissons une équipe de professionnels compétents, dynamiques et accessibles, qui évolue dans un environnement de travail stimulant. Grâce à l’intégration des technologies actuelles, nous nous engageons à fournir des solutions comptables personnalisées, innovantes et de haute qualité.</p>
<h2>Ce qui nous distingue</h2>
<ul class="check"><li><strong>Une origine en financement d’entreprises.</strong> Notre associé principal cumule plus de vingt ans d’expérience en financement : nous savons ce que les prêteurs attendent de vos chiffres.</li>
<li><strong>Une vision d’entrepreneur.</strong> Nos associés ont bâti et fait croître des entreprises, notamment en immobilier. Nous savons ce que représente une comptabilité qui suit.</li>
<li><strong>Une équipe complète.</strong> Tenue de livres, paie, certification, fiscalité et accompagnement stratégique sous un même toit.</li>
<li><strong>Trois points de service.</strong> Montréal, Saguenay et Saint-Eustache, avec la possibilité de tout faire à distance.</li></ul>
<h2>Nos entités</h2>
<p><strong>Cabinet Firma Plus CPA Inc.</strong> dessert la clientèle de Montréal et du Saguenay. <strong>Cabinet Firma Plus Rive-Nord S.E.N.C.R.L.</strong> dessert la clientèle de Saint-Eustache et de la Rive-Nord.</p>
</div><div class="reveal">
<div class="photo wide" style="margin-bottom:26px">{photo("equipe-bureau", "L’équipe de Firma Plus en réunion")}</div>
<div class="panel"><span class="kicker">En bref</span>
<div class="stats" style="grid-template-columns:1fr 1fr;margin-top:10px;color:var(--ink)"><div class="stat"><b>3</b><span class="muted">points de service</span></div><div class="stat"><b>{N_PEOPLE}</b><span class="muted">professionnels</span></div><div class="stat"><b>2</b><span class="muted">cabinets</span></div><div class="stat"><b>6</b><span class="muted">services</span></div></div></div>
<div class="quote" style="margin-top:30px">Fort de plus de vingt ans d’expérience en financement d’entreprises, Nicolas reconnaît l’importance d’un accès rapide aux informations financières.<cite>Nicolas Lessard, M.Sc. Fin., CPA — associé principal</cite></div>
</div></div></section>
<section class="alt"><div class="wrap"><div class="head"><h2>Nos associés</h2></div><div class="team">{"".join(member_card(p["name"], p["cred"], p["role"], p["office"], p["bio"]) for p in PARTNERS)}</div>
<p style="margin-top:28px"><a class="btn btn-outline" href="{{root}}equipe/">Toute l’équipe</a></p></div></section>
<section><div class="wrap"><div class="head"><h2>Nos bureaux</h2></div><div class="grid g2">{"".join(office_card(o) for o in OFFICES)}</div></div></section>'''
    body += cta_band()
    page("a-propos/index.html", "À propos de Firma Plus", "Firma Plus est une firme comptable fondée pour fournir aux PME des solutions comptables personnalisées, innovantes et de haute qualité.", body, "apropos")

def build_intake():
    svc = "".join(f'<label><input type="checkbox" name="service" value="{s["slug"]}"> {s["title"]}</label>' for s in SERVICES)
    sec = '<option value="">Choisir…</option>' + "".join(f'<option value="{s["slug"]}">{s["title"]}</option>' for s in SECTORS) + '<option value="autre">Autre</option>'
    body = hero("Devenir client", "Parlez-nous de votre entreprise",
        "Quelques questions pour bien comprendre vos besoins. Un spécialiste vous répond dans un délai d’un jour ouvrable avec une proposition ou une rencontre.",
        "", crumbs(("Accueil", "{root}"), ("Devenir client", "")), img=P+"signature.jpg")
    body += f'''<section><div class="wrap split"><div class="panel reveal">
<form data-form="devenir-client" data-subject="Nouveau client potentiel" novalidate>
<h3 style="margin-bottom:18px">1. Vos coordonnées</h3>
<div class="row"><div class="field"><label for="i-nom">Nom complet <span class="req">*</span></label><input id="i-nom" name="nom" autocomplete="name" required></div>
<div class="field"><label for="i-titre">Fonction</label><input id="i-titre" name="fonction" autocomplete="organization-title"></div></div>
<div class="row"><div class="field"><label for="i-mail">Courriel <span class="req">*</span></label><input id="i-mail" type="email" name="courriel" autocomplete="email" required></div>
<div class="field"><label for="i-tel">Téléphone <span class="req">*</span></label><input id="i-tel" type="tel" name="telephone" autocomplete="tel" required></div></div>
<h3 style="margin:16px 0 18px">2. Votre entreprise</h3>
<div class="row"><div class="field"><label for="i-ent">Nom de l’entreprise <span class="req">*</span></label><input id="i-ent" name="entreprise" autocomplete="organization" required></div>
<div class="field"><label for="i-sec">Secteur</label><select id="i-sec" name="secteur">{sec}</select></div></div>
<div class="row"><div class="field"><label for="i-emp">Nombre d’employés</label><select id="i-emp" name="employes"><option value="">Choisir…</option><option>Aucun</option><option>1 à 5</option><option>6 à 20</option><option>21 à 50</option><option>Plus de 50</option></select></div>
<div class="field"><label for="i-ca">Chiffre d’affaires annuel</label><select id="i-ca" name="chiffre_affaires"><option value="">Choisir…</option><option>Moins de 250 000 $</option><option>250 000 $ à 1 M$</option><option>1 M$ à 5 M$</option><option>5 M$ à 20 M$</option><option>Plus de 20 M$</option></select></div></div>
<div class="row"><div class="field"><label for="i-log">Logiciel comptable actuel</label><input id="i-log" name="logiciel" placeholder="Ex. QuickBooks, Sage, Acomba, Zoho Books, aucun"></div>
<div class="field"><label for="i-etat">État des livres</label><select id="i-etat" name="etat_livres"><option value="">Choisir…</option><option>À jour</option><option>Quelques mois de retard</option><option>Plus d’un an de retard</option><option>Nouvelle entreprise</option></select></div></div>
<h3 style="margin:16px 0 18px">3. Vos besoins</h3>
<fieldset><legend class="lbl" style="margin-bottom:10px">Services recherchés</legend><div class="opts">{svc}</div></fieldset>
<div class="row"><div class="field"><label for="i-bur">Bureau souhaité</label><select id="i-bur" name="bureau">{office_options()}</select></div>
<div class="field"><label for="i-quand">Échéance</label><select id="i-quand" name="echeance"><option>Dès que possible</option><option>D’ici 1 mois</option><option>D’ici 3 mois</option><option>Je m’informe</option></select></div></div>
<div class="field"><label for="i-msg">Précisions</label><textarea id="i-msg" name="message" placeholder="Votre situation, vos échéances, vos questions"></textarea></div>
<div class="field"><label for="i-src">Comment avez-vous entendu parler de nous ?</label><select id="i-src" name="source"><option value="">Choisir…</option><option>Recommandation</option><option>Recherche Web</option><option>LinkedIn</option><option>Facebook</option><option>Institution financière</option><option>Autre</option></select></div>
{HP}{CONSENT}{MARKETING}
<button class="btn btn-primary" type="submit">Envoyer ma demande</button>
<p class="form-msg" role="status"></p>
</form></div>
<div class="reveal"><div class="photo wide" style="margin-bottom:28px">{photo("services-pro", "Une conseillère de Firma Plus avec une cliente")}</div><span class="kicker">La suite</span><h2>Ce qui se passe ensuite</h2>
<div class="steps" style="grid-template-columns:1fr;margin-top:26px">
<div class="step"><h3>Nous vous appelons</h3><p>Un spécialiste communique avec vous dans un délai d’un jour ouvrable.</p></div>
<div class="step"><h3>Nous analysons</h3><p>Nous évaluons l’état de vos livres et vos échéances, sans engagement.</p></div>
<div class="step"><h3>Nous proposons</h3><p>Vous recevez une proposition claire : services, fréquence et honoraires.</p></div></div>
<div class="note" style="margin-top:30px">Vous préférez téléphoner ? Montréal <a href="tel:+14388170057">438-817-0057</a> · Saguenay <a href="tel:+15817054344">581-705-4344</a> · Saint-Eustache <a href="tel:+14504722828">450-472-2828</a></div>
</div></div></section>'''
    page("devenir-client/index.html", "Devenir client | Firma Plus", "Parlez-nous de votre entreprise et recevez une proposition de services comptables sur mesure.", body)

def build_contact():
    body = hero("Nous joindre", "Contactez nos spécialistes",
        "Tenue de livres, paie, budgets et prévisions, déboursés bancaires ou tout autre besoin comptable : nous répondons avec professionnalisme et expertise.",
        "", crumbs(("Accueil", "{root}"), ("Contact", "")), img=P+"montreal-soir.jpg")
    body += f'''<section><div class="wrap split"><div class="panel reveal">
<form data-form="contact" data-subject="Demande d’information" novalidate>
<h3 style="margin-bottom:18px">Écrivez-nous</h3>
<div class="row"><div class="field"><label for="c-nom">Nom <span class="req">*</span></label><input id="c-nom" name="nom" autocomplete="name" required></div>
<div class="field"><label for="c-ent">Entreprise</label><input id="c-ent" name="entreprise" autocomplete="organization"></div></div>
<div class="row"><div class="field"><label for="c-mail">Courriel <span class="req">*</span></label><input id="c-mail" type="email" name="courriel" autocomplete="email" required></div>
<div class="field"><label for="c-tel">Téléphone</label><input id="c-tel" type="tel" name="telephone" autocomplete="tel"></div></div>
<div class="row"><div class="field"><label for="c-svc">Sujet</label><select id="c-svc" name="service">{service_options()}</select></div>
<div class="field"><label for="c-bur">Bureau</label><select id="c-bur" name="bureau">{office_options()}</select></div></div>
<div class="field"><label for="c-msg">Message <span class="req">*</span></label><textarea id="c-msg" name="message" required></textarea></div>
{HP}{CONSENT}{MARKETING}
<button class="btn btn-primary" type="submit">Envoyer</button><p class="form-msg" role="status"></p>
</form></div>
<div class="reveal">{"".join(office_card(o) for o in OFFICES).replace('class="card office reveal"', 'class="card office" style="margin-bottom:22px"')}
<p class="muted">Vous cherchez un emploi ? Voyez nos <a href="{{root}}carrieres/">carrières</a>.</p></div>
</div></section>'''
    page("contact/index.html", "Contactez nos spécialistes | Firma Plus", "Coordonnées des bureaux de Firma Plus à Montréal, au Saguenay et à Saint-Eustache, et formulaire de contact.", body, "contact")

def build_careers():
    body = hero("Carrières", "Bâtissez votre carrière avec Firma Plus",
        "Une équipe dynamique, un environnement stimulant et des outils actuels. Nous recrutons dans nos trois points de service.", "", crumbs(("Accueil", "{root}"), ("Carrières", "")), img=P+"demarrage.jpg")
    body += f'''<section><div class="wrap split"><div class="reveal">
<div class="photo wide" style="margin-bottom:28px">{photo("equipe-reunion", "Équipe de Firma Plus")}</div>
<h2>Pourquoi nous joindre</h2>
<ul class="check" style="margin-top:18px"><li>Des dossiers variés de PME de plusieurs secteurs</li><li>L’encadrement de CPA et un parcours de développement</li><li>Des outils infonuagiques et des processus modernes</li><li>Trois bureaux : Montréal, Saguenay et Saint-Eustache</li></ul>
<h2 style="margin-top:40px">Profils recherchés</h2>
<div class="grid g2" style="margin-top:18px">
<div class="card">{icon("book")}<h3>Technicien·ne comptable</h3><p>Tenue de livres complète, rapprochements, remises et déclarations de taxes.</p></div>
<div class="card">{icon("users")}<h3>Commis comptable</h3><p>Saisie, comptes fournisseurs et clients, soutien à l’équipe.</p></div>
<div class="card">{icon("shield")}<h3>CPA</h3><p>Responsabilité de dossiers, états financiers, mandats de certification.</p></div>
<div class="card">{icon("handshake")}<h3>Candidature spontanée</h3><p>Votre profil ne figure pas ici ? Écrivez-nous quand même.</p></div></div></div>
<div class="panel sticky reveal"><form data-form="carrieres" data-subject="Candidature" enctype="multipart/form-data" novalidate>
<h3 style="margin-bottom:18px">Postuler</h3>
<div class="field"><label for="j-nom">Nom complet <span class="req">*</span></label><input id="j-nom" name="nom" autocomplete="name" required></div>
<div class="row"><div class="field"><label for="j-mail">Courriel <span class="req">*</span></label><input id="j-mail" type="email" name="courriel" required></div>
<div class="field"><label for="j-tel">Téléphone</label><input id="j-tel" type="tel" name="telephone"></div></div>
<div class="row"><div class="field"><label for="j-poste">Poste</label><select id="j-poste" name="poste"><option>Technicien·ne comptable</option><option>Commis comptable</option><option>CPA</option><option>Candidature spontanée</option></select></div>
<div class="field"><label for="j-bur">Bureau</label><select id="j-bur" name="bureau">{office_options()}</select></div></div>
<div class="field"><label for="j-cv">CV (PDF, max. 5 Mo)</label><input id="j-cv" type="file" name="cv" accept=".pdf,.doc,.docx"></div>
<div class="field"><label for="j-msg">Message</label><textarea id="j-msg" name="message"></textarea></div>
{HP}{CONSENT}
<button class="btn btn-primary" type="submit">Envoyer ma candidature</button><p class="form-msg" role="status"></p>
<p class="muted" style="font-size:.78rem;margin-top:8px">Si votre logiciel de courriel s’ouvre, joignez votre CV au message avant l’envoi.</p>
</form></div></div></section>'''
    page("carrieres/index.html", "Carrières | Firma Plus", "Emplois en comptabilité chez Firma Plus à Montréal, au Saguenay et à Saint-Eustache.", body)

def build_misc():
    page("merci/index.html", "Merci | Firma Plus", "Votre demande a bien été reçue.",
         hero("Merci", "Votre demande a bien été reçue", "Un membre de notre équipe communiquera avec vous dans un délai d’un jour ouvrable.", '<a class="btn btn-primary" href="{root}">Retour à l’accueil</a><a class="btn btn-ghost" href="{root}perspectives/">Lire nos perspectives</a>'))
    page("404.html", "Page introuvable | Firma Plus", "Page introuvable.",
         hero("Erreur 404", "Cette page n’existe pas ou a été déplacée", "Le site de Firma Plus a été renouvelé. Utilisez le menu ou revenez à l’accueil.", '<a class="btn btn-primary" href="/">Retour à l’accueil</a><a class="btn btn-ghost" href="/contact/">Nous joindre</a>'))
    terms = '''<section><div class="wrap prose">
<p class="note">Texte à faire valider par Firma Plus avant la mise en ligne.</p>
<h2>Utilisation du site</h2><p>Le contenu de ce site est fourni à titre informatif. Il ne constitue pas un avis comptable, fiscal ou juridique et ne crée aucune relation professionnelle. Une relation professionnelle débute uniquement par la signature d’une lettre de mission.</p>
<h2>Propriété intellectuelle</h2><p>Les textes, logos et éléments graphiques de ce site appartiennent à Firma Plus ou sont utilisés avec autorisation. Toute reproduction sans autorisation écrite est interdite.</p>
<h2>Liens externes</h2><p>Firma Plus n’est pas responsable du contenu des sites externes vers lesquels ce site renvoie.</p>
<h2>Exactitude</h2><p>Nous nous efforçons de maintenir l’information à jour. Les règles fiscales et réglementaires évoluent ; vérifiez auprès d’un professionnel avant d’agir.</p>
<h2>Droit applicable</h2><p>Les présentes conditions sont régies par les lois de la province de Québec et les lois fédérales du Canada qui s’y appliquent.</p></div></section>'''
    page("conditions-dutilisation/index.html", "Conditions d’utilisation | Firma Plus", "Conditions d’utilisation du site de Firma Plus.", hero("Légal", "Conditions d’utilisation", "", "") + terms)
    privacy = f'''<section><div class="wrap prose">
<p class="note">Texte à faire valider par Firma Plus avant la mise en ligne, notamment le nom de la personne responsable de la protection des renseignements personnels (Loi 25).</p>
<h2>Responsable de la protection des renseignements personnels</h2><p>[Nom et titre à confirmer] — <a href="mailto:{SITE["email"]}">{SITE["email"]}</a></p>
<h2>Renseignements recueillis</h2><p>Par les formulaires de ce site, nous recueillons les renseignements que vous nous fournissez : nom, coordonnées, nom de l’entreprise, description de vos besoins et, pour une candidature, votre CV.</p>
<h2>Fins</h2><p>Ces renseignements servent uniquement à répondre à votre demande, à préparer une proposition de services, à traiter une candidature ou, si vous y avez consenti, à vous transmettre notre infolettre.</p>
<h2>Communication et hébergement</h2><p>Vos renseignements ne sont ni vendus ni loués. Ils peuvent être hébergés par nos fournisseurs de services technologiques, liés par des obligations de confidentialité, y compris à l’extérieur du Québec.</p>
<h2>Conservation</h2><p>Nous conservons vos renseignements le temps nécessaire aux fins ci-dessus, puis les détruisons de façon sécuritaire.</p>
<h2>Vos droits</h2><p>Vous pouvez demander l’accès à vos renseignements, leur rectification ou le retrait de votre consentement en écrivant à la personne responsable. Vous pouvez vous désabonner de l’infolettre en tout temps.</p>
<h2>Témoins (cookies)</h2><p>Ce site n’utilise que les témoins nécessaires à son fonctionnement (préférence de thème clair ou sombre, conservée dans votre navigateur).</p></div></section>'''
    page("confidentialite/index.html", "Politique de confidentialité | Firma Plus", "Politique de confidentialité et protection des renseignements personnels de Firma Plus.", hero("Légal", "Politique de confidentialité", "", "") + privacy)

def build_redirects():
    """Keep the old WordPress URLs working."""
    redirects = {
        "a-propos/montreal-jonquiere/index.html": "/bureaux/montreal-saguenay/",
        "a-propos/st-eustache/index.html": "/bureaux/saint-eustache/",
    }
    for path, to in redirects.items():
        full = os.path.join(OUT, path); os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(f'<!doctype html><html lang="fr-CA"><head><meta charset="utf-8"><title>Redirection</title><link rel="canonical" href="https://firmaplus.ca{to}"><meta http-equiv="refresh" content="0; url={to}"></head><body><a href="{to}">Continuer</a></body></html>\n')

def build_sitemap():
    urls = [p for p in BUILT if p != "404.html" and not p.startswith("merci")]
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for p in urls:
            loc = "https://firmaplus.ca/" + (p[:-len("index.html")] if p.endswith("index.html") else p)
            f.write(f"  <url><loc>{loc}</loc></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\nDisallow: /_build/\nSitemap: https://firmaplus.ca/sitemap.xml\n")

if __name__ == "__main__":
    build_home(); build_services(); build_sectors(); build_team(); build_insights()
    build_about(); build_intake(); build_contact(); build_careers(); build_misc(); build_redirects(); build_sitemap()
    print(f"{len(BUILT)} pages built")
