class Player extends User {
  constructor(userId, name, username, password, balance) {
    super(userId, name, username, password);
    this.balance = balance;
  }

  addBalance(amount) {
    this.balance += amount;
  }

  deductBalance(amount) {
    if (this.balance >= amount) {
      this.balance -= amount;
      return true;
    }
    return false;
  }
}
