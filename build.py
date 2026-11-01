#!/usr/bin/env python3
"""Generates the support and privacy pages published at https://dionlima1.github.io/apps/.

    python3 build.py      # writes index.html and <app>/index.html + <app>/privacy.html
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
ISSUES = "https://github.com/dionlima1/apps/issues"
UPDATED_EN, UPDATED_PT = "October 22, 2026", "22 de outubro de 2026"

# Apps with their own site are only linked from the home page.
EXTERNAL = [
    ("Wakeful", "Keep your Mac awake while you work and while your AI agents run.", "https://dionlima1.github.io/wakeful/"),
    ("Extracta", "Unzip RAR, ZIP, 7Z and more on your Mac.", "https://dionlima1.github.io/extracta/"),
]

APPS = {
    "b737-recurrent": {
        "name": "B737 Recurrent",
        "updated": ("November 1, 2026", "1º de novembro de 2026"),
        "tagline": "Study the Boeing 737 NG and MAX systems with questions, flashcards and spaced review.",
        "tagline_pt": "Estude os sistemas do Boeing 737 NG e MAX com perguntas, flashcards e revisão espaçada.",
        "faq": [
            ("Can I use this app for flight?",
             "No. B737 Recurrent is a study aid only. Your company's approved manuals always take precedence, and the app must never be used for flight, flight planning or any operational decision."),
            ("Is the app affiliated with Boeing or an airline?",
             "No. It is independent and not affiliated with, endorsed or sponsored by The Boeing Company or any airline. Boeing and 737 are trademarks of The Boeing Company."),
            ("How do I cancel my subscription?",
             "Subscriptions are managed by Apple or Google. On iPhone: Settings, your name, Subscriptions. On Android: Google Play, Payments and subscriptions. Cancel at least 24 hours before the renewal date."),
            ("I bought a subscription on another phone. How do I get it back?",
             "Open Settings in the app and tap Restore purchases, signed in to the same Apple ID or Google account."),
        ],
        "privacy": [
            "<strong>B737 Recurrent does not collect, sell or share personal data for advertising or tracking.</strong>",
            "Your answers, flashcard progress, statistics and settings are stored only on your phone. Deleting the app removes them.",
            "Study reminders are local notifications scheduled on your phone; no server sends them.",
            "Subscriptions are processed by Apple or Google. We use RevenueCat to confirm whether a subscription is active; it receives an anonymous app user ID and the purchase receipt from the store, not your name or email. See RevenueCat's privacy policy at revenuecat.com.",
            "There are no accounts, no analytics and no advertising.",
        ],
        "privacy_pt": [
            "<strong>O B737 Recurrent não coleta, vende nem compartilha dados pessoais para publicidade ou rastreamento.</strong>",
            "Suas respostas, o progresso dos flashcards, as estatísticas e os ajustes ficam só no seu celular. Apagar o app apaga tudo.",
            "Os lembretes de estudo são notificações locais agendadas no próprio celular; nenhum servidor as envia.",
            "As assinaturas são processadas pela Apple ou pelo Google. Usamos o RevenueCat para confirmar se a assinatura está ativa; ele recebe um identificador anônimo do app e o recibo da loja, não seu nome nem seu e-mail.",
            "Não há conta, análise de uso nem anúncios.",
        ],
    },
    "diskorbit": {
        "name": "DiskOrbit",
        "tagline": "See what is using space on your Mac, and get it back safely.",
        "tagline_pt": "Veja o que ocupa espaço no seu Mac e recupere esse espaço com segurança.",
        "faq": [
            ("Does DiskOrbit delete files on its own?",
             "No. Files only go to the Trash after you confirm, and you can restore them from the Trash."),
            ("Why does DiskOrbit ask for Full Disk Access?",
             "It is optional. Without it, macOS hides some protected folders from every app. The in-app assistant explains how to grant it if you want complete totals."),
            ("Does DiskOrbit upload anything?",
             "No. DiskOrbit never connects to the internet; scans stay on your Mac."),
        ],
        "privacy": [
            "<strong>DiskOrbit does not collect, store, transmit or share any personal data.</strong>",
            "Scans happen locally. File names, sizes and folder structure never leave your Mac.",
            "DiskOrbit has no accounts, no analytics, no advertising and no tracking of any kind, and it does not connect to the internet.",
            "The only information DiskOrbit keeps is stored on your Mac: the folders you chose to scan, a short summary of previous scans (to show which folders grew) and your settings. Deleting the app removes all of it.",
            "Files are only moved to the Trash when you explicitly confirm it.",
        ],
        "privacy_pt": [
            "<strong>O DiskOrbit não coleta, armazena, transmite nem compartilha nenhum dado pessoal.</strong>",
            "Os scans acontecem no seu Mac. Nomes, tamanhos e estrutura de pastas nunca saem dele.",
            "Não há conta, análise de uso, anúncios nem rastreamento, e o app não se conecta à internet.",
            "O app guarda apenas, no próprio Mac, as pastas que você escolheu, um resumo dos scans anteriores e seus ajustes. Apagar o app apaga tudo isso.",
            "Arquivos só vão para a Lixeira quando você confirma.",
        ],
    },
    "convert-anything": {
        "name": "Convert Anything",
        "tagline": "Convert photos, videos, music, PDFs and documents on your Mac.",
        "tagline_pt": "Converta fotos, vídeos, músicas, PDFs e documentos no seu Mac.",
        "faq": [
            ("Are my files uploaded anywhere?",
             "No. Every conversion runs on your Mac with Apple's own frameworks; the app has no internet access."),
            ("Will a conversion overwrite my original?",
             "Never. If “Photo.jpg” already exists, the new file is saved as “Photo 2.jpg”."),
            ("Why does the app ask for access to a folder?",
             "macOS requires your permission before an app can save next to the original file. The app explains the step before the system dialog appears."),
        ],
        "privacy": [
            "<strong>Convert Anything does not collect, store, transmit or share any personal data.</strong>",
            "Files are converted locally on your Mac and never leave it. The app has no network access.",
            "There are no accounts, no analytics, no advertising and no tracking.",
            "Your settings and presets are stored only on your Mac. Deleting the app removes them.",
        ],
        "privacy_pt": [
            "<strong>O Convert Anything não coleta, armazena, transmite nem compartilha nenhum dado pessoal.</strong>",
            "Os arquivos são convertidos no seu Mac e nunca saem dele. O app não tem acesso à internet.",
            "Não há conta, análise de uso, anúncios nem rastreamento.",
            "Ajustes e predefinições ficam só no seu Mac. Apagar o app apaga tudo.",
        ],
    },
    "veracard": {
        "name": "Veracard",
        "tagline": "Find fake SD cards and USB drives before you lose your files.",
        "tagline_pt": "Descubra cartões SD e pendrives falsificados antes de perder seus arquivos.",
        "faq": [
            ("Does the test erase my card?",
             "No. Veracard only writes to free space and deletes its test files afterwards. Back up important files anyway, as with any disk test."),
            ("Why does Veracard ask me to select the card?",
             "The Mac App Store sandbox requires your permission, given through the standard Open panel, before an app can write to a card."),
            ("What does the Community tab share?",
             "Nothing unless you tap Share With the Community after a check. Reading the community list works without signing in; sharing requires iCloud. You can report any entry and block its author."),
        ],
        "privacy": [
            "Veracard has no accounts, no analytics, no advertising and no third-party SDKs, and it does not track you.",
            "Checks run locally. Your files and the contents of your cards never leave your Mac.",
            "<strong>Community reports (optional).</strong> Only when you tap <em>Share With the Community</em>, Veracard publishes to Apple's CloudKit public database: the store name, platform and country, optionally the city and price, the card's claimed and real capacity, the verdict and the chip's manufacturer ID. Reports are not linked to your identity; CloudKit only associates an anonymous per-app identifier, used so other people can hide or report entries.",
            "Entries can be reported by anyone and are hidden after several reports; you can block an author on your Mac. To remove a report you shared, open an issue at the link below.",
            "Your check history and settings are stored only on your Mac. Deleting the app removes them.",
        ],
        "privacy_pt": [
            "O Veracard não tem conta, análise de uso, anúncios nem SDKs de terceiros, e não rastreia você.",
            "Os testes acontecem no seu Mac. Seus arquivos e o conteúdo dos cartões nunca saem dele.",
            "<strong>Relatos da comunidade (opcionais).</strong> Só quando você toca em <em>Compartilhar com a comunidade</em>, o Veracard publica no banco público do CloudKit da Apple: nome da loja, plataforma e país, opcionalmente cidade e preço, a capacidade anunciada e a real, o veredito e o ID do fabricante do chip. Os relatos não são vinculados à sua identidade; o CloudKit associa apenas um identificador anônimo por app, usado para que outras pessoas possam ocultar ou denunciar entradas.",
            "Qualquer pessoa pode denunciar uma entrada, que some depois de algumas denúncias, e você pode bloquear um autor no seu Mac. Para remover um relato seu, abra uma issue no link abaixo.",
            "O histórico de testes e os ajustes ficam só no seu Mac. Apagar o app apaga tudo.",
        ],
    },
}

STYLE = """
:root { --bg:#f7f6fb; --surface:#fff; --ink:#1d1b2e; --muted:#5f5c74; --accent:#3b5bdb; --line:#e4e2ef; }
@media (prefers-color-scheme: dark) { :root { --bg:#0f0e1f; --surface:#1a1930; --ink:#f1f0f8; --muted:#a9a6c2; --accent:#8ea2ff; --line:#2c2a47; } }
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--ink); font:17px/1.6 -apple-system,BlinkMacSystemFont,"SF Pro Text","Helvetica Neue",sans-serif; }
main { max-width:780px; margin:0 auto; padding:48px 16px 64px; }
a { color:var(--accent); }
h1 { font-size:clamp(30px,5vw,40px); letter-spacing:-0.02em; margin:8px 0 4px; }
h2 { font-size:22px; margin-top:36px; }
.lead { color:var(--muted); font-size:19px; margin-top:0; }
.meta { color:var(--muted); }
section, details, .card { background:var(--surface); border:1px solid var(--line); border-radius:14px; }
section { padding:8px 22px 18px; margin-top:24px; }
details { padding:14px 18px; margin:10px 0; }
summary { cursor:pointer; font-weight:600; }
details p { color:var(--muted); margin:10px 0 0; }
.grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:14px; margin-top:24px; }
.card { padding:18px 20px; text-decoration:none; color:inherit; display:block; }
.card strong { display:block; font-size:18px; margin-bottom:4px; }
.card span { color:var(--muted); font-size:15px; }
footer { text-align:center; color:var(--muted); font-size:14px; padding:8px 16px 40px; }
"""


def page(title: str, body: str, depth: int = 1) -> str:
    css = "../" * depth + "style.css"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
<main>
{body}
</main>
<footer>© 2026 Dion Lima · <a href="{ISSUES}">Support</a></footer>
</body>
</html>
"""


