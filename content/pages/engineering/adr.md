Title: Architecture Decision Records
Date: Tue 11 Sep 2021 13:56:10 AEST
Category: Engineering 
Tags: development,agile,architecture,decisions
Slug: adr 
Author: Oliver Daff
Summary: How we document our decisions

- [Introduction](#introduction)
- [ADR Structure](#adr-structure)
    - [Title](#title)
    - [Status](#status)
    - [Context](#context)
    - [Decision](#decision)
    - [Alternatives](#alternatives)
    - [Consequences](#consequences)
    - [Compliance](#compliance)
    - [Notes](#notes)
- [Storage](#storage)
  - [Template](#template)
- [References](#references)


In this section we explain how we document and communicate our decisions.

# Introduction

The harrison.ai data engineering team record their decisions using Architectural Decision Records (ADR).  [ADR](https://adr.github.io/) were first mentioned by Michael Nygard in a [blog post](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).  Architectural decisions are those which impact the structure of the application, nonfunctional characteristics, dependencies, interfaces or construction techniques.

We understand that communicating the why is just as important as the how.  By using ADR we ensure we have a clear record of our decisions and why we made them letting us learn as as team.  By using ADR we choose to avoid email driven decisions by establishing a single system of record.  ARD allows everyone to see why a decision was made capturing both the technical and business considerations relevant to the decision.

# ADR Structure
The ADR contains eight sections:

### Title
The title of the ADR is a sequentially numbered record and includes a short concise description of the architectural decision.

### Status
The ADR can be in one of five states:
*	RFC (Request for Change)
*	Proposed
*	Accepted
*	Superseded

To start initial discussions the ADR should be raised in a RFC status.  A RFC status must have a deadline by which all comments must be submitted.
A Proposed ADR must be reviewed by the team through the PR process and discussed.  At this point cost, cross team impact and security concerns must be considered to indicate if a wider group needs to be included in the discussions.
An accepted ADR is implemented by the team and part of the architecture of the system.
An ADR may supersede another ADR based on lessons learnt or changes in requirements of technologies.

It is important that the link between superseded ADRs be maintained so a memory of the decisions and their motivations exist.

### Context
The context of an ADR answers the question `what is forcing me to make this decision?`.  The context section allows the current architecture and requirements to be described "The Orchestration service must pass information to the metadata catalogue service to find which files need to be retrieved from storage this could be done via REST or async messaging".

### Decision
The decision section contains both the decision along with the full justification of why this decision was reached.  This section should focus on the why rather than the how to help the team understand why the decision was made rather than how it works.

### Alternatives
The alternatives section should highlight any alternative options which were considered and why they were not chosen.

### Consequences
Every decision has tradeoffs so focus on the impact of a decision to see if the good outweighs the bad.  Documenting the tradeoffs helps those who come afterwards see the ideas that were considered and discussed.

### Compliance
How will this decision be measured and governed by the team?  Will this be a manual process or can it be automated with a fitness function?

### Notes
The notes section contains meta data

*	Original author
*	Approval Date
*	Approved by
*	Superseded date
*	Last modified date
*	Last modified by
*	Last modification


# Storage
The ADR files are stored in git with their respective applications in a `ADR` folder.  All `ADR` folders are linked to from the `ADR` repository.
ADRs that cross bounded contexts are stored in the `ADR` repository.


## Template
```
# TITLE
Number followed by a short concise description of the decision.

#Status
RFC, Proposed, Accepted, Superseded

#Context
What is forcing me to make this decision?

#Decision
What is the decision and why is this the correct one?

#Alternatives
What alternatives were considered and why were they not accepted?

#Consequences
What is the impact of this decision?

#Compliance
How will the team ensure compliance with this decision?

#Notes

*	Original author
*	Approval Date
*	Approved by
*	Superseded date
*	Last modified date
*	Last modified by
*	Last modification
```



# References
The following books, articles and blogs were referenced in the creation of this content.

* https://adr.github.io/ .
*  Richards, Mark, and Neal Ford. _Fundamentals of Software Architecture: An Engineering Approach_. First edition. Beijing Boston Farnham Sebastopol Tokyo: O’Reilly, 2020.
*  https://github.com/joelparkerhenderson/architecture-decision-record
*  https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
*  https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records
