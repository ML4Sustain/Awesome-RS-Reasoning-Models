<p align="center">
  <img src="assets/header.svg" alt="Awesome Remote Sensing Reasoning" width="100%">
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <a href="https://ml4sustain.github.io/Awesome-RS-Reasoning-Models/"><img src="https://img.shields.io/badge/website-explore_online-16858a?style=flat-square&amp;logo=githubpages&amp;logoColor=white" alt="Explore the online catalog"></a>
  <a href="https://github.com/ML4Sustain/Awsome-RS-Reasoning-Models/actions"><img src="https://img.shields.io/github/actions/workflow/status/ML4Sustain/Awsome-RS-Reasoning-Models/catalog.yml?label=catalog&amp;style=flat-square" alt="Catalog status"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/contributions-welcome-39b54a?style=flat-square" alt="Contributions welcome"></a>
  <a href="LICENSE-DATA"><img src="https://img.shields.io/badge/data-CC_BY_4.0-ef9421?style=flat-square" alt="CC BY 4.0"></a>
  <a href="https://www.preprints.org/frontend/manuscript/046ed51d5cc524d60bc9281a57caf963/download_pub"><img src="https://img.shields.io/badge/survey-read_preprint-16858a?style=flat-square" alt="Read the survey preprint"></a>
  <img src="https://hits.sh/github.com/ML4Sustain/Awesome-RS-Reasoning-Models.svg?style=flat-square&amp;label=project%20views&amp;color=16858a&amp;labelColor=24292f" alt="Project views">
</p>

## Contents

