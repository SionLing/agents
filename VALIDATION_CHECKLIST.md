# Agent Validation Checklist

Use this checklist to systematically verify that each agent in the adversarial document analysis system is working correctly.

## Pre-Testing Setup ✅

### Environment Verification
- [ ] All agent files (.md) are present in the repository
- [ ] Claude Code has access to the working directory
- [ ] Internet connection is available for data-researcher
- [ ] CLAUDE.md file is properly configured
- [ ] Test documents are prepared

### Agent File Integrity
- [ ] **data-researcher.md** - File exists and has correct YAML frontmatter
- [ ] **pro-side-analyst.md** - File exists and has correct YAML frontmatter  
- [ ] **con-side-analyst.md** - File exists and has correct YAML frontmatter
- [ ] **argument-orchestrator.md** - File exists and has correct YAML frontmatter

### Claude Code Agent Recognition
- [ ] Claude Code can list all 4 agents when asked
- [ ] Agent descriptions are properly displayed
- [ ] No syntax errors in agent definitions

---

## Individual Agent Validation

### 🔍 Data-Researcher Agent

#### Basic Functionality Test
**Test Command:** `"Use data-researcher to research mobile app user engagement statistics"`

#### Validation Checklist:
- [ ] **Tool Usage:** Agent uses WebSearch and/or WebFetch tools
- [ ] **Source Quality:** Provides 3+ credible sources (academic, industry, government)
- [ ] **Citations:** Includes proper URLs and source references
- [ ] **Recency:** Prioritizes recent data (within 2-3 years)
- [ ] **Structure:** Uses organized report format
- [ ] **Objectivity:** Presents information without bias
- [ ] **Quality Assessment:** Evaluates source credibility
- [ ] **Gaps Identification:** Notes areas where data is limited

#### Advanced Functionality Test
**Test Command:** `"Research conflicting evidence about remote work productivity"`

- [ ] **Multiple Perspectives:** Finds both supporting and contradictory evidence
- [ ] **Cross-Verification:** Seeks multiple sources for claims
- [ ] **Bias Recognition:** Identifies potential source biases
- [ ] **Methodology Analysis:** Comments on study quality when relevant

---

### 📝 Pro-Side Analyst Agent

#### Basic Functionality Test  
**Test Command:** `"Use pro-side-analyst to create requirements for an online booking system"`

#### Validation Checklist:
- [ ] **Document Structure:** Creates well-organized document with clear sections
- [ ] **Completeness:** Includes all major requirement categories
- [ ] **Evidence-Based:** Supports claims with rationale
- [ ] **Success Criteria:** Defines measurable outcomes
- [ ] **Risk Assessment:** Identifies potential challenges
- [ ] **Professional Format:** Uses appropriate business document style
- [ ] **Implementation Focus:** Requirements are actionable
- [ ] **Stakeholder Consideration:** Addresses different user needs

#### Critique Response Test
**Test Command:** `"Respond to these critiques of your document: [provide 3-5 mock rejection points]"`

- [ ] **Systematic Analysis:** Addresses each critique individually  
- [ ] **Categorization:** Properly classifies critiques (accept/reject/mitigate)
- [ ] **Evidence Support:** Provides rationale for all responses
- [ ] **Document Updates:** Makes appropriate revisions when accepting critiques
- [ ] **Change Documentation:** Clearly explains what changed and why
- [ ] **Defense Quality:** Provides solid justification for rejected critiques

---

### 🔍 Con-Side Analyst Agent

#### Basic Functionality Test
**Test Command:** `"Use con-side-analyst to critique this requirements document: [provide sample document]"`

#### Validation Checklist:
- [ ] **Issue Identification:** Finds legitimate problems in the document
- [ ] **Rejection Point Count:** Provides 1-10 points (appropriate to document quality)
- [ ] **Severity Ratings:** Uses Critical/High/Medium/Low classifications correctly
- [ ] **Specific References:** Cites exact document sections/lines
- [ ] **Constructive Tone:** Maintains professional, helpful approach
- [ ] **Evidence-Based:** Supports critiques with logical reasoning
- [ ] **Improvement Suggestions:** Provides actionable guidance
- [ ] **Structured Format:** Uses consistent rejection point format

#### Quality Assessment Test
**Test Command:** `"Analyze this high-quality document: [provide well-written requirements]"`

- [ ] **Appropriate Response:** Finds fewer issues with better documents
- [ ] **Minor Issues Focus:** Identifies remaining improvement opportunities
- [ ] **Acknowledges Quality:** Recognizes strong aspects of good documents
- [ ] **Proportional Criticism:** Criticism matches actual document quality

#### Flawed Document Test  
**Test Command:** `"Critique this problematic document: [provide intentionally flawed requirements]"`

- [ ] **Major Issue Detection:** Identifies fundamental problems
- [ ] **Priority Ranking:** Addresses most critical issues first
- [ ] **Comprehensive Analysis:** Covers multiple problem categories
- [ ] **Impact Assessment:** Explains why issues matter

---

### 🎯 Argument Orchestrator Agent

#### Basic Functionality Test
**Test Command:** `"Use argument-orchestrator to manage analysis of this document"`

