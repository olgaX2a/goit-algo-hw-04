from pathlib import Path

def total_salary(path):
    file_path = Path(path)

    total = 0
    average = 0

    if(file_path.exists()):
        with open(path, "r", encoding='utf-8') as sd:
            lines = [el.strip() for el in sd.readlines()]

            employees_amount = len(lines)

            for line in lines:
                salary_data = line.split(',')
                total = total + int(salary_data[1]) 
            
            average = total / employees_amount
    
    else: 
        print('Provided path does not exist')
    
    return (total, average)