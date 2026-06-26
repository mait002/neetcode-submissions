public class Solution {

    public string Encode(IList<string> strs) {
        if (strs.Count == 0){
            return "";
        }

        List<int> sizes = new List<int>();
        StringBuilder res = new StringBuilder();
        foreach (string str in strs){
            sizes.Add(str.Length);
        }
        foreach (int size in sizes){
            res.Append(size).Append(',');
        }
        res.Append('#');
        foreach (string str in strs){
            res.Append(str);
        }
        return res.ToString();
    
        
    }

    public List<string> Decode(string s) {
        if (s.Length == 0){
            return new List<string>();
        }
        List<int> sizes = new List<int>();
        List<string> res = new List<string>();

        int count = 0;
        while (s[count] != '#'){
            int j = count;
            while (s[j] != ','){
                j++;
            }
            sizes.Add(int.Parse(s.Substring(count, j-count)));
            count = j+1;
            
            

        }
        count++;
        
        foreach (int sz in sizes){
            res.Add(s.Substring(count, sz));
            count+=sz;
        }
        return res;

   }
}
