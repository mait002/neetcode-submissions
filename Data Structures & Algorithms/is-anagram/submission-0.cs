public class Solution {
    public bool IsAnagram(string s, string t) {

        // If length doesn't match return false
        if (s.Length != t.Length)
        {
            return false;
        }

        Dictionary<char, int> store = new Dictionary<char, int>();

        for (int i = 0; i < s.Length; i++)
        {
            if (store.ContainsKey(s[i]))
            {
                store[s[i]]++;
            }
            else
            {
                store[s[i]] = 1;
            }
            if (store.ContainsKey(t[i]))
            {
                store[t[i]]--;
            }
            else
            {
                store[t[i]] = -1;
            }
        }
        char[] keys = store.Keys.ToArray();

        foreach (char key in keys)
        {
            if (store[key] > 0)
            {
                return false;
            }
        }
        return true;

    }
}
