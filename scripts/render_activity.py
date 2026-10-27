"""Render a small public-repository snapshot for the profile README.

Uses only GitHub's public repositories endpoint. A request failure exits before
replacing the existing image, so the README keeps its last valid asset.
"""

from __future__ import annotations

import json
import os
from html import escape
from collections import Counter
from pathlib import Path
from urllib.request import Request, urlopen


OWNER = "SiriZhao"
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "assets/generated"


def fetch_repositories() -> list[dict]:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "SiriZhao-profile"}
    if token := os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"
    repositories: list[dict] = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{OWNER}/repos?per_page=100&page={page}&type=public"
        with urlopen(Request(url, headers=headers), timeout=20) as response:
            batch = json.load(response)
        if not isinstance(batch, list):
            raise ValueError("GitHub did not return a repository list")
        repositories.extend(repo for repo in batch if not repo.get("fork") and not repo.get("private"))
        if len(batch) < 100:
            break
        page += 1
    return repositories


def render(repositories: list[dict], mode: str) -> str:
    count = len(repositories)
    language_counts = Counter(repo["language"] for repo in repositories if repo.get("language"))
    leading_language = language_counts.most_common(1)[0][0] if language_counts else "Unknown"
    leading_language = escape(leading_language[:16])
    language_size = 30 if len(leading_language) <= 9 else 22
    ink, muted, line = (
        ("#d7dee6", "#a9b7c2", "#475564") if mode == "dark" else ("#24313c", "#5c6a77", "#d8dfe5")
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="720" height="104" viewBox="0 0 720 104" role="img" aria-labelledby="title desc">
<title id="title">Public GitHub work</title>
<desc id="desc">{count} public non-fork repositories. {leading_language} is the most common primary repository language.</desc>
<line x1="0" y1="1" x2="720" y2="1" stroke="{line}"/>
<line x1="0" y1="103" x2="720" y2="103" stroke="{line}"/>
<text x="4" y="27" fill="{muted}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="12" letter-spacing="1.2">PUBLIC WORK</text>
<text x="4" y="74" fill="{ink}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="38" font-weight="600">{count}</text>
<text x="63" y="69" fill="{muted}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="14">original repositories</text>
<line x1="380" y1="23" x2="380" y2="81" stroke="{line}"/>
<text x="415" y="65" fill="{ink}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="{language_size}" font-weight="600">{leading_language}</text>
<text x="415" y="84" fill="{muted}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="12">most common primary language</text>
</svg>'''


if __name__ == "__main__":
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    repositories = fetch_repositories()
    for mode in ("light", "dark"):
        output = OUTPUT_DIR / f"activity-{mode}.svg"
        content = render(repositories, mode)
        # Preserve the timestamp and avoid a commit when the data did not change.
        if not output.exists() or output.read_text(encoding="utf-8") != content:
            output.write_text(content, encoding="utf-8")
        print(f"Rendered {output.name}")
