class Transaction {
  constructor(transactionId, playerId, amount, transactionType, timestamp) {
    this.transactionId = transactionId;
    this.playerId = playerId;
    this.amount = amount;
    this.transactionType = transactionType;
    this.timestamp = timestamp;
  }
}
