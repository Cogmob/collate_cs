public void transfer_funds()
    account source = new account()
    source.deposit(200m)

    account destination = new account()
    destination.deposit(150m)

    source.transfer_funds(destination, 100m)

    assert.are_equal(250m, destination.balance)
    assert.are_equal(100m, source.balance)
