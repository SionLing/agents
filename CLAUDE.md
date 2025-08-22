# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository contains specialized AI subagents for an **Adversarial Document Analysis System**. The system uses multiple agents to collaboratively analyze and improve requirements documents and analysis documents through an iterative, debate-style process.

## System Architecture

The system consists of four core agents that work together:

### Core Agents
1. **data-researcher**: Searches Google and reliable websites for supporting data and evidence
2. **pro-side-analyst**: Creates and defends documents, responds to critiques with improvements
3. **con-side-analyst**: Analyzes documents to find flaws, inconsistencies, and weak points
4. **argument-orchestrator**: Manages the iterative debate process and enforces stop conditions

### Analysis Workflow

1. **Initial Document Creation**: Pro-side agent creates the initial document/analysis
2. **Research Phase**: Data agent gathers supporting evidence and relevant information
3. **Critique Phase**: Con-side agent analyzes document and identifies rejection points (max 10)
4. **Defense Phase**: Pro-side agent evaluates con-side opinions and optimizes document
5. **Iteration**: Process repeats until stop conditions are met

### Stop Conditions
The process terminates when either:
- **5 argument rounds** have been completed
- **Fewer than 3 rejection points** remain (out of maximum 10)

## Subagent File Format

Each agent follows this YAML frontmatter format:

```markdown
---
name: agent-name
description: When this agent should be invoked in the analysis process
model: sonnet|opus  # Most agents use sonnet or opus for complex reasoning
tools: WebSearch, WebFetch, Read, Write, Edit  # Specific tools needed
---

System prompt defining the agent's role, analysis methodology, and output format
```

## Model Assignment Strategy

- **Sonnet**: Standard analysis, research, and document processing tasks
- **Opus**: Complex reasoning, argument evaluation, and critical analysis requiring deep thinking
- **Haiku**: Not recommended for this system due to complexity requirements

## Agent Specifications

### data-researcher Agent
- **Purpose**: Gather supporting evidence and factual information
- **Tools**: WebSearch, WebFetch for Google searches and reliable sources
- **Output**: Structured research findings with source citations
- **Model**: Sonnet (efficient for search and data collection)

### pro-side-analyst Agent  
- **Purpose**: Create, defend, and improve documents based on feedback
- **Methodology**: Constructive argumentation, evidence-based improvements
- **Output**: Optimized documents with rationale for changes
- **Model**: Opus (complex document creation and optimization)

### con-side-analyst Agent
- **Purpose**: Critical analysis to identify flaws and weak points
- **Methodology**: Systematic evaluation, devil's advocate approach
- **Output**: Up to 10 rejection points with detailed explanations
- **Model**: Opus (deep critical thinking and analysis)

### argument-orchestrator Agent
- **Purpose**: Manage the iterative process and track progress
- **Responsibilities**: Round counting, rejection point scoring, stop condition evaluation
- **Output**: Process status, final results, and iteration summaries
- **Model**: Sonnet (process management and coordination)

## Development Guidelines

### No Build/Test Commands Required
This repository contains only markdown agent definitions - no compilation or testing infrastructure needed.

### Agent Creation Standards
1. Use descriptive, role-based filenames (e.g., `pro-side-analyst.md`)
2. Define clear invocation criteria for the analysis workflow
3. Specify required tools for each agent's function
4. Structure prompts for consistent output formats
5. Include examples of expected input/output

### Quality Standards
- **Objectivity**: Agents must maintain analytical objectivity
- **Evidence-based**: All conclusions must be supported by data/research
- **Structured Output**: Consistent formatting for easy processing
- **Iterative Design**: Agents must work effectively in the debate cycle

## Usage Patterns

### Typical Analysis Session
1. User provides requirements document or analysis document
2. System automatically invokes appropriate agents in sequence
3. Iterative improvement cycle runs until stop conditions
4. Final optimized document and analysis summary provided

### Manual Invocation
Users can invoke specific agents:
- "Use data-researcher to find supporting evidence for this claim"
- "Have pro-side-analyst optimize this requirements section"
- "Get con-side-analyst to critique this analysis approach"

## Output Formats

### Document Versions
- **Version tracking**: Each iteration creates numbered document versions
- **Change logs**: Clear documentation of what changed and why
- **Rejection tracking**: Systematic recording of identified issues

### Final Deliverables
- **Optimized document**: Final version after all iterations
- **Analysis report**: Summary of all rejection points and resolutions
- **Evidence base**: Compiled research supporting document claims
- **Process log**: Complete record of the adversarial analysis cycle

## Community Guidelines

This repository follows established standards defined in:
- `.github/CODE_OF_CONDUCT.md`: Community behavior expectations
- `.github/CONTRIBUTING.md`: Contribution process and quality standards

## Repository Maintenance

### License
MIT License - allows broad use and modification of the adversarial analysis system

### Integration
- Designed specifically for Claude Code's multi-agent orchestration
- Compatible with existing Claude Code workflow patterns
- Extensible for domain-specific document analysis needs

This system provides a robust, multi-perspective approach to document analysis that combines research, advocacy, and critical evaluation to produce higher-quality requirements and analysis documents.