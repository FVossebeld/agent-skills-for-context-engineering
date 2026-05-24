---
name: responsible-ai-guardrails
description: This skill should be used when applying Microsoft Responsible AI controls to agents: content filters, Prompt Shields, groundedness checks, task adherence, protected material handling, red teaming, monitoring, and safety evaluation.
---

# Responsible AI Guardrails

Responsible AI guardrails are the safety and trust layer around an agent's context, tools, and outputs. In Microsoft-native systems, these guardrails combine Foundry safety features, Azure AI Content Safety, evaluation, monitoring, and human review.

## When to Activate

Activate this skill when:

- Designing safety controls for Foundry agents or Azure OpenAI applications.
- Adding Prompt Shields, content filtering, groundedness checks, or task adherence checks.
- Evaluating prompt injection, jailbreak, protected content, or harmful-output risk.
- Planning red teaming or post-deployment safety monitoring.
- Deciding which tool calls require policy checks or human approval.

Do not activate this skill for adjacent work owned by other skills:

- Generic evaluation design: core `evaluation`.
- Context failure diagnosis without a safety-control implementation: core `context-degradation`.
- Tool catalog design and versioning: `foundry-tool-governance`.
- Identity and access boundaries: `azure-identity-for-agents`.

## Core Concepts

Guardrails are not a single filter. They are layered controls that reduce unsafe input, unsafe retrieval, unsafe tool use, and unsafe output. Treat each model interaction as a boundary where untrusted text can enter the agent.

Use these layers:

| Layer | Microsoft-native control |
| --- | --- |
| Prompt and retrieved text | Prompt Shields, injection-aware retrieval filtering |
| Generated answer | Content filters, groundedness evaluation, protected-material checks |
| Tool use | Task adherence checks, allowed-tool scopes, human approval |
| Production behavior | Foundry evaluations, Azure Monitor, Application Insights, red teaming |

## Practical Guidance

1. Define the harms and policy boundaries before choosing products.
2. Put deterministic access controls before model-based safety checks.
3. Run groundedness and relevance checks for RAG answers that cite private sources.
4. Treat retrieved documents and tool outputs as untrusted input.
5. Add human approval for irreversible, external, financial, or privilege-changing actions.
6. Monitor production traces and sample outputs for continuous evaluation.

## Examples

**Example: private knowledge assistant**

```text
Controls:
- OBO retrieval for SharePoint permissions.
- Prompt Shields on user prompt and retrieved snippets.
- Groundedness evaluator before final answer is accepted.
- Azure Monitor alert when groundedness or safety metrics degrade.
```

**Example: action-taking agent**

```text
Read-only actions: allowed after policy checks.
Write actions: require scoped tool and audit event.
Destructive actions: require explicit human approval.
```

## Guidelines

1. Use policy and identity before relying on the model to self-police.
2. Separate safety evaluation from quality evaluation.
3. Preserve traces for safety debugging without logging secrets.
4. Red-team the full tool path, not just the final response.
5. Document which risks remain outside automated controls.

## Gotchas

1. **Groundedness is not truth**: A response can be grounded in an outdated or wrong source. Pair groundedness with source quality and freshness checks.
2. **Prompt injection can arrive through tools**: Treat search results, documents, and API responses as adversarial context.
3. **A blocked output is not enough**: The agent may already have called an unsafe tool. Guard action selection, not only final text.

## Integration

- core evaluation - Owns quality gates and regression suites.
- core context-degradation - Explains poisoning, distraction, and clash failure modes.
- foundry-tool-governance - Applies safety policy to tools and Toolbox versions.
- azure-identity-for-agents - Keeps data access aligned with user and workload permissions.

## References

- Azure AI Content Safety: https://learn.microsoft.com/azure/ai-services/content-safety/overview
- Microsoft Foundry evaluations: https://learn.microsoft.com/azure/ai-foundry/concepts/evaluation-approach-gen-ai
- Foundry content filtering: https://learn.microsoft.com/azure/ai-foundry/concepts/content-filtering
- Foundry tool best practices: https://learn.microsoft.com/azure/foundry/agents/concepts/tool-best-practice

---

## Skill Metadata

**Created**: 2026-05-24
**Last Updated**: 2026-05-24
**Author**: Agent Skills for Context Engineering Contributors
**Version**: azure-0.1.0

