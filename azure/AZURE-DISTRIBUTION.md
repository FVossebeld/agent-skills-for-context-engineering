# Azure AI / Microsoft-native adaptation

This adaptation turns the context-engineering skill collection into an opinionated Microsoft-native implementation guide without replacing the underlying mechanisms. The root `context-engineering` package includes these Azure skills by default.

## Design rule

Use the core skill for the mechanism. Use this Azure distribution for the default Microsoft product choice, security boundary, deployment surface, and operational caveats.

Default bias:

1. Prefer Microsoft Foundry Agent Service and Foundry Hosted Agents for managed agent runtimes.
2. Prefer Microsoft Agent Framework or Semantic Kernel for enterprise code-first orchestration.
3. Prefer Foundry Workflow Agents for declarative multi-step and human-in-the-loop orchestration when preview risk is acceptable.
4. Prefer Foundry Toolbox for curated tool catalogs once the agent has more than a small non-overlapping tool set.
5. Prefer Foundry IQ, Azure AI Search, File Search, SharePoint grounding, Fabric Data Agent, and Cosmos DB over ad hoc retrieval or memory infrastructure.
6. Prefer Entra ID, managed identity, RBAC, on-behalf-of auth, private networking, and Azure Monitor before adding custom governance.

## Core skill to Microsoft-native mapping

| Core skill | Microsoft-native default | Notes |
| --- | --- | --- |
| `context-fundamentals` | Foundry model catalog, API Management AI Gateway token policies | Keep attention-budget concepts platform-independent. Use Azure controls to enforce budget and routing. |
| `context-degradation` | Foundry evaluations, Content Safety Prompt Shields, groundedness checks, task adherence checks | Product checks operationalize some degradation modes, but lost-in-middle remains a model behavior to test. |
| `context-compression` | Thread state plus Cosmos DB or Blob summaries | Foundry does not expose a universal managed auto-compaction primitive. Keep compression logic application-owned. |
| `context-optimization` | Foundry IQ, Azure AI Search, File Search, APIM semantic caching, selective retrieval | Use managed knowledge bases, retrieval scope, and cache policy to reduce repeated context injection. |
| `latent-briefing` | No direct Azure product equivalent | Treat KV-state sharing as a research mechanism ahead of the current Foundry product surface. |
| `multi-agent-patterns` | Foundry Workflow Agents, Hosted Agents, Microsoft Agent Framework, Semantic Kernel, AutoGen | Choose topology for context isolation first, then bind to the runtime. |
| `memory-systems` | Foundry IQ, Azure AI Search, Cosmos DB, Blob Storage, SharePoint, Fabric Data Agent | Use Foundry IQ for reusable enterprise knowledge bases; use the shallowest durable layer that satisfies retrieval, identity, and audit needs. |
| `tool-design` | Foundry Toolbox, tool catalog, Azure Functions, OpenAPI, MCP, APIM AI Gateway | Toolbox is the preferred Azure answer for curated, versioned tool surfaces. |
| `filesystem-context` | Hosted Agent sandbox filesystem, Blob Storage, ADLS Gen2, Azure Files | Use files for durable scratchpads, handoffs, and large-output offloading. |
| `hosted-agents` | Foundry Hosted Agents, Azure Container Apps, Azure Functions for tools | Hosted Agents are the managed runtime for production agent execution; Container Apps remains useful for custom control. |
| `evaluation` | Foundry evaluations, Azure Monitor, Application Insights, OpenTelemetry | Run deterministic checks before judge-based evaluations, then monitor production traces. |
| `advanced-evaluation` | Foundry custom evaluators and model benchmarks | Pairwise bias mitigation is still a custom evaluator pattern, not a one-click built-in. |
| `harness-engineering` | Foundry versioning, GitHub Actions or Azure DevOps, Workflow human approval, append Blob logs | Keep locked evaluators and human-controlled promotion explicit. |
| `project-development` | Foundry playground, model benchmarks, structured outputs, APIM quotas | Prototype manually, estimate cost, then turn the pipeline into durable stages. |
| `bdi-mental-states` | Semantic Kernel process patterns plus Cosmos DB graph-like state | Azure has no formal managed BDI product. Treat this as application architecture. |

## Companion skills

| Azure skill | Owns | Defers to |
| --- | --- | --- |
| `azure-identity-for-agents` | Managed identity, RBAC, OBO, tenant boundaries | `tool-design`, `harness-engineering` |
| `foundry-hosted-agents` | Managed agent runtime, endpoints, sandboxing, runtime state, scaling, production execution boundaries | `hosted-agents`, `harness-engineering` |
| `foundry-iq-knowledge-layer` | Foundry IQ knowledge bases, federated enterprise grounding, permission-aware knowledge APIs | `memory-systems`, `context-optimization` |
| `foundry-tool-governance` | Toolbox, tool catalog, MCP governance, APIM gateway | `tool-design` |
| `azure-agentic-retrieval` | Azure AI Search agentic retrieval, knowledge sources, citations | `memory-systems`, `context-optimization` |
| `responsible-ai-guardrails` | Content filters, Prompt Shields, groundedness, red teaming | `evaluation`, `context-degradation` |
| `agent-publishing` | Foundry versioning, Teams, Microsoft 365 Copilot, Entra Agent Registry | `hosted-agents`, `harness-engineering` |
| `fabric-data-agent` | Fabric semantic-model and lakehouse grounding | `memory-systems` |
| `azure-memory-state` | Cosmos DB, Blob, Redis, session and episodic state | `memory-systems`, `filesystem-context` |

## Product caveats

- Preview features should not be treated as stable architecture boundaries. Foundry Workflow Agents, Hosted Agents, Toolbox, some grounding tools, AI Gateway capabilities, and Fabric agent surfaces may change.
- Foundry IQ should be treated as the preferred managed enterprise knowledge layer when available, but product APIs and naming may move while the IQ surfaces mature.
- Bing grounding and web search have compliance and data-flow considerations. Regulated workloads should prefer private grounding through Azure AI Search, SharePoint, Fabric, or customer-controlled indexes.
- SharePoint and Microsoft 365 grounding require tenant, license, and identity alignment. Always design for the user's effective permissions, not a service account's broad access.
- Foundry Toolbox is the right abstraction for a curated tool set, but the tool descriptions still need the same mechanism-level discipline as any MCP or OpenAPI tool.
- No Azure service replaces the need for deterministic validation, locked evaluators, append-only logs, or human approval boundaries in autonomous harnesses.

## References

- Microsoft Foundry Agent Service: https://learn.microsoft.com/azure/foundry/agents/overview
- Foundry Agent Service concepts: https://learn.microsoft.com/azure/foundry/agents/concepts/agents
- Foundry IQ overview and announcements: https://aka.ms/iq-series
- Foundry tool catalog: https://learn.microsoft.com/azure/foundry/agents/concepts/tool-catalog
- Foundry tool best practices: https://learn.microsoft.com/azure/foundry/agents/concepts/tool-best-practice
- Microsoft Foundry evaluations and observability: https://learn.microsoft.com/azure/ai-foundry/concepts/evaluation-approach-gen-ai
- Azure AI Search RAG and agentic retrieval: https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview
- Azure AI Content Safety: https://learn.microsoft.com/azure/ai-services/content-safety/overview
- API Management AI Gateway: https://learn.microsoft.com/azure/api-management/genai-gateway-capabilities
- Cosmos DB for AI agents: https://learn.microsoft.com/azure/cosmos-db/ai-agents
- Semantic Kernel: https://learn.microsoft.com/semantic-kernel/overview/
- AutoGen: https://microsoft.github.io/autogen/stable/
