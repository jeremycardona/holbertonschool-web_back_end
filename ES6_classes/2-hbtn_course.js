export default class HolbertonCourse {
  constructor(name, length, students) {
    // Verify attribute types during obj creation
    if (Object.getPrototypeOf(name) !== String.prototype) throw TypeError('name must be a string');
    if (Object.getPrototypeOf(length) !== Number.prototype) throw TypeError('length must be a number');
    if (Object.getPrototypeOf(students) !== Array.prototype) throw TypeError('students must be an array of strings');
    students.forEach((student) => {
      if (Object.getPrototypeOf(student) !== String.prototype) throw TypeError('students must be an array of strings');
    });

    // Create objs
    this._name = name;
    this._length = length;
    this._students = students;
  }

  // Setters
  set name(value) {
    if (Object.getPrototypeOf(value) !== String.prototype) throw TypeError('name must be a string');
    this._name = value;
  }

  set length(value) {
    if (Object.getPrototypeOf(value) !== Number.prototype) throw TypeError('length must be a number');
    this._length = value;
  }

  set students(value) {
    if (Object.getPrototypeOf(value) !== Array.prototype) throw TypeError('students must be an array');
    value.forEach((student) => {
      if (Object.getPrototypeOf(student) !== String.prototype) throw TypeError('students must be an array of strings');
    });
    this._students = value;
  }

  // Getters

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }
}
