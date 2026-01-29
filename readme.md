# Day 1 – User Profile Validator

This script checks whether basic user details entered from the terminal follow a few predefined rules. It uses straightforward Python logic without any external libraries.

### What the program checks

* **Name** should contain a space and must not start or end with one
* **Email** should contain exactly one `@`, with no spaces
* **Mobile number** must be numeric, 10 digits long, and not start with `0`
* **Age** must fall between **18 and 60**

### How to use

Run the script and enter the details when prompted:

```bash
python user_profile_validation_system.py
```
This program will then tell you whether the prifile is valid or not.

### Purpose
This challange focuses on practicing
- User input handling
- Conditions checks
- Basic exception handling