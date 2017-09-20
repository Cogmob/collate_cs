public void transfer_funds()
    account source = new account()
    source.deposit(200m)

    account destination = new account()
    destination.deposit(150m)

    source.transfer_funds(destination, 100m)

    Assert.AreEqual(250m, destination.balance_prop)
    Assert.AreEqual(100m, source.balance_prop)
