# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a collection of 75 specialized AI subagents for Claude Code. Each subagent is an expert in a specific domain (development, security, infrastructure, business, etc.) and is automatically invoked based on context or explicitly called when needed.

## Repository Structure

This repository contains individual markdown files (`.md`) for each subagent:
- Language specialists (python-pro, rust-pro, typescript-pro, etc.)
- Architecture & development (backend-architect, frontend-developer, etc.)
- Infrastructure & operations (devops-troubleshooter, cloud-architect, etc.)
- Quality & security (code-reviewer, security-auditor, test-automator, etc.)
- Data & AI (data-scientist, ai-engineer, ml-engineer, etc.)
- Business & marketing (business-analyst, content-marketer, etc.)
- SEO specialists (seo-content-auditor, seo-meta-optimizer, etc.)
- Documentation (docs-architect, api-documenter, tutorial-engineer, etc.)

## Subagent File Format

Each subagent follows this YAML frontmatter format:
```markdown
---
name: subagent-name
description: When this subagent should be invoked
model: haiku|sonnet|opus  # Optional - specify which Claude model to use
tools: tool1, tool2       # Optional - defaults to all tools
---

System prompt defining the subagent's role and capabilities
```

## Model Assignments

Subagents are configured with specific Claude models based on task complexity:

- **Haiku (Fast & Cost-Effective)** - 15 agents: Simple tasks like data analysis, documentation, and standard responses
- **Sonnet (Balanced Performance)** - 44 agents: Development tasks, code review, testing, and standard engineering work  
- **Opus (Maximum Capability)** - 15 agents: Critical tasks like security auditing, architecture review, incident response, and AI/ML engineering

## Key Subagent Categories

### High-Impact Agents (Opus)
- `security-auditor`: Vulnerability analysis and OWASP compliance
- `ai-engineer`: LLM applications, RAG systems, prompt engineering
- `incident-responder`: Production incident handling with urgency
- `cloud-architect`: Infrastructure design and optimization
- `performance-engineer`: Application bottleneck optimization

### Development Core (Sonnet)
- `code-reviewer`: Code quality with configuration security focus
- `backend-architect`: RESTful APIs, microservices, database design
- `frontend-developer`: React components, responsive layouts
- Language specialists (`python-pro`, `rust-pro`, `typescript-pro`, etc.)

### Automation & Support (Haiku)
- `api-documenter`: OpenAPI/Swagger documentation
- `business-analyst`: Metrics and KPI tracking
- `content-marketer`: Blog posts and SEO content
- SEO specialists for optimization tasks

## Development Workflow

### No Build/Test Commands Required
This repository contains only markdown documentation files - no compilation, linting, or testing is required.

### File Editing Guidelines
When modifying subagent files:
1. Preserve the YAML frontmatter format exactly
2. Keep descriptions concise and specific about when to invoke
3. Maintain the established model assignments (haiku/sonnet/opus)
4. Follow the existing system prompt structure and tone

### Creating New Subagents
1. Use lowercase, hyphen-separated names
2. Write clear descriptions for automatic invocation
3. Choose appropriate model based on task complexity
4. Include specific domain expertise in the system prompt
5. Focus on practical implementation over theory

## Usage Patterns

### Automatic Invocation
Claude Code analyzes requests and delegates to appropriate subagents based on:
- Keywords and context in the request
- Technical domain indicators
- Task complexity and requirements

### Explicit Invocation
Users can request specific subagents:
- "Use code-reviewer to analyze these changes"
- "Have security-auditor check for vulnerabilities"  
- "Get performance-engineer to optimize this"

### Multi-Agent Workflows
Subagents coordinate automatically for complex tasks:
- Feature development: backend-architect → frontend-developer → test-automator → security-auditor
- Performance optimization: performance-engineer + database-optimizer → combined recommendations
- Production issues: incident-responder → devops-troubleshooter → error-detective

## Special Considerations

### Configuration Security Focus
The `code-reviewer` subagent has specialized training for configuration changes that could cause production outages, with particular emphasis on:
- Connection pool settings
- Timeout configurations
- Memory and resource limits
- Security misconfigurations

### Model-Specific Capabilities
- **Opus agents** handle complex analysis requiring deep reasoning
- **Sonnet agents** balance capability with efficiency for most tasks
- **Haiku agents** optimize for speed on straightforward operations

## Repository Maintenance

### License
MIT License - see LICENSE file

### External Links
- Repository is linked to Claude Code documentation and GitHub
- Contains multilingual README support
- References companion Commands repository for advanced workflows

This repository serves as a comprehensive library of domain expertise that extends Claude Code's capabilities across all major areas of software development and business operations.