int commonCharacterCount(std::string s1, std::string s2) {

    int count = 0;
    for (int i = 0; i < s1.size(); i++)
    {
        for (int j = 0; j < s2.size(); j++)
        {
            if (s1[i] == s2[j])
            {
                count++;
                s2.erase(j,1);
                i++;
                j = -1;
            }
        }
    }
    return count;
}
