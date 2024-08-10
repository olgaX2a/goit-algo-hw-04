def total_salary(path):
    with open(path, "r") as sd:
        lines = [el.strip() for el in sd.readlines()]

        employees_amount = len(lines)
        
        total = 0

        for line in lines:
            salary_data = line.split(',')
            total = total + int(salary_data[1]) 
        
        average = total / employees_amount

        return (total, average)
