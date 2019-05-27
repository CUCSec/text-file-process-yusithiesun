
import os
with open("text-file-process-yusithiesun\\text-file-process\\log_files\\201811113003.log",encoding='utf-8') as f:
  counter=0
  for line in f:
    student_id=line.split(',')[1]
    student_id=student_id.strip()
    print(student_id)
    if student_id[3:]=='201811113003':
      counter+=1
  print(counter)

