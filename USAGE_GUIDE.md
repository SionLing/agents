# How to Use the Adversarial Document Analysis System

This guide explains how to use the optimized adversarial document analysis system to improve your requirements documents, analysis reports, and other critical business documents.

## Quick Start (5 Minutes)

### Step 1: Prepare Your Document
Place your document in the working directory or have it ready to paste into Claude Code.

### Step 2: Start Analysis
```bash
# Basic command - let the system auto-manage the process
"Run adversarial analysis on this document: [paste your document or provide file path]"

# Or be more specific
"Use the adversarial analysis system to analyze my requirements document for a mobile app project"
```

### Step 3: Monitor Progress
The system will automatically:
1. Create analysis output files in `[document_name]_output/` directory
2. Run up to 10 rounds of critique and improvement
3. Stop when quality threshold is reached (<3 Low-priority opinions)
4. Generate final comprehensive report

## Detailed Usage Instructions

### Method 1: Automatic Full Analysis (Recommended)

**Command:**
```bash
"Analyze this document using the complete adversarial analysis system: [document content or file path]"
```

**What Happens:**
1. **argument-orchestrator** manages the entire process
2. **data-researcher** gathers supporting evidence (if needed)
3. **con-side-analyst** identifies issues and assigns priorities
4. **pro-side-analyst** evaluates critiques and improves document
5. Process repeats until stop conditions met (10 rounds OR <3 Low-priority opinions)

**Output Files Generated:**
```
[document_name]_output/
├── round_1_con_opinions.md         # Con-side analysis with priorities
├── round_1_version_diff.md         # Changes made and reasoning  
├── [document_name]_v1.1.md         # Improved document version
├── round_2_con_opinions.md         # Next round analysis
├── round_2_version_diff.md         # Next round changes
├── [document_name]_v1.2.md         # Further improved version
└── final_analysis_report.md        # Complete process summary
```

### Method 2: Step-by-Step Manual Control

#### Step 1: Initial Analysis
```bash
"Use con-side-analyst to analyze this document and generate Round 1 opinions: [document]"
```
**Output:** `[document_name]_output/round_1_con_opinions.md` with prioritized opinions

#### Step 2: Document Improvement
```bash
"Use pro-side-analyst to respond to the con-side opinions and improve the document"
```
**Output:** 
- `[document_name]_output/round_1_version_diff.md` (changes made)
- `[document_name]_output/[document_name]_v1.1.md` (improved document)

#### Step 3: Continue or Stop
```bash
"Use argument-orchestrator to determine if we should continue analysis or stop"
```
**Decision based on:**
- Current round number (max 10)
- Opinion count and priorities from latest analysis

### Method 3: Targeted Analysis

#### Focus on Specific Aspects
```bash
"Use con-side-analyst to focus specifically on the technical feasibility of this requirements document"

"Use pro-side-analyst to strengthen the business justification sections based on market research"

"Use data-researcher to find supporting evidence for the cost estimates in this analysis"
```

## Understanding the Output Files

### Round Opinion Files (`round_[N]_con_opinions.md`)

**Structure:**
```markdown
# Con-Side Analysis Report - Round [N]

## Round [N] Opinions Summary
**High Priority**: 2 opinions    # Critical issues preventing implementation
**Normal Priority**: 3 opinions  # Significant problems reducing effectiveness  
**Low Priority**: 1 opinions     # Minor improvements

---

## Opinion [N].1: Missing Cost Analysis
**Priority**: High
**Category**: Completeness
**Section**: Implementation Plan

### Problem Description
The document lacks any cost estimation or budget analysis...

### Suggested Resolution
Add detailed cost breakdown including development, infrastructure, and operational costs...
```

### Version Diff Files (`round_[N]_version_diff.md`)

**Structure:**
```markdown
# Document Version Diff - Round [N]
**Original Version**: Requirements v1.0
**New Version**: Requirements v1.1

## Changes Made

### Change 1: Added Cost Analysis Section
**Reason**: Response to Opinion 1.1 (High Priority)
**Change Type**: Addition

#### Before (v1.0)
[No cost analysis section existed]

#### After (v1.1)  
## Cost Analysis
- Development: $150,000
- Infrastructure: $25,000/year
- Operational: $40,000/year

#### Rationale
Added comprehensive cost breakdown to address critical gap in financial planning...

## Changes Rejected

### Opinion 1.3: Change Technology Stack
**Priority**: Normal
**Decision**: Rejected
**Reasoning**: Current stack is well-established and changing would introduce unnecessary risk...
```

### Updated Document Versions (`[document_name]_v[X.Y].md`)

- Complete document with all accepted changes applied
- Ready for stakeholder review or implementation
- Version numbers track document evolution (v1.0 → v1.1 → v1.2, etc.)

## Stop Conditions Explained

