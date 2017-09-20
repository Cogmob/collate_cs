public void OnAfterDeserialize()
    this.Clear()

    if(keys.Count != values.Count)
        throw new System.Exception(string.Format(
                "there are {0} keys and {1} values after deserialization. " +
                "Make sure that both key and value types are serializable."))

    for(int i = 0; i < keys.Count; i++)
        this.Add(keys[i], values[i])
