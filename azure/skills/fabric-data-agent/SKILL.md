---
name: fabric-data-agent
description: This skill should be used when grounding agents in Microsoft Fabric: Fabric Data Agent, semantic models, lakehouses, warehouses, Power BI aligned metrics, governed analytical data, and natural-language data access.
---

# Fabric Data Agent

Fabric Data Agent is the Microsoft-native binding for analytical data grounding. Use it when the agent needs governed answers from semantic models, lakehouses, warehouses, or Power BI-aligned business definitions rather than document chunks.

## When to Activate

Activate this skill when:

- The agent answers questions over Fabric semantic models, lakehouses, warehouses, or Power BI datasets.
- Business metric definitions must match governed analytical models.
- Retrieval needs structured data, measures, dimensions, filters, and aggregations.
- Users expect natural-language data analysis over enterprise analytics assets.
- Data access must inherit Fabric, Foundry IQ, and Microsoft 365 governance.

Do not activate this skill for adjacent work owned by other skills:

- Reusable enterprise knowledge bases: `foundry-iq-knowledge-layer`.
- Direct unstructured document retrieval and custom indexing: `azure-agentic-retrieval`.
- General memory architecture: core `memory-systems`.
- Tool schema design around Fabric APIs: `foundry-tool-governance`.
- Model-judge evaluation of data answers: core `advanced-evaluation`.

## Core Concepts

Analytical grounding is not the same as document retrieval. A document chunk can explain what a metric means, but a semantic model computes the metric. When users ask business questions, prefer the governed analytical layer that owns definitions and permissions.

Use Fabric when the agent needs:

| Need | Why Fabric fits |
| --- | --- |
| Consistent business metrics | Semantic model definitions prevent prompt-level metric drift |
| Structured aggregations | Lakehouse and warehouse data support filtered computation |
| Power BI alignment | Answers can match reports and dashboards |
| Enterprise governance | Permissions and lineage remain close to the data estate |

## Practical Guidance

1. Identify whether the question is analytical, documentary, or mixed.
2. Route analytical questions to Fabric Data Agent or a governed Fabric-backed tool.
3. Route policy or explanatory document questions to Azure AI Search or SharePoint grounding.
4. Return measure names, filters, time periods, and source artifacts with the answer.
5. Evaluate numerical answers with deterministic checks where possible.
6. Keep data definitions in Fabric, not duplicated in prompts.

## Examples

**Example: mixed grounding**

```text
Question: Why did support cost rise last month?

Fabric: compute support cost by month, region, and product line.
Azure AI Search: retrieve operational notes explaining staffing changes.
Final answer: separate computed metrics from explanatory evidence.
```

**Example: metric ownership**

```text
Avoid: prompt says "gross margin means revenue minus cost" for every agent.
Prefer: query the semantic model where gross margin is defined and governed.
```

## Guidelines

1. Use Fabric for governed analytical facts, not free-text document search.
2. Preserve metric names, filters, and time windows in the response.
3. Do not let the model invent business definitions that already exist in semantic models.
4. Keep permission checks aligned with Fabric workspace and item governance.
5. Combine Fabric with document retrieval only when the answer needs both computation and explanation.

## Gotchas

1. **Natural language hides query ambiguity**: Users may ask "revenue" without specifying gross, net, booked, or recognized. Ask or default to a governed semantic measure.
2. **Documents and metrics can disagree**: Treat computed Fabric data as the quantitative source of truth and documents as explanatory evidence unless the business owner says otherwise.
3. **Preview surfaces can move**: Keep Fabric-specific setup details in references or deployment docs so product changes do not rot the skill body.

## Integration

- foundry-iq-knowledge-layer - Complements Fabric with reusable enterprise knowledge bases.
- azure-agentic-retrieval - Complements Fabric with direct unstructured document grounding and custom indexes.
- azure-memory-state - Stores session state and analytical context outside prompts.
- foundry-tool-governance - Packages Fabric access through curated tools or toolbox entries.
- core evaluation - Adds deterministic checks for computed outputs.

## References

- Microsoft Fabric documentation: https://learn.microsoft.com/fabric/
- Foundry Agent Service tool catalog: https://learn.microsoft.com/azure/foundry/agents/concepts/tool-catalog
- Microsoft Foundry evaluations: https://learn.microsoft.com/azure/ai-foundry/concepts/evaluation-approach-gen-ai

---

## Skill Metadata

**Created**: 2026-05-24
**Last Updated**: 2026-05-24
**Author**: Agent Skills for Context Engineering Contributors
**Version**: azure-0.1.0
