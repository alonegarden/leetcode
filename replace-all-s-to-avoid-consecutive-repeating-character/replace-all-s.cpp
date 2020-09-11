
string modifyString(string s) 
{
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '?') {
            s[i] ='a'; //设为a
            while ( (i < s.size()-1 && s[i]==s[i+1]) ||
                    (i > 0 && s[i] == s[i-1])) 
                s[i] +=1; //判断跟旁边一样就+1
            }
        }
        return s;
}