### Quality Threshold Reached (Early Termination)
**Condition:** Fewer than 3 opinions AND all remaining opinions are Low priority

**Example:**
```
Round 4 Results:
- Opinion 4.1: Fix minor typo (Low Priority)
- Opinion 4.2: Improve formatting (Low Priority)

Result: STOP - Quality threshold achieved
```

### Round Limit Reached
**Condition:** 10 complete rounds finished

**Result:** Process stops regardless of remaining opinions, final report generated

## Best Practices

### 1. Document Preparation
- **Length:** Works best with 2-20 page documents
- **Format:** Markdown, plain text, or structured documents
- **Content:** Requirements documents, analysis reports, business plans, technical specifications
- **Language:** System works with multiple languages (tested with English and Chinese)

### 2. Optimal Usage Scenarios
- **Requirements Documents:** Business requirements, technical specifications, user stories
- **Analysis Reports:** Market analysis, feasibility studies, research reports  
- **Planning Documents:** Project plans, implementation roadmaps, strategy documents
- **Policy Documents:** Process documentation, governance frameworks, compliance guides

### 3. Review Process
- **Read Opinion Files:** Understand what issues were identified
- **Check Version Diffs:** See exactly what changed and why
- **Review Final Document:** Verify all changes make sense
- **Use Final Report:** Share process summary with stakeholders

## Advanced Usage

### Custom Research Integration
```bash
"Before starting adversarial analysis, use data-researcher to gather current market data about mobile app development costs and user retention statistics"
```

### Industry-Specific Analysis
```bash
"Run adversarial analysis on this healthcare requirements document, paying special attention to regulatory compliance and patient privacy"
```

### Multi-Document Analysis
```bash
"Analyze these three related documents as a suite: technical requirements, business requirements, and implementation plan"
```

## Troubleshooting

### Common Issues

#### Analysis Doesn't Start
**Problem:** System doesn't recognize the request
**Solution:** Use clearer language:
- "Run adversarial analysis on this document"
- "Use the adversarial analysis system to improve this document"

#### Files Not Generated
**Problem:** Output files missing from [document_name]_output directory
**Solution:** Check that:
- Claude Code has write permissions to the directory
- Document is properly formatted and readable
- Agents are functioning correctly (run individual agent tests)

#### Process Stops Too Early/Late
**Problem:** Analysis terminates unexpectedly or runs too long
**Solution:**
- Early termination: Document may already be high quality
- Runs too long: May have fundamental structural issues requiring manual intervention

#### Poor Quality Opinions
**Problem:** Con-side agent provides generic or unhelpful feedback
**Solution:** 
- Be more specific about document type and purpose
- Provide more context about intended audience and use case
- Try manual step-by-step approach for better control

### Getting Help

#### Test Individual Agents
```bash
"Use con-side-analyst to analyze this simple requirements document: [basic example]"
"Use pro-side-analyst to improve this section: [specific section]"
"Use data-researcher to find supporting evidence for [specific claim]"
```

#### Check System Status
```bash
"List all available agents and their current status"
"Show the contents of the [document_name]_output directory"
```

## Example Workflows

### Workflow 1: New Requirements Document
1. **Draft** initial requirements document
2. **Run** adversarial analysis: `"Analyze this requirements document for a customer portal project"`
3. **Review** opinion files to understand identified issues
4. **Check** version diffs to see what improvements were made
5. **Use** final document version for stakeholder review

### Workflow 2: Improving Existing Document
1. **Import** existing document that needs improvement
2. **Run** targeted analysis: `"Focus analysis on implementation feasibility and risk assessment"`
3. **Review** specific improvements in areas of concern
4. **Iterate** if needed: `"Continue analysis focusing on business justification"`

### Workflow 3: Collaborative Document Review
1. **Team creates** initial draft document
2. **Run** adversarial analysis for objective critique
3. **Share** opinion files with team to see identified issues
4. **Review** version diffs to understand suggested improvements
5. **Discuss** rejected opinions to confirm decisions
6. **Use** improved document as foundation for team refinement

## Success Metrics

### Document Quality Indicators
- **Completeness:** All required sections present and detailed
- **Evidence Support:** Claims backed by credible sources and data
- **Logic Consistency:** No internal contradictions or gaps
- **Implementation Readiness:** Clear, actionable requirements
- **Risk Management:** Potential issues identified and addressed

### Process Effectiveness
- **Opinion Resolution Rate:** >80% of High/Normal priority opinions addressed
- **Version Improvement:** Measurable enhancement in document quality
- **Stakeholder Readiness:** Document suitable for implementation/approval
- **Time Efficiency:** Significant improvement achieved within reasonable timeframe (typically 15-45 minutes)

The adversarial document analysis system is designed to be intuitive and powerful - start with the basic automatic analysis and explore advanced features as you become more comfortable with the system!