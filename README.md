<p align="center">
  <img src="assets/header.svg" alt="Awesome Remote Sensing Reasoning" width="100%">
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <a href="https://github.com/ML4Sustain/Awsome-RS-Reasoning-Models/actions"><img src="https://img.shields.io/github/actions/workflow/status/ML4Sustain/Awsome-RS-Reasoning-Models/catalog.yml?label=catalog&amp;style=flat-square" alt="Catalog status"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/contributions-welcome-39b54a?style=flat-square" alt="Contributions welcome"></a>
  <a href="LICENSE-DATA"><img src="https://img.shields.io/badge/data-CC_BY_4.0-ef9421?style=flat-square" alt="CC BY 4.0"></a>
</p>

## Contents

- [1. Landscape: from perception to reasoning](#1-landscape)
  - [Operational scope and taxonomy](#operational-scope-and-taxonomy)
  - [Index pulse](#index-pulse)
  - [Publication timeline](#publication-timeline)
- [2. Reasoning-specific systems](#2-reasoning-specific-systems)
- [3. Enabling foundations](#3-enabling-foundations)
- [4. Data foundations and evaluation](#4-data-foundations-and-evaluation)
- [5. Scope and maintenance](#5-scope-and-maintenance)
- [6. Contributing](#6-contributing)
- [7. Citation](#7-citation)

<a id="1-landscape"></a>
## 1. Landscape: from perception to reasoning

Remote sensing is moving from recognizing **what is where** to establishing **why a conclusion follows from evidence**. This independent index tracks that transition across models, datasets, benchmarks, and executable agents.

> **RS-Reasoning** is task-dependent, multi-step inference that combines Earth observation evidence with geographic, temporal, or domain constraints and exposes an auditable support structure.

Entries link directly to their original paper and verified official code. Repository popularity is stored as a dated snapshot in this repository, never inferred from a transient live badge.

<a id="operational-scope-and-taxonomy"></a>
### Operational scope and taxonomy

| 01 · 🧩 Supervised | 02 · 🎯 Reinforcement | 03 · 🛠️ Agentic |
| --- | --- | --- |
| Learns from rationales, traces, masks, or structured intermediate supervision. | Optimizes answer, grounding, consistency, or process rewards. | Plans and executes tools, retrieval, GIS operations, or multi-step workflows. |
| **Observe:** answer + trace | **Observe:** reward + evidence | **Observe:** action + trajectory |

The tracks sit on top of enabling datasets and vision-language models, and support four application clusters from the survey:

`urban & social space` · `disaster assessment` · `environmental monitoring` · `spatiotemporal QA`

<a id="index-pulse"></a>
### Index pulse

<!-- AUTO_DASHBOARD_START -->

| 🌍 Methods & models | 🧠 Reasoning | 🗃️ Data / benches | 💻 Official repos | 📦 Weights | 🔁 MS mirrors |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **90** | **37** | **49** | **69** | **44** | **11** |

Repository Stars are stored snapshots refreshed daily by GitHub Actions. Last refresh: **2026-08-24**.

#### Most starred official repositories

| Resource | Category | Repository | Stars (snapshot) |
| :---: | :---: | :---: | :---: |
| RemoteCLIP | Contrastive VLMs | [Code](https://github.com/ChenDelong1999/RemoteCLIP) | 587 |
| Falcon | Generative Large VLMs | [Code](https://github.com/TianHuiLab/Falcon) | 382 |
| SatCLIP | Contrastive VLMs | [Code](https://github.com/microsoft/satclip) | 373 |
| GeoRSCLIP | Contrastive VLMs | [Code](https://github.com/om-ai-lab/RS5M) | 314 |
| LAE-DINO | Task-Specific VLMs | [Code](https://github.com/jaychempan/LAE-DINO) | 286 |

<!-- AUTO_DASHBOARD_END -->

<a id="publication-timeline"></a>
### Publication timeline

<details open>
<summary><b>Representative work by first public release</b></summary>

<p align="center"><img src="assets/timeline.svg" alt="Timeline of remote sensing reasoning models" width="100%"></p>

</details>

<a id="2-reasoning-specific-systems"></a>
## 2. Reasoning-specific systems

These works satisfy the repository's operational reasoning criteria: evidence is composed across steps, intermediate claims or actions are traceable, and evaluation extends beyond final-answer accuracy. Following the survey, the three paradigms are **non-exclusive** and indicate the dominant acquisition or execution mechanism. The catalog currently contains 37 systems, sorted by stored GitHub Stars inside each paradigm.

<!-- AUTO_CATALOG_START -->

<details open>
<summary><b>Reasoning Models › Supervised Reasoning</b> · 7 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **SegEarth-R1** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2504.09644) | [HuggingFace](https://huggingface.co/earth-insights/SegEarth-R1-EarthReason) · [ModelScope](https://modelscope.cn/models/earth-insights/SegEarth-R1-EarthReason) | [Code](https://github.com/earth-insights/SegEarth-R1) | 156 |
| **TerraScope** | 2026 · CVPR | [Paper](https://arxiv.org/abs/2603.19039) | [HuggingFace](https://huggingface.co/sy1998/TerraScope) · [ModelScope](https://modelscope.cn/models/shuyanshuyan/terrascope) | [Code](https://github.com/shuyansy/Earth-Observation-VLMs) | 138 |
| **SegEarth-R2** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2512.20013) | — | [Code](https://github.com/earth-insights/SegEarth-R2) | 68 |
| **EarthVL** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2601.02783) | — | [Code](https://github.com/Junjue-Wang/EarthVL) | 43 |
| **GeoChrono** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2607.15768) | [HuggingFace](https://huggingface.co/Davidup1/GeoChrono) · [ModelScope](https://modelscope.cn/models/Davidup1/GeoChrono) | [Code](https://github.com/IntelliSensing/GeoChrono) | 9 |
| **Delta-LLaVA** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2604.14044) | — | — | — |
| **GeoHeightChat** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2603.25565) | — | — | — |

</details>

<details open>
<summary><b>Reasoning Models › RL-Driven Reasoning</b> · 19 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **RSThinker** | 2026 · ICLR | [Paper](https://arxiv.org/abs/2509.22221) | [HuggingFace](https://huggingface.co/minglanga/RSThinker) | [Code](https://github.com/minglangL/RSThinker) | 38 |
| **GeoVLM-R1** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2509.25026) | — | [Code](https://github.com/mustansarfiaz/GeoVLM-R1-Toolkit) | 32 |
| **RS-EoT** | 2026 · CVPR | [Paper](https://arxiv.org/abs/2511.22396) | [HuggingFace](https://huggingface.co/ShaoRun/RS-EoT-7B) · [Project Website](https://geox-lab.github.io/Asking_like_Socrates/) | [Code](https://github.com/GeoX-Lab/Asking_like_Socrates) | 26 |
| **GeoZero** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2511.22645) | [HuggingFace](https://huggingface.co/hjvsl/GeoZero) · [Baidu NetDisk](https://pan.baidu.com/s/1nJjBwO4UlVv4GFl60gjM3w?pwd=15gn) | [Code](https://github.com/MiliLab/GeoZero) | 26 |
| **RemoteAgent** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2604.07765) | — | [Code](https://github.com/1e12Leon/RemoteAgent) | 20 |
| **RemoteReasoner** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2507.19280) | [HuggingFace](https://huggingface.co/1e12Leon/RemoteReasoner) · [ModelScope](https://modelscope.cn/models/AIMGroup/RemoteReasoner) | [Code](https://github.com/1e12Leon/RemoteReasoner) | 17 |
| **Geo-R1** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2509.21976) | [HuggingFace](https://huggingface.co/Geo-R1) | [Code](https://github.com/Geo-R1/geo-r1) | 16 |
| **GeoEyes** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2602.14201) | — | [Code](https://github.com/nanocm/GeoEyes) | 15 |
| **TinyRS-R1** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2505.12099) | [HuggingFace](https://huggingface.co/aybora/Qwen2-VL-TinyRS-R1) | [Code](https://github.com/aybora/TinyRS) | 13 |
| **GeoReason** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2601.04118) | [HuggingFace](https://huggingface.co/WenshuaiLi/GeoReason) | [Code](https://github.com/canlanqianyan/GeoReason) | 10 |
| **GeoVista** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2605.14475) | [HuggingFace](https://huggingface.co/ryan6073/GeoVista-7B-Instruct) · [HuggingFace](https://huggingface.co/ryan6073/GeoVista-7B-Preview) | [Code](https://github.com/ryan6073/GeoVista) | 10 |
| **Geo-R** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2601.00388) | — | [Code](https://github.com/aialt/geo-r) | 3 |
| **GeoSolver** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2603.09551) | [HuggingFace](https://huggingface.co/minglanga/GeoSolver) | [Code](https://github.com/minglangL/GeoSolver) | 3 |
| **RemoteZero** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2605.04451) | — | [Code](https://github.com/1e12Leon/RemoteZero) | 1 |
| **RS-HyRe-R1** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2604.17504) | [HuggingFace](https://huggingface.co/geozgz/RS-HyRe-R1) | [Code](https://github.com/GeoX-Lab/RS-HyRe-R1) | 1 |
| **GeoX** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2605.20006) | — | — | — |
| **EAR** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2603.12788) | — | [Code](https://github.com/CV-ShuchangLyu/ME-RSRG) | — |
| **RSGround-R1** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2601.21634) | — | [Code](https://github.com/NTU-CS/RSGround-R1) | — |
| **FineRS (FINERS)** | 2025 · NeurIPS | [Paper](https://arxiv.org/abs/2510.21311) | — | — | — |

</details>

<details open>
<summary><b>Reasoning Models › Agentic / Tool-Augmented Reasoning</b> · 11 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Earth-Agent** | 2026 · ICLR | [Paper](https://arxiv.org/abs/2509.23141) | — | [Code](https://github.com/opendatalab/Earth-Agent) | 194 |
| **OpenEarthAgent** | 2026 · ECCV | [Paper](https://arxiv.org/abs/2602.17665) | [HuggingFace](https://huggingface.co/MBZUAI/OpenEarthAgent) · [ModelScope](https://modelscope.cn/models/MBZUAI/OpenEarthAgent) | [Code](https://github.com/mbzuai-oryx/OpenEarthAgent) | 95 |
| **GeoMMAgent** | 2026 · CVPR | [Paper](https://arxiv.org/abs/2604.08896) | — | [Code](https://github.com/Shihao-Cheng/GeoMMAgent) | 49 |
| **EarthAgent** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2511.17198) | — | [Code](https://github.com/earth-insights/EarthAgent) | 13 |
| **TerraAgent** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2606.13148) | — | [Code](https://github.com/Takerdat23/TerraBench) | 4 |
| **MAP-Agent** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2605.12237) | — | [Code](https://github.com/MiliLab/UHR-Micro) | 1 |
| **PMMC** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2608.00962) | — | — | — |
| **Earth AI** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2510.18318) | — | — | — |
| **VRA** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2509.16343) | — | — | — |
| **GeoFlow** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2508.04719) | — | — | — |
| **CangLing-KnowFlow** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2512.15231) | — | — | — |

</details>

<!-- AUTO_CATALOG_END -->

<a id="3-enabling-foundations"></a>
## 3. Enabling foundations

Reasoning is built on perception and remote-sensing vision-language modeling. This section therefore tracks 53 **reasoning-enabling** resources separately from reasoning-specific systems: contrastive alignment models, generative and task-specific VLMs, ultra-high-resolution interfaces, retrieval, detection, segmentation, and data generation. Inclusion here indicates foundational relevance, not demonstrated multi-step reasoning.

<!-- AUTO_ECOSYSTEM_START -->

<details open>
<summary><b>Remote Sensing Vision-Language Modeling › Contrastive VLMs</b> · 7 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **RemoteCLIP** | 2024 · TGRS | [Paper](https://doi.org/10.1109/TGRS.2024.3390838) | [HuggingFace](https://huggingface.co/chendelong/RemoteCLIP) | [Code](https://github.com/ChenDelong1999/RemoteCLIP) | 587 |
| **SatCLIP** | 2024 · arXiv | [Paper](https://arxiv.org/abs/2311.17179) | [HuggingFace](https://huggingface.co/microsoft/SatCLIP-ViT16-L40) · [ModelScope](https://modelscope.cn/models/microsoft/SatCLIP-ViT16-L40) | [Code](https://github.com/microsoft/satclip) | 373 |
| **GeoRSCLIP** | 2024 · TGRS | [Paper](https://doi.org/10.1109/TGRS.2024.3449154) | [HuggingFace](https://huggingface.co/Zilun/GeoRSCLIP) | [Code](https://github.com/om-ai-lab/RS5M) | 314 |
| **DGTRS-CLIP** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2503.19311) | [HuggingFace](https://huggingface.co/MitsuiChen14/DGTRS-CLIP-ViT-L-14) · [HuggingFace](https://huggingface.co/MitsuiChen14/DGTRS-CLIP-ViT-B-16) | [Code](https://github.com/MitsuiChen14/DGTRS) | 32 |
| **PriorCLIP** | 2023 · MM | [Paper](https://doi.org/10.1145/3581783.3612587) | [Baidu NetDisk](https://pan.baidu.com/s/1urfZ_64DFRelAQz-LYkcCQ?pwd=2v3v) | [Code](https://github.com/jaychempan/PriorCLIP) | 30 |
| **GeoAlignCLIP** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2603.09566) | — | — | — |
| **TimeSenCLIP** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2508.11919) | [HuggingFace](https://huggingface.co/pallavijainpj/TimeSenCLIP) | — | — |

</details>

<details open>
<summary><b>Remote Sensing Vision-Language Modeling › Generative Large VLMs</b> · 14 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **GeoChat** | 2024 · CVPR | [Paper](https://arxiv.org/abs/2311.15826) | [HuggingFace](https://huggingface.co/MBZUAI/geochat-7B) · [ModelScope](https://modelscope.cn/models/MBZUAI/geochat-7B) | [Code](https://github.com/mbzuai-oryx/GeoChat) | 743 |
| **Falcon** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2503.11070) | [HuggingFace](https://huggingface.co/TianHuiLab/Falcon-Single-Instruction-Large) | [Code](https://github.com/TianHuiLab/Falcon) | 382 |
| **LHRS-Bot** | 2024 · ECCV | [Paper](https://arxiv.org/abs/2402.02544) | [Google Drive](https://drive.google.com/drive/folders/1dzWTE1k935MjMVnfLtTJiIqw7yCj-e3m?usp=drive_link) · [Baidu NetDisk](https://pan.baidu.com/s/1n1h_ZImeKTgvoNHjr5bq3Q?pwd=qhqw) | [Code](https://github.com/NJU-LHRS/LHRS-Bot) | 194 |
| **EarthGPT** | 2024 · TGRS | [Paper](https://arxiv.org/abs/2401.16822) | — | [Code](https://github.com/wivizhang/EarthGPT) | 160 |
| **RSGPT** | 2025 · ISPRS | [Paper](https://arxiv.org/abs/2307.15266) | — | [Code](https://github.com/Lavender105/RSGPT) | 150 |
| **TEOChat** | 2025 · ICLR | [Paper](https://arxiv.org/abs/2410.06234) | [HuggingFace](https://huggingface.co/jirvin16/TEOChat) | [Code](https://github.com/ermongroup/TEOChat) | 150 |
| **SkySenseGPT** | 2024 · arXiv | [Paper](https://arxiv.org/abs/2406.10100) | [HuggingFace](https://huggingface.co/ll-13/SkySenseGPT-7B-CLIP-ViT) | [Code](https://github.com/Luo-Z13/SkySense-Chat) | 149 |
| **SkyEyeGPT** | 2025 · ISPRS | [Paper](https://arxiv.org/abs/2401.09712) | [HuggingFace](https://huggingface.co/ZhanYang-nwpu/SkyEyeGPT) | [Code](https://github.com/ZhanYang-nwpu/SkyEyeGPT) | 139 |
| **RSUniVLM** | 2024 · arXiv | [Paper](https://arxiv.org/abs/2412.05679) | [Google Drive](https://drive.google.com/drive/folders/1TtaoOPmh167gpgHHWRNBMCaA7t_XZ4Vg?usp=sharing) | [Code](https://github.com/xuliu-cyber/RSUniVLM) | 47 |
| **EarthMarker** | 2024 · TGRS | [Paper](https://ieeexplore.ieee.org/document/10817639) | — | [Code](https://github.com/wivizhang/EarthMarker) | 46 |
| **Earth-OneVision** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2606.10819) | — | — | — |
| **SkyNative** | 2026 · arXiv | [Paper](https://arxiv.org/abs/2605.17949) | — | — | — |
| **FUSAR-GPT** | 2026 · CVPR | [Paper](https://arxiv.org/abs/2602.19190) | — | [Code](https://github.com/yangyifremad/FUSAR-KLIP) | — |
| **RingMoGPT** | 2024 · TGRS | — | — | — | — |

</details>

<details open>
<summary><b>Remote Sensing Vision-Language Modeling › Task-Specific VLMs</b> · 15 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **LAE-DINO** | 2025 · AAAI | [Paper](https://arxiv.org/abs/2408.09110) | [HuggingFace](https://huggingface.co/ML4Sustain/LAE-DINO) · [ModelScope](https://modelscope.cn/models/ML4Sustain/LAE-DINO) | [Code](https://github.com/jaychempan/LAE-DINO) | 286 |
| **RemoteSAM** | 2025 · MM | [Paper](https://arxiv.org/abs/2505.18022) | [HuggingFace](https://huggingface.co/1e12Leon/RemoteSAM) | [Code](https://github.com/1e12Leon/RemoteSAM) | 246 |
| **EarthMind** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2506.01667) | [HuggingFace](https://huggingface.co/sy1998/EarthMind-4B) | [Code](https://github.com/shuyansy/Earth-Observation-VLMs) | 138 |
| **InstructSAM** | 2025 · NeurIPS | [Paper](https://arxiv.org/abs/2505.15818) | — | [Code](https://github.com/VoyagerXvoyagerx/InstructSAM) | 117 |
| **GeoGround** | 2024 · arXiv | [Paper](https://arxiv.org/abs/2411.11904) | [HuggingFace](https://huggingface.co/erenzhou/GeoGround) · [ModelScope](https://modelscope.cn/models/zytx121/geoground) | [Code](https://github.com/VisionXLab/GeoGround) | 94 |
| **CastDet** | 2024 · ECCV | [Paper](https://arxiv.org/abs/2311.11646) | — | [Code](https://github.com/VisionXLab/CastDet) | 85 |
| **UniGeoSeg** | 2026 · CVPR | [Paper](https://arxiv.org/abs/2511.23332) | [HuggingFace](https://huggingface.co/nishuo1999/UniGeoSeg) | [Code](https://github.com/MiliLab/UniGeoSeg) | 42 |
| **OpenRSD** | 2025 · ICCV | [Paper](https://arxiv.org/abs/2503.06146) | [Baidu NetDisk](https://pan.baidu.com/s/1sV3GHgneC3dQskIaYABefg?pwd=aan9) | [Code](https://github.com/floatingstarZ/OpenRSD) | 42 |
| **RSVG-ZeroOV** | 2026 · AAAI | [Paper](https://arxiv.org/abs/2509.18711) | — | [Code](https://github.com/like413/RSVG-ZeroOV) | 26 |
| **LLaMA-Unidetector** | 2025 · TGRS | [Paper](https://doi.org/10.1109/TGRS.2025.3564332) | [Google Drive](https://drive.google.com/file/d/1AwUn5EebmmLBo7njjW_Ng1q9zDrqkNbB/view) · [Baidu NetDisk](https://pan.baidu.com/s/1P3pW3euqqxYVZQvw-is1vQ?pwd=1234) | [Code](https://github.com/ChloeeGrace/LLaMA-Unidetector) | 15 |
| **Cross-View OVD** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2510.03858) | — | — | — |
| **FASE** | 2025 · CIKM | [Paper](https://doi.org/10.1145/3746252.3760838) | — | — | — |
| **GeoMag** | 2025 · MM | [Paper](https://arxiv.org/abs/2507.05887) | — | — | — |
| **GeoPix** | 2025 · GRSM | [Paper](https://doi.org/10.1109/MGRS.2025.3560293) | [HuggingFace](https://huggingface.co/Norman-Ou/GeoPix) | [Code](https://github.com/Norman-Ou/GeoPix) | — |
| **REO-VLM** | 2024 · arXiv | [Paper](https://arxiv.org/abs/2412.15115) | — | [Code](https://github.com/REO-VLM-anonymous/REO-VLM) | — |

</details>

<details open>
<summary><b>Reasoning-Enabling Models › Ultra-High-Resolution VLMs</b> · 3 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **GeoLLaVA-8K** | 2025 · NeurIPS | [Paper](https://arxiv.org/abs/2505.21375) | [HuggingFace](https://huggingface.co/initiacms/GeoLLaVA-8K) | [Code](https://github.com/MiliLab/GeoLLaVA-8K) | 55 |
| **ZoomEarth** | 2026 · CVPR | [Paper](https://arxiv.org/abs/2511.12267) | [HuggingFace](https://huggingface.co/HappyBug/ZoomEarth-3B) | [Code](https://github.com/earth-insights/ZoomEarth) | 45 |
| **Zoom-RS (Look Where It Matters)** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2511.20460) | — | [Code](https://github.com/kiki-zyq/ZoomSearch) | 27 |

</details>

<details open>
<summary><b>Reasoning-Enabling Models › Generation Models</b> · 2 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Text2Earth** | 2025 · GRSM | [Paper](https://ieeexplore.ieee.org/document/10988859) | [HuggingFace](https://huggingface.co/lcybuaa/Text2Earth) · [ModelScope](https://modelscope.cn/models/lcybuaa1111/Text2Earth) | [Code](https://github.com/Chen-Yang-Liu/Text2Earth) | 187 |
| **Earthsynth** | 2025 · arXiv | [Paper](https://arxiv.org/abs/2505.12108) | [HuggingFace](https://huggingface.co/jaychempan/EarthSynth) · [ModelScope](https://modelscope.cn/models/ML4Sustain/EarthSynth) | [Code](https://github.com/jaychempan/EarthSynth) | 60 |

</details>

<details open>
<summary><b>Perception Foundations › Object Detection</b> · 6 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **CalNet** | 2023 · MM | — | [Baidu NetDisk](https://pan.baidu.com/s/1PnmdKqIxPnTgK6yQ6WfwpA) | [Code](https://github.com/hexiao0275/CALNet-Dronevehicle) | 68 |
| **Enhance-then-Search (AugSearch)** | 2025 · CVPR | [Paper](https://arxiv.org/abs/2504.04517) | [Baidu NetDisk](https://pan.baidu.com/s/17wECMZ7X-wkFMXSCQ_SvAw?pwd=ttue) | [Code](https://github.com/jaychempan/ETS) | 57 |
| **S2A-Det** | 2023 · TGRS | — | — | [Code](https://github.com/hexiao0275/S2ADet) | 51 |
| **LCMA** | 2026 · Electronics | — | — | [Code](https://github.com/hexiao0275/LCMA_RGBT) | 2 |
| **SDCM** | 2025 · TMM | — | — | — | — |
| **Semantic-Aware Ship Detection** | 2025 · IGARSS | [Paper](https://arxiv.org/abs/2508.15930) | — | — | — |

</details>

<details open>
<summary><b>Perception Foundations › Semantic Segmentation</b> · 2 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Rethinking Transformers (RS Segmentation)** | 2023 · TGRS | [Paper](https://doi.org/10.1109/TGRS.2023.3302024) | [Google Drive](https://drive.google.com/file/d/1yV070cXTrkCN2FTHKM2DIXI_dtVjaTJ6/view) | [Code](https://github.com/lyhnsn/GLOTS) | 17 |
| **Multilevel Multimodal Fusion Transformer** | 2024 · TGRS | [Paper](https://doi.org/10.1109/TGRS.2024.3373033) | — | [Code](https://github.com/yida12345/FTransUNet) | 1 |

</details>

<details open>
<summary><b>Perception Foundations › Data Augmentation</b> · 1 resource</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Diverse Instance Generation (Diffusion)** | 2025 · GRSL | [Paper](https://arxiv.org/abs/2511.18031) | — | — | — |

</details>

<details open>
<summary><b>Perception Foundations › Cross-Modal Retrieval</b> · 3 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **SAN (Scene-aware Aggregation)** | 2023 · ICMR | [Paper](https://doi.org/10.1145/3591106.3592236) | [Baidu NetDisk](https://pan.baidu.com/s/1qDSdcvm6as2rKmAmC_86VA?pwd=86a2) | [Code](https://github.com/jaychempan/SWAN) | 37 |
| **PiR (Prior Instruction Representation)** | 2024 · arXiv | [Paper](https://arxiv.org/abs/2405.10160) | [Baidu NetDisk](https://pan.baidu.com/s/1urfZ_64DFRelAQz-LYkcCQ?pwd=2v3v) | [Code](https://github.com/jaychempan/PriorCLIP) | 30 |
| **DOVE (Direction-Oriented Embedding)** | 2024 · TGRS | [Paper](https://doi.org/10.1109/TGRS.2024.3392779) | — | — | — |

</details>

<!-- AUTO_ECOSYSTEM_END -->

<a id="4-data-foundations-and-evaluation"></a>
## 4. Data foundations and evaluation

Following the paper's distinction, **general-purpose multimodal datasets** provide supervision for representation learning and transfer, while **task-oriented benchmarks** define capability-specific inputs, outputs, and evaluation protocols. The table keeps both resource types searchable without treating dataset scale as evidence of reasoning quality.

<!-- AUTO_DATASETS_START -->

| Dataset / benchmark | Type | Companion model | Focus | Links |
| :---: | :---: | :---: | :---: | :---: |
| **EarthVLSet** | Dataset + benchmark | EarthVL | Earth vision-language understanding | [HuggingFace](https://huggingface.co/datasets/Kingdrone-Junjue/EarthVLSet) |
| **GeoChrono-Data** | Benchmark + instruction | GeoChrono | Long-term temporal understanding | [HuggingFace](https://huggingface.co/datasets/Davidup1/GeoChrono-Data) |
| **GeoHeight-Bench** | Reasoning benchmark | GeoHeightChat | Height-aware multimodal reasoning | [Project/Paper](https://arxiv.org/abs/2603.25565) |
| **GeoReason-Bench** | Reasoning benchmark | GeoReason | Logical consistency reasoning | [HuggingFace](https://huggingface.co/datasets/WenshuaiLi/GeoReason-Bench) |
| **GeoSeg-Bench** | Segmentation benchmark | UniGeoSeg | Open-world geospatial segmentation | [HuggingFace](https://huggingface.co/datasets/nishuo1999/GeoSeg-Bench) |
| **ME-RSRG** | Reasoning-grounding benchmark | EAR | Multi-entity reasoning and grounding | [GitHub](https://github.com/CV-ShuchangLyu/ME-RSRG) |
| **MMRS-OneVision** | Instruction dataset | Earth-OneVision | Multi-sensor and multi-task instruction tuning | [Project/Paper](https://arxiv.org/abs/2606.10819) |
| **RSFG-100k** | Alignment dataset | GeoAlignCLIP | Fine-grained region-text alignment | [Project/Paper](https://arxiv.org/abs/2603.09566) |
| **TerraBench** | Reasoning benchmark | TerraScope | Earth-observation reasoning | [Project/Paper](https://arxiv.org/search/?query=TerraBench+remote+sensing&searchtype=all) |
| **UHR-CoZ** | Ultra-high-resolution benchmark | GeoEyes | Active zooming and compositional reasoning | [GitHub](https://github.com/nanocm/GeoEyes) |
| **UHR-Micro** | Ultra-high-resolution benchmark | UHR reasoning models | Small-object perception and reasoning | [Project/Paper](https://arxiv.org/search/?query=UHR-Micro&searchtype=all) |
| **Delta-QA** | Change-QA benchmark | Delta-LLaVA | Bi-temporal visual question answering | [Project/Paper](https://arxiv.org/search/?query=Delta-QA+remote+sensing&searchtype=all) |
| **DisasterInsight** | Benchmark | Disaster-response VLMs | Disaster scene reasoning | [Project/Paper](https://arxiv.org/search/?query=DisasterInsight&searchtype=all) |
| **EarthReason** | Dataset + benchmark | SegEarth-R1 | Geospatial pixel reasoning | [HuggingFace](https://huggingface.co/datasets/earth-insights/EarthReason) |
| **FINERS-4k** | Reasoning-segmentation dataset | FineRS (FINERS) | Fine-grained small-object reasoning and segmentation | [Project](https://iiau-zhanglu.github.io/FINERS/) |
| **GAIA** | Instruction dataset | General-purpose VLMs | Geospatial instruction alignment | [Project/Paper](https://arxiv.org/search/?query=GAIA+remote+sensing+dataset&searchtype=all) |
| **GTPBD-MM** | Multimodal benchmark | Reasoning VLMs | Geospatial planning and decision reasoning | [Project/Paper](https://arxiv.org/search/?query=GTPBD-MM&searchtype=all) |
| **GeoMMBench** | Multimodal benchmark | Remote-sensing VLMs | Geospatial multimodal understanding | [Project/Paper](https://arxiv.org/search/?query=GeoMMBench&searchtype=all) |
| **Git-10M** | Pretraining dataset | Text2Earth | Global text-to-Earth generation | [HuggingFace](https://huggingface.co/datasets/lcybuaa/Git-10M) |
| **GroundSet** | Grounding benchmark | Grounding VLMs | Referring-expression grounding | [Project/Paper](https://arxiv.org/search/?query=GroundSet+remote+sensing&searchtype=all) |
| **HM-Bench** | Reasoning benchmark | Reasoning VLMs | Hierarchical multimodal reasoning | [Project/Paper](https://arxiv.org/search/?query=HM-Bench+remote+sensing&searchtype=all) |
| **KnowFlow-Bench** | Agent benchmark | CangLing-KnowFlow | Workflow generation and execution | [Project](https://cangling-agent.github.io/KnowFlow/) |
| **LAE-1M** | Pretraining dataset | LAE-DINO | Language-aware object detection | [HuggingFace](https://huggingface.co/datasets/ML4Sustain/LAE-1M) |
| **LaSeRS** | Reasoning benchmark | SegEarth-R2 | Complex-instruction segmentation | [HuggingFace](https://huggingface.co/datasets/earth-insights/LaSeRS) |
| **Landsat30-AU** | Multimodal dataset | General-purpose VLMs | Global Landsat image-text understanding | [Project/Paper](https://arxiv.org/search/?query=Landsat30-AU&searchtype=all) |
| **NeSy-Route** | Neuro-symbolic benchmark | GeoSolver | Route and spatial reasoning | [Project/Paper](https://arxiv.org/search/?query=NeSy-Route&searchtype=all) |
| **OmniEarth** | Multimodal benchmark | Remote-sensing VLMs | Multi-task Earth observation evaluation | [Project/Paper](https://arxiv.org/search/?query=OmniEarth+benchmark&searchtype=all) |
| **RSME-Bench** | Reasoning benchmark | Reasoning VLMs | Multi-entity remote-sensing reasoning | [Project/Paper](https://arxiv.org/search/?query=RSME-Bench&searchtype=all) |
| **RemoteSAM270k** | Instruction dataset | RemoteSAM | Segmentation and recognition | [HuggingFace](https://huggingface.co/datasets/1e12Leon/RemoteSAM270k) |
| **SAR-TEXT** | Image-text dataset | SAR VLMs | SAR image-language alignment | [Project/Paper](https://arxiv.org/search/?query=SAR-TEXT&searchtype=all) |
| **SARLANG-1M** | Pretraining dataset | SAR VLMs | Million-scale SAR-language pretraining | [Project/Paper](https://arxiv.org/search/?query=SARLANG-1M&searchtype=all) |
| **TEOChatlas** | Temporal dataset | TEOChat | Temporal Earth observation dialogue | [HuggingFace](https://huggingface.co/datasets/jirvin16/TEOChatlas) |
| **VLRS-Bench** | Vision-language benchmark | Remote-sensing VLMs | Comprehensive vision-language evaluation | [Project/Paper](https://arxiv.org/search/?query=VLRS-Bench&searchtype=all) |
| **BigEarthNet-MM** | Multimodal pretraining dataset | General-purpose VLMs | Multispectral image-text representation | [Project/Paper](https://arxiv.org/abs/2404.07043) |
| **BigEarthNet.txt** | Caption dataset | General-purpose VLMs | Multilingual Earth-observation descriptions | [Project/Paper](https://arxiv.org/search/?query=BigEarthNet.txt&searchtype=all) |
| **ChatEarthNet** | Instruction dataset | ChatEarthNet | Earth-observation dialogue and instruction tuning | [Project/Paper](https://arxiv.org/abs/2402.11325) |
| **DisasterM3** | Dataset + benchmark | Disaster-response VLMs | Multimodal multi-hazard understanding | [Project/Paper](https://arxiv.org/search/?query=DisasterM3&searchtype=all) |
| **FIT-RS** | Instruction dataset | SkySenseGPT | Fine-grained remote-sensing tasks | [HuggingFace](https://huggingface.co/datasets/ll-13/FIT-RS) |
| **GeoChat-Instruct** | Instruction dataset | GeoChat | Grounded remote-sensing dialogue | [HuggingFace](https://huggingface.co/datasets/MBZUAI/GeoChat_Instruct) |
| **LuoJiaHOG** | Multimodal dataset | General-purpose VLMs | Remote-sensing vision-language understanding | [Project/Paper](https://arxiv.org/search/?query=LuoJiaHOG&searchtype=all) |
| **REO-Instruct** | Instruction dataset | REO-VLM | Continuous Earth-observation regression | [GitHub](https://github.com/REO-VLM-anonymous/REO-VLM) |
| **RS5M** | Pretraining dataset | GeoRSCLIP | Remote-sensing image-text alignment | [HuggingFace](https://huggingface.co/datasets/omlab/RS5M) |
| **RSRCC** | Change-reasoning benchmark | Change-reasoning models | Reasoning over bi-temporal change | [Project/Paper](https://arxiv.org/search/?query=RSRCC+remote+sensing&searchtype=all) |
| **SkyEye-968k** | Instruction dataset | SkyEyeGPT | Multi-task remote-sensing instruction | [HuggingFace](https://huggingface.co/datasets/ZhanYang-nwpu/SkyEye-968k) |
| **SkyScript** | Pretraining dataset | RemoteCLIP | Large-scale image-text alignment | [Project/Paper](https://arxiv.org/abs/2312.11029) |
| **VRSBench** | Dataset + benchmark | General-purpose VLMs | Captioning VQA and grounding | [GitHub](https://github.com/lzw-lzw/VRSBench) |
| **refGeo** | Grounding dataset | GeoGround | Multi-format visual grounding | [HuggingFace](https://huggingface.co/datasets/erenzhou/refGeo) |
| **RSICap** | Caption dataset | RSGPT | Remote-sensing image captioning | [Project/Paper](https://arxiv.org/abs/2307.15266) |
| **SECOND-CC** | Change-caption dataset | Change-captioning models | Semantic change description | [GitHub](https://github.com/Chen-Yang-Liu/RSICC) |

<!-- AUTO_DATASETS_END -->

<a id="5-scope-and-maintenance"></a>
## 5. Scope and maintenance

### Inclusion boundary

A reasoning-specific work should demonstrate:

1. **Composition** — a conclusion combines multiple evidence items or inference steps.
2. **Traceability** — claims or actions link to observations, constraints, or tool outputs.
3. **Process-aware evaluation** — evaluation probes grounding, consistency, calibration, or execution beyond final-answer accuracy.

Perception, semantic alignment, generation, or grounding work remains valuable, but is labeled as an enabling foundation unless it meets these criteria.

### Reproduce and update the index

```bash
python -m pip install -r requirements.txt

# Add or edit a resource
$EDITOR data/survey.csv

# Fill missing scholarly metadata
python scripts/fetch_arxiv_meta.py

# Store current GitHub Stars and forks
python scripts/fetch_github_metrics.py

# Render derived files
python scripts/build_readme.py
python scripts/plot_timeline.py
```

- `data/survey.csv` stores paper metadata and official repository URLs.
- `data/github_metrics.json` stores dated Star/fork snapshots.
- `data/ecosystem.csv` stores the extended 90-resource model and hosting audit.
- `data/ecosystem_github_stars.json` stores its dated official-repository Star snapshot.
- `data/datasets.csv` stores standalone dataset and benchmark releases.
- README sections between `AUTO_*` markers are generated; editorial sections stay untouched.
- GitHub Actions verifies generated files and refreshes popularity snapshots on a schedule.

<a id="6-contributing"></a>
## 6. Contributing

Corrections and new resources are welcome. Follow [CONTRIBUTING.md](CONTRIBUTING.md), edit [data/survey.csv](data/survey.csv), or open a **Resource submission** issue.

Please include the official code URL and describe what evidence, trace, or tool trajectory makes the work reasoning-specific. Unknown fields should stay empty rather than being guessed.

<a id="7-citation"></a>
## 7. Citation

If this collection supports your research, please cite both the survey that defines the taxonomy and this repository when you use the continuously maintained resource metadata.

### Survey paper

> Jiancheng Pan, Liang Yao, Zilun Zhang, Yijie Zheng, Jiahao Li, Xiao He, Wenjia Xu, Yuqian Fu, Fan Liu, Zhaojun Liu, Jianwei Yin, and Xiaomeng Huang. “From Perception to Reasoning in Remote Sensing: A Survey and Outlook.” Manuscript, 2026.

```bibtex
@article{pan2026perception,
  title   = {From Perception to Reasoning in Remote Sensing: A Survey and Outlook},
  author  = {Pan, Jiancheng and Yao, Liang and Zhang, Zilun and
             Zheng, Yijie and Li, Jiahao and He, Xiao and Xu, Wenjia and
             Fu, Yuqian and Liu, Fan and Liu, Zhaojun and Yin, Jianwei and
             Huang, Xiaomeng},
  year    = {2026},
  note    = {Manuscript}
}
```

### Living repository

```bibtex
@misc{pan2026awesomeRSreasoning,
  title        = {Awesome Remote Sensing Reasoning: Models, Datasets, Benchmarks, and Agents},
  author       = {Pan, Jiancheng and Yao, Liang and Zhang, Zilun and
                  Zheng, Yijie and Li, Jiahao and He, Xiao and Xu, Wenjia and
                  Fu, Yuqian and Liu, Fan and Liu, Zhaojun and Yin, Jianwei and
                  Huang, Xiaomeng},
  year         = {2026},
  howpublished = {GitHub repository},
  url          = {https://github.com/ML4Sustain/Awsome-RS-Reasoning-Models},
  note         = {Living resource; accessed YYYY-MM-DD}
}
```

GitHub can also generate citation formats automatically from [CITATION.cff](CITATION.cff). Replace `YYYY-MM-DD` with your access date when citing the evolving catalog.

### Data provenance

The extended ecosystem was imported on 2026-08-24 from the public [VoyagerX/Awesome-RS-Reasoning-Models ModelScope Studio](https://modelscope.cn/studios/VoyagerX/Awesome-RS-Reasoning-Models/files), then normalized and stored locally. This repository does not require that Studio at build or runtime; later corrections and Star snapshots are maintained here.

## 8. License

Code is licensed under [MIT](LICENSE); catalog data under [CC BY 4.0](LICENSE-DATA). Linked resources retain their original licenses.

<p align="center"><sub>Maintained as an evidence-first map of reasoning over our planet.</sub></p>
