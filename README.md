# Factory Maintenance Assistant

An AI assistant that answers equipment troubleshooting questions from
maintenance manuals and past maintenance logs, with cited sources.

## Problem
On a factory floor, technicians lose 30+ minutes per breakdown searching long
PDF manuals and asking senior staff when a machine stops. Knowledge sits in
long PDF manuals and scattered maintenance logs.

## Users
- Primary: line maintenance technicians (junior to mid-level)
- Secondary: shift supervisors deciding whether to stop a line

## What it does (target by Oct 31)
- Answers questions from manuals with page citations (RAG)
- Checks past maintenance records for similar failures (agent tool)
- Asks a clarifying question when the input is too vague

## Success criteria
Initial targets, to be revised after the first evaluation run in Week 2.

- Retrieval: correct manual section in top 3 for >= 80% of test questions
- Answers: faithful to sources on >= 90% of a 25-question golden set
- Latency: < 5 s per answer; cost: < $0.01 per query

## Tech stack
Python, FastAPI, LangChain/LangGraph, Gemini API, Chroma, Docker, AWS

## Status
- [x] Week 0: environment and first LLM call
- [ ] Week 1: RAG API
- [ ] Week 2: agent + evaluation
- [ ] Week 3: deploy + monitoring
