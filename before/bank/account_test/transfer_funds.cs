public void _method()
    account source = (new account
        balance = 0 
    )

    source.deposit(200m)

    if (source.balance < 10000)
        account destination = new account()
        destination.deposit(150m)

        source.transfer_funds(destination, 100m)

        Assert.AreEqual(250m, destination.balance)
        Assert.AreEqual(100m, source.balance)
