class Employee extends User {
  constructor(userId, name, username, password, address, phone) {
    super(userId, name, username, password);
    this.address = address;
    this.phone = phone;
  }
}
