"""Regenerate the paired, non-data project diagrams using the standard library."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "assets/projects"
ROOT.mkdir(parents=True, exist_ok=True)

PALETTES = {
    "light": {"ink": "#263440", "muted": "#60717f", "line": "#c9d4dc", "soft": "#e9eef1", "accent": "#55758b", "paper": "#f8fafb"},
    "dark": {"ink": "#dce4e9", "muted": "#a1b0bc", "line": "#4a5a67", "soft": "#26333e", "accent": "#a0bbcc", "paper": "#1a232b"},
}


def base(title: str, desc: str, body: str, p: dict[str, str]) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="720" height="184" viewBox="0 0 720 184" role="img" aria-labelledby="title desc">
<title id="title">{title}</title><desc id="desc">{desc}</desc>
<rect x="0.5" y="0.5" width="719" height="183" fill="{p['paper']}" stroke="{p['line']}"/>
{body}
</svg>'''


def text(x: int, y: int, value: str, color: str, size: int = 13, weight: int = 400, spacing: float = 0) -> str:
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Arial,sans-serif" font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}">{value}</text>'


def alpha(p: dict[str, str]) -> str:
    b = [
        text(24, 31, "ALPHA MOSAIC", p["muted"], 11, 600, 1.5),
        text(530, 31, "RESEARCH WORKBENCH", p["muted"], 10, 500, 1.1),
        f'<line x1="24" y1="43" x2="696" y2="43" stroke="{p["line"]}"/>',
        text(24, 76, "01", p["accent"], 12, 600),
        text(57, 76, "Collect &amp; validate", p["ink"], 15, 600),
        text(57, 101, "Market history", p["muted"], 12),
        text(57, 121, "Provider status", p["muted"], 12),
        text(265, 76, "02", p["accent"], 12, 600),
        text(298, 76, "Calculate", p["ink"], 15, 600),
        text(298, 101, "Deterministic factors", p["muted"], 12),
        text(298, 121, "Risk filters", p["muted"], 12),
        text(500, 76, "03", p["accent"], 12, 600),
        text(533, 76, "Document", p["ink"], 15, 600),
        text(533, 101, "Evidence bundles", p["muted"], 12),
        text(533, 121, "Paper diagnostics", p["muted"], 12),
        f'<path d="M225 94h24m-8-6 8 6-8 6M460 94h24m-8-6 8 6-8 6" fill="none" stroke="{p["accent"]}" stroke-width="1.4"/>',
        f'<line x1="24" y1="145" x2="696" y2="145" stroke="{p["line"]}"/>',
        text(24, 166, "Evidence before a conclusion", p["muted"], 12),
        text(513, 166, "NO BROKER EXECUTION", p["accent"], 10, 600, 1),
    ]
    return base("Alpha Mosaic research stages", "Validated inputs flow into deterministic factors and documented paper diagnostics; no broker execution.", "\n".join(b), p)


def meridian(p: dict[str, str]) -> str:
    b = [
        text(24, 31, "MERIDIAN ALPHA", p["muted"], 11, 600, 1.5),
        text(545, 31, "DECISION SYSTEM", p["muted"], 10, 500, 1.1),
        f'<line x1="24" y1="43" x2="696" y2="43" stroke="{p["line"]}"/>',
    ]
    labels = [(24, "DATA"), (161, "RESEARCH"), (298, "DECISION"), (435, "RISK"), (572, "PAPER")]
    for i, (x, label) in enumerate(labels):
        b += [
            f'<rect x="{x}" y="66" width="118" height="46" fill="{p["soft"]}" stroke="{p["line"]}"/>',
            text(x + 12, 94, label, p["ink"], 11, 600, 0.8),
        ]
        if i < 4:
            b.append(f'<path d="M{x+119} 89h17m-6-5 6 5-6 5" fill="none" stroke="{p["accent"]}" stroke-width="1.25"/>')
    b += [
        f'<line x1="24" y1="133" x2="696" y2="133" stroke="{p["line"]}"/>',
        text(24, 158, "Evidence checks", p["muted"], 12),
        text(207, 158, "Explicit states", p["muted"], 12),
        text(394, 158, "Deterministic gates", p["muted"], 12),
        text(602, 158, "PAPER_ONLY", p["accent"], 10, 600, 1),
    ]
    return base("Meridian Alpha decision stages", "Data, research, decision, and risk gates precede the paper ledger. Broker execution is disabled.", "\n".join(b), p)


def mobile_base(title: str, desc: str, body: str, p: dict[str, str]) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="360" height="188" viewBox="0 0 360 188" role="img" aria-labelledby="title desc">
<title id="title">{title}</title><desc id="desc">{desc}</desc>
<rect x="0.5" y="0.5" width="359" height="187" fill="{p['paper']}" stroke="{p['line']}"/>
{body}
</svg>'''


def alpha_mobile(p: dict[str, str]) -> str:
    b = [text(16, 24, "ALPHA MOSAIC / RESEARCH", p["muted"], 10, 600, 1),
         f'<line x1="16" y1="34" x2="344" y2="34" stroke="{p["line"]}"/>']
    for y, number, label, detail in [(63, "01", "Validate inputs", "Market data &amp; provider state"),
                                      (111, "02", "Calculate factors", "Deterministic methods &amp; risk"),
                                      (159, "03", "Document evidence", "Reports &amp; paper diagnostics")]:
        b += [text(16, y, number, p["accent"], 12, 600), text(48, y, label, p["ink"], 15, 600),
              text(48, y + 17, detail, p["muted"], 11)]
    return mobile_base("Alpha Mosaic research stages", "Validated data, deterministic factors, and paper diagnostics.", "\n".join(b), p)


def meridian_mobile(p: dict[str, str]) -> str:
    b = [text(16, 24, "MERIDIAN ALPHA / DECISIONS", p["muted"], 10, 600, 1),
         f'<line x1="16" y1="34" x2="344" y2="34" stroke="{p["line"]}"/>']
    for y, left, right in [(49, "DATA", "RESEARCH"), (97, "DECISION", "RISK")]:
        b += [f'<rect x="16" y="{y}" width="145" height="34" fill="{p["soft"]}" stroke="{p["line"]}"/>',
              f'<rect x="199" y="{y}" width="145" height="34" fill="{p["soft"]}" stroke="{p["line"]}"/>',
              text(29, y + 22, left, p["ink"], 12, 600, .6), text(212, y + 22, right, p["ink"], 12, 600, .6),
              f'<path d="M167 {y+17}h25m-7-5 7 5-7 5" fill="none" stroke="{p["accent"]}" stroke-width="1.3"/>']
    b += [f'<line x1="16" y1="148" x2="344" y2="148" stroke="{p["line"]}"/>',
          text(16, 173, "GATED PAPER LEDGER", p["accent"], 11, 600, 1),
          text(270, 173, "PAPER_ONLY", p["accent"], 9, 600)]
    return mobile_base("Meridian Alpha decision stages", "Explicit data, research, decision, and risk gates lead to paper only.", "\n".join(b), p)


for mode, palette in PALETTES.items():
    (ROOT / f"alpha-{mode}.svg").write_text(alpha(palette), encoding="utf-8")
    (ROOT / f"meridian-{mode}.svg").write_text(meridian(palette), encoding="utf-8")
    (ROOT / f"alpha-mobile-{mode}.svg").write_text(alpha_mobile(palette), encoding="utf-8")
    (ROOT / f"meridian-mobile-{mode}.svg").write_text(meridian_mobile(palette), encoding="utf-8")
