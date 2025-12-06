## README: GradeBook Analyzer

The `GradeBook Analyzer` is a Python script designed to process student marks, perform statistical analysis, assign grades, and present the results in a clear, formatted manner.

### Project Files

  * "gradebook.py": The core Python script containing all the logic for data input, calculations, grade assignment, and output.
  * "students.csv": A sample CSV file containing student names and their corresponding marks, used as input for the "Load from CSV" option.

### How to Run the Program

1.  **Prerequisites**: Ensure you have **Python 3** installed on your system.

2.  **Execution**: Open your terminal or command prompt, navigate to the directory where the files are saved, and run the script:

    ```bash
    python gradebook.py
    ```

### Program Usage

The program runs in a **Command Line Interface (CLI)** loop, presenting a menu of options.

#### Main Menu
===== GradeBook Analyzer =====

1. Manual entry
2. Load from CSV
3. Exit

Choose an option (1-3):
```

1.  **Manual Entry**: Allows the user to type in student names and their marks one by one. The input loop stops when an empty name is entered.
2.  **Load from CSV**: Prompts the user for a CSV filename. The program will read the data, assuming a format of `Name, Mark` per line (e.g., as in `students.csv`).
3.  **Exit**: Terminates the program.

#### Output

After successfully loading data (either manually or from CSV), the script will display a comprehensive analysis:

1.  **Statistical Summary**: Calculates and displays the **average** and **median** scores, and identifies the student with the **highest** and **lowest** scores.
2.  **Grade Distribution**: Shows the count of students who received each grade (A, B, C, D, F).
3.  **Pass / Fail**: Lists the names of students who passed (score $\ge 40$) and those who failed (score $< 40$).
4.  **Results Table**: Prints a formatted table showing each student's **Name**, **Marks**, and assigned **Grade**.

-----

### Data Structure and CSV Format

The program expects student data to be stored internally as a Python dictionary where the **key** is the student's name (`str`) and the **value** is their mark (`float`).

#### Example CSV Format (`students.csv`)

The `load_from_csv` function is designed to handle a simple two-column CSV structure:

| Name | Mark |
| :--- | :--- |
| Alice | 78.5 |
| Bob | 92 |
| Charlie | 35 |
| ... | ... |

*(Note: The provided `students.csv` file has a header line: `Name,Mark`. The current implementation of `load_from_csv` does **not** skip a header by default; if a header is present, the script would need a minor modification, such as uncommenting the `next(reader, None)` line.)*

-----

### Functions Implemented

The `gradebook.py` script is structured around several functions, corresponding to the assignment tasks:

| Function Category | Function Name | Description | Task |
| :--- | :--- | :--- | :--- |
| **Statistical** | `calculate_average` | Calculates the average score. | Task 3 |
| | `calculate_median` | Calculates the median score. | Task 3 |
| | `find_max_score` | Finds the name and score of the highest-scoring student. | Task 3 |
| | `find_min_score` | Finds the name and score of the lowest-scoring student. | Task 3 |
| **Grading** | `assign_grade` | Maps a score to a letter grade (A: $\ge 90$, B: $\ge 80$, C: $\ge 70$, D: $\ge 60$, F: $< 60$). | Task 4 |
| | `build_grades_dict` | Creates a dictionary mapping student names to their letter grades. | Task 4 |
| | `grade_distribution` | Calculates the count for each letter grade. | Task 4 |
| **Input** | `manual_entry` | Handles interactive input from the user. | Task 2 |
| | `load_from_csv` | Reads and processes student data from a specified CSV file. | Task 2 |
| **Pass/Fail** | `get_pass_fail_lists` | Separates students into **passed** ($\ge 40$) and **failed** ($< 40$) lists using **list comprehension**. | Task 5 |
| **Output** | `print_results_table` | Prints the final, formatted table of all results. | Task 6 |
| **Main** | `main` | Manages the main menu, user interaction, and function calls. | Task 1 & 6 |

-----

### Example: Loading `students.csv`

If you choose option **2** and enter `students.csv`, the program will load the data:

  * **Alice**: 78.5
  * **Bob**: 92
  * **Charlie**: 35
  * **Diana**: 66
  * **Ethan**: 91.2
  * **Fiona**: 59.9
  * **Greg**: 80

And then generate the full report.
