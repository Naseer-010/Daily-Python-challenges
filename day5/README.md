# Emergency Resource Dispatch Analyzer

## Overview

This project is part of the **Python Code2Xplore – 60 Days Challenge (Day 5)**.
The program simulates a disaster management scenario where different zones request emergency resources. The system analyzes these requests, filters unrealistic or invalid entries, categorizes valid demands, and generates a final dispatch report based on a personalized rule.

---

## Problem Statement

During emergency drills, resource requests from various zones may contain:

* Invalid values (negative numbers)
* No-demand entries
* Low, moderate, or high demand values

The objective of this program is to:

1. Accept a list of integer requests.
2. Process each value using a **for loop**.
3. Classify requests into categories:

   * **Invalid Request** → value < 0
   * **No Demand** → value = 0
   * **Low Demand** → 1 to 20
   * **Moderate Demand** → 21 to 50
   * **High Demand** → above 50
4. Apply a **Personalized Logic Index (PLI)** rule.
5. Generate a final dispatch summary.

---

## Personalization Logic (PLI)

### Name Details

Full Name: **Naseer Hussain**

Length of name (excluding spaces):

* Naseer → 6 characters
* Hussain → 7 characters

Total length (L) = **13**

PLI Calculation:

```
PLI = L % 3
PLI = 13 % 3 = 1
```

### Applied Rule

**PLI = 1 → Rule B**

Rule B:
All **High Demand** requests are removed from the final dispatch report.

---

## Implementation Approach

The program follows these steps:

1. A list of resource requests is defined.
2. A **for loop** iterates through each request.
3. Conditional statements categorize each value into:

   * low_demand
   * moderate_demand
   * high_demand
   * invalid_requests
4. Requests with value **0** are ignored.
5. A counter tracks:

   * Total valid requests
   * Number of requests removed due to PLI
6. Based on the calculated PLI, the required category is filtered.
7. The final categorized lists and summary are printed.

---

## Input Used

```
[10, 25, 60, -3, 0, 45, 80]
```

---

## Output Summary (Based on PLI = 1)

* High demand requests are removed.
* Final dispatch includes only low and moderate demand values along with invalid entries.

---

## Constraints Followed

* Used lists for storage
* Used a **for loop** for processing
* Used conditional statements
* No list comprehension
* No dictionaries or sets
* No built-in functions like sum(), max(), min(), or sorting

---

## Personalization Summary

| Parameter    | Value              |
| ------------ | ------------------ |
| Name         | Naseer Hussain     |
| Length (L)   | 13                 |
| PLI          | 1                  |
| Applied Rule | Remove High Demand |

---

## Conclusion

This project demonstrates how basic Python constructs like loops, lists, and conditions can be used to simulate a real-world decision system. The personalization through PLI ensures that each student’s output and logic remain unique.