#### Validation Checklist:
- [ ] **Process Initialization:** Properly starts the analysis workflow
- [ ] **Agent Coordination:** Successfully invokes other agents in sequence
- [ ] **Progress Tracking:** Maintains accurate round counting
- [ ] **Status Updates:** Provides clear process status reports
- [ ] **Stop Condition Monitoring:** Correctly evaluates termination criteria
- [ ] **Final Reporting:** Generates comprehensive analysis summaries

#### Stop Condition Test - Round Limit
**Test Command:** `"Manage analysis ensuring it stops at exactly 5 rounds"`

- [ ] **Round Counting:** Accurately tracks 1-5 rounds
- [ ] **Force Stop:** Terminates at round 5 regardless of rejection points
- [ ] **Final Report:** Generates complete process summary
- [ ] **Status Communication:** Clearly explains why process stopped

#### Stop Condition Test - Quality Threshold  
**Test Command:** `"Manage analysis of high-quality document to test early termination"`

- [ ] **Point Counting:** Accurately counts rejection points
- [ ] **Early Termination:** Stops when <3 rejection points achieved
- [ ] **Success Recognition:** Identifies when quality threshold is met
- [ ] **Efficiency:** Doesn't continue unnecessarily when quality achieved

---

## Integration Testing

### 🔄 Agent-to-Agent Communication

#### Data Flow Test
**Test Command:** `"Have data-researcher find evidence, then pro-side-analyst use it, then con-side-analyst critique the result"`

#### Validation Checklist:
- [ ] **Sequential Processing:** Each agent builds on previous agent's output
- [ ] **Data Utilization:** Later agents reference earlier agents' findings
- [ ] **Context Preservation:** Information flows correctly between agents
- [ ] **No Contradictions:** Agents don't provide conflicting guidance
- [ ] **Collaborative Output:** Final result shows input from all agents

### 🔁 Full Workflow Integration

#### Complete Process Test
**Test Command:** `"Run complete adversarial analysis on [test document]"`

#### Validation Checklist:
- [ ] **Process Initiation:** System starts correctly with document analysis
- [ ] **Agent Sequence:** All agents participate in correct order
- [ ] **Iteration Logic:** Multiple rounds work properly
- [ ] **Document Evolution:** Document improves through iterations
- [ ] **Progress Tracking:** Clear visibility into process status
- [ ] **Natural Termination:** Process stops at appropriate conditions
- [ ] **Final Deliverables:** Complete report and optimized document provided

---

## Performance Validation

### ⏱️ Response Time Testing
- [ ] **Individual Agent Response:** <60 seconds per agent call
- [ ] **Full Round Completion:** <5 minutes for complete cycle
- [ ] **Process Completion:** <25 minutes for full 5-round analysis
- [ ] **Web Research Speed:** <90 seconds for data-researcher queries

### 📊 Quality Metrics
- [ ] **Research Quality:** Data-researcher provides >3 credible sources consistently
- [ ] **Document Quality:** Pro-side creates comprehensive, structured documents
- [ ] **Critique Quality:** Con-side identifies 4-8 legitimate issues in typical documents
- [ ] **Process Success:** >90% of tests complete without errors

---

## Edge Case Validation

### 📄 Document Types
- [ ] **Empty Document:** System handles minimal input gracefully
- [ ] **Long Document:** Works with 10+ page requirements
- [ ] **Technical Document:** Handles specialized technical requirements
- [ ] **Business Document:** Works with business process requirements
- [ ] **Flawed Document:** Properly identifies and addresses major problems

### 🚨 Error Handling
- [ ] **Network Issues:** Data-researcher handles connection problems
- [ ] **Invalid Input:** Agents respond appropriately to unclear instructions
- [ ] **Tool Failures:** System continues when individual tools have issues
- [ ] **Process Interruption:** Can resume or restart cleanly

---

## Final System Validation

### ✅ Success Criteria
The system passes validation when:
- [ ] All individual agents respond correctly to test commands
- [ ] Full workflow completes successfully with test documents
- [ ] Stop conditions (rounds and quality threshold) work properly
- [ ] Document quality improves measurably through iterations
- [ ] Agents coordinate effectively without conflicts
- [ ] Final reports are comprehensive and accurate
- [ ] Performance meets expected benchmarks
- [ ] Edge cases are handled gracefully

### 📝 Documentation Review
- [ ] CLAUDE.md accurately describes system capabilities
- [ ] Agent descriptions match actual behavior
- [ ] Testing guide is accurate and complete
- [ ] Troubleshooting procedures are effective

### 🎯 Ready for Production
- [ ] All validation items above are checked ✅
- [ ] System consistently produces high-quality results
- [ ] Users can successfully operate the system
- [ ] Documentation is complete and accurate

---

## Quick Validation Command

For rapid system validation, use this single comprehensive test:

```bash
"Run adversarial analysis on this test document: 

Mobile App Push Notification System Requirements v1.0

Core Requirements:
- Send notifications to users when important events occur
- Allow users to customize notification preferences  
- Track notification delivery and engagement rates
- Support both iOS and Android platforms

Success Metrics:
- 95% notification delivery rate
- <5% unsubscribe rate
- Improved user engagement by 20%

Timeline: 6 weeks development, 2 weeks testing"
```

**Expected Results:**
- Process should complete in 15-20 minutes
- 2-3 rounds typically needed
- Document should be significantly improved
- All agents should contribute meaningfully

If this test passes completely, your system is ready for production use!