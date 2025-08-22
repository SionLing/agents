# Testing Guide for Adversarial Document Analysis System

This guide provides comprehensive testing procedures to verify that all agents in the adversarial document analysis system work correctly together.

## Quick Start Testing

### 1. Individual Agent Testing

Test each agent separately before testing the full workflow:

#### Test Data Researcher
```bash
# In Claude Code, use:
"Use data-researcher to find evidence about mobile app user retention rates"
```
**Expected Output:**
- Structured research report with citations
- Multiple reliable sources (academic, industry reports)
- Clear confidence assessments
- Recent data (within 2-3 years)

#### Test Pro-Side Analyst
```bash
# In Claude Code, use:
"Use pro-side-analyst to create a requirements document for a mobile app analytics dashboard"
```
**Expected Output:**
- Well-structured document with clear sections
- Evidence-based requirements
- Success criteria and metrics
- Risk assessment section

#### Test Con-Side Analyst
```bash
# In Claude Code, provide the pro-side document and use:
"Use con-side-analyst to analyze this requirements document for flaws"
```
**Expected Output:**
- Up to 10 numbered rejection points
- Clear severity ratings (Critical/High/Medium/Low)
- Specific document section references
- Constructive improvement suggestions

#### Test Argument Orchestrator
```bash
# In Claude Code, use:
"Use argument-orchestrator to manage an analysis of this document"
```
**Expected Output:**
- Clear process status tracking
- Round counting (1-5)
- Stop condition monitoring
- Agent coordination instructions

### 2. End-to-End System Testing

#### Simple Test Case
```bash
"Analyze this simple requirements document using the adversarial analysis system: 

Requirements Document: Mobile App Login Feature
- Users must be able to log in with email/password
- Login must work within 3 seconds
- Failed logins should be tracked
- Password reset functionality required"
```

#### Complex Test Case
```bash
"Use the adversarial analysis system to evaluate this comprehensive business requirements document: [Attach a multi-page requirements document]"
```

## Detailed Testing Procedures

### Phase 1: Agent Availability Testing

#### Step 1: Check Agent Installation
```bash
# In Claude Code working directory, verify agent files exist:
ls -la *.md
```
**Should show:**
- data-researcher.md
- pro-side-analyst.md  
- con-side-analyst.md
- argument-orchestrator.md
- CLAUDE.md

#### Step 2: Agent Recognition Test
```bash
# Test if Claude Code can see the agents:
"List all available agents in this repository"
```
**Expected:** Claude should identify all 4 agents with their descriptions

### Phase 2: Individual Agent Validation

#### Data Researcher Validation
```bash
Test Command: "Use data-researcher to research cloud computing adoption rates in 2024"

Validation Checklist:
□ Uses WebSearch/WebFetch tools
□ Provides multiple credible sources
□ Includes source URLs and citations
□ Assesses data quality and recency
□ Identifies research gaps where applicable
□ Maintains objective tone
```

#### Pro-Side Analyst Validation
```bash
Test Command: "Use pro-side-analyst to create requirements for an e-commerce checkout system"

Validation Checklist:
□ Creates structured document with clear sections
□ Includes success criteria and metrics
□ Provides evidence-based rationale
□ Identifies risks and mitigation strategies
□ Uses professional, comprehensive format
□ Document is implementation-ready
```

#### Con-Side Analyst Validation
```bash
Test Command: "Use con-side-analyst to critique [the pro-side document from above]"

Validation Checklist:
□ Identifies specific, actionable issues
□ Uses severity ratings (Critical/High/Medium/Low)
□ References specific document sections
□ Provides up to 10 rejection points
□ Suggests improvement directions
□ Maintains constructive, professional tone
□ Focuses on legitimate flaws, not nitpicking
```

#### Argument Orchestrator Validation
```bash
Test Command: "Use argument-orchestrator to manage the analysis process"

Validation Checklist:
□ Tracks current round (1-5)
□ Counts rejection points accurately
□ Monitors stop conditions
□ Coordinates between other agents
□ Provides clear process status updates
□ Generates comprehensive final reports
```

### Phase 3: Integration Testing

#### Test Scenario 1: Basic Workflow
```bash
Input: Simple, flawed requirements document
Expected Flow:
1. Pro-side creates/refines document
2. Data-researcher provides supporting evidence  
3. Con-side identifies 5-7 issues
4. Pro-side addresses valid critiques
5. Process continues until <3 rejection points or 5 rounds
```

#### Test Scenario 2: High-Quality Document
```bash
Input: Well-written requirements document
Expected Flow:
1. Con-side finds only 1-2 minor issues
2. Process terminates early due to quality threshold
3. Orchestrator confirms successful completion
```

