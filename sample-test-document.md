# Sample Test Documents for Adversarial Analysis System

These sample documents are designed to test different aspects of the adversarial analysis system.

## Test Document 1: Simple Requirements (Quick Validation)

```markdown
# Mobile App Login System Requirements v1.0

## Overview
This document outlines requirements for implementing a user login system in our mobile application.

## Core Requirements

### Authentication
- Users must provide email and password to log in
- System should remember login status for 30 days
- Failed login attempts should be limited to 5 per hour

### Performance
- Login process must complete within 3 seconds
- System must handle 1000 concurrent login attempts

### Security  
- Passwords must be encrypted
- Two-factor authentication optional

## Success Criteria
- 95% of login attempts successful
- Zero security breaches in first 6 months
- User satisfaction score >4.0/5.0

## Timeline
- Development: 2 weeks
- Testing: 1 week  
- Deployment: 1 week
```

**Expected Test Results:**
- **Pro-side:** Should create well-structured analysis
- **Con-side:** Should find 3-5 moderate issues (vague requirements, missing details)
- **Process:** Should complete in 2-3 rounds

---

## Test Document 2: Flawed Requirements (Con-Side Testing)

```markdown
# Revolutionary AI-Powered Time Management App Requirements v1.0

## Vision
Create the world's best time management app that will replace all existing productivity tools and make everyone 500% more productive.

## Requirements

### Core Features
- AI that reads users' minds to predict their needs
- Automatic task completion using advanced algorithms
- Time travel functionality to give users extra hours
- 100% accuracy in predicting user behavior
- Zero learning curve - works perfectly immediately

### Technical Specifications  
- Works on all devices (phones, computers, smart toasters)
- Infinite scalability 
- Zero downtime ever
- Faster than the speed of light response times
- Uses no server resources or bandwidth

### Business Goals
- Capture 100% market share in 3 months
- Generate $1 billion revenue in first year
- Replace Google, Microsoft, and Apple as dominant tech company
- Eliminate all competing apps from existence

### Success Metrics
- Every user becomes perfectly productive
- World hunger solved through better time management
- Global happiness index reaches maximum
- Time itself becomes more efficient

## Budget & Timeline
- Development cost: $500 
- Timeline: 2 weeks total development
- Team size: 1 junior developer (part-time)
- Marketing budget: $50

## Risk Assessment
No risks identified. This project cannot fail.
```

**Expected Test Results:**
- **Con-side:** Should identify 8-10 critical issues (impossible features, unrealistic goals, insufficient budget)
- **Pro-side:** Should struggle to defend most points, requiring major document overhaul
- **Process:** Should run full 5 rounds

---

## Test Document 3: High-Quality Requirements (Early Termination Testing)

