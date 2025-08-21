# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a curated collection of 11 specialized AI subagents for Flutter mobile app development with Claude Code. Each subagent is an expert in a specific aspect of mobile development and is automatically invoked based on context or explicitly called when needed.

## Repository Structure

This repository contains individual markdown files (`.md`) for each Flutter development subagent:
- **Flutter & Mobile Development**: flutter-expert, mobile-developer, ios-developer
- **UI/UX Development**: frontend-developer, ui-ux-designer  
- **Code Quality & Testing**: code-reviewer, test-automator, debugger
- **Performance & Security**: performance-engineer, security-auditor
- **Documentation & Integration**: api-documenter

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

Flutter development subagents are configured with specific Claude models based on task complexity:

- **Haiku (Fast & Cost-Effective)** - 1 agent: API documentation and specifications
- **Sonnet (Balanced Performance)** - 8 agents: Flutter development, UI/UX, code quality, and testing tasks
- **Opus (Maximum Capability)** - 2 agents: Security auditing and performance optimization

## Key Subagent Categories

### High-Impact Agents (Opus)
- `security-auditor`: Mobile security vulnerability analysis and compliance
- `performance-engineer`: App performance optimization and profiling

### Development Core (Sonnet)
- `flutter-expert`: Flutter development with Dart, widgets, state management, and animations
- `mobile-developer`: Cross-platform mobile app development with native integrations
- `ios-developer`: Native iOS development and Flutter iOS-specific implementations
- `frontend-developer`: Responsive UI components and client-side state management
- `ui-ux-designer`: Mobile interface design, wireframes, and design systems
- `code-reviewer`: Code quality analysis with security focus
- `test-automator`: Comprehensive test suites for mobile apps
- `debugger`: Mobile app debugging and error investigation

### Documentation & Support (Haiku)
- `api-documenter`: API integration documentation and specifications

## Development Workflow

### Flutter Development Context
This repository provides subagents specifically for Flutter mobile app development. No build/test commands are required for the agent files themselves (markdown only), but the agents understand Flutter development workflows including:

- `flutter pub get` - Install dependencies
- `flutter run` - Run on connected devices/emulators  
- `flutter test` - Run unit and widget tests
- `flutter build android/ios` - Build for production
- `flutter analyze` - Static analysis
- `flutter doctor` - Environment health check

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
Subagents coordinate automatically for Flutter development tasks:
- Feature development: flutter-expert → ui-ux-designer → test-automator → security-auditor
- Performance optimization: performance-engineer → flutter-expert → ios-developer
- Cross-platform implementation: flutter-expert → ios-developer → test-automator
- Security review: security-auditor → flutter-expert → test-automator

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

### Flutter Development Focus
- Optimized for cross-platform mobile app development
- Covers Android and iOS deployment scenarios
- Includes native integration capabilities
- Supports modern Flutter architecture patterns

This repository serves as a focused library of Flutter mobile development expertise that extends Claude Code's capabilities specifically for cross-platform mobile app development.