#### Test Scenario 3: Problematic Document
```bash
Input: Fundamentally flawed document
Expected Flow:
1. Con-side identifies 8-10 critical issues
2. Pro-side makes substantial improvements
3. Process runs full 5 rounds
4. Final document significantly improved
```

## Testing Checklists

### Pre-Test Setup Checklist
- [ ] All agent .md files present in repository
- [ ] Claude Code can access the working directory
- [ ] Internet connection available for data-researcher
- [ ] Test documents prepared

### Agent Communication Test
```bash
Test: "Have data-researcher find evidence, then pro-side-analyst use it to improve this document, then con-side-analyst critique the result"

Validation Points:
□ Agents reference each other's outputs
□ Data flows properly between agents
□ No contradictory instructions
□ Each agent builds on previous work
```

### Stop Condition Test
```bash
Test 1 - Round Limit: Use document that will take 5+ rounds
□ Process stops exactly at round 5
□ Final report generated correctly

Test 2 - Quality Threshold: Use high-quality document
□ Process stops when <3 rejection points achieved
□ Early termination handled properly
```

## Sample Test Documents

### Test Document 1: Simple (for quick validation)
```
Mobile App Requirements v1.0

Feature: User Registration
- Users can create accounts
- Email verification required
- Profile information collected

Success Metrics:
- Registration completion rate >80%
```

### Test Document 2: Complex (for full system testing)
```
Enterprise Data Analytics Platform Requirements v1.0

Executive Summary:
Our company needs a comprehensive data analytics platform to improve decision-making across all departments...

[Continue with 3-4 page detailed requirements document]
```

### Test Document 3: Intentionally Flawed (for con-side testing)
```
Requirements for Time Travel Application v1.0

Core Features:
- Travel to any point in history
- 100% accuracy guaranteed  
- No paradox risks
- Implementation by next month
- Budget: $1000

Success Criteria:
- Works perfectly on first try
```

## Troubleshooting Guide

### Common Issues and Solutions

#### Agent Not Responding
**Symptoms:** Agent doesn't activate when called
**Solutions:**
1. Check agent file exists and has correct YAML frontmatter
2. Verify agent name matches filename
3. Restart Claude Code session
4. Check for syntax errors in agent .md files

#### Poor Quality Outputs
**Symptoms:** Agent produces generic or irrelevant responses
**Solutions:**
1. Verify model assignment (opus/sonnet) is appropriate
2. Check if tools are specified correctly
3. Review system prompt for clarity
4. Test with more specific input prompts

#### Agents Don't Coordinate
**Symptoms:** Agents work individually but don't build on each other's work
**Solutions:**
1. Use argument-orchestrator to manage the process
2. Ensure agents are invoked in correct sequence
3. Check that outputs are properly formatted for next agent
4. Verify Read/Write tools are available for document sharing

#### Process Doesn't Stop
**Symptoms:** Analysis continues beyond expected termination
**Solutions:**
1. Check argument-orchestrator is properly counting rounds
2. Verify stop conditions are being evaluated correctly
3. Manual termination: "Stop the analysis process and provide final report"

#### Web Research Fails
**Symptoms:** Data-researcher can't find information
**Solutions:**
1. Check internet connectivity
2. Verify WebSearch/WebFetch tools are available
3. Try more specific search terms
4. Check if websites are accessible

## Performance Benchmarks

### Expected Response Times
- **Individual Agent Response:** 30-60 seconds
- **Full Round (all agents):** 3-5 minutes
- **Complete 5-Round Process:** 15-25 minutes

### Quality Metrics
- **Data Researcher:** >3 credible sources per research request
- **Pro-Side Analyst:** Documents with >5 clear requirements sections
- **Con-Side Analyst:** 4-8 rejection points for typical documents
- **Process Success Rate:** >90% of tests should complete successfully

## Advanced Testing

### Load Testing
Test with multiple documents simultaneously to verify system stability.

### Edge Case Testing
- Empty documents
- Documents in different formats
- Very long documents (>10 pages)
- Technical vs. business requirements
- Documents with intentional contradictions

### Integration Testing with Claude Code Features
Test compatibility with:
- File reading/writing operations
- Multi-step workflows
- Background processing
- Error handling and recovery

## Success Criteria

The system passes testing when:
- [ ] All 4 agents respond to individual calls
- [ ] End-to-end workflow completes successfully
- [ ] Stop conditions work correctly (both <3 points and 5 rounds)
- [ ] Document quality improves through iterations
- [ ] Agents coordinate effectively
- [ ] Final reports are comprehensive and accurate
- [ ] System handles edge cases gracefully

Run these tests after any changes to agent configurations or when setting up the system for the first time.