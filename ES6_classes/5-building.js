export default class Building {
  constructor(sqft) {
    if (new.target === Building) {
      throw new TypeError('Cannot construct Building instances directly');
    }
    this.sqft = sqft;
  }

  // Getter for sqft
  get sqft() {
    return this._sqft;
  }

  // Setter for sqft
  set sqft(value) {
    if (typeof value !== 'number') {
      throw new TypeError('sqft must be a number');
    }
    this._sqft = value;
  }

  // Abstract method (must be implemented by subclasses)
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}

// Example subclass that correctly implements the abstract method
class OfficeBuilding extends Building {
  evacuationWarningMessage() {
    return 'Evacuate the office building immediately!';
  }
}
