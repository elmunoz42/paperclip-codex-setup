# ADR-001: Keep agent headquarters separate from product source

- **Status:** Accepted, 2026-09-04
- **Context:** The headquarters coordinates both a live WordPress site and a separate immersive solar-system application, neither of which belongs in this repository.
- **Decision:** Store only operating artifacts, runbooks, plans, and safe support automation here. Keep product code and deployment configuration in their own repositories.
- **Consequences:** This repository stays small and reviewable; product changes require separate access and scoped tasks.
- **Owner / revisit:** Carlos; revisit when a cross-repository integration contract is defined.