```markdown
# Customer Support Ticket System Requirements v2.3

## Executive Summary

This document specifies requirements for implementing a web-based customer support ticket system to replace our current email-based support process. The system aims to improve response times, track issue resolution, and provide better customer experience.

## Background and Context

### Current State
- Support requests handled via email (support@company.com)
- Average response time: 48 hours
- No systematic tracking of issues
- Customer satisfaction: 3.2/5.0
- Support team: 5 full-time agents

### Business Drivers  
- Improving customer satisfaction scores to >4.0/5.0
- Reducing average response time to <24 hours
- Better workload distribution among support agents
- Comprehensive reporting for management oversight

## Functional Requirements

### FR-001: Ticket Creation
- **Requirement:** Customers can submit tickets via web form
- **Details:** 
  - Required fields: Name, email, subject, description
  - Optional fields: Priority level, category, file attachments
  - Auto-generated unique ticket ID
  - Email confirmation sent to customer
- **Acceptance Criteria:**
  - Form validates all required fields
  - Ticket ID follows format: YYYY-MM-NNNNNN
  - Confirmation email sent within 5 minutes

### FR-002: Ticket Assignment  
- **Requirement:** System automatically assigns tickets to available agents
- **Details:**
  - Round-robin distribution by default
  - Skill-based routing for specialized categories
  - Priority tickets assigned to senior agents
  - Maximum 20 open tickets per agent
- **Acceptance Criteria:**
  - Assignment occurs within 1 minute of ticket creation
  - Load balancing maintains <15% variance between agents
  - Priority escalation rules followed correctly

### FR-003: Agent Workspace
- **Requirement:** Agents have dashboard to manage their tickets
- **Details:**
  - List view showing: ID, customer, subject, priority, age
  - Filtering by status, priority, category, date range
  - Quick actions: Update status, add notes, reassign
  - Email templates for common responses
- **Acceptance Criteria:**
  - Dashboard loads in <3 seconds
  - All filters function correctly
  - Email templates maintain formatting

### FR-004: Customer Communication
- **Requirement:** Customers receive updates on ticket progress
- **Details:**
  - Email notifications for status changes
  - Customer portal to view ticket history
  - Optional SMS notifications for urgent issues
  - Satisfaction survey after ticket closure
- **Acceptance Criteria:**
  - Emails sent within 10 minutes of status change
  - Portal shows real-time ticket status
  - Survey response rate >30%

## Non-Functional Requirements

### Performance
- System response time: <2 seconds for all user actions
- Support 500 concurrent users
- 99.5% uptime during business hours (8 AM - 6 PM EST)
- Database queries optimized for <500ms execution

### Security
- HTTPS encryption for all communications
- Role-based access control (admin, agent, customer)
- Audit logging for all ticket modifications
- GDPR compliance for customer data handling
- Regular security assessments quarterly

### Scalability
- Architecture supports growth to 2000 tickets/day
- Horizontal scaling capability for web servers
- Database partitioning strategy documented
- Performance monitoring and alerting implemented

## Technical Architecture

### Technology Stack
- **Frontend:** React.js with TypeScript
- **Backend:** Node.js with Express framework  
- **Database:** PostgreSQL 13+ with Redis caching
- **Email Service:** SendGrid API integration
- **Hosting:** AWS with auto-scaling groups
- **Monitoring:** CloudWatch with custom dashboards

### Integration Requirements
- **CRM Integration:** Sync customer data with Salesforce
- **Knowledge Base:** Link to existing help articles
- **Analytics:** Export data to Google Analytics
- **Single Sign-On:** SAML integration with company LDAP

## Implementation Plan

### Phase 1: Core System (Weeks 1-4)
- Basic ticket creation and assignment
- Agent dashboard with essential features
- Email notifications
- Administrative interface

### Phase 2: Enhanced Features (Weeks 5-8)  
- Customer portal development
- Advanced reporting capabilities
- CRM integration implementation
- Performance optimization

### Phase 3: Advanced Features (Weeks 9-12)
- Knowledge base integration
- Advanced automation rules  
- Mobile-responsive design
- Comprehensive testing and deployment

## Resource Requirements

### Development Team
- 1 Technical Lead (full-time, 12 weeks)
- 2 Full-stack Developers (full-time, 12 weeks) 
- 1 UI/UX Designer (half-time, 8 weeks)
- 1 QA Engineer (full-time, 6 weeks)

### Infrastructure Costs
- AWS hosting: $500/month estimated
- SendGrid email service: $200/month
- Third-party licenses: $300/month
- Development tools and services: $150/month

### Total Budget Estimate
- Development: $180,000 (team costs)
- Infrastructure Year 1: $13,800
- Third-party services Year 1: $6,000
- **Total Year 1:** $199,800

## Risk Assessment

### High-Risk Items
- **Integration Complexity:** Salesforce API changes could impact timeline
  - *Mitigation:* Early API testing, fallback manual sync process
- **Performance Requirements:** High concurrent user load  
  - *Mitigation:* Load testing throughout development, scalable architecture

### Medium-Risk Items  
- **User Adoption:** Staff resistance to new system
  - *Mitigation:* Comprehensive training program, gradual rollout
- **Data Migration:** Moving historical email data
  - *Mitigation:* Automated migration tools, validation procedures

### Low-Risk Items
- **Technology Familiarity:** Team experienced with chosen tech stack
- **Vendor Reliability:** AWS and SendGrid proven platforms

## Success Metrics

### Operational Metrics
- Average response time: Reduce from 48h to <24h
- Customer satisfaction: Improve from 3.2 to >4.0
- Ticket resolution rate: >95% within SLA
- System uptime: >99.5% during business hours

### Business Metrics
- Support cost per ticket: Reduce by 25%
- Agent productivity: Handle 30% more tickets
- Customer retention: Improve by 15%
- Escalation rate: <5% of tickets require management involvement

## Appendices

### Appendix A: Wireframes and UI Mockups
[Reference to design documents]

### Appendix B: Database Schema Design  
[Reference to technical specifications]

### Appendix C: API Documentation
[Reference to integration specifications]

### Appendix D: Testing Strategy
[Reference to QA plans and test cases]
```

**Expected Test Results:**
- **Con-side:** Should find only 0-2 minor issues (well-written document)
- **Process:** Should terminate early due to quality threshold
- **Data-researcher:** Should find supporting evidence for most claims

---

## Test Document 4: Edge Case - Empty/Minimal Document

```markdown
# Requirements Document

## Overview
We need a system.

## Requirements
- It should work
- Users should like it
- Make money

## Timeline
Soon.
```

**Expected Test Results:**
- **Con-side:** Should identify severe completeness issues (8-10 rejection points)
- **Pro-side:** Should request clarification and expand significantly
- **Process:** Should require full 5 rounds for major development

---

## How to Use These Test Documents

### Quick System Validation
1. Use Test Document 1 for basic functionality testing
2. Expected completion: 10-15 minutes total

### Comprehensive Testing
1. Use Test Document 2 to verify con-side finds major flaws
2. Use Test Document 3 to test early termination
3. Use Test Document 4 for edge case handling
4. Expected completion: 45-60 minutes total

### Testing Commands

#### For Individual Agent Testing:
```bash
"Use data-researcher to research customer support system best practices"
"Use pro-side-analyst to improve this requirements document: [paste Test Document 1]"
"Use con-side-analyst to critique this document: [paste Test Document 2]"
```

#### For Full System Testing:
```bash
"Use the adversarial analysis system to analyze this requirements document: [paste chosen test document]"
```

#### For Process Control Testing:
```bash
"Start adversarial analysis of this document and stop after exactly 3 rounds"
"Analyze this high-quality document and confirm early termination works"
```

These test documents provide comprehensive coverage of system functionality and edge cases.