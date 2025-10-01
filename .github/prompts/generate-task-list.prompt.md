---
mode: product-manager
description: 'Using the Product Requirements Document (PRD) generated in the previous phase, create a detailed task list to guide the implementation of the feature or code change.'
---

# Generate Task List

## Primary Directive

Using the Product Requirements Document (PRD) generated in the previous phase - ensure you ask the user to explicitly supply the file - create a detailed task list to guide the implementation of the feature or code change. The task list should break down the PRD into manageable, actionable tasks.  Your output must be machine-readable, deterministic, and structured for autonomous execution by other AI systems or humans.

## Core Requirements

- Generate implementation plans that consist of discrete, atomic phases and that are fully executable by AI or humans
- Use deterministic language with zero ambiguity
- Ensure complete self-containment with no external or cross-phase dependencies (unless explicitly declared) for understanding

## Phase Architecture

- Tasks within phases must be executable in parallel unless dependencies are specified
- All task descriptions must include specific file paths, function names, and exact implementation details
- No task should require human interpretation or decision-making

## AI-Optimized Implementation Standards

- Use explicit, unambiguous language with zero interpretation required
- Structure all content as machine-parseable formats (tables, lists, structured data)
- Include specific file paths, line numbers, and exact code references where applicable
- Define all variables, constants, and configuration values explicitly
- Provide complete context within each task description
- Use standardized prefixes for all identifiers (REQ-, TASK-, etc.)
- Include validation criteria that can be verified

## Output File Specifications

- Save implementation plan files in `/.github/task-list/` directory
- Use naming convention: `task-list-[feature-or-component-name]-[version].md`
- File must be valid Markdown with proper front matter structure

## Mandatory Template Structure

All implementation plans must strictly adhere to the following template. Each section is required and must be populated with specific, actionable content.

## Template Validation Rules

- All front matter fields must be present and properly formatted
- All section headers must match exactly (case-sensitive)
- All identifier prefixes must follow the specified format
- Tables must include all required columns
- No placeholder text may remain in the final output


```md
---
goal: [Concise Title Describing the feat]
version: [Optional: e.g., 1.0, Date]
date_created: [YYYY-MM-DD]
last_updated: [Optional: YYYY-MM-DD]
owner: [Optional: Team/Individual responsible for this spec]

# Introduction

[A short concise introduction to the plan and the goal it is intended to achieve.]

## 2. Implementation plan

Use the phases defined in the user-supplied PRD (`Development Roadmap` section) to structure the implementation plan. Each phase must include a clear goal and a list of tasks required to achieve that goal.

Repeat the following structure for each phase, expanding or contracting the number of rows in the task table as necessary:

### Phase [#]

- GOAL-[#]: [Describe the goal of this phase, e.g., "Implement feature X", "Refactor module Y", etc.]
- Core Feature number: [Link to the relevant core feature(s) from the PRD that this phase addresses, e.g., "Core Feature 1", "Core Feature 2", etc.]

| Task | Description |
|------|-------------|
| TASK-001 | Description of task 1 |
| TASK-002 | Description of task 2 |
| TASK-003 | Description of task 3 |


```