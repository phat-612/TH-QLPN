class Room {
  constructor(roomId) {
    this.roomId = roomId;
    this.computers = [];
  }

  addComputer(computer) {
    this.computers.push(computer);
  }
}