def write(path: pathlib.Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    write(ROOT / "style.css", STYLE.strip() + "\n")

    cards = [f'<a class="card" href="{slug}/"><strong>{html.escape(a["name"])}</strong><span>{html.escape(a["tagline"])}</span></a>'
             for slug, a in APPS.items()]
    cards += [f'<a class="card" href="{url}"><strong>{html.escape(name)}</strong><span>{html.escape(tagline)}</span></a>'
              for name, tagline, url in EXTERNAL]
    write(ROOT / "index.html", page("Apps by Dion Lima", f"""<h1>Apps by Dion Lima</h1>
<p class="lead">Small, private apps. Support and privacy policies for each one.</p>
<div class="grid">
{chr(10).join(cards)}
</div>""", depth=0))

    for slug, app in APPS.items():
        name = html.escape(app["name"])
        faq = "\n".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>"
                        for q, a in app["faq"])
        write(ROOT / slug / "index.html", page(f"{app['name']} Support", f"""<p><a href="../">← All apps</a></p>
<h1>{name}</h1>
<p class="lead">{html.escape(app["tagline"])}</p>
<h2>Support</h2>
{faq}
<p>Something else? <a href="{ISSUES}">Open an issue</a> and I will get back to you. · <a href="privacy.html">Privacy Policy</a></p>
<h2 lang="pt-BR">Suporte em português</h2>
<p lang="pt-BR">{html.escape(app["tagline_pt"])} Dúvidas ou problemas? <a href="{ISSUES}">Abra uma issue</a>. Veja também a <a href="privacy.html#pt">política de privacidade</a>.</p>"""))

        items = "\n".join(f"<li>{line}</li>" for line in app["privacy"])
        items_pt = "\n".join(f"<li>{line}</li>" for line in app["privacy_pt"])
        write(ROOT / slug / "privacy.html", page(f"{app['name']} Privacy Policy", f"""<p><a href="./">← {name}</a></p>
<h1>{name} Privacy Policy</h1>
<p class="meta">Last updated: {app.get("updated", (UPDATED_EN, UPDATED_PT))[0]}</p>
<section>
<ul>
{items}
</ul>
<p>Apple processes App Store purchases; the developer never receives your payment details. Questions about this policy: <a href="{ISSUES}">open an issue</a>.</p>
</section>
<section id="pt" lang="pt-BR">
<h2>Política de privacidade (português)</h2>
<p class="meta">Última atualização: {app.get("updated", (UPDATED_EN, UPDATED_PT))[1]}</p>
<ul>
{items_pt}
</ul>
<p>As compras são processadas pela Apple; o desenvolvedor nunca recebe seus dados de pagamento. Dúvidas: <a href="{ISSUES}">abra uma issue</a>.</p>
</section>"""))
    print("site written:", ", ".join(["index.html"] + [f"{s}/" for s in APPS]))


if __name__ == "__main__":
    main()
