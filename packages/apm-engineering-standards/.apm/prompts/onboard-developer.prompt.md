---
description: Interactive developer onboarding experience to guide new team members.
input:
  - developer_name: "Name of the new developer"
  - role: "Role of the new developer (e.g., Backend, Frontend, Fullstack)"
allowed-tools: [bash, read, grep]
---

# Onboard Developer: ${input:developer_name}

Welcome ${input:developer_name}! I am the repository's AI agent. I will help you get familiar with our codebase and standards for your role as a **${input:role}**.

## Step 1: Discover Project Layout
First, I will run `ls -la` and examine the root directory to show you the basic structure of the repository. I will explain where the source code, tests, and configuration files live.

## Step 2: Explain Key Standards
Next, I will review the engineering standards present in my context (such as the `git-workflow` and `task-tracking` rules). I will summarize the most important conventions you need to know before making your first commit.

## Step 3: Interactive Q&A
Finally, I will open the floor for any questions you might have about specific modules, testing strategies, or how to build and run the project locally.

Let's begin with the project layout!
