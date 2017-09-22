public void serialization()
    account source = new account()
    source.deposit(200m)

    IFormatter formatter = new BinaryFormatter()
    Stream stream = new MemoryStream()
    formatter.Serialize(stream, source)
    stream.Seek(0, SeekOrigin.Begin)
    account res = (account) formatter.Deserialize(stream)

    Assert.AreEqual(res.balance, 201m)
