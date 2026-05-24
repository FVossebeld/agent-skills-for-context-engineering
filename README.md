# Agent Skills for Context Engineering

A Microsoft-native adaptation of the Agent Skills for Context Engineering collection.

The default `context-engineering` package now installs both the core context-engineering skills and the Azure AI / Microsoft Foundry implementation skills. This is not a separate extension layered on afterward. The standard distribution is intended to help agents move from mechanism-level context engineering to Microsoft-native architecture choices by default: Microsoft Foundry Agent Service and Hosted Agents, Foundry IQ, Foundry Toolbox, Azure AI Search, Fabric, Entra identity, Responsible AI guardrails, publishing, and Azure memory/state.

## Install

For Claude Code, copy and run these two commands:

```text
/plugin marketplace add FVossebeld/agent-skills-for-context-engineering
/plugin install context-engineering@context-engineering-marketplace
```

That installs the full standard package: 24 skills, including the Azure and Microsoft-native adaptation skills. There is no separate Azure install step.

For Open Plugins compatible tools, use this manifest URL:

```text
https://raw.githubusercontent.com/FVossebeld/agent-skills-for-context-engineering/main/.plugin/plugin.json
```

For local use or inspection:

```bash
git clone https://github.com/FVossebeld/agent-skills-for-context-engineering.git
```

## What this adaptation does

Context engineering is the discipline of curating everything that enters a model's context window: system prompts, tool definitions, retrieved documents, message history, tool outputs, memory, files, and operating-loop state. The core skills teach the transferable mechanisms. The Azure skills bind those mechanisms to Microsoft products, identity boundaries, deployment surfaces, governance controls, and operational caveats.

Default bias:

1. Prefer Microsoft Foundry Agent Service and Foundry Hosted Agents for managed agent runtimes.
2. Prefer Microsoft Agent Framework or Semantic Kernel for enterprise code-first orchestration.
3. Prefer Foundry Toolbox for curated tool catalogs once a system has more than a small non-overlapping tool set.
4. Prefer Foundry IQ, Azure AI Search, File Search, SharePoint grounding, Fabric Data Agent, Cosmos DB, Blob, and Redis over ad hoc retrieval or memory infrastructure.
5. Prefer Entra ID, managed identity, RBAC, on-behalf-of access, private networking, Azure Monitor, and Responsible AI controls before adding custom governance.

## What gets installed

- 15 core context-engineering and harness-engineering skills under [`skills/`](skills/)
- 9 Microsoft-native implementation skills under [`azure/skills/`](azure/skills/)
- The researcher operating system under [`researcher/`](researcher/) for deterministic gates, mechanism provenance, activation fixtures, and benchmark reporting

The default Claude marketplace manifest is:

```text
.claude-plugin/marketplace.json
```

The default Open Plugins manifest is:

```text
.plugin/plugin.json
```

The older Azure-only manifests remain available as subset install paths for environments that want only Microsoft-native binding skills, but they are no longer the primary distribution contract:

```text
.plugin/plugin.azure.json
.claude-plugin/marketplace.azure.json
```

## Skill map

### Core context and harness skills

