# Siri Zhao

**Independent Developer — Agentic AI, Software Engineering & Quantitative Systems**

_Agronomy Major · Computer Science Minor_<br>
_Nanjing Agricultural University_

[About](#about) · [Areas of interest](#areas-of-interest) · [Selected work](#selected-work) · [Toolkit](#toolkit) · [Activity](#activity)

## About

Academic training at Nanjing Agricultural University combines a major in Agronomy with a formally admitted minor in Computer Science. Beyond the classroom, independent software development provides a practical foundation for exploring intelligent systems, research-oriented applications, and the engineering challenges that emerge at the intersection of disciplines.

Particular attention goes to the engineering of **agentic AI**: the architecture of LLM-powered systems and the mechanisms through which language models interact with external tools, coordinate multi-stage workflows, and operate within well-defined constraints. Context management, orchestration, evaluation, and human oversight matter here because they distinguish a useful autonomous workflow from a convincing demonstration.

Alongside applied AI, **quantitative research infrastructure** forms another substantial focus. Projects including **Alpha Mosaic** and **Meridian Alpha** explore financial data organization, analytical workflows, strategy evaluation, and paper-only decision-support systems. The emphasis rests on methodological transparency, reproducibility, and the integration of computational research with informed human judgment.

**Python** constitutes the primary development language, complemented by **C/C++** and **JavaScript/TypeScript**. Current technical interests also extend toward software architecture, developer tooling, AI-assisted engineering workflows, and the integration of intelligent software with real-world systems — particularly automation, smart agriculture, and intelligent manufacturing.

Underlying these pursuits is a consistent engineering principle: functionality alone is insufficient without an understanding of the assumptions, limitations, and trade-offs that shape a system's behavior. The objective is not simply to make software work, but to make its design intelligible, its outputs verifiable, and its evolution sustainable.

## Areas of interest

**Agentic systems**<br>
Tool integration · Workflow orchestration · Context management

**Software engineering**<br>
Developer tooling · Automation · Software architecture

**Quantitative systems**<br>
Research infrastructure · Data pipelines · Strategy evaluation

**Applied intelligence**<br>
Intelligent systems · Smart agriculture · Industrial automation

---

## Selected work

### 01 / CleanText Studio

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/projects/cleantext-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="assets/projects/cleantext-light.png">
  <img src="assets/projects/cleantext-light.png" alt="Actual CleanText Studio desktop interface, version 2.1.0" width="720">
</picture>

**Document engineering for everyday work.** CleanText Studio turns copied or AI-assisted text into editable documents while retaining useful structure. A shared document tree powers preview and DOCX export; basic cleanup runs locally, with optional AI refinement initiated by the user.

_Python · structure-aware parsing · DOCX/TXT export · local-first processing_<br>
[Source](https://github.com/SiriZhao/CleanText-Studio) · [Latest release](https://github.com/SiriZhao/CleanText-Studio/releases/latest)

### 02 / Alpha Mosaic

<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/projects/alpha-mobile-dark.svg">
  <source media="(max-width: 600px) and (prefers-color-scheme: light)" srcset="assets/projects/alpha-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/projects/alpha-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/projects/alpha-light.svg">
  <img src="assets/projects/alpha-light.svg" alt="Diagram of Alpha Mosaic's data validation, factor research, and report stages" width="720">
</picture>

**An evidence-first quantitative research workbench.** It discovers a bounded US equity universe, validates available market data, computes deterministic factors, and saves research reports. Provider health, evidence, factor calculations, and report generation remain explicit; historical replay is diagnostic and paper evaluation stays separate from live trading. The project makes no claim of demonstrated alpha.

_Python · deterministic factors · evidence-gated evaluation · read-only MCP_<br>
[Source](https://github.com/SiriZhao/alpha-mosaic) · [Architecture](https://github.com/SiriZhao/alpha-mosaic/blob/main/ARCHITECTURE.md)

### 03 / Meridian Alpha

<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/projects/meridian-mobile-dark.svg">
  <source media="(max-width: 600px) and (prefers-color-scheme: light)" srcset="assets/projects/meridian-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/projects/meridian-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/projects/meridian-light.svg">
  <img src="assets/projects/meridian-light.svg" alt="Diagram of Meridian Alpha's evidence, decision, risk, and paper-ledger gates" width="720">
</picture>

**Decision support with explicit gates.** Meridian connects research evidence to deterministic risk checks, status-aware reports, and a persistent paper ledger. Its stateful pipeline separates data, research, decision, risk, and paper stages. It is an independent project from Alpha Mosaic. Its current boundary is `PAPER_ONLY`: broker orders and real-account execution are disabled.

_Python · stateful workflows · risk gates · paper ledger_<br>
[Source](https://github.com/SiriZhao/meridian-alpha) · [System boundaries](https://github.com/SiriZhao/meridian-alpha/blob/main/docs/adr/ADR-001-system-boundaries.md)

## Further work

**[RecallForge AI](https://github.com/SiriZhao/recallforge-ai)** — A full-stack study workspace that turns course materials into source-anchored review, active recall, and exportable study packs. Generated material remains a study aid to verify against its sources. `FastAPI` · `React` · [v0.6.0 release](https://github.com/SiriZhao/recallforge-ai/releases/tag/v0.6.0)

**[RecallForge Skill](https://github.com/SiriZhao/recallforge-skill)** — A host-executed Agent Skill for inspecting learning materials, reconstructing course knowledge, and testing recall. Visual understanding depends on the selected host's capabilities. `Agent Skills` · `Python` · [v2.2.0 release](https://github.com/SiriZhao/recallforge-skill/releases/tag/v2.2.0)

## Toolkit

**Languages** — Python · C · C++ · JavaScript · TypeScript<br>
**Development** — Git · GitHub · GitHub Actions · FastAPI · React · Docker · SQLite<br>
**AI & research** — LLM applications · agent workflows · tool integration · research automation · data processing · quantitative research

## Activity

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/generated/activity-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/generated/activity-light.svg">
  <img src="assets/generated/activity-light.svg" alt="Public GitHub repository activity snapshot" width="720">
</picture>

<details>
<summary>Contribution trail</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/generated/snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/generated/snake-light.svg">
  <img src="assets/generated/snake-light.svg" alt="Animated trail through Siri Zhao's public GitHub contribution graph" width="720">
</picture>

</details>

<sub>Activity assets are regenerated through this repository's [GitHub Actions](https://github.com/SiriZhao/SiriZhao/actions). The contribution trail uses [snk](https://github.com/Platane/snk) and stays secondary to the project notes above.</sub>

---

[Explore all public repositories](https://github.com/SiriZhao?tab=repositories)
