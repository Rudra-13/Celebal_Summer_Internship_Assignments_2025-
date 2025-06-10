select
case when grades.grade >= 8 then students.name else 'NULL' end as name,
  grades.grade,
  students.marks
from students
join grades on students.marks between grades.min_mark and grades.max_mark
order by 
  grades.grade desc,
  case when grades.grade >= 8 then students.name end asc,
  case when grades.grade < 8 then students.marks end asc;