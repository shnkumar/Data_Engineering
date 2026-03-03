"""A quiet student is the one who took at least one exam and did not score the highest or the lowest score.

Write a solution to report the students (student_id, student_name) being quiet in all exams. Do not return the student who has never taken any exam.

Return the result table ordered by student_id.

The result format is in the following example.

 

Example 1:

Input: 
Student table:
+-------------+---------------+
| student_id  | student_name  |
+-------------+---------------+
| 1           | Daniel        |
| 2           | Jade          |
| 3           | Stella        |
| 4           | Jonathan      |
| 5           | Will          |
+-------------+---------------+
Exam table:
+------------+--------------+-----------+
| exam_id    | student_id   | score     |
+------------+--------------+-----------+
| 10         |     1        |    70     |
| 10         |     2        |    80     |
| 10         |     3        |    90     |
| 20         |     1        |    80     |
| 30         |     1        |    70     |
| 30         |     3        |    80     |
| 30         |     4        |    90     |
| 40         |     1        |    60     |
| 40         |     2        |    70     |
| 40         |     4        |    80     |
+------------+--------------+-----------+
Output: 
+-------------+---------------+
| student_id  | student_name  |
+-------------+---------------+
| 2           | Jade          |
+-------------+---------------+
Explanation: 
For exam 1: Student 1 and 3 hold the lowest and high scores respectively.
For exam 2: Student 1 hold both highest and lowest score.
For exam 3 and 4: Student 1 and 4 hold the lowest and high scores respectively.
Student 2 and 5 have never got the highest or lowest in any of the exams.
Since student 5 is not taking any exam, he is excluded from the result.
So, we only return the information of Student 2"""

"""
# Write your MySQL query statement below
# Write your MySQL query statement below
WITH flag AS (
		SELECT *
			,CASE 
				WHEN score = (max(score) OVER (PARTITION BY exam_id))
					THEN 1
				WHEN score = (min(score) OVER (PARTITION BY exam_id))
					THEN 1
				ELSE 0
				END AS flag
		FROM Exam
		)

SELECT f.student_id
	,s.student_name
FROM flag f
LEFT JOIN Student s ON f.student_id = s.student_id
GROUP BY f.student_id
HAVING sum(flag) = 0
ORDER BY f.student_id

"""
