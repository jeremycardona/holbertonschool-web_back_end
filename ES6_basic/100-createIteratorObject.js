export default function createIteratorObject(report) {
  const departments = Object.values(report.allEmployees);
  const employees = [];

  // Flatten all employees into a single array
  for (const deptEmployees of departments) {
    employees.push(...deptEmployees);
  }

  // Generator function to yield each employee
  function* employeeIterator() {
    for (const employee of employees) {
      yield employee;
    }
  }

  // Return the iterator object
  return {
    [Symbol.iterator]: employeeIterator,
  };
}
