# Azure AI / Microsoft-native companion distribution

This directory is an additive Microsoft-native companion layer for Agent Skills for Context Engineering. It keeps the original `skills/` corpus mechanism-first and platform-agnostic while providing opinionated Azure AI and Microsoft Foundry implementation guidance.

## Scope

Use this distribution when the implementation target is Microsoft-native:

- Microsoft Foundry Agent Service and Hosted Agents for managed agent runtimes, endpoints, and production execution
- Foundry IQ for reusable, permission-aware enterprise knowledge bases
- Foundry Toolbox and tool catalog for curated tool surfaces
- Azure AI Search, File Search, SharePoint, Fabric, and Blob Storage for retrieval and memory
- Azure Functions, OpenAPI, MCP, and API Management AI Gateway for actions and governance
- Microsoft Foundry evaluations, Azure Monitor, Application Insights, and OpenTelemetry for quality and observability
- Entra ID, managed identity, RBAC, and on-behalf-of flows for enterprise access control

The core skills still own the generic mechanisms. Azure skills own only the Microsoft-native binding of those mechanisms to current products.

## Distribution contract

- Core skills stay under `../skills/` and remain product-agnostic.
- Azure companion skills live under `skills/` inside this `azure/` source root.
- Azure metadata lives under `corpus/`, not under `../researcher/corpus/index.json`.
- Azure claims and volatile product notes are cited in references and should not be added to the core `../researcher/claims/index.jsonl` unless a core skill owns the claim.
- Azure plugin manifests should use `source: "./azure"` from the repo root so installing the Azure distribution does not cache the full researcher OS.

## Start here

Read `AZURE-DISTRIBUTION.md` first. It maps every core skill to Microsoft-native defaults and explains where the Azure companion skills should be activated.
