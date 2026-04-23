# Daily Reflection Tree – Internship Assignment

## Overview

This project implements a structured reflection system using a decision tree model.
It simulates how a user moves through awareness, action, and reflection phases.

## Components

### 1. Reflection Tree

* Stored in `/tree/reflection-tree.json`
* Contains structured nodes (questions, decisions, actions, reflections)

### 2. Agent

* Located in `/agent/agent.py`
* Traverses the tree interactively or via predefined inputs
* Tracks user responses and outputs a summary

### 3. Transcripts

* Two personas:

  * Efficient (goal-oriented)
  * Distracted (avoidance behavior)

### 4. Diagram

* Visual representation of tree structure

---

## How to Run

```bash
cd agent
python agent.py
```

Choose:

* Interactive mode
* Auto mode (test persona)

---

## Design Philosophy

The tree models a behavioral loop:
Awareness → Decision → Action → Reflection

It is based on:

* Habit loops
* Cognitive load theory
* Behavioral feedback cycles

---

## Author

M Ashlesh Mallya
