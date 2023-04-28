import csv

with open('challenge.csv', newline='') as csvfile:

    reader = csv.DictReader(csvfile)

    department_expenses = {}

    for row in reader:
        department = row['Department']
        exspense = row['2012 Actual']

        if exspense:
            exspense = float(exspense)
        
            if department in department_expenses:
                department_expenses[department] += exspense
            else:
                department_expenses[department] = exspense

    for department, expenses in department_expenses.items():
        formatted_exspense = '${:,.2f}'.format(expenses)
        
        print(f'{department}\t{formatted_exspense}')
