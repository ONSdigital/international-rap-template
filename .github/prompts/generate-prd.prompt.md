---
mode: product-manager
---

Using the requirements gathered in the previous phase, generate a Product Requirements Document (PRD) in the exact format shown below. Do not deviate from this structure. Ensure the output is:
- Clear and readable for both technical and non-technical stakeholders
- Scoped appropriately for implementation
- Technically feasible and logically structured
- Written in professional, concise markdown

Save the PRD file in the `/.github/prd/` directory with the naming convention: `prd-[feature-or-component-name]-[version].md` (e.g., `prd-user-authentication-1.md`).

Tone and Style Guidelines:
- Use plain language and avoid unnecessary jargon
- Keep explanations high-level unless technical detail is explicitly required. This does not apply to the Development Roadmap section, which requires technical detail.
- Prioritize clarity and brevity over verbosity
- Use consistent formatting and bullet points where appropriate

<context>
# Overview
[Provide a high-level overview of your product here. Explain what problem it solves, who it's for, and why it's valuable.]

# Core Features
[Using numbered list(s), describe the main features of your product. For each feature, include:
- What it does
- Why it's important
- How it works at a high level]

# User Experience
[Describe the user journey and experience. Include:
- User stories
- Key user flows
- UI/UX considerations, if any]
</context>

<PRD>
# Technical Architecture
[Outline the technical implementation details. These may include, where relevant:
- System components
- Data models
- APIs and integrations
- Infrastructure requirements]

# Logical Dependency Chain
[Define the logical order of development:
- Which features need to be built first (foundation)
- Getting as quickly as possible to something usable that works
- Properly pacing and scoping each feature so it is atomic but can also be built upon and improved as development approaches]

# Development Roadmap
[Break down the development process into phases:
- MVP requirements
- Future enhancements, if any
- Do not think about timelines whatsoever -- all that matters is scope and detailing exactly what needs to be built in each phase so it can later be cut up into tasks]

# Risks and Mitigations
[Identify potential risks and how they'll be addressed:
- Technical challenges
- Figuring out the MVP that we can build upon
- Resource constraints]

# Appendix
[Include any additional information, e.g. technical specifications]
</PRD>
