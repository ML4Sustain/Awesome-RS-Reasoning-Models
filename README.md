<p align="center">
  <img src="assets/header.svg" alt="Awesome Remote Sensing Reasoning" width="100%">
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <a href="https://github.com/ML4Sustain/Awsome-RS-Reasoning-Models/actions"><img src="https://img.shields.io/github/actions/workflow/status/ML4Sustain/Awsome-RS-Reasoning-Models/catalog.yml?label=catalog&amp;style=flat-square" alt="Catalog status"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/contributions-welcome-39b54a?style=flat-square" alt="Contributions welcome"></a>
  <a href="LICENSE-DATA"><img src="https://img.shields.io/badge/data-CC_BY_4.0-ef9421?style=flat-square" alt="CC BY 4.0"></a>
</p>

<p align="center">
  <a href="#-radar">Radar</a> •
  <a href="#-resource-index">Resource index</a> •
  <a href="#-datasets--benchmarks">Datasets</a> •
  <a href="#-update-the-index">Update</a> •
  <a href="#-contributing">Contribute</a>
</p>

## The signal

Remote sensing is moving from recognizing **what is where** to establishing **why a conclusion follows from evidence**. This independent index tracks that transition across models, datasets, benchmarks, and executable agents.

> **RS-Reasoning** is task-dependent, multi-step inference that combines Earth observation evidence with geographic, temporal, or domain constraints and exposes an auditable support structure.

Entries link directly to their original paper and verified official code. Repository popularity is stored as a dated snapshot in this repository, never inferred from a transient live badge.

## 🧭 Radar

| 01 · 🧩 Supervised | 02 · 🎯 Reinforcement | 03 · 🛠️ Agentic |
| --- | --- | --- |
| Learns from rationales, traces, masks, or structured intermediate supervision. | Optimizes answer, grounding, consistency, or process rewards. | Plans and executes tools, retrieval, GIS operations, or multi-step workflows. |
| **Observe:** answer + trace | **Observe:** reward + evidence | **Observe:** action + trajectory |

The tracks sit on top of enabling datasets and vision-language models, and support four application clusters from the survey:

`urban & social space` · `disaster assessment` · `environmental monitoring` · `spatiotemporal QA`

## 📡 Index pulse

<!-- AUTO_DASHBOARD_START -->

| 🌍 Methods & models | 🧠 Reasoning | 🗃️ Data / benches | 💻 Official repos | 📦 Weights | 🔁 MS mirrors |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **79** | **30** | **14** | **63** | **43** | **11** |

#### Most starred official repositories