- [1. Definition and scope of RS-Reasoning](#1-definition-and-scope)
  - [Definition and inclusion criteria](#definition-and-inclusion-criteria)
  - [Resource overview](#resource-overview)
  - [Development timeline](#development-timeline)
- [2. Taxonomy of RS-Reasoning methods](#2-taxonomy-of-rs-reasoning-methods)
- [3. Remote sensing vision-language foundations](#3-remote-sensing-vision-language-foundations)
- [4. Multimodal datasets and benchmarks](#4-multimodal-datasets-and-benchmarks)
- [5. Repository scope and maintenance](#5-repository-scope-and-maintenance)
- [6. Contributing](#6-contributing)
- [7. Citation](#7-citation)

<a id="1-definition-and-scope"></a>
## 1. Definition and scope of RS-Reasoning

Remote sensing is moving from recognizing **what is where** to establishing **why a conclusion follows from evidence**. This independent index tracks that transition across models, datasets, benchmarks, and executable agents.

> **RS-Reasoning** is task-dependent, multi-step inference that combines Earth observation evidence with geographic, temporal, or domain constraints and exposes an auditable support structure.

Entries link directly to their original paper and verified official code. Repository popularity is stored as a dated snapshot in this repository, never inferred from a transient live badge.

Read the complete survey: **[From Perception to Reasoning in Remote Sensing: A Survey and Outlook](https://www.preprints.org/frontend/manuscript/046ed51d5cc524d60bc9281a57caf963/download_pub)** ([Preprints.org](https://www.preprints.org/)).

<a id="definition-and-inclusion-criteria"></a>
### Definition and inclusion criteria

| 01 · Supervised | 02 · Reinforcement | 03 · Agentic / tool-augmented |
| --- | --- | --- |
| Learns from rationales, traces, masks, or structured intermediate supervision. | Optimizes answer, grounding, consistency, or process rewards. | Plans and executes tools, retrieval, GIS operations, or multi-step workflows. |
| **Observe:** answer + trace | **Observe:** reward + evidence | **Observe:** action + trajectory |

The tracks sit on top of enabling datasets and vision-language models, and support four application clusters from the survey:

`urban & social space` · `disaster assessment` · `environmental monitoring` · `spatiotemporal QA`

<a id="resource-overview"></a>
### Resource overview

<!-- AUTO_DASHBOARD_START -->

| Methods & models | Reasoning systems | Data & benchmarks | Official repositories | Model weights | ModelScope mirrors |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **80** | **27** | **49** | **65** | **44** | **11** |

Repository Stars are stored snapshots refreshed daily by GitHub Actions. Last refresh: **2026-09-04**.

<!-- AUTO_DASHBOARD_END -->

<a id="development-timeline"></a>
### Development timeline

<details open>
<summary><b>Representative work by first public release</b></summary>

<p align="center"><img src="assets/timeline.svg" alt="Timeline of remote sensing reasoning models" width="100%"></p>

</details>

<a id="2-taxonomy-of-rs-reasoning-methods"></a>
## 2. Taxonomy of RS-Reasoning methods

These works satisfy the repository's operational reasoning criteria: evidence is composed across steps, intermediate claims or actions are traceable, and evaluation extends beyond final-answer accuracy. Following Table V of the survey, the three paradigms are **non-exclusive** and indicate the dominant acquisition or execution mechanism. The core taxonomy contains 27 systems, sorted by stored GitHub Stars inside each paradigm; the development timeline above uses the same method set.

<!-- AUTO_CATALOG_START -->

<details open>
<summary><b>Reasoning Models › Supervised Reasoning</b> · 6 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **SegEarth-R1** | 2025 · arXiv | <a href="https://arxiv.org/abs/2504.09644"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/earth-insights/SegEarth-R1-EarthReason"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> · <a href="https://modelscope.cn/models/earth-insights/SegEarth-R1-EarthReason"><img alt="Weights: ModelScope" width="93" height="20" src="https://img.shields.io/badge/ModelScope-624aff?style=flat&amp;logo=modelscope&amp;logoColor=white"></a> | <a href="https://github.com/earth-insights/SegEarth-R1"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/earth-insights/SegEarth-R1/stargazers"><img alt="Stars: 157" width="52" height="20" src="https://img.shields.io/badge/157-59636e?style=flat&amp;logo=github"></a> |
| **TerraScope** | 2026 · CVPR | <a href="https://arxiv.org/abs/2603.19039"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/sy1998/TerraScope"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> · <a href="https://modelscope.cn/models/shuyanshuyan/terrascope"><img alt="Weights: ModelScope" width="93" height="20" src="https://img.shields.io/badge/ModelScope-624aff?style=flat&amp;logo=modelscope&amp;logoColor=white"></a> | <a href="https://github.com/shuyansy/Earth-Observation-VLMs"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/shuyansy/Earth-Observation-VLMs/stargazers"><img alt="Stars: 139" width="52" height="20" src="https://img.shields.io/badge/139-59636e?style=flat&amp;logo=github"></a> |
| **SegEarth-R2** | 2025 · arXiv | <a href="https://arxiv.org/abs/2512.20013"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | <a href="https://github.com/earth-insights/SegEarth-R2"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/earth-insights/SegEarth-R2/stargazers"><img alt="Stars: 71" width="46" height="20" src="https://img.shields.io/badge/71-59636e?style=flat&amp;logo=github"></a> |
| **EarthVL** | 2026 · arXiv | <a href="https://arxiv.org/abs/2601.02783"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | <a href="https://github.com/Junjue-Wang/EarthVL"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/Junjue-Wang/EarthVL/stargazers"><img alt="Stars: 43" width="46" height="20" src="https://img.shields.io/badge/43-59636e?style=flat&amp;logo=github"></a> |
| **GeoChrono** | 2026 · arXiv | <a href="https://arxiv.org/abs/2607.15768"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/Davidup1/GeoChrono"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> · <a href="https://modelscope.cn/models/Davidup1/GeoChrono"><img alt="Weights: ModelScope" width="93" height="20" src="https://img.shields.io/badge/ModelScope-624aff?style=flat&amp;logo=modelscope&amp;logoColor=white"></a> | <a href="https://github.com/IntelliSensing/GeoChrono"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/IntelliSensing/GeoChrono/stargazers"><img alt="Stars: 9" width="46" height="20" src="https://img.shields.io/badge/9-59636e?style=flat&amp;logo=github"></a> |
| **Delta-LLaVA** | 2026 · arXiv | <a href="https://arxiv.org/abs/2604.14044"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | — | — |

</details>

<details open>
<summary><b>Reasoning Models › RL-Driven Reasoning</b> · 14 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **RSThinker** | 2026 · ICLR | <a href="https://arxiv.org/abs/2509.22221"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/minglanga/RSThinker"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/minglangL/RSThinker"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/minglangL/RSThinker/stargazers"><img alt="Stars: 38" width="46" height="20" src="https://img.shields.io/badge/38-59636e?style=flat&amp;logo=github"></a> |
| **GeoVLM-R1** | 2025 · arXiv | <a href="https://arxiv.org/abs/2509.25026"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | <a href="https://github.com/mustansarfiaz/GeoVLM-R1-Toolkit"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/mustansarfiaz/GeoVLM-R1-Toolkit/stargazers"><img alt="Stars: 32" width="46" height="20" src="https://img.shields.io/badge/32-59636e?style=flat&amp;logo=github"></a> |
| **RS-EoT** | 2026 · CVPR | <a href="https://arxiv.org/abs/2511.22396"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/ShaoRun/RS-EoT-7B"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> · <a href="https://geox-lab.github.io/Asking_like_Socrates/"><img alt="Project: Website" width="72" height="20" src="https://img.shields.io/badge/Website-16858a?style=flat"></a> | <a href="https://github.com/GeoX-Lab/Asking_like_Socrates"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/GeoX-Lab/Asking_like_Socrates/stargazers"><img alt="Stars: 27" width="46" height="20" src="https://img.shields.io/badge/27-59636e?style=flat&amp;logo=github"></a> |
| **GeoZero** | 2025 · arXiv | <a href="https://arxiv.org/abs/2511.22645"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/hjvsl/GeoZero"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> · <a href="https://pan.baidu.com/s/1nJjBwO4UlVv4GFl60gjM3w?pwd=15gn"><img alt="Weights: Baidu" width="62" height="20" src="https://img.shields.io/badge/Baidu-1677ff?style=flat&amp;logo=baidu"></a> | <a href="https://github.com/MiliLab/GeoZero"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/MiliLab/GeoZero/stargazers"><img alt="Stars: 27" width="46" height="20" src="https://img.shields.io/badge/27-59636e?style=flat&amp;logo=github"></a> |
| **RemoteAgent** | 2026 · TGRS | <a href="https://arxiv.org/abs/2604.07765"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | <a href="https://github.com/1e12Leon/RemoteAgent"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/1e12Leon/RemoteAgent/stargazers"><img alt="Stars: 23" width="46" height="20" src="https://img.shields.io/badge/23-59636e?style=flat&amp;logo=github"></a> |
| **RemoteReasoner** | 2026 · AAAI | <a href="https://doi.org/10.1609/aaai.v40i14.38175"><img alt="Paper: DOI" width="49" height="20" src="https://img.shields.io/badge/DOI-4051b5?style=flat&amp;logo=doi"></a> | <a href="https://huggingface.co/1e12Leon/RemoteReasoner"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> · <a href="https://modelscope.cn/models/AIMGroup/RemoteReasoner"><img alt="Weights: ModelScope" width="93" height="20" src="https://img.shields.io/badge/ModelScope-624aff?style=flat&amp;logo=modelscope&amp;logoColor=white"></a> | <a href="https://github.com/1e12Leon/RemoteReasoner"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/1e12Leon/RemoteReasoner/stargazers"><img alt="Stars: 18" width="46" height="20" src="https://img.shields.io/badge/18-59636e?style=flat&amp;logo=github"></a> |
| **Geo-R1** | 2025 · arXiv | <a href="https://arxiv.org/abs/2509.21976"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/Geo-R1"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/Geo-R1/geo-r1"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/Geo-R1/geo-r1/stargazers"><img alt="Stars: 16" width="46" height="20" src="https://img.shields.io/badge/16-59636e?style=flat&amp;logo=github"></a> |
| **TinyRS-R1** | 2025 · arXiv | <a href="https://arxiv.org/abs/2505.12099"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/aybora/Qwen2-VL-TinyRS-R1"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/aybora/TinyRS"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/aybora/TinyRS/stargazers"><img alt="Stars: 14" width="46" height="20" src="https://img.shields.io/badge/14-59636e?style=flat&amp;logo=github"></a> |
| **GeoReason** | 2026 · arXiv | <a href="https://arxiv.org/abs/2601.04118"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/WenshuaiLi/GeoReason"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/canlanqianyan/GeoReason"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/canlanqianyan/GeoReason/stargazers"><img alt="Stars: 10" width="46" height="20" src="https://img.shields.io/badge/10-59636e?style=flat&amp;logo=github"></a> |
| **GeoVista** | 2026 · arXiv | <a href="https://arxiv.org/abs/2605.14475"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/ryan6073/GeoVista-7B-Instruct"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> · <a href="https://huggingface.co/ryan6073/GeoVista-7B-Preview"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/ryan6073/GeoVista"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/ryan6073/GeoVista/stargazers"><img alt="Stars: 10" width="46" height="20" src="https://img.shields.io/badge/10-59636e?style=flat&amp;logo=github"></a> |
| **GeoSolver** | 2026 · arXiv | <a href="https://arxiv.org/abs/2603.09551"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/minglanga/GeoSolver"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/minglangL/GeoSolver"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/minglangL/GeoSolver/stargazers"><img alt="Stars: 3" width="46" height="20" src="https://img.shields.io/badge/3-59636e?style=flat&amp;logo=github"></a> |
| **RemoteZero** | 2026 · arXiv | <a href="https://arxiv.org/abs/2605.04451"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | <a href="https://github.com/1e12Leon/RemoteZero"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/1e12Leon/RemoteZero/stargazers"><img alt="Stars: 1" width="46" height="20" src="https://img.shields.io/badge/1-59636e?style=flat&amp;logo=github"></a> |
| **RS-HyRe-R1** | 2026 · arXiv | <a href="https://arxiv.org/abs/2604.17504"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/geozgz/RS-HyRe-R1"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/GeoX-Lab/RS-HyRe-R1"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/GeoX-Lab/RS-HyRe-R1/stargazers"><img alt="Stars: 1" width="46" height="20" src="https://img.shields.io/badge/1-59636e?style=flat&amp;logo=github"></a> |
| **GeoX** | 2026 · arXiv | <a href="https://arxiv.org/abs/2605.20006"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | — | — |

</details>

<details open>
<summary><b>Reasoning Models › Agentic / Tool-Augmented Reasoning</b> · 7 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Earth-Agent** | 2026 · ICLR | <a href="https://arxiv.org/abs/2509.23141"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | <a href="https://github.com/opendatalab/Earth-Agent"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/opendatalab/Earth-Agent/stargazers"><img alt="Stars: 198" width="52" height="20" src="https://img.shields.io/badge/198-59636e?style=flat&amp;logo=github"></a> |
| **OpenEarthAgent** | 2026 · ECCV | <a href="https://arxiv.org/abs/2602.17665"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/MBZUAI/OpenEarthAgent"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> · <a href="https://modelscope.cn/models/MBZUAI/OpenEarthAgent"><img alt="Weights: ModelScope" width="93" height="20" src="https://img.shields.io/badge/ModelScope-624aff?style=flat&amp;logo=modelscope&amp;logoColor=white"></a> | <a href="https://github.com/mbzuai-oryx/OpenEarthAgent"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/mbzuai-oryx/OpenEarthAgent/stargazers"><img alt="Stars: 104" width="52" height="20" src="https://img.shields.io/badge/104-59636e?style=flat&amp;logo=github"></a> |
| **GeoMMAgent** | 2026 · CVPR | <a href="https://arxiv.org/abs/2604.08896"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | <a href="https://github.com/Shihao-Cheng/GeoMMAgent"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/Shihao-Cheng/GeoMMAgent/stargazers"><img alt="Stars: 50" width="46" height="20" src="https://img.shields.io/badge/50-59636e?style=flat&amp;logo=github"></a> |
| **EarthAgent** | 2025 · arXiv | <a href="https://arxiv.org/abs/2511.17198"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | <a href="https://github.com/earth-insights/EarthAgent"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/earth-insights/EarthAgent/stargazers"><img alt="Stars: 13" width="46" height="20" src="https://img.shields.io/badge/13-59636e?style=flat&amp;logo=github"></a> |
| **TerraAgent** | 2026 · arXiv | <a href="https://arxiv.org/abs/2606.13148"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | <a href="https://github.com/Takerdat23/TerraBench"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/Takerdat23/TerraBench/stargazers"><img alt="Stars: 4" width="46" height="20" src="https://img.shields.io/badge/4-59636e?style=flat&amp;logo=github"></a> |
| **MAP-Agent** | 2026 · arXiv | <a href="https://arxiv.org/abs/2605.12237"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | <a href="https://github.com/MiliLab/UHR-Micro"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/MiliLab/UHR-Micro/stargazers"><img alt="Stars: 1" width="46" height="20" src="https://img.shields.io/badge/1-59636e?style=flat&amp;logo=github"></a> |
| **Earth AI** | 2025 · arXiv | <a href="https://arxiv.org/abs/2510.18318"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | — | — |

</details>

<!-- AUTO_CATALOG_END -->

<a id="3-remote-sensing-vision-language-foundations"></a>
## 3. Remote sensing vision-language foundations

Reasoning is built on perception and remote-sensing vision-language modeling. This section therefore tracks 53 **reasoning-enabling** resources separately from reasoning-specific systems: contrastive alignment models, generative and task-specific VLMs, ultra-high-resolution interfaces, retrieval, detection, segmentation, and data generation. Inclusion here indicates foundational relevance, not demonstrated multi-step reasoning.

<!-- AUTO_ECOSYSTEM_START -->

<details open>
<summary><b>Remote Sensing Vision-Language Modeling › Contrastive VLMs</b> · 7 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **RemoteCLIP** | 2024 · TGRS | <a href="https://doi.org/10.1109/TGRS.2024.3390838"><img alt="Paper: DOI" width="49" height="20" src="https://img.shields.io/badge/DOI-4051b5?style=flat&amp;logo=doi"></a> | <a href="https://huggingface.co/chendelong/RemoteCLIP"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/ChenDelong1999/RemoteCLIP"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/ChenDelong1999/RemoteCLIP/stargazers"><img alt="Stars: 591" width="52" height="20" src="https://img.shields.io/badge/591-59636e?style=flat&amp;logo=github"></a> |
| **SatCLIP** | 2025 · AAAI | <a href="https://doi.org/10.1609/aaai.v39i4.32457"><img alt="Paper: DOI" width="49" height="20" src="https://img.shields.io/badge/DOI-4051b5?style=flat&amp;logo=doi"></a> | <a href="https://huggingface.co/microsoft/SatCLIP-ViT16-L40"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> · <a href="https://modelscope.cn/models/microsoft/SatCLIP-ViT16-L40"><img alt="Weights: ModelScope" width="93" height="20" src="https://img.shields.io/badge/ModelScope-624aff?style=flat&amp;logo=modelscope&amp;logoColor=white"></a> | <a href="https://github.com/microsoft/satclip"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/microsoft/satclip/stargazers"><img alt="Stars: 376" width="52" height="20" src="https://img.shields.io/badge/376-59636e?style=flat&amp;logo=github"></a> |
| **GeoRSCLIP** | 2024 · TGRS | <a href="https://doi.org/10.1109/TGRS.2024.3449154"><img alt="Paper: DOI" width="49" height="20" src="https://img.shields.io/badge/DOI-4051b5?style=flat&amp;logo=doi"></a> | <a href="https://huggingface.co/Zilun/GeoRSCLIP"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/om-ai-lab/RS5M"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/om-ai-lab/RS5M/stargazers"><img alt="Stars: 315" width="52" height="20" src="https://img.shields.io/badge/315-59636e?style=flat&amp;logo=github"></a> |
| **DGTRS-CLIP** | 2025 · arXiv | <a href="https://arxiv.org/abs/2503.19311"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/MitsuiChen14/DGTRS-CLIP-ViT-L-14"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> · <a href="https://huggingface.co/MitsuiChen14/DGTRS-CLIP-ViT-B-16"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/MitsuiChen14/DGTRS"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/MitsuiChen14/DGTRS/stargazers"><img alt="Stars: 33" width="46" height="20" src="https://img.shields.io/badge/33-59636e?style=flat&amp;logo=github"></a> |
| **PriorCLIP** | 2023 · MM | <a href="https://doi.org/10.1145/3581783.3612587"><img alt="Paper: DOI" width="49" height="20" src="https://img.shields.io/badge/DOI-4051b5?style=flat&amp;logo=doi"></a> | <a href="https://pan.baidu.com/s/1urfZ_64DFRelAQz-LYkcCQ?pwd=2v3v"><img alt="Weights: Baidu" width="62" height="20" src="https://img.shields.io/badge/Baidu-1677ff?style=flat&amp;logo=baidu"></a> | <a href="https://github.com/jaychempan/PriorCLIP"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/jaychempan/PriorCLIP/stargazers"><img alt="Stars: 30" width="46" height="20" src="https://img.shields.io/badge/30-59636e?style=flat&amp;logo=github"></a> |
| **TimeSenCLIP** | 2026 · ISPRS J. P&RS | <a href="https://doi.org/10.1016/j.isprsjprs.2026.03.043"><img alt="Paper: DOI" width="49" height="20" src="https://img.shields.io/badge/DOI-4051b5?style=flat&amp;logo=doi"></a> | <a href="https://huggingface.co/pallavijainpj/TimeSenCLIP"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | — | — |
| **GeoAlignCLIP** | 2026 · arXiv | <a href="https://arxiv.org/abs/2603.09566"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | — | — |

</details>

<details open>
<summary><b>Remote Sensing Vision-Language Modeling › Generative Large VLMs</b> · 14 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **GeoChat** | 2024 · CVPR | <a href="https://arxiv.org/abs/2311.15826"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/MBZUAI/geochat-7B"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> · <a href="https://modelscope.cn/models/MBZUAI/geochat-7B"><img alt="Weights: ModelScope" width="93" height="20" src="https://img.shields.io/badge/ModelScope-624aff?style=flat&amp;logo=modelscope&amp;logoColor=white"></a> | <a href="https://github.com/mbzuai-oryx/GeoChat"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/mbzuai-oryx/GeoChat/stargazers"><img alt="Stars: 748" width="52" height="20" src="https://img.shields.io/badge/748-59636e?style=flat&amp;logo=github"></a> |
| **Falcon** | 2025 · arXiv | <a href="https://arxiv.org/abs/2503.11070"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/TianHuiLab/Falcon-Single-Instruction-Large"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/TianHuiLab/Falcon"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/TianHuiLab/Falcon/stargazers"><img alt="Stars: 384" width="52" height="20" src="https://img.shields.io/badge/384-59636e?style=flat&amp;logo=github"></a> |
| **LHRS-Bot** | 2024 · ECCV | <a href="https://arxiv.org/abs/2402.02544"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://drive.google.com/drive/folders/1dzWTE1k935MjMVnfLtTJiIqw7yCj-e3m?usp=drive_link"><img alt="Weights: Google Drive" width="76" height="20" src="https://img.shields.io/badge/Google%20Drive-526d82?style=flat"></a> · <a href="https://pan.baidu.com/s/1n1h_ZImeKTgvoNHjr5bq3Q?pwd=qhqw"><img alt="Weights: Baidu" width="62" height="20" src="https://img.shields.io/badge/Baidu-1677ff?style=flat&amp;logo=baidu"></a> | <a href="https://github.com/NJU-LHRS/LHRS-Bot"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/NJU-LHRS/LHRS-Bot/stargazers"><img alt="Stars: 194" width="52" height="20" src="https://img.shields.io/badge/194-59636e?style=flat&amp;logo=github"></a> |
| **EarthGPT** | 2024 · TGRS | <a href="https://arxiv.org/abs/2401.16822"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | <a href="https://github.com/wivizhang/EarthGPT"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/wivizhang/EarthGPT/stargazers"><img alt="Stars: 161" width="52" height="20" src="https://img.shields.io/badge/161-59636e?style=flat&amp;logo=github"></a> |
| **TEOChat** | 2025 · ICLR | <a href="https://arxiv.org/abs/2410.06234"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/jirvin16/TEOChat"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/ermongroup/TEOChat"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/ermongroup/TEOChat/stargazers"><img alt="Stars: 152" width="52" height="20" src="https://img.shields.io/badge/152-59636e?style=flat&amp;logo=github"></a> |
| **RSGPT** | 2025 · ISPRS | <a href="https://arxiv.org/abs/2307.15266"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | <a href="https://github.com/Lavender105/RSGPT"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/Lavender105/RSGPT/stargazers"><img alt="Stars: 151" width="52" height="20" src="https://img.shields.io/badge/151-59636e?style=flat&amp;logo=github"></a> |
| **SkySenseGPT** | 2024 · arXiv | <a href="https://arxiv.org/abs/2406.10100"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/ll-13/SkySenseGPT-7B-CLIP-ViT"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/Luo-Z13/SkySense-Chat"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/Luo-Z13/SkySense-Chat/stargazers"><img alt="Stars: 150" width="52" height="20" src="https://img.shields.io/badge/150-59636e?style=flat&amp;logo=github"></a> |
| **SkyEyeGPT** | 2025 · ISPRS | <a href="https://arxiv.org/abs/2401.09712"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/ZhanYang-nwpu/SkyEyeGPT"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/ZhanYang-nwpu/SkyEyeGPT"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/ZhanYang-nwpu/SkyEyeGPT/stargazers"><img alt="Stars: 139" width="52" height="20" src="https://img.shields.io/badge/139-59636e?style=flat&amp;logo=github"></a> |
| **RSUniVLM** | 2024 · arXiv | <a href="https://arxiv.org/abs/2412.05679"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://drive.google.com/drive/folders/1TtaoOPmh167gpgHHWRNBMCaA7t_XZ4Vg?usp=sharing"><img alt="Weights: Google Drive" width="76" height="20" src="https://img.shields.io/badge/Google%20Drive-526d82?style=flat"></a> | <a href="https://github.com/xuliu-cyber/RSUniVLM"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/xuliu-cyber/RSUniVLM/stargazers"><img alt="Stars: 47" width="46" height="20" src="https://img.shields.io/badge/47-59636e?style=flat&amp;logo=github"></a> |
| **EarthMarker** | 2024 · TGRS | <a href="https://ieeexplore.ieee.org/document/10817639"><img alt="Paper: IEEE" width="55" height="20" src="https://img.shields.io/badge/IEEE-00629b?style=flat&amp;logo=ieee"></a> | — | <a href="https://github.com/wivizhang/EarthMarker"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/wivizhang/EarthMarker/stargazers"><img alt="Stars: 46" width="46" height="20" src="https://img.shields.io/badge/46-59636e?style=flat&amp;logo=github"></a> |
| **FUSAR-GPT** | 2026 · CVPR | <a href="https://arxiv.org/abs/2602.19190"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | <a href="https://github.com/yangyifremad/FUSAR-KLIP"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/yangyifremad/FUSAR-KLIP/stargazers"><img alt="Stars: 33" width="46" height="20" src="https://img.shields.io/badge/33-59636e?style=flat&amp;logo=github"></a> |
| **Earth-OneVision** | 2026 · arXiv | <a href="https://arxiv.org/abs/2606.10819"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | — | — |
| **SkyNative** | 2026 · arXiv | <a href="https://arxiv.org/abs/2605.17949"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | — | — |
| **RingMoGPT** | 2024 · TGRS | — | — | — | — |

</details>

<details open>
<summary><b>Remote Sensing Vision-Language Modeling › Task-Specific VLMs</b> · 15 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **LAE-DINO** | 2025 · AAAI | <a href="https://arxiv.org/abs/2408.09110"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/ML4Sustain/LAE-DINO"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> · <a href="https://modelscope.cn/models/ML4Sustain/LAE-DINO"><img alt="Weights: ModelScope" width="93" height="20" src="https://img.shields.io/badge/ModelScope-624aff?style=flat&amp;logo=modelscope&amp;logoColor=white"></a> | <a href="https://github.com/jaychempan/LAE-DINO"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/jaychempan/LAE-DINO/stargazers"><img alt="Stars: 291" width="52" height="20" src="https://img.shields.io/badge/291-59636e?style=flat&amp;logo=github"></a> |
| **RemoteSAM** | 2025 · MM | <a href="https://arxiv.org/abs/2505.18022"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/1e12Leon/RemoteSAM"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/1e12Leon/RemoteSAM"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/1e12Leon/RemoteSAM/stargazers"><img alt="Stars: 247" width="52" height="20" src="https://img.shields.io/badge/247-59636e?style=flat&amp;logo=github"></a> |
| **EarthMind** | 2025 · arXiv | <a href="https://arxiv.org/abs/2506.01667"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/sy1998/EarthMind-4B"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/shuyansy/Earth-Observation-VLMs"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/shuyansy/Earth-Observation-VLMs/stargazers"><img alt="Stars: 139" width="52" height="20" src="https://img.shields.io/badge/139-59636e?style=flat&amp;logo=github"></a> |
| **InstructSAM** | 2025 · NeurIPS | <a href="https://arxiv.org/abs/2505.15818"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | <a href="https://github.com/VoyagerXvoyagerx/InstructSAM"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/VoyagerXvoyagerx/InstructSAM/stargazers"><img alt="Stars: 119" width="52" height="20" src="https://img.shields.io/badge/119-59636e?style=flat&amp;logo=github"></a> |
| **GeoGround** | 2024 · arXiv | <a href="https://arxiv.org/abs/2411.11904"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/erenzhou/GeoGround"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> · <a href="https://modelscope.cn/models/zytx121/geoground"><img alt="Weights: ModelScope" width="93" height="20" src="https://img.shields.io/badge/ModelScope-624aff?style=flat&amp;logo=modelscope&amp;logoColor=white"></a> | <a href="https://github.com/VisionXLab/GeoGround"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/VisionXLab/GeoGround/stargazers"><img alt="Stars: 94" width="46" height="20" src="https://img.shields.io/badge/94-59636e?style=flat&amp;logo=github"></a> |
| **CastDet** | 2024 · ECCV | <a href="https://arxiv.org/abs/2311.11646"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | <a href="https://github.com/VisionXLab/CastDet"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/VisionXLab/CastDet/stargazers"><img alt="Stars: 85" width="46" height="20" src="https://img.shields.io/badge/85-59636e?style=flat&amp;logo=github"></a> |
| **GeoPix** | 2025 · GRSM | <a href="https://doi.org/10.1109/MGRS.2025.3560293"><img alt="Paper: DOI" width="49" height="20" src="https://img.shields.io/badge/DOI-4051b5?style=flat&amp;logo=doi"></a> | <a href="https://huggingface.co/Norman-Ou/GeoPix"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/Norman-Ou/GeoPix"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/Norman-Ou/GeoPix/stargazers"><img alt="Stars: 75" width="46" height="20" src="https://img.shields.io/badge/75-59636e?style=flat&amp;logo=github"></a> |
| **UniGeoSeg** | 2026 · CVPR | <a href="https://arxiv.org/abs/2511.23332"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/nishuo1999/UniGeoSeg"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/MiliLab/UniGeoSeg"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/MiliLab/UniGeoSeg/stargazers"><img alt="Stars: 44" width="46" height="20" src="https://img.shields.io/badge/44-59636e?style=flat&amp;logo=github"></a> |
| **OpenRSD** | 2025 · ICCV | <a href="https://arxiv.org/abs/2503.06146"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://pan.baidu.com/s/1sV3GHgneC3dQskIaYABefg?pwd=aan9"><img alt="Weights: Baidu" width="62" height="20" src="https://img.shields.io/badge/Baidu-1677ff?style=flat&amp;logo=baidu"></a> | <a href="https://github.com/floatingstarZ/OpenRSD"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/floatingstarZ/OpenRSD/stargazers"><img alt="Stars: 42" width="46" height="20" src="https://img.shields.io/badge/42-59636e?style=flat&amp;logo=github"></a> |
| **RSVG-ZeroOV** | 2026 · AAAI | <a href="https://arxiv.org/abs/2509.18711"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | <a href="https://github.com/like413/RSVG-ZeroOV"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/like413/RSVG-ZeroOV/stargazers"><img alt="Stars: 27" width="46" height="20" src="https://img.shields.io/badge/27-59636e?style=flat&amp;logo=github"></a> |
| **LLaMA-Unidetector** | 2025 · TGRS | <a href="https://doi.org/10.1109/TGRS.2025.3564332"><img alt="Paper: DOI" width="49" height="20" src="https://img.shields.io/badge/DOI-4051b5?style=flat&amp;logo=doi"></a> | <a href="https://drive.google.com/file/d/1AwUn5EebmmLBo7njjW_Ng1q9zDrqkNbB/view"><img alt="Weights: Google Drive" width="76" height="20" src="https://img.shields.io/badge/Google%20Drive-526d82?style=flat"></a> · <a href="https://pan.baidu.com/s/1P3pW3euqqxYVZQvw-is1vQ?pwd=1234"><img alt="Weights: Baidu" width="62" height="20" src="https://img.shields.io/badge/Baidu-1677ff?style=flat&amp;logo=baidu"></a> | <a href="https://github.com/ChloeeGrace/LLaMA-Unidetector"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/ChloeeGrace/LLaMA-Unidetector/stargazers"><img alt="Stars: 15" width="46" height="20" src="https://img.shields.io/badge/15-59636e?style=flat&amp;logo=github"></a> |
| **REO-VLM** | 2024 · arXiv | <a href="https://arxiv.org/abs/2412.15115"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | <a href="https://github.com/REO-VLM-anonymous/REO-VLM"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/REO-VLM-anonymous/REO-VLM/stargazers"><img alt="Stars: 10" width="46" height="20" src="https://img.shields.io/badge/10-59636e?style=flat&amp;logo=github"></a> |
| **Cross-View OVD** | 2025 · arXiv | <a href="https://arxiv.org/abs/2510.03858"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | — | — |
| **FASE** | 2025 · CIKM | <a href="https://doi.org/10.1145/3746252.3760838"><img alt="Paper: DOI" width="49" height="20" src="https://img.shields.io/badge/DOI-4051b5?style=flat&amp;logo=doi"></a> | — | — | — |
| **GeoMag** | 2025 · MM | <a href="https://arxiv.org/abs/2507.05887"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | — | — |

</details>

<details open>
<summary><b>Reasoning-Enabling Models › Ultra-High-Resolution VLMs</b> · 3 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **GeoLLaVA-8K** | 2025 · NeurIPS | <a href="https://arxiv.org/abs/2505.21375"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/initiacms/GeoLLaVA-8K"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/MiliLab/GeoLLaVA-8K"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/MiliLab/GeoLLaVA-8K/stargazers"><img alt="Stars: 59" width="46" height="20" src="https://img.shields.io/badge/59-59636e?style=flat&amp;logo=github"></a> |
| **ZoomEarth** | 2026 · CVPR | <a href="https://arxiv.org/abs/2511.12267"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/HappyBug/ZoomEarth-3B"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> | <a href="https://github.com/earth-insights/ZoomEarth"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/earth-insights/ZoomEarth/stargazers"><img alt="Stars: 45" width="46" height="20" src="https://img.shields.io/badge/45-59636e?style=flat&amp;logo=github"></a> |
| **Zoom-RS (Look Where It Matters)** | 2025 · arXiv | <a href="https://arxiv.org/abs/2511.20460"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | <a href="https://github.com/kiki-zyq/ZoomSearch"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/kiki-zyq/ZoomSearch/stargazers"><img alt="Stars: 27" width="46" height="20" src="https://img.shields.io/badge/27-59636e?style=flat&amp;logo=github"></a> |

</details>

<details open>
<summary><b>Reasoning-Enabling Models › Generation Models</b> · 2 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Text2Earth** | 2025 · GRSM | <a href="https://ieeexplore.ieee.org/document/10988859"><img alt="Paper: IEEE" width="55" height="20" src="https://img.shields.io/badge/IEEE-00629b?style=flat&amp;logo=ieee"></a> | <a href="https://huggingface.co/lcybuaa/Text2Earth"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> · <a href="https://modelscope.cn/models/lcybuaa1111/Text2Earth"><img alt="Weights: ModelScope" width="93" height="20" src="https://img.shields.io/badge/ModelScope-624aff?style=flat&amp;logo=modelscope&amp;logoColor=white"></a> | <a href="https://github.com/Chen-Yang-Liu/Text2Earth"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/Chen-Yang-Liu/Text2Earth/stargazers"><img alt="Stars: 189" width="52" height="20" src="https://img.shields.io/badge/189-59636e?style=flat&amp;logo=github"></a> |
| **Earthsynth** | 2025 · arXiv | <a href="https://arxiv.org/abs/2505.12108"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://huggingface.co/jaychempan/EarthSynth"><img alt="Weights: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> · <a href="https://modelscope.cn/models/ML4Sustain/EarthSynth"><img alt="Weights: ModelScope" width="93" height="20" src="https://img.shields.io/badge/ModelScope-624aff?style=flat&amp;logo=modelscope&amp;logoColor=white"></a> | <a href="https://github.com/jaychempan/EarthSynth"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/jaychempan/EarthSynth/stargazers"><img alt="Stars: 61" width="46" height="20" src="https://img.shields.io/badge/61-59636e?style=flat&amp;logo=github"></a> |

</details>

<details open>
<summary><b>Perception Foundations › Object Detection</b> · 6 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **CalNet** | 2023 · MM | — | <a href="https://pan.baidu.com/s/1PnmdKqIxPnTgK6yQ6WfwpA"><img alt="Weights: Baidu" width="62" height="20" src="https://img.shields.io/badge/Baidu-1677ff?style=flat&amp;logo=baidu"></a> | <a href="https://github.com/hexiao0275/CALNet-Dronevehicle"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/hexiao0275/CALNet-Dronevehicle/stargazers"><img alt="Stars: 68" width="46" height="20" src="https://img.shields.io/badge/68-59636e?style=flat&amp;logo=github"></a> |
| **Enhance-then-Search (AugSearch)** | 2025 · CVPR | <a href="https://arxiv.org/abs/2504.04517"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://pan.baidu.com/s/17wECMZ7X-wkFMXSCQ_SvAw?pwd=ttue"><img alt="Weights: Baidu" width="62" height="20" src="https://img.shields.io/badge/Baidu-1677ff?style=flat&amp;logo=baidu"></a> | <a href="https://github.com/jaychempan/ETS"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/jaychempan/ETS/stargazers"><img alt="Stars: 57" width="46" height="20" src="https://img.shields.io/badge/57-59636e?style=flat&amp;logo=github"></a> |
| **S2A-Det** | 2023 · TGRS | — | — | <a href="https://github.com/hexiao0275/S2ADet"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/hexiao0275/S2ADet/stargazers"><img alt="Stars: 50" width="46" height="20" src="https://img.shields.io/badge/50-59636e?style=flat&amp;logo=github"></a> |
| **LCMA** | 2026 · Electronics | — | — | <a href="https://github.com/hexiao0275/LCMA_RGBT"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/hexiao0275/LCMA_RGBT/stargazers"><img alt="Stars: 2" width="46" height="20" src="https://img.shields.io/badge/2-59636e?style=flat&amp;logo=github"></a> |
| **SDCM** | 2025 · TMM | — | — | — | — |
| **Semantic-Aware Ship Detection** | 2025 · IGARSS | <a href="https://arxiv.org/abs/2508.15930"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | — | — |

</details>

<details open>
<summary><b>Perception Foundations › Semantic Segmentation</b> · 2 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Rethinking Transformers (RS Segmentation)** | 2023 · TGRS | <a href="https://doi.org/10.1109/TGRS.2023.3302024"><img alt="Paper: DOI" width="49" height="20" src="https://img.shields.io/badge/DOI-4051b5?style=flat&amp;logo=doi"></a> | <a href="https://drive.google.com/file/d/1yV070cXTrkCN2FTHKM2DIXI_dtVjaTJ6/view"><img alt="Weights: Google Drive" width="76" height="20" src="https://img.shields.io/badge/Google%20Drive-526d82?style=flat"></a> | <a href="https://github.com/lyhnsn/GLOTS"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/lyhnsn/GLOTS/stargazers"><img alt="Stars: 17" width="46" height="20" src="https://img.shields.io/badge/17-59636e?style=flat&amp;logo=github"></a> |
| **Multilevel Multimodal Fusion Transformer** | 2024 · TGRS | <a href="https://doi.org/10.1109/TGRS.2024.3373033"><img alt="Paper: DOI" width="49" height="20" src="https://img.shields.io/badge/DOI-4051b5?style=flat&amp;logo=doi"></a> | — | <a href="https://github.com/yida12345/FTransUNet"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/yida12345/FTransUNet/stargazers"><img alt="Stars: 1" width="46" height="20" src="https://img.shields.io/badge/1-59636e?style=flat&amp;logo=github"></a> |

</details>

<details open>
<summary><b>Perception Foundations › Data Augmentation</b> · 1 resource</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Diverse Instance Generation (Diffusion)** | 2025 · GRSL | <a href="https://arxiv.org/abs/2511.18031"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | — | — | — |

</details>

<details open>
<summary><b>Perception Foundations › Cross-Modal Retrieval</b> · 3 resources</summary>

| Resource | Year / Venue | Paper | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **SAN (Scene-aware Aggregation)** | 2023 · ICMR | <a href="https://doi.org/10.1145/3591106.3592236"><img alt="Paper: DOI" width="49" height="20" src="https://img.shields.io/badge/DOI-4051b5?style=flat&amp;logo=doi"></a> | <a href="https://pan.baidu.com/s/1qDSdcvm6as2rKmAmC_86VA?pwd=86a2"><img alt="Weights: Baidu" width="62" height="20" src="https://img.shields.io/badge/Baidu-1677ff?style=flat&amp;logo=baidu"></a> | <a href="https://github.com/jaychempan/SWAN"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/jaychempan/SWAN/stargazers"><img alt="Stars: 37" width="46" height="20" src="https://img.shields.io/badge/37-59636e?style=flat&amp;logo=github"></a> |
| **PiR (Prior Instruction Representation)** | 2024 · arXiv | <a href="https://arxiv.org/abs/2405.10160"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> | <a href="https://pan.baidu.com/s/1urfZ_64DFRelAQz-LYkcCQ?pwd=2v3v"><img alt="Weights: Baidu" width="62" height="20" src="https://img.shields.io/badge/Baidu-1677ff?style=flat&amp;logo=baidu"></a> | <a href="https://github.com/jaychempan/PriorCLIP"><img alt="Code: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> | <a href="https://github.com/jaychempan/PriorCLIP/stargazers"><img alt="Stars: 30" width="46" height="20" src="https://img.shields.io/badge/30-59636e?style=flat&amp;logo=github"></a> |
| **DOVE (Direction-Oriented Embedding)** | 2024 · TGRS | <a href="https://doi.org/10.1109/TGRS.2024.3392779"><img alt="Paper: DOI" width="49" height="20" src="https://img.shields.io/badge/DOI-4051b5?style=flat&amp;logo=doi"></a> | — | — | — |

</details>

<!-- AUTO_ECOSYSTEM_END -->

<a id="4-multimodal-datasets-and-benchmarks"></a>
## 4. Multimodal datasets and benchmarks

Following the paper's distinction, **general-purpose multimodal datasets** provide supervision for representation learning and transfer, while **task-oriented benchmarks** define capability-specific inputs, outputs, and evaluation protocols. The table keeps both resource types searchable without treating dataset scale as evidence of reasoning quality.

<!-- AUTO_DATASETS_START -->

| Resource | Year / Type | Purpose | Access |
| :---: | :---: | :---: | :---: |
| **Delta-QA**<br><sub>with Delta-LLaVA</sub> | 2026 · Change-QA benchmark | Bi-temporal visual question answering | <a href="https://arxiv.org/abs/2604.14044"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **DisasterInsight**<br><sub>with Disaster-response VLMs</sub> | 2026 · Benchmark | Disaster scene reasoning | <a href="https://arxiv.org/abs/2601.18493"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **EarthVLSet**<br><sub>with EarthVL</sub> | 2026 · Dataset + benchmark | Earth vision-language understanding | <a href="https://huggingface.co/datasets/Kingdrone-Junjue/EarthVLSet"><img alt="Data: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> |
| **GTPBD-MM**<br><sub>with Reasoning VLMs</sub> | 2026 · Multimodal benchmark | Terraced parcel and boundary understanding | <a href="https://arxiv.org/abs/2604.12315"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **GeoChrono-Data**<br><sub>with GeoChrono</sub> | 2026 · Benchmark + instruction | Long-term temporal understanding | <a href="https://huggingface.co/datasets/Davidup1/GeoChrono-Data"><img alt="Data: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> |
| **GeoHeight-Bench**<br><sub>with GeoHeightChat</sub> | 2026 · Reasoning benchmark | Height-aware multimodal reasoning | <a href="https://arxiv.org/abs/2603.25565"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **GeoMMBench**<br><sub>with GeoMMAgent</sub> | 2026 · Multimodal benchmark | Geoscience and remote-sensing multimodal understanding | <a href="https://arxiv.org/abs/2604.08896"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **GeoReason-Bench**<br><sub>with GeoReason</sub> | 2026 · Reasoning benchmark | Logical consistency reasoning | <a href="https://huggingface.co/datasets/WenshuaiLi/GeoReason-Bench"><img alt="Data: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> |
| **GeoSeg-Bench**<br><sub>with UniGeoSeg</sub> | 2026 · Segmentation benchmark | Open-world geospatial segmentation | <a href="https://huggingface.co/datasets/nishuo1999/GeoSeg-Bench"><img alt="Data: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> |
| **GroundSet**<br><sub>with Grounding VLMs</sub> | 2026 · Grounding benchmark | Cadastral-grounded spatial understanding | <a href="https://arxiv.org/abs/2603.14609"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **HM-Bench**<br><sub>with Reasoning VLMs</sub> | 2026 · Reasoning benchmark | Hyperspectral multimodal reasoning | <a href="https://arxiv.org/abs/2604.08884"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **ME-RSRG**<br><sub>with EAR</sub> | 2026 · Reasoning-grounding benchmark | Multi-entity reasoning and grounding | <a href="https://github.com/CV-ShuchangLyu/ME-RSRG"><img alt="Data: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> |
| **MMRS-OneVision**<br><sub>with Earth-OneVision</sub> | 2026 · Instruction dataset | Multi-sensor and multi-task instruction tuning | <a href="https://arxiv.org/abs/2606.10819"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **NeSy-Route**<br><sub>with GeoSolver</sub> | 2026 · Neuro-symbolic benchmark | Constrained route planning | <a href="https://arxiv.org/abs/2603.16307"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **OmniEarth**<br><sub>with Remote-sensing VLMs</sub> | 2026 · Multimodal benchmark | Multi-task Earth observation evaluation | <a href="https://arxiv.org/abs/2603.09471"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **RSFG-100k**<br><sub>with GeoAlignCLIP</sub> | 2026 · Alignment dataset | Fine-grained region-text alignment | <a href="https://arxiv.org/abs/2603.09566"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **RSME-Bench**<br><sub>with SkyNative</sub> | 2026 · Reasoning benchmark | Multi-entity remote-sensing reasoning | <a href="https://arxiv.org/abs/2605.17949"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **RSRCC**<br><sub>with Change-reasoning models</sub> | 2026 · Change-reasoning benchmark | Reasoning over bi-temporal change | <a href="https://arxiv.org/abs/2604.20623"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **TerraBench**<br><sub>with TerraAgent</sub> | 2026 · Agent benchmark | Executable Earth-data workflows | <a href="https://arxiv.org/abs/2606.13148"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **UHR-CoZ**<br><sub>with GeoEyes</sub> | 2026 · Ultra-high-resolution benchmark | Active zooming and compositional reasoning | <a href="https://github.com/nanocm/GeoEyes"><img alt="Data: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> |
| **UHR-Micro**<br><sub>with MAP-Agent</sub> | 2026 · Ultra-high-resolution benchmark | Small-object perception and reasoning | <a href="https://arxiv.org/abs/2605.12237"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **VLRS-Bench**<br><sub>with Remote-sensing VLMs</sub> | 2026 · Vision-language benchmark | Comprehensive vision-language reasoning | <a href="https://arxiv.org/abs/2602.07045"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **DisasterM3**<br><sub>with Disaster-response VLMs</sub> | 2025 · Dataset + benchmark | Multimodal multi-hazard understanding | <a href="https://arxiv.org/abs/2505.21089"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **EarthReason**<br><sub>with SegEarth-R1</sub> | 2025 · Dataset + benchmark | Geospatial pixel reasoning | <a href="https://huggingface.co/datasets/earth-insights/EarthReason"><img alt="Data: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> |
| **FINERS-4k**<br><sub>with FineRS (FINERS)</sub> | 2025 · Reasoning-segmentation dataset | Fine-grained small-object reasoning and segmentation | <a href="https://iiau-zhanglu.github.io/FINERS/"><img alt="Project: Website" width="72" height="20" src="https://img.shields.io/badge/Website-16858a?style=flat"></a> |
| **GAIA**<br><sub>with General-purpose VLMs</sub> | 2025 · Instruction dataset | Geospatial instruction alignment | <a href="https://arxiv.org/abs/2502.09598"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **Git-10M**<br><sub>with Text2Earth</sub> | 2025 · Pretraining dataset | Global text-to-Earth generation | <a href="https://huggingface.co/datasets/lcybuaa/Git-10M"><img alt="Data: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> |
| **KnowFlow-Bench**<br><sub>with CangLing-KnowFlow</sub> | 2025 · Agent benchmark | Workflow generation and execution | <a href="https://cangling-agent.github.io/KnowFlow/"><img alt="Project: Website" width="72" height="20" src="https://img.shields.io/badge/Website-16858a?style=flat"></a> |
| **LAE-1M**<br><sub>with LAE-DINO</sub> | 2025 · Pretraining dataset | Language-aware object detection | <a href="https://huggingface.co/datasets/ML4Sustain/LAE-1M"><img alt="Data: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> |
| **LaSeRS**<br><sub>with SegEarth-R2</sub> | 2025 · Reasoning benchmark | Complex-instruction segmentation | <a href="https://huggingface.co/datasets/earth-insights/LaSeRS"><img alt="Data: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> |
| **Landsat30-AU**<br><sub>with General-purpose VLMs</sub> | 2025 · Multimodal dataset | Global Landsat image-text understanding | <a href="https://arxiv.org/abs/2508.03127"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **RemoteSAM270k**<br><sub>with RemoteSAM</sub> | 2025 · Instruction dataset | Segmentation and recognition | <a href="https://huggingface.co/datasets/1e12Leon/RemoteSAM270k"><img alt="Data: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> |
| **SAR-TEXT**<br><sub>with SAR VLMs</sub> | 2025 · Image-text dataset | SAR image-language alignment | <a href="https://arxiv.org/abs/2507.18743"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **SARLANG-1M**<br><sub>with SAR VLMs</sub> | 2025 · Pretraining dataset | Million-scale SAR-language pretraining | <a href="https://arxiv.org/abs/2504.03254"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **TEOChatlas**<br><sub>with TEOChat</sub> | 2025 · Temporal dataset | Temporal Earth observation dialogue | <a href="https://huggingface.co/datasets/jirvin16/TEOChatlas"><img alt="Data: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> |
| **BigEarthNet-MM**<br><sub>with General-purpose VLMs</sub> | 2024 · Multimodal pretraining dataset | Multispectral image-text representation | <a href="https://arxiv.org/abs/2404.07043"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **BigEarthNet.txt**<br><sub>with General-purpose VLMs</sub> | 2024 · Caption dataset | Multilingual Earth-observation descriptions | <a href="https://arxiv.org/abs/2603.29630"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **ChatEarthNet**<br><sub>with ChatEarthNet</sub> | 2024 · Instruction dataset | Earth-observation dialogue and instruction tuning | <a href="https://arxiv.org/abs/2402.11325"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **FIT-RS**<br><sub>with SkySenseGPT</sub> | 2024 · Instruction dataset | Fine-grained remote-sensing tasks | <a href="https://huggingface.co/datasets/ll-13/FIT-RS"><img alt="Data: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> |
| **GeoChat-Instruct**<br><sub>with GeoChat</sub> | 2024 · Instruction dataset | Grounded remote-sensing dialogue | <a href="https://huggingface.co/datasets/MBZUAI/GeoChat_Instruct"><img alt="Data: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> |
| **LuoJiaHOG**<br><sub>with General-purpose VLMs</sub> | 2024 · Multimodal dataset | Remote-sensing vision-language understanding | <a href="https://arxiv.org/abs/2403.10887"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **REO-Instruct**<br><sub>with REO-VLM</sub> | 2024 · Instruction dataset | Continuous Earth-observation regression | <a href="https://github.com/REO-VLM-anonymous/REO-VLM"><img alt="Data: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> |
| **RS5M**<br><sub>with GeoRSCLIP</sub> | 2024 · Pretraining dataset | Remote-sensing image-text alignment | <a href="https://huggingface.co/datasets/omlab/RS5M"><img alt="Data: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> |
| **SkyEye-968k**<br><sub>with SkyEyeGPT</sub> | 2024 · Instruction dataset | Multi-task remote-sensing instruction | <a href="https://huggingface.co/datasets/ZhanYang-nwpu/SkyEye-968k"><img alt="Data: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> |
| **SkyScript**<br><sub>with RemoteCLIP</sub> | 2024 · Pretraining dataset | Large-scale image-text alignment | <a href="https://arxiv.org/abs/2312.11029"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **VRSBench**<br><sub>with General-purpose VLMs</sub> | 2024 · Dataset + benchmark | Captioning VQA and grounding | <a href="https://github.com/lzw-lzw/VRSBench"><img alt="Data: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> |
| **refGeo**<br><sub>with GeoGround</sub> | 2024 · Grounding dataset | Multi-format visual grounding | <a href="https://huggingface.co/datasets/erenzhou/refGeo"><img alt="Data: Hugging Face" width="103" height="20" src="https://img.shields.io/badge/Hugging%20Face-f4b400?style=flat&amp;logo=huggingface"></a> |
| **RSICap**<br><sub>with RSGPT</sub> | 2023 · Caption dataset | Remote-sensing image captioning | <a href="https://arxiv.org/abs/2307.15266"><img alt="Paper: arXiv" width="57" height="20" src="https://img.shields.io/badge/arXiv-b31b1b?style=flat&amp;logo=arxiv"></a> |
| **SECOND-CC**<br><sub>with Change-captioning models</sub> | 2023 · Change-caption dataset | Semantic change description | <a href="https://github.com/Chen-Yang-Liu/RSICC"><img alt="Data: GitHub" width="69" height="20" src="https://img.shields.io/badge/GitHub-24292f?style=flat&amp;logo=github"></a> |

<!-- AUTO_DATASETS_END -->

<a id="5-repository-scope-and-maintenance"></a>
## 5. Repository scope and maintenance

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
