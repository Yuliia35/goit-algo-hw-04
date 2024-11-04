import re
from pathlib import Path as File_work

def total_salary(path):
    try:
        total=0
        count=0
        with open(path, "r", encoding='utf-8') as File_work:
            for line in File_work:
                line=line.strip()
                if line:
                    parts=line.split(',')
                    if len(parts)==2:
                        salary=int(parts[1].strip())
                        total+=salary
                        count+=1
        average=int(total/count) if count>0 else 0
        return total,average
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found")
        return 0, 0
    except ValueError:
        print ("Error: Invalid data format in the file.")
        return 0, 0

total, average = total_salary("C:\Projects/File_work.txt")
print(f"Total salary: {total}, average salary: {average}")