| Resource | Category | Repository | Stored stars |
| :---: | :---: | :---: | :---: |
| RemoteCLIP | Contrastive VLMs | [Code](https://github.com/ChenDelong1999/RemoteCLIP) | ⭐ 587 |
| Falcon | Generative Large VLMs | [Code](https://github.com/TianHuiLab/Falcon) | ⭐ 382 |
| SatCLIP | Contrastive VLMs | [Code](https://github.com/microsoft/satclip) | ⭐ 373 |
| GeoRSCLIP | Contrastive VLMs | [Code](https://github.com/om-ai-lab/RS5M) | ⭐ 314 |
| LAE-DINO | Task-Specific VLMs | [Code](https://github.com/jaychempan/LAE-DINO) | ⭐ 286 |

<!-- AUTO_DASHBOARD_END -->

<details>
<summary><b>View the publication timeline</b></summary>

<p align="center"><img src="assets/timeline.svg" alt="Timeline of remote sensing reasoning models" width="100%"></p>

</details>

## 📚 Resource index

The complete reasoning core: 30 models across supervised, reinforcement-driven, and agentic/tool-augmented tracks. Sorted by stored GitHub Stars inside each track.

<!-- AUTO_CATALOG_START -->

<details>
<summary><b>Reasoning Models › Supervised Reasoning</b> · 6 resources</summary>

| Resource | Year / Venue | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: |
| **SegEarth-R1** | 2025 · arXiv | [HuggingFace](https://huggingface.co/earth-insights/SegEarth-R1-EarthReason) · [ModelScope](https://modelscope.cn/models/earth-insights/SegEarth-R1-EarthReason) | [Code](https://github.com/earth-insights/SegEarth-R1) | ⭐ 156 |
| **TerraScope** | 2026 · CVPR | [HuggingFace](https://huggingface.co/sy1998/TerraScope) · [ModelScope](https://modelscope.cn/models/shuyanshuyan/terrascope) | [Code](https://github.com/shuyansy/Earth-Observation-VLMs) | ⭐ 138 |
| **SegEarth-R2** | 2025 · arXiv | — | [Code](https://github.com/earth-insights/SegEarth-R2) | ⭐ 68 |
| **EarthVL** | 2026 · arXiv | — | [Code](https://github.com/Junjue-Wang/EarthVL) | ⭐ 43 |
| **GeoChrono** | 2026 · arXiv | [HuggingFace](https://huggingface.co/Davidup1/GeoChrono) · [ModelScope](https://modelscope.cn/models/Davidup1/GeoChrono) | [Code](https://github.com/IntelliSensing/GeoChrono) | ⭐ 9 |
| **Delta-LLaVA** | 2026 · arXiv | — | — | — |

</details>

<details>
<summary><b>Reasoning Models › RL-Driven Reasoning</b> · 15 resources</summary>

| Resource | Year / Venue | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: |
| **RSThinker** | 2026 · ICLR | [HuggingFace](https://huggingface.co/minglanga/RSThinker) | [Code](https://github.com/minglangL/RSThinker) | ⭐ 38 |
| **GeoVLM-R1** | 2025 · arXiv | — | [Code](https://github.com/mustansarfiaz/GeoVLM-R1-Toolkit) | ⭐ 32 |
| **RS-EoT** | 2026 · CVPR | [HuggingFace](https://huggingface.co/ShaoRun/RS-EoT-7B) · [Project Website](https://geox-lab.github.io/Asking_like_Socrates/) | [Code](https://github.com/GeoX-Lab/Asking_like_Socrates) | ⭐ 26 |
| **GeoZero** | 2025 · arXiv | [HuggingFace](https://huggingface.co/hjvsl/GeoZero) · [Baidu NetDisk](https://pan.baidu.com/s/1nJjBwO4UlVv4GFl60gjM3w?pwd=15gn) | [Code](https://github.com/MiliLab/GeoZero) | ⭐ 26 |
| **RemoteAgent** | 2026 · arXiv | — | [Code](https://github.com/1e12Leon/RemoteAgent) | ⭐ 20 |
| **RemoteReasoner** | 2025 · arXiv | [HuggingFace](https://huggingface.co/1e12Leon/RemoteReasoner) · [ModelScope](https://modelscope.cn/models/AIMGroup/RemoteReasoner) | [Code](https://github.com/1e12Leon/RemoteReasoner) | ⭐ 17 |
| **Geo-R1** | 2025 · arXiv | [HuggingFace](https://huggingface.co/Geo-R1) | [Code](https://github.com/Geo-R1/geo-r1) | ⭐ 16 |
| **TinyRS-R1** | 2025 · arXiv | [HuggingFace](https://huggingface.co/aybora/Qwen2-VL-TinyRS-R1) | [Code](https://github.com/aybora/TinyRS) | ⭐ 13 |
| **GeoReason** | 2026 · arXiv | [HuggingFace](https://huggingface.co/WenshuaiLi/GeoReason) | [Code](https://github.com/canlanqianyan/GeoReason) | ⭐ 10 |
| **GeoVista** | 2026 · arXiv | [HuggingFace](https://huggingface.co/ryan6073/GeoVista-7B-Instruct) · [HuggingFace](https://huggingface.co/ryan6073/GeoVista-7B-Preview) | [Code](https://github.com/ryan6073/GeoVista) | ⭐ 10 |
| **Geo-R** | 2026 · arXiv | — | [Code](https://github.com/aialt/geo-r) | ⭐ 3 |
| **GeoSolver** | 2026 · arXiv | [HuggingFace](https://huggingface.co/minglanga/GeoSolver) | [Code](https://github.com/minglangL/GeoSolver) | ⭐ 3 |
| **RemoteZero** | 2026 · arXiv | — | [Code](https://github.com/1e12Leon/RemoteZero) | ⭐ 1 |
| **RS-HyRe-R1** | 2026 · arXiv | [HuggingFace](https://huggingface.co/geozgz/RS-HyRe-R1) | [Code](https://github.com/GeoX-Lab/RS-HyRe-R1) | ⭐ 1 |
| **GeoX** | 2026 · arXiv | — | — | — |

</details>

<details>
<summary><b>Reasoning Models › Agentic / Tool-Augmented Reasoning</b> · 9 resources</summary>

| Resource | Year / Venue | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: |
| **Earth-Agent** | 2026 · ICLR | — | [Code](https://github.com/opendatalab/Earth-Agent) | ⭐ 194 |
| **OpenEarthAgent** | 2026 · ECCV | [HuggingFace](https://huggingface.co/MBZUAI/OpenEarthAgent) · [ModelScope](https://modelscope.cn/models/MBZUAI/OpenEarthAgent) | [Code](https://github.com/mbzuai-oryx/OpenEarthAgent) | ⭐ 95 |
| **GeoMMAgent** | 2026 · CVPR | — | [Code](https://github.com/Shihao-Cheng/GeoMMAgent) | ⭐ 49 |
| **EarthAgent** | 2025 · arXiv | — | [Code](https://github.com/earth-insights/EarthAgent) | ⭐ 13 |
| **TerraAgent** | 2026 · arXiv | — | [Code](https://github.com/Takerdat23/TerraBench) | ⭐ 4 |
| **MAP-Agent** | 2026 · arXiv | — | [Code](https://github.com/MiliLab/UHR-Micro) | ⭐ 1 |
| **PMMC** | 2026 · arXiv | — | — | — |
| **Earth AI** | 2025 · arXiv | — | — | — |
| **VRA** | 2025 · arXiv | — | — | — |

</details>

<!-- AUTO_CATALOG_END -->

## 🌍 Extended ecosystem

Beyond the 30-model reasoning core, this index tracks 49 enabling resources: vision-language foundations, ultra-high-resolution models, generation, detection, segmentation, augmentation, and retrieval. Expand only the category you need.

<!-- AUTO_ECOSYSTEM_START -->

<details>
<summary><b>Vision-Language Models › Contrastive VLMs</b> · 6 resources</summary>

| Resource | Year / Venue | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: |
| **RemoteCLIP** | 2024 · TGRS | [HuggingFace](https://huggingface.co/chendelong/RemoteCLIP) | [Code](https://github.com/ChenDelong1999/RemoteCLIP) | ⭐ 587 |
| **SatCLIP** | 2024 · arXiv | [HuggingFace](https://huggingface.co/microsoft/SatCLIP-ViT16-L40) · [ModelScope](https://modelscope.cn/models/microsoft/SatCLIP-ViT16-L40) | [Code](https://github.com/microsoft/satclip) | ⭐ 373 |
| **GeoRSCLIP** | 2024 · TGRS | [HuggingFace](https://huggingface.co/Zilun/GeoRSCLIP) | [Code](https://github.com/om-ai-lab/RS5M) | ⭐ 314 |
| **DGTRS-CLIP** | 2025 · arXiv | [HuggingFace](https://huggingface.co/MitsuiChen14/DGTRS-CLIP-ViT-L-14) · [HuggingFace](https://huggingface.co/MitsuiChen14/DGTRS-CLIP-ViT-B-16) | [Code](https://github.com/MitsuiChen14/DGTRS) | ⭐ 32 |
| **PriorCLIP** | 2023 · MM | [Baidu NetDisk](https://pan.baidu.com/s/1urfZ_64DFRelAQz-LYkcCQ?pwd=2v3v) | [Code](https://github.com/jaychempan/PriorCLIP) | ⭐ 30 |
| **TimeSenCLIP** | 2025 · arXiv | [HuggingFace](https://huggingface.co/pallavijainpj/TimeSenCLIP) | — | — |

</details>

<details>
<summary><b>Vision-Language Models › Generative Large VLMs</b> · 13 resources</summary>

| Resource | Year / Venue | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: |
| **GeoChat** | 2024 · CVPR | [HuggingFace](https://huggingface.co/MBZUAI/geochat-7B) · [ModelScope](https://modelscope.cn/models/MBZUAI/geochat-7B) | [Code](https://github.com/mbzuai-oryx/GeoChat) | ⭐ 743 |
| **Falcon** | 2025 · arXiv | [HuggingFace](https://huggingface.co/TianHuiLab/Falcon-Single-Instruction-Large) | [Code](https://github.com/TianHuiLab/Falcon) | ⭐ 382 |
| **LHRS-Bot** | 2024 · ECCV | [Google Drive](https://drive.google.com/drive/folders/1dzWTE1k935MjMVnfLtTJiIqw7yCj-e3m?usp=drive_link) · [Baidu NetDisk](https://pan.baidu.com/s/1n1h_ZImeKTgvoNHjr5bq3Q?pwd=qhqw) | [Code](https://github.com/NJU-LHRS/LHRS-Bot) | ⭐ 194 |
| **EarthGPT** | 2024 · TGRS | — | [Code](https://github.com/wivizhang/EarthGPT) | ⭐ 160 |
| **RSGPT** | 2025 · ISPRS | — | [Code](https://github.com/Lavender105/RSGPT) | ⭐ 150 |
| **TEOChat** | 2025 · ICLR | [HuggingFace](https://huggingface.co/jirvin16/TEOChat) | [Code](https://github.com/ermongroup/TEOChat) | ⭐ 150 |
| **SkySenseGPT** | 2024 · arXiv | [HuggingFace](https://huggingface.co/ll-13/SkySenseGPT-7B-CLIP-ViT) | [Code](https://github.com/Luo-Z13/SkySense-Chat) | ⭐ 149 |
| **SkyEyeGPT** | 2025 · ISPRS | [HuggingFace](https://huggingface.co/ZhanYang-nwpu/SkyEyeGPT) | [Code](https://github.com/ZhanYang-nwpu/SkyEyeGPT) | ⭐ 139 |
| **RSUniVLM** | 2024 · arXiv | [Google Drive](https://drive.google.com/drive/folders/1TtaoOPmh167gpgHHWRNBMCaA7t_XZ4Vg?usp=sharing) | [Code](https://github.com/xuliu-cyber/RSUniVLM) | ⭐ 47 |
| **EarthMarker** | 2024 · TGRS | — | [Code](https://github.com/wivizhang/EarthMarker) | ⭐ 46 |
| **Earth-OneVision** | 2026 · arXiv | — | — | — |
| **SkyNative** | 2026 · arXiv | — | — | — |
| **RingMoGPT** | 2024 · TGRS | — | — | — |

</details>

<details>
<summary><b>Vision-Language Models › Task-Specific VLMs</b> · 13 resources</summary>

| Resource | Year / Venue | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: |
| **LAE-DINO** | 2025 · AAAI | [HuggingFace](https://huggingface.co/ML4Sustain/LAE-DINO) · [ModelScope](https://modelscope.cn/models/ML4Sustain/LAE-DINO) | [Code](https://github.com/jaychempan/LAE-DINO) | ⭐ 286 |
| **RemoteSAM** | 2025 · MM | [HuggingFace](https://huggingface.co/1e12Leon/RemoteSAM) | [Code](https://github.com/1e12Leon/RemoteSAM) | ⭐ 246 |
| **EarthMind** | 2025 · arXiv | [HuggingFace](https://huggingface.co/sy1998/EarthMind-4B) | [Code](https://github.com/shuyansy/Earth-Observation-VLMs) | ⭐ 138 |
| **InstructSAM** | 2025 · NeurIPS | — | [Code](https://github.com/VoyagerXvoyagerx/InstructSAM) | ⭐ 117 |
| **GeoGround** | 2024 · arXiv | [HuggingFace](https://huggingface.co/erenzhou/GeoGround) · [ModelScope](https://modelscope.cn/models/zytx121/geoground) | [Code](https://github.com/VisionXLab/GeoGround) | ⭐ 94 |
| **CastDet** | 2024 · ECCV | — | [Code](https://github.com/VisionXLab/CastDet) | ⭐ 85 |
| **UniGeoSeg** | 2026 · CVPR | [HuggingFace](https://huggingface.co/nishuo1999/UniGeoSeg) | [Code](https://github.com/MiliLab/UniGeoSeg) | ⭐ 42 |
| **OpenRSD** | 2025 · ICCV | [Baidu NetDisk](https://pan.baidu.com/s/1sV3GHgneC3dQskIaYABefg?pwd=aan9) | [Code](https://github.com/floatingstarZ/OpenRSD) | ⭐ 42 |
| **RSVG-ZeroOV** | 2026 · AAAI | — | [Code](https://github.com/like413/RSVG-ZeroOV) | ⭐ 26 |
| **LLaMA-Unidetector** | 2025 · TGRS | [Google Drive](https://drive.google.com/file/d/1AwUn5EebmmLBo7njjW_Ng1q9zDrqkNbB/view) · [Baidu NetDisk](https://pan.baidu.com/s/1P3pW3euqqxYVZQvw-is1vQ?pwd=1234) | [Code](https://github.com/ChloeeGrace/LLaMA-Unidetector) | ⭐ 15 |
| **Cross-View OVD** | 2025 · arXiv | — | — | — |
| **FASE** | 2025 · CIKM | — | — | — |
| **GeoMag** | 2025 · MM | — | — | — |

</details>

<details>
<summary><b>Related RS Models › Ultra-High-Resolution VLMs</b> · 3 resources</summary>

| Resource | Year / Venue | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: |
| **GeoLLaVA-8K** | 2025 · NeurIPS | [HuggingFace](https://huggingface.co/initiacms/GeoLLaVA-8K) | [Code](https://github.com/MiliLab/GeoLLaVA-8K) | ⭐ 55 |
| **ZoomEarth** | 2026 · CVPR | [HuggingFace](https://huggingface.co/HappyBug/ZoomEarth-3B) | [Code](https://github.com/earth-insights/ZoomEarth) | ⭐ 45 |
| **Zoom-RS (Look Where It Matters)** | 2025 · arXiv | — | [Code](https://github.com/kiki-zyq/ZoomSearch) | ⭐ 27 |

</details>

<details>
<summary><b>Related RS Models › Generation Models</b> · 2 resources</summary>

| Resource | Year / Venue | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: |
| **Text2Earth** | 2025 · GRSM | [HuggingFace](https://huggingface.co/lcybuaa/Text2Earth) · [ModelScope](https://modelscope.cn/models/lcybuaa1111/Text2Earth) | [Code](https://github.com/Chen-Yang-Liu/Text2Earth) | ⭐ 187 |
| **Earthsynth** | 2025 · arXiv | [HuggingFace](https://huggingface.co/jaychempan/EarthSynth) · [ModelScope](https://modelscope.cn/models/ML4Sustain/EarthSynth) | [Code](https://github.com/jaychempan/EarthSynth) | ⭐ 60 |

</details>

<details>
<summary><b>Perception Models › Object Detection</b> · 6 resources</summary>

| Resource | Year / Venue | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: |
| **CalNet** | 2023 · MM | [Baidu NetDisk](https://pan.baidu.com/s/1PnmdKqIxPnTgK6yQ6WfwpA) | [Code](https://github.com/hexiao0275/CALNet-Dronevehicle) | ⭐ 68 |
| **Enhance-then-Search (AugSearch)** | 2025 · CVPR | [Baidu NetDisk](https://pan.baidu.com/s/17wECMZ7X-wkFMXSCQ_SvAw?pwd=ttue) | [Code](https://github.com/jaychempan/ETS) | ⭐ 57 |
| **S2A-Det** | 2023 · TGRS | — | [Code](https://github.com/hexiao0275/S2ADet) | ⭐ 51 |
| **LCMA** | 2026 · Electronics | — | [Code](https://github.com/hexiao0275/LCMA_RGBT) | ⭐ 2 |
| **SDCM** | 2025 · TMM | — | — | — |
| **Semantic-Aware Ship Detection** | 2025 · IGARSS | — | — | — |

</details>

<details>
<summary><b>Perception Models › Semantic Segmentation</b> · 2 resources</summary>

| Resource | Year / Venue | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: |
| **Rethinking Transformers (RS Segmentation)** | 2023 · TGRS | [Google Drive](https://drive.google.com/file/d/1yV070cXTrkCN2FTHKM2DIXI_dtVjaTJ6/view) | [Code](https://github.com/lyhnsn/GLOTS) | ⭐ 17 |
| **Multilevel Multimodal Fusion Transformer** | 2024 · TGRS | — | [Code](https://github.com/yida12345/FTransUNet) | ⭐ 1 |

</details>

<details>
<summary><b>Perception Models › Data Augmentation</b> · 1 resources</summary>

| Resource | Year / Venue | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: |
| **Diverse Instance Generation (Diffusion)** | 2025 · GRSL | — | — | — |

</details>

<details>
<summary><b>Perception Models › Cross-Modal Retrieval</b> · 3 resources</summary>

| Resource | Year / Venue | Weights / Data | Official code | Stars |
| :---: | :---: | :---: | :---: | :---: |
| **SAN (Scene-aware Aggregation)** | 2023 · ICMR | [Baidu NetDisk](https://pan.baidu.com/s/1qDSdcvm6as2rKmAmC_86VA?pwd=86a2) | [Code](https://github.com/jaychempan/SWAN) | ⭐ 37 |
| **PiR (Prior Instruction Representation)** | 2024 · arXiv | [Baidu NetDisk](https://pan.baidu.com/s/1urfZ_64DFRelAQz-LYkcCQ?pwd=2v3v) | [Code](https://github.com/jaychempan/PriorCLIP) | ⭐ 30 |
| **DOVE (Direction-Oriented Embedding)** | 2024 · TGRS | — | — | — |

</details>

<!-- AUTO_ECOSYSTEM_END -->

## 🗃️ Datasets & benchmarks

Standalone training, instruction, grounding, temporal, segmentation, and reasoning resources extracted from verified release links in the ecosystem audit.

<!-- AUTO_DATASETS_START -->

| Dataset / benchmark | Type | Companion model | Focus | Access |
| :---: | :---: | :---: | :---: | :---: |
| [**EarthVLSet**](https://huggingface.co/datasets/Kingdrone-Junjue/EarthVLSet) | Dataset + benchmark | EarthVL | Earth vision-language understanding | HuggingFace · Open |
| [**GeoChrono-Data**](https://huggingface.co/datasets/Davidup1/GeoChrono-Data) | Benchmark + instruction | GeoChrono | Long-term temporal understanding | HuggingFace · Open |
| [**GeoReason-Bench**](https://huggingface.co/datasets/WenshuaiLi/GeoReason-Bench) | Reasoning benchmark | GeoReason | Logical consistency reasoning | HuggingFace · Open |
| [**GeoSeg-Bench**](https://huggingface.co/datasets/nishuo1999/GeoSeg-Bench) | Segmentation benchmark | UniGeoSeg | Open-world geospatial segmentation | HuggingFace · Open |
| [**EarthReason**](https://huggingface.co/datasets/earth-insights/EarthReason) | Dataset + benchmark | SegEarth-R1 | Geospatial pixel reasoning | HuggingFace · Open |
| [**LAE-1M**](https://huggingface.co/datasets/ML4Sustain/LAE-1M) | Pretraining dataset | LAE-DINO | Language-aware object detection | HuggingFace · Open |
| [**LaSeRS**](https://huggingface.co/datasets/earth-insights/LaSeRS) | Reasoning benchmark | SegEarth-R2 | Complex-instruction segmentation | HuggingFace · Open |
| [**RemoteSAM270k**](https://huggingface.co/datasets/1e12Leon/RemoteSAM270k) | Instruction dataset | RemoteSAM | Segmentation and recognition | HuggingFace · Open |
| [**TEOChatlas**](https://huggingface.co/datasets/jirvin16/TEOChatlas) | Temporal dataset | TEOChat | Temporal Earth observation dialogue | HuggingFace · Open |
| [**FIT-RS**](https://huggingface.co/datasets/ll-13/FIT-RS) | Instruction dataset | SkySenseGPT | Fine-grained remote-sensing tasks | HuggingFace · Open |
| [**GeoChat-Instruct**](https://huggingface.co/datasets/MBZUAI/GeoChat_Instruct) | Instruction dataset | GeoChat | Grounded remote-sensing dialogue | HuggingFace · Open |
| [**RS5M**](https://huggingface.co/datasets/omlab/RS5M) | Pretraining dataset | GeoRSCLIP | Remote-sensing image-text alignment | HuggingFace · Open |
| [**SkyEye-968k**](https://huggingface.co/datasets/ZhanYang-nwpu/SkyEye-968k) | Instruction dataset | SkyEyeGPT | Multi-task remote-sensing instruction | HuggingFace · Open |
| [**refGeo**](https://huggingface.co/datasets/erenzhou/refGeo) | Grounding dataset | GeoGround | Multi-format visual grounding | HuggingFace · Open |

<!-- AUTO_DATASETS_END -->

## 🔍 Curation boundary

A reasoning-specific work should demonstrate:

1. **Composition** — a conclusion combines multiple evidence items or inference steps.
2. **Traceability** — claims or actions link to observations, constraints, or tool outputs.
3. **Process-aware evaluation** — evaluation probes grounding, consistency, calibration, or execution beyond final-answer accuracy.

Perception, semantic alignment, generation, or grounding work remains valuable, but is labeled as an enabling foundation unless it meets these criteria.

## 🔄 Update the index

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
- `data/ecosystem.csv` stores the extended 79-resource model and hosting audit.
- `data/ecosystem_github_stars.json` stores its dated official-repository Star snapshot.
- `data/datasets.csv` stores standalone dataset and benchmark releases.
- README sections between `AUTO_*` markers are generated; editorial sections stay untouched.
- GitHub Actions verifies generated files and refreshes popularity snapshots on a schedule.

## 🤝 Contributing

Corrections and new resources are welcome. Follow [CONTRIBUTING.md](CONTRIBUTING.md), edit [data/survey.csv](data/survey.csv), or open a **Resource submission** issue.

Please include the official code URL and describe what evidence, trace, or tool trajectory makes the work reasoning-specific. Unknown fields should stay empty rather than being guessed.

## 📝 Citation

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

## License

Code is licensed under [MIT](LICENSE); catalog data under [CC BY 4.0](LICENSE-DATA). Linked resources retain their original licenses.

<p align="center"><sub>Maintained as an evidence-first map of reasoning over our planet.</sub></p>
