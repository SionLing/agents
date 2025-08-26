# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is the **server** subdirectory of the Adversarial Document Analysis System. It contains specialized AI subagents and SDK testing tools that extend the core adversarial analysis system located in the parent directory.

## Repository Structure

This server directory contains:

- **Agent Definitions**: Additional specialized agent markdown files for domain-specific document analysis
- **SDK Testing**: Python scripts for testing the Claude Code SDK integration 
- **Agent Deployment**: Shell scripts for copying agent definitions to Claude Code

## Key Files

### Agent Files
- `pro_novel_hub.md`: Specialized agent for analyzing "Novel Open Source" concept documents (Chinese content)
- `pro_travel_ai_assist.md`: Specialized agent for travel/tourism product requirements analysis

### Testing and Deployment
- `test_sdk.py`: Claude Code SDK integration test script using asyncio
- `copy_agents.sh`: Shell script to copy agent markdown files from parent directory to `.claude/agents/`

## Commands

### Testing SDK Integration
```bash
python test_sdk.py
```
Run the Claude Code SDK test to verify adversarial analysis functionality. The script:
- Uses asyncio for asynchronous operations
- Tests the Claude Code SDK with system prompts for Senior Product Manager persona
- Runs adversarial analysis on documents like `pro_novel_hub.md`
- Streams responses with content extraction

### Deploying Agents
```bash
./copy_agents.sh
```
Copies all `.md` agent files from the parent directory to the local `.claude/agents/` directory. This enables:
- Local development and testing of agent modifications
- Isolated agent deployments for specific projects
- Version control of agent definitions

## System Architecture

This server extends the core 4-agent adversarial analysis system:

### Core System (from parent directory)
1. **argument-orchestrator**: Process management and coordination (Sonnet)
2. **data-researcher**: Evidence gathering and fact verification (Sonnet) 
3. **con-side-analyst**: Critical analysis and flaw identification (Opus)
4. **pro-side-analyst**: Document optimization and defense (Opus)

### Extended Agents (this directory)
- **Domain-Specific Analysts**: Specialized agents for particular industries or document types
- **Cultural/Language Specialists**: Agents optimized for non-English content analysis
- **Product-Specific Validators**: Agents focused on particular product categories (travel, literature, etc.)

## Development Workflow

### Agent Development
1. Create new agent `.md` files following the YAML frontmatter format:
```markdown
---
name: agent-name
description: When this agent should be invoked
model: sonnet|opus
tools: WebSearch, WebFetch, Read, Write, Edit
---

[System prompt content]
```

2. Test agents using the SDK integration script
3. Deploy using `copy_agents.sh` when ready

### Testing Process
1. **Unit Testing**: Test individual agents with specific document types
2. **SDK Integration**: Use `test_sdk.py` to verify Claude Code SDK compatibility
3. **End-to-End Testing**: Run complete adversarial analysis cycles
4. **Performance Validation**: Monitor response times and quality metrics

## Agent File Format

All agent files must follow the standardized format:
- **YAML Frontmatter**: Defines agent metadata, model assignment, and tool access
- **System Prompt**: Detailed instructions for agent behavior and output format
- **Examples**: Sample inputs and expected outputs where applicable

## Integration Notes

### With Parent System
- Inherits all core functionality from the main adversarial analysis system
- Extends capabilities with domain-specific expertise
- Maintains compatibility with the standard workflow (5 rounds max, priority-based feedback)

### With Claude Code SDK
- Supports both synchronous and asynchronous operations
- Implements streaming response handling
- Provides robust error handling and timeout management
- Uses proper authentication and session management

## Quality Standards

### Agent Quality Requirements
- **Specificity**: Domain-specific agents must demonstrate clear expertise advantage
- **Consistency**: Output format must align with core system expectations  
- **Reliability**: Agents must handle edge cases and error conditions gracefully
- **Performance**: Response times should be optimized for production use

### Code Quality Standards
- **Error Handling**: All scripts must include comprehensive error handling
- **Documentation**: All functions and complex logic must be documented
- **Testing**: Critical paths must have test coverage
- **Security**: No hardcoded credentials or sensitive data in code

## Usage Patterns

### Running Domain-Specific Analysis
```bash
"Use the travel AI analysis agent to review this product requirements document"
"Run novel concept analysis on this Chinese literature document"
```

### SDK Testing and Development  
```bash
python test_sdk.py  # Test basic SDK integration
# Modify system prompts in test_sdk.py for different personas
# Add new test scenarios for specialized agents
```

### Agent Deployment Pipeline
```bash
# 1. Develop agents in this directory
# 2. Test with SDK integration
./copy_agents.sh  # 3. Deploy to Claude Code
# 4. Validate in production environment
```

This server directory enables extended capabilities while maintaining full compatibility with the core adversarial document analysis system architecture.