| Skill | Owns |
| --- | --- |
| [`context-fundamentals`](skills/context-fundamentals/) | Context-window mental models, anatomy of context, attention-budget reasoning |
| [`context-degradation`](skills/context-degradation/) | Lost-in-middle, context poisoning, distraction, clash, and degraded long-session behavior |
| [`context-compression`](skills/context-compression/) | Summaries, handoffs, artifact trails, and tokens-per-task reduction |
| [`context-optimization`](skills/context-optimization/) | Observation masking, prefix/cache strategy, retrieval precision, budget allocation |
| [`latent-briefing`](skills/latent-briefing/) | Task-guided KV cache compaction for worker models when the runtime exposes compatible KV state |
| [`multi-agent-patterns`](skills/multi-agent-patterns/) | Orchestrator, peer, hierarchical, and parallel-agent coordination patterns |
| [`memory-systems`](skills/memory-systems/) | Short-term, long-term, graph, vector, entity, and filesystem memory choices |
| [`tool-design`](skills/tool-design/) | Agent-tool contracts, schemas, descriptions, tool consolidation, actionable errors |
| [`filesystem-context`](skills/filesystem-context/) | File-backed scratchpads, dynamic discovery, large-output offloading, cross-agent handoffs |
| [`hosted-agents`](skills/hosted-agents/) | Remote sandboxes, warm pools, background agent infrastructure, multiplayer agent sessions |
| [`evaluation`](skills/evaluation/) | Deterministic checks, regression suites, production monitoring, quality gates |
| [`advanced-evaluation`](skills/advanced-evaluation/) | LLM judges, pairwise comparison, calibration, bias mitigation |
| [`harness-engineering`](skills/harness-engineering/) | Autonomous loops, locked evaluators, novelty gates, durable logs, rollback, approvals |
| [`project-development`](skills/project-development/) | Task-model fit, staged pipelines, structured outputs, operational cost |
| [`bdi-mental-states`](skills/bdi-mental-states/) | Belief-desire-intention state modeling, rational traces, neuro-symbolic transformations |

### Microsoft-native implementation skills

| Skill | Owns |
| --- | --- |
| [`azure-identity-for-agents`](azure/skills/azure-identity-for-agents/) | Managed identity, RBAC, OBO access, tenant boundaries, per-user authorization |
| [`foundry-hosted-agents`](azure/skills/foundry-hosted-agents/) | Foundry Hosted Agents, managed runtimes, production endpoints, sandboxing, runtime state |
| [`foundry-iq-knowledge-layer`](azure/skills/foundry-iq-knowledge-layer/) | Foundry IQ knowledge bases, reusable enterprise grounding, federated knowledge APIs |
| [`foundry-tool-governance`](azure/skills/foundry-tool-governance/) | Foundry Toolbox, tool catalog, MCP governance, OpenAPI tools, APIM AI Gateway |
| [`azure-agentic-retrieval`](azure/skills/azure-agentic-retrieval/) | Azure AI Search, agentic retrieval, File Search, SharePoint grounding, citations |
| [`responsible-ai-guardrails`](azure/skills/responsible-ai-guardrails/) | Content filters, Prompt Shields, groundedness checks, task adherence, red teaming |
| [`agent-publishing`](azure/skills/agent-publishing/) | Foundry versions, stable endpoints, Teams, Microsoft 365 Copilot, promotion, rollback |
| [`fabric-data-agent`](azure/skills/fabric-data-agent/) | Fabric Data Agent, semantic models, lakehouses, warehouses, Power BI aligned answers |
| [`azure-memory-state`](azure/skills/azure-memory-state/) | Cosmos DB, Blob, ADLS, Redis, session state, episodic memory, append-only logs |

Start with [`azure/AZURE-DISTRIBUTION.md`](azure/AZURE-DISTRIBUTION.md) when applying the core mechanisms to the Microsoft stack.

## Core-to-Azure routing

| Core decision | Microsoft-native default |
| --- | --- |
| Runtime and sandboxing | `hosted-agents` plus `foundry-hosted-agents` |
| Tool contract and governance | `tool-design` plus `foundry-tool-governance` |
| Enterprise knowledge and retrieval | `memory-systems`, `context-optimization`, `foundry-iq-knowledge-layer`, `azure-agentic-retrieval` |
| Identity and data boundaries | `tool-design`, `harness-engineering`, `azure-identity-for-agents` |
| Safety and quality gates | `context-degradation`, `evaluation`, `advanced-evaluation`, `responsible-ai-guardrails` |
| Publishing and rollout | `hosted-agents`, `harness-engineering`, `agent-publishing` |
| Analytical data grounding | `memory-systems`, `fabric-data-agent` |
| Durable memory and state | `memory-systems`, `filesystem-context`, `azure-memory-state` |

The core skill usually owns the mechanism. The Azure skill owns the Microsoft product choice, deployment caveat, security boundary, and operational control.

## Recognition

This repository is cited in academic research as foundational work on static skill architecture:

> "While static skills are well-recognized [Anthropic, 2025b; Muratcan Koylan, 2025], MCE is among the first to dynamically evolve them, bridging manual skill engineering and autonomous self-improvement."

