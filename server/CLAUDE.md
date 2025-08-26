# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is the **server** subdirectory of the Adversarial Document Analysis System. It contains active analysis results, specialized AI subagents, and SDK testing tools that extend the core adversarial analysis system.

## Repository Structure

This server directory contains:

- **Active Analysis Results**: Live output from adversarial document analysis sessions in `[document_name]_output/`
- **Specialized Agent Definitions**: Domain-specific agent markdown files for targeted analysis
- **Document Versions**: Multiple versions of analyzed documents showing iterative improvements  
- **SDK Testing Tools**: Python scripts for testing Claude Code SDK integration
- **Agent Deployment Scripts**: Shell scripts for agent management

## Key Files and Directories

### Analysis Output Directory (`[document_name]_output/`)
Contains results from actual adversarial analysis sessions:
- `final_report.md`: Complete process summary with quality metrics
- `process_log.md`: Round-by-round analysis tracking
- `round_[N]_con_analysis.md`: Con-side critique files with prioritized opinions
- `round_[N]_pro_response.md`: Pro-side improvement responses
- `round_[N]_research_findings.md`: Data researcher evidence reports

### Specialized Agent Files
- `pro_novel_hub.md`: Chinese language agent for "Novel Open Source" concept analysis
- `pro_travel_ai_assist.md`: Product requirements agent for travel/AI assistant applications  
- `pro_novel_hub_v1.1.md`, `pro_novel_hub_v1.2.md`: Version-tracked document improvements

### Testing and Deployment
- `test_sdk.py`: Asyncio-based Claude Code SDK integration testing
- `copy_agents.sh`: Agent deployment script from parent directory

## Commands

### Running Adversarial Analysis
```bash
# Full automatic analysis on existing documents
"Run adversarial analysis on pro_novel_hub.md"

# Domain-specific analysis with specialized agents
"Use the travel AI agent to analyze pro_travel_ai_assist.md"

# Manual step-by-step control
"Use con-side-analyst to analyze pro_novel_hub.md and generate Round 1 opinions"
```

### SDK Testing and Validation
```bash
python test_sdk.py
```
Tests Claude Code SDK integration with:
- Asyncio streaming response handling
- Senior Product Manager system prompt configuration  
- Adversarial analysis invocation on `pro_novel_hub.md`
- Error handling and timeout management

### Agent Management
```bash
./copy_agents.sh
```
Copies all agent files from `../` to local `.claude/agents/` directory for:
- Local development testing
- Isolated agent deployments
- Version-controlled agent modifications

## System Architecture

This server directory demonstrates the adversarial analysis system in action with real analysis results and specialized extensions.

### Analysis Process Flow
1. **Document Input**: Source documents (e.g., `pro_novel_hub.md`) analyzed through adversarial process
2. **Multi-Round Analysis**: Up to 5 rounds of critique→improvement→evaluation cycles  
3. **Priority-Based Feedback**: Opinions classified as High/Normal/Low priority for systematic resolution
4. **Quality Threshold**: Process terminates when <3 opinions remain OR all are Low priority
5. **Comprehensive Output**: Complete analysis trail in `[document_name]_output/` directory

### Core Agents (from parent directory)
1. **argument-orchestrator**: Manages process flow, enforces stop conditions, tracks metrics (Sonnet)
2. **data-researcher**: Gathers supporting evidence, validates claims, provides citations (Sonnet)
3. **con-side-analyst**: Identifies flaws/gaps, assigns priorities, suggests improvements (Opus)  
4. **pro-side-analyst**: Evaluates critiques, implements improvements, justifies decisions (Opus)

### Specialized Extensions (this directory)
- **Domain-Specific Analysis**: Agents optimized for particular content types (literature, travel/AI products)
- **Multi-Language Support**: Agents capable of analyzing Chinese and English documents
- **Product Requirements Focus**: Specialized agents for technical product specification analysis

## Analysis Output Structure

Based on actual analysis sessions in this directory, the system produces:

### Comprehensive Result Files
```
[document_name]_output/
├── final_report.md           # Executive summary with quality metrics and outcomes
├── process_log.md            # Round-by-round process tracking and agent coordination
├── round_[N]_con_analysis.md # Con-side critique with prioritized opinions (High/Normal/Low)
├── round_[N]_pro_response.md # Pro-side evaluation and document improvements  
├── round_[N]_research_*.md   # Data research findings and evidence validation
└── [document]_v[X.Y].md      # Version-tracked document improvements
```

### Quality Metrics Tracked
- **Opinion Resolution Rate**: Typically >85% of High/Normal priority issues addressed
- **Document Growth**: Often 40-65% content expansion with substantive improvements
- **Process Efficiency**: Most documents achieve quality threshold in 2-4 rounds
- **Version Evolution**: Clear progression from conceptual to implementation-ready

### Success Patterns Observed
- **Round 1**: Usually identifies 6-10 issues, typically structural/completeness gaps
- **Round 2-3**: Focus on evidence strengthening, implementation details, risk mitigation  
- **Final**: Typically 0-3 Low-priority issues (formatting, minor improvements)

## Proven Usage Patterns

### Automatic Full Analysis (Recommended)
```bash
"Run adversarial analysis on pro_novel_hub.md"
```
**Results**: Complete 3-round analysis with:
- Chinese concept document → comprehensive implementation framework
- 8 initial rejection points → 2 Low-priority final issues  
- ~65% content expansion with evidence-based improvements

### Manual Process Control
```bash
"Use con-side-analyst to analyze pro_novel_hub.md and generate Round 1 opinions"
"Use pro-side-analyst to respond to the con-side opinions and improve the document"
"Use argument-orchestrator to determine if we should continue analysis"
```

### Domain-Specific Invocation  
```bash
"Use the travel AI agent to analyze pro_travel_ai_assist.md for product requirements gaps"
"Apply Chinese literature analysis expertise to evaluate novel concept feasibility"
```

## Testing and Validation

### SDK Integration Testing
```bash
python test_sdk.py
```
**Validates**: 
- AsyncIO response streaming from Claude Code SDK
- System prompt configuration (Senior Product Manager persona)
- Multi-turn adversarial analysis invocation
- Error handling and timeout management

### Quality Validation Checklist
Based on successful analysis sessions:
- [ ] Analysis produces `final_report.md` with clear quality metrics
- [ ] Round files show decreasing opinion counts (8→4→2 pattern)  
- [ ] Document versions show substantive improvements (v1.0 → v1.1 → v1.2)
- [ ] Process terminates at quality threshold (<3 Low-priority opinions)
- [ ] Final documents are implementation-ready with evidence support

### Agent File Requirements
Following the established YAML frontmatter format:
```markdown
---
name: agent-name
description: When this agent should be invoked  
model: sonnet|opus  # Use opus for complex reasoning, sonnet for coordination
tools: WebSearch, WebFetch, Read, Write, Edit
---

System prompt with specific instructions for agent behavior and output format
```

## Development Guidelines

### Agent Creation Standards
- **Specificity**: Focus on clear domain expertise (travel products, literature analysis, etc.)
- **Multi-language**: Support both English and Chinese content where applicable
- **Output Consistency**: Maintain compatibility with core system expectations
- **Evidence-Based**: All analysis must be supported by research and data

### File Management
- Use descriptive filenames following `pro_[domain]_[purpose].md` pattern
- Version track improved documents as `[document]_v[X.Y].md`
- Maintain clean separation between source documents and analysis output

This server directory demonstrates production-ready adversarial analysis with documented success patterns and comprehensive output tracking.