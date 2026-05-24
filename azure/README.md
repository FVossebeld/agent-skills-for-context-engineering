# Azure AI / Microsoft-native adaptation

This directory contains the Microsoft-native part of the standard Agent Skills for Context Engineering package. The default root plugin includes these skills alongside the core mechanism-first skills.

## Scope

Use this distribution when the implementation target is Microsoft-native:

- Microsoft Foundry Agent Service and Hosted Agents for managed agent runtimes, endpoints, and production execution
- Foundry IQ for reusable, permission-aware enterprise knowledge bases
- Foundry Toolbox and tool catalog for curated tool surfaces
- Azure AI Search, File Search, SharePoint, Fabric, and Blob Storage for retrieval and memory
- Azure Functions, OpenAPI, MCP, and API Management AI Gateway for actions and governance
- Microsoft Foundry evaluations, Azure Monitor, Application Insights, and OpenTelemetry for quality and observability
- Entra ID, managed identity, RBAC, and on-behalf-of flows for enterprise access control

The core skills still own the generic mechanisms. Azure skills own the Microsoft-native binding of those mechanisms to current products.

## Distribution contract

- Core skills stay under `../skills/` and remain product-agnostic.
- Azure adaptation skills live under `skills/` inside this `azure/` source root.
- Azure metadata lives under `corpus/`, not under `../researcher/corpus/index.json`.
- Azure claims and volatile product notes are cited in references and should not be added to the core `../researcher/claims/index.jsonl` unless a core skill owns the claim.
- The default root marketplace includes these skills via `./azure/skills/...`.
- Azure-only plugin manifests still use `source: "./azure"` from the repo root for subset installs that do not need the core skills or researcher OS.

## Start here

Read `AZURE-DISTRIBUTION.md` first. It maps every core skill to Microsoft-native defaults and explains where the Azure adaptation skills should be activated.