1. [Meta Context Engineering via Agentic Skill Evolution](https://arxiv.org/pdf/2601.21557), Peking University State Key Laboratory of General Artificial Intelligence (2025)
2. [Agent Harness Engineering: A Survey](https://openreview.net/pdf/f358711a95aaaf61fdeffd4ef3fc60fba9b8da57.pdf), CMU, Yale, JHU, NEU, Tulane, UAB, OSU, Virginia Tech, and Amazon (2026)

## Researcher operating system

The [`researcher/`](researcher/) directory is a file-based operating system for turning external research into skill changes. It keeps the corpus auditable instead of leaving it as a static anthology.

It includes:

- Rubrics for content curation, skill changes, harness changes, and pairwise skill revision
- A mechanism registry with append-only accepted and rejected ledgers
- Claim provenance for numeric, benchmark, volatile, and vendor-performance claims
- A corpus index for the mechanism-first core skills
- Activation regression fixtures and adversarial benchmark scenarios
- A run state machine for autonomous research loops
- Deterministic validation scripts used by CI

The core researcher corpus remains mechanism-first. Azure product bindings have their own [`azure/corpus/index.json`](azure/corpus/index.json) so Microsoft product defaults do not pollute core mechanism provenance.

## Validation

Top-level gates:

```bash
python3 researcher/scripts/validate_repo.py --strict
python3 researcher/scripts/skill_health.py --strict --no-history
python3 azure/scripts/validate_azure.py
python3 researcher/scripts/check_activation_cases.py
python3 researcher/scripts/run_benchmarks.py
```

Example project gates:

```bash
cd examples/llm-as-judge-skills
npm install
npm run build
npm test
npm run lint
npm run typecheck

cd examples/interleaved-thinking
pip install -e ".[dev]"
pytest
ruff check .
```

## Examples

The [`examples/`](examples/) directory contains complete system designs that demonstrate how multiple skills compose.

| Example | Description | Skills applied |
| --- | --- | --- |
| [`digital-brain-skill`](examples/digital-brain-skill/) | Personal operating system with progressive disclosure, module isolation, append-only memory, and automation scripts | `context-fundamentals`, `context-optimization`, `memory-systems`, `tool-design`, `multi-agent-patterns`, `evaluation`, `project-development` |
| [`x-to-book-system`](examples/x-to-book-system/) | Multi-agent system that monitors X accounts and generates daily synthesized books | `multi-agent-patterns`, `memory-systems`, `context-optimization`, `tool-design`, `evaluation` |
| [`llm-as-judge-skills`](examples/llm-as-judge-skills/) | TypeScript LLM evaluation tools with direct scoring, pairwise comparison, rubric generation, and evaluator agents | `advanced-evaluation`, `tool-design`, `context-fundamentals`, `evaluation` |
| [`book-sft-pipeline`](examples/book-sft-pipeline/) | Pipeline for training small models to write in an author's style | `project-development`, `context-compression`, `multi-agent-patterns`, `evaluation` |
| [`interleaved-thinking`](examples/interleaved-thinking/) | Reasoning trace optimizer that converts agent failure patterns into generated skills | `evaluation`, `advanced-evaluation`, `context-degradation`, `harness-engineering` |

## Structure

```text
skills/<skill-name>/SKILL.md          # Core mechanism-first skills
azure/skills/<skill-name>/SKILL.md    # Microsoft-native implementation skills
azure/AZURE-DISTRIBUTION.md           # Core-to-Azure mapping
researcher/                           # Deterministic research and validation OS
template/SKILL.md                     # Canonical skill template
```

## Contributing

When changing skills, update every surface that owns the behavior: frontmatter description, `When to Activate`, integration guidance, manifests, corpus index, activation fixtures, and validation. Keep core mechanism claims in `researcher/`; keep Microsoft product-binding metadata in `azure/` unless a core skill owns the claim.

Agents may prepare changes and pass gates, but push and merge remain human-controlled.

## License

MIT License - see [LICENSE](LICENSE) for details.
