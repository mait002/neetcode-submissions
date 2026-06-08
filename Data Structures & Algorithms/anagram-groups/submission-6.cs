public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        
        
        Dictionary<string, List<string>> store = new Dictionary<string, List<string>>();
        
        List<List<string>> res = new List<List<string>>();
        for (int i = 0; i < strs.Length; i++)
        {
            
            string charID = string.Concat(strs[i].OrderBy(c => c));
            
            if (!store.ContainsKey(charID))
            {
                store[charID] = new List<string>();
                store[charID].Add(strs[i]);
            }
            else
            {
                store[charID].Add(strs[i]);
            }
        }

        foreach (string key in store.Keys.ToList())
        {
            res.Add(store[key]);
        }
        return res;
    }
}
