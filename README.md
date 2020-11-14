# SSD Assignment-3C

GitHub Repo: https://github.com/mansi-k/SSD_A3p1
branch: partC

### Question1
#### Changes:
Modularized the code using functions
#### Cyclomatic Complexity:
![alt text](https://github.com/mansi-k/SSD_A3p1/blob/partC/q1tc.png)
#### Assumptions/Working:
1. Input file (org.json) is assumed to be in proper json format (with double quotes for all keys and values) and with the same attributes as shown in the example except for the numbers (enclsosed in "") instead of A,B,C... for emp name.
2. Input for 2 employee names is taken as 2 space separated strings. Eg: name1 name2.
3. Output is printed on the terminal only (not in txt file).
4. Lowest common leader is given as output.
5. It's assumed that no employee would be his own leader. 
6. It's assumed that levels in the input are ordered and no level is skipped and that an employee has his leader in the immediate preceding level (level-1).
7. If no common leader exists, then "No common leader" is printed.
8. I/O format as mentioned in moodle comments:
`Input:`
<emp1> <emp2>
`Output:`
<xyz>
<xyz> is <number> levels above <emp1>
<xyz> is <number> levels above <emp2>

### Question2
#### Changes:
Modularized the code using functions
#### Cyclomatic Complexity:
![alt text](https://github.com/mansi-k/SSD_A3p1/blob/partC/q2tc.png)
#### Assumptions/Working:
1. It's assumed that the input file (date_calculator.txt) would be in the same format as given in example (Date1: and Date2: mentioned) and with only 2 dates.
2. All date inputs are considers to be valid and only in the given formats.
3. Eg: 10th September, 2020 : there should be space after comma.
4. Output is printed on the terminal as well as written in the output.txt file.
5. Output format : "Date Difference: N days".
6. The program is tested by comparing the results with difference that the datetime library gives.


### Question3
#### Changes:
Modularized the code using functions. Keep employee.txt files in q3_emp folder.
#### Cyclomatic Complexity:
![alt text](https://github.com/mansi-k/SSD_A3p1/blob/partC/q3tc.png)
#### Assumptions/Working:
1. All the .txt files to be given as input should be placed inside q3_emp folder.
2. It's assumed that all the files would have only one date. If dates vary, then "No slot available" is printed.
3. It's assumed that the input slots would be in the ascending order (as mentioned in moodle comments).
4. The slot duration in hours is taken as input from the terminal in decimal format (Eg: 1, 1.5, 2.25)
5. The output is written in a file (output.txt) as well as printed on the terminal.
6. Whether there exists a common slot or not, the list of all available slots for each employee is shown.
7. It was mentioned in moodle that datetime library could be used for this question
8. If no common slot is found, "No slot available" is shown.

