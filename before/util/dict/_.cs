public class dict<t_key, t_val> :
        Dictionary<t_key, t_val>,
        ISerializationCallbackReceiver

    // http://answers.unity3d.com/questions/460727/
    //         how-to-serialize-dictionary-with-unity-serializati.html

    [SerializeField]
    private List<TKey keys = new List<TKey>()

    [SerializeField]
    private List<TValue> values = new List<TValue>()
