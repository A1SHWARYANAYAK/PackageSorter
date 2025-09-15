# Package Sorter

## Overview

A simple package sorting system that categorizes packages into three stacks (STANDARD, SPECIAL, or REJECTED) based on their physical dimensions and mass. The system uses volume and dimensional thresholds to determine if packages are "bulky" and mass thresholds to determine if they are "heavy", then applies sorting rules to classify each package appropriately.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Core Logic Design
The system implements a rule-based classification algorithm using boolean logic and ternary operators for clean, readable code. The main sorting function calculates package volume and evaluates two key criteria:

- **Bulky Classification**: Packages with volume ≥ 1,000,000 cm³ OR any dimension ≥ 150cm
- **Heavy Classification**: Packages with mass ≥ 20kg

### Sorting Rules
The system uses a hierarchical decision tree:
1. **REJECTED**: Packages that are both heavy AND bulky
2. **SPECIAL**: Packages that are either heavy OR bulky (but not both)
3. **STANDARD**: All other packages

### Code Organization
- Single-file architecture with focused functionality
- Pure functions with no side effects for easy testing
- Comprehensive test suite with edge cases and boundary conditions
- Clear separation between core logic and testing functionality

### Design Decisions
- **Ternary Operators**: Chosen for concise, readable conditional logic over traditional if-else blocks
- **Threshold-Based Classification**: Simple numerical thresholds provide clear, deterministic sorting rules
- **Volume Calculation**: Direct multiplication approach for straightforward dimensional analysis

## External Dependencies

This is a standalone Python application with no external dependencies. It uses only Python's built-in functions and standard library features.
