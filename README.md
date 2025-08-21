<div align="right">
  <details>
    <summary >🌐 Language</summary>
    <div>
      <div align="center">
        <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=en">English</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=zh-CN">简体中文</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=zh-TW">繁體中文</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=ja">日本語</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=ko">한국어</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=hi">हिन्दी</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=th">ไทย</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=fr">Français</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=de">Deutsch</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=es">Español</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=it">Italiano</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=ru">Русский</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=pt">Português</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=nl">Nederlands</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=pl">Polski</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=ar">العربية</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=fa">فارسی</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=tr">Türkçe</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=vi">Tiếng Việt</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=id">Bahasa Indonesia</a>
        | <a href="https://openaitx.github.io/view.html?user=wshobson&project=agents&lang=as">অসমীয়া</
      </div>
    </div>
  </details>
</div>

# Flutter Mobile Development Agents

A curated collection of specialized AI subagents for [Claude Code](https://docs.anthropic.com/en/docs/claude-code), specifically focused on Flutter Android/iOS mobile app development workflows.

## Overview

This repository contains 11 specialized subagents tailored for Flutter mobile development. Each subagent is an expert in a specific aspect of mobile app development, automatically invoked based on context or explicitly called when needed. All agents are configured with appropriate Claude models based on task complexity.

## Available Subagents

### Flutter & Mobile Development
- **[flutter-expert](flutter-expert.md)** - Master Flutter development with Dart, widgets, state management, and platform integrations
- **[mobile-developer](mobile-developer.md)** - Develop cross-platform mobile apps with native integrations
- **[ios-developer](ios-developer.md)** - Handle native iOS development and Flutter iOS-specific implementations
- **[frontend-developer](frontend-developer.md)** - Build responsive UI components and handle client-side state management
- **[ui-ux-designer](ui-ux-designer.md)** - Create mobile interface designs, wireframes, and design systems

### Code Quality & Testing
- **[code-reviewer](code-reviewer.md)** - Expert code review with security focus and production reliability
- **[test-automator](test-automator.md)** - Create comprehensive test suites with unit, integration, and widget tests
- **[debugger](debugger.md)** - Debugging specialist for errors, test failures, and unexpected behavior
- **[performance-engineer](performance-engineer.md)** - Profile mobile apps, optimize bottlenecks, and implement caching strategies
- **[security-auditor](security-auditor.md)** - Review mobile apps for vulnerabilities and ensure security compliance

### Documentation & Integration
- **[api-documenter](api-documenter.md)** - Create API integration documentation and specifications for mobile backends


## Model Assignments

The 11 Flutter development subagents are configured with specific Claude models based on task complexity:

### 🚀 Haiku (Fast & Cost-Effective) - 1 agent
**Model:** `haiku`
- `api-documenter` - API integration documentation and specifications

### ⚡ Sonnet (Balanced Performance) - 8 agents  
**Model:** `sonnet`
- `flutter-expert` - Flutter development with Dart, widgets, state management, and animations
- `mobile-developer` - Cross-platform mobile app development with native integrations
- `ios-developer` - Native iOS development and Flutter iOS-specific implementations
- `frontend-developer` - Responsive UI components and client-side state management
- `ui-ux-designer` - Mobile interface design, wireframes, and design systems
- `code-reviewer` - Code quality analysis with security focus
- `test-automator` - Comprehensive test suites for mobile apps
- `debugger` - Mobile app debugging and error investigation

### 🧠 Opus (Maximum Capability) - 2 agents
**Model:** `opus`
- `security-auditor` - Mobile security vulnerability analysis and compliance
- `performance-engineer` - Mobile app performance optimization and profiling

## Installation

These Flutter development subagents are automatically available when placed in `~/.claude/agents/` directory.

```bash
cd ~/.claude
git clone https://github.com/[your-repo]/flutter-agents.git agents
```

## Usage

### Automatic Invocation
Claude Code will automatically delegate to the appropriate subagent based on the task context and the subagent's description.

### Explicit Invocation
Mention the subagent by name in your request:
```
"Use flutter-expert to implement this custom widget"
"Have security-auditor scan my app for vulnerabilities"
"Get performance-engineer to optimize app startup time"
```

## Usage Examples

### Single Agent Tasks
```bash
# Flutter development
"Use flutter-expert to implement a custom animated widget"
"Have flutter-expert set up state management with Riverpod"
"Get mobile-developer to add native Android permissions"

# iOS-specific tasks
"Use ios-developer to implement native iOS camera integration"
"Have ios-developer set up push notifications for Flutter"

# UI/UX and design
"Get ui-ux-designer to create a mobile-first design system"
"Use frontend-developer to implement responsive layouts"

# Code quality and testing
"Have code-reviewer analyze this Flutter widget for best practices"
"Use test-automator to create widget tests for this component"
"Get debugger to investigate this app crash on Android"

# Performance and security
"Use performance-engineer to optimize app memory usage"
"Have security-auditor review API integration security"

# Documentation
"Get api-documenter to document REST API integration"
```

### Multi-Agent Workflows

These Flutter subagents work together seamlessly for complex mobile app development tasks:

```bash
# Flutter app feature development
"Implement user profile screen with photo upload"
# Automatically uses: flutter-expert → ui-ux-designer → test-automator → security-auditor

# Cross-platform optimization workflow
"Optimize app for both Android and iOS performance"
# Automatically uses: flutter-expert → ios-developer → performance-engineer

# UI/UX implementation workflow
"Build a complete onboarding flow with animations"
# Automatically uses: ui-ux-designer → flutter-expert → test-automator

# Security and API integration workflow
"Add secure authentication with biometric login"
# Automatically uses: security-auditor → flutter-expert → ios-developer → test-automator

# Performance debugging workflow
"Fix app crashes and improve startup time"
# Automatically uses: debugger → performance-engineer → flutter-expert

# Production-ready feature workflow
"Implement payment processing with error handling"
# Automatically uses: flutter-expert → security-auditor → test-automator → api-documenter
```


## Subagent Format

Each subagent follows this structure:
```markdown
---
name: subagent-name
description: When this subagent should be invoked
model: haiku  # Optional - specify which model to use (haiku/sonnet/opus)
tools: tool1, tool2  # Optional - defaults to all tools
---

System prompt defining the subagent's role and capabilities
```

### Model Configuration

As of Claude Code v1.0.64, subagents can specify which Claude model they should use. This allows for cost-effective task delegation based on complexity:

- **Low Complexity (Haiku)**: Simple tasks like basic data analysis, documentation generation, and standard responses
- **Medium Complexity (Sonnet)**: Development tasks, code review, testing, and standard engineering work  
- **High Complexity (Opus)**: Critical tasks like security auditing, architecture review, incident response, and AI/ML engineering

Available models (using simplified naming as of Claude Code v1.0.64):
- `haiku` - Fast and cost-effective for simple tasks
- `sonnet` - Balanced performance for most development work
- `opus` - Most capable for complex analysis and critical tasks

If no model is specified, the subagent will use the system's default model.

## Agent Orchestration Patterns

Claude Code automatically coordinates agents using these common patterns:

### Sequential Workflows
```
User Request → Agent A → Agent B → Agent C → Result

Example: "Build a new API feature"
backend-architect → frontend-developer → test-automator → security-auditor
```

### Parallel Execution
```
User Request → Agent A + Agent B (simultaneously) → Merge Results

Example: "Optimize application performance" 
performance-engineer + database-optimizer → Combined recommendations
```

### Conditional Branching
```
User Request → Analysis → Route to appropriate specialist

Example: "Fix this bug"
debugger (analyzes) → Routes to: backend-architect OR frontend-developer OR devops-troubleshooter
```

### Review & Validation
```
Primary Agent → Review Agent → Final Result

Example: "Implement payment processing"
payment-integration → security-auditor → Validated implementation
```

## When to Use Which Agent

### 🏗️ Planning & Architecture
- **backend-architect**: API design, database schemas, system architecture
- **frontend-developer**: UI/UX planning, component architecture
- **ui-ux-designer**: Interface design, wireframes, design systems, user research
- **cloud-architect**: Infrastructure design, scalability planning

### 🔧 Implementation & Development  
- **python-pro**: Python-specific development tasks
- **ruby-pro**: Ruby metaprogramming, Rails applications, gem development, RSpec/Minitest testing
- **golang-pro**: Go-specific development tasks
- **rust-pro**: Rust-specific development, memory safety, systems programming
- **c-pro**: C programming, embedded systems, performance-critical code
- **javascript-pro**: Modern JavaScript, async patterns, Node.js/browser code
- **typescript-pro**: Advanced TypeScript, generics, type inference, enterprise patterns
- **java-pro**: Modern Java development, streams, concurrency, Spring Boot
- **elixir-pro**: Elixir development, OTP patterns, Phoenix frameworks, functional programming
- **csharp-pro**: Modern C# development, .NET frameworks, enterprise patterns
- **scala-pro**: Enterprise Scala with functional programming, Apache Pekko/Akka actors, Apache Spark, ZIO/Cats Effect, reactive architectures
- **flutter-expert**: Flutter development, Dart, state management, animations, cross-platform deployment
- **unity-developer**: Unity game development, C# scripting, performance optimization
- **minecraft-bukkit-pro**: Minecraft plugin development, event systems, server-side features
- **ios-developer**: Native iOS development with Swift/SwiftUI
- **sql-pro**: Database queries, schema design, query optimization
- **mobile-developer**: React Native/Flutter development

### 🛠️ Operations & Maintenance
- **devops-troubleshooter**: Production issues, deployment problems
- **incident-responder**: Critical outages requiring immediate response
- **database-optimizer**: Query performance, indexing strategies
- **database-admin**: Backup strategies, replication, user management, disaster recovery
- **terraform-specialist**: Infrastructure as Code, Terraform modules, state management
- **network-engineer**: Network connectivity, load balancers, SSL/TLS, DNS debugging

### 📊 Analysis & Optimization
- **performance-engineer**: Application bottlenecks, optimization
- **security-auditor**: Vulnerability scanning, compliance checks
- **data-scientist**: Data analysis, insights, reporting
- **mlops-engineer**: ML infrastructure, experiment tracking, model registries, pipeline automation

### 🧪 Quality Assurance
- **code-reviewer**: Code quality, configuration security, production reliability
- **test-automator**: Test strategy, test suite creation
- **debugger**: Bug investigation, error resolution
- **error-detective**: Log analysis, error pattern recognition, root cause analysis
- **search-specialist**: Deep web research, competitive analysis, fact-checking

### 📚 Documentation
- **api-documenter**: OpenAPI/Swagger specs, API documentation
- **docs-architect**: Comprehensive technical documentation, architecture guides, system manuals
- **reference-builder**: Exhaustive API references, configuration guides, parameter documentation
- **tutorial-engineer**: Step-by-step tutorials, learning paths, educational content

### 💼 Business & Strategy
- **business-analyst**: KPIs, revenue models, growth projections, investor metrics
- **risk-manager**: Portfolio risk, hedging strategies, R-multiples, position sizing
- **content-marketer**: SEO content, blog posts, social media, email campaigns
- **sales-automator**: Cold emails, follow-ups, proposals, lead nurturing
- **customer-support**: Support tickets, FAQs, help documentation, troubleshooting
- **legal-advisor** - Draft privacy policies, terms of service, disclaimers, and legal notices

## Best Practices

### 🎯 Task Delegation
1. **Let Claude Code delegate automatically** - The main agent analyzes context and selects optimal agents
2. **Be specific about requirements** - Include constraints, tech stack, and quality requirements
3. **Trust agent expertise** - Each agent is optimized for their domain

### 🔄 Multi-Agent Workflows
4. **Start with high-level requests** - Let agents coordinate complex multi-step tasks
5. **Provide context between agents** - Ensure agents have necessary background information
6. **Review integration points** - Check how different agents' outputs work together

### 🎛️ Explicit Control
7. **Use explicit invocation for specific needs** - When you want a particular expert's perspective
8. **Combine multiple agents strategically** - Different specialists can validate each other's work
9. **Request specific review patterns** - "Have security-auditor review backend-architect's API design"

### 📈 Optimization
10. **Monitor agent effectiveness** - Learn which agents work best for your use cases
11. **Iterate on complex tasks** - Use agent feedback to refine requirements
12. **Leverage agent strengths** - Match task complexity to agent capabilities

## Contributing

To add a new subagent:
1. Create a new `.md` file following the format above
2. Use lowercase, hyphen-separated names
3. Write clear descriptions for when the subagent should be used
4. Include specific instructions in the system prompt

## Troubleshooting

### Common Issues

**Agent not being invoked automatically:**
- Ensure your request clearly indicates the domain (e.g., "performance issue" → performance-engineer)
- Be specific about the task type (e.g., "review code" → code-reviewer)

**Unexpected agent selection:**
- Provide more context about your tech stack and requirements
- Use explicit invocation if you need a specific agent

**Multiple agents producing conflicting advice:**
- This is normal - different specialists may have different priorities
- Ask for clarification: "Reconcile the recommendations from security-auditor and performance-engineer"

**Agent seems to lack context:**
- Provide background information in your request
- Reference previous conversations or established patterns

### Getting Help

If agents aren't working as expected:
1. Check agent descriptions in their individual files
2. Try more specific language in your requests
3. Use explicit invocation to test specific agents
4. Provide more context about your project and goals

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Learn More

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Subagents Documentation](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Claude Code GitHub](https://github.com/anthropics/claude-code)
