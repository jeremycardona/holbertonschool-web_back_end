import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this.floors = floors;
  }

  // Getter for floors
  get floors() {
    return this._floors;
  }

  // Setter for floors
  set floors(value) {
    if (typeof value !== 'number') {
      throw new TypeError('floors must be a number');
    }
    this._floors = value;
  }

  // Override the evacuationWarningMessage method
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors.`;
  }
}
