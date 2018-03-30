bool palindromeRearranging(std::string s) {

    for (int i = 0; i < s.size(); i++)
    {
        for (int j = i+1; j < s.size(); j++)
        {
            if (s[i] == s[j])
            {
                s.erase(i,1);
                s.erase(j-1,1);
                i--;
                j = s.size();
            }
        }
    }
    return (s.size() <= 1);
}
