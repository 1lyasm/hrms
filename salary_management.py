class SalaryManagementSystem:
    def __init__(self, budget, tax_rate):
        self.budget = budget
        self.tax_rate = tax_rate

    def calculate_net_salary(self, employee):
        tax = employee.salary * self.tax_rate
        net_salary = employee.salary - tax
        return net_salary

    def calculate_total_salary_cost(self):
        total_cost = sum(employee.salary for employee in self.employees)
        return total_cost

    def make_salary_payments(self):
        total_cost = self.calculate_total_salary_cost()
        if total_cost <= self.budget:
            for employee in self.employees:
                net_salary = self.calculate_net_salary(employee)
                print(f"Employee: {employee.name}, Position: {employee.position}, Net Salary: {net_salary}")
        else:
            print("Insufficient budget to make salary payments.")


# salary_management_system = SalaryManagementSystem(budget=100000000, tax_rate=0.2)
