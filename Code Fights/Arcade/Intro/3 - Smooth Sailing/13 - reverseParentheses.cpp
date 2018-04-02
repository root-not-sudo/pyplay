std::string reverseParentheses(std::string s) {

    for(int i = 0; i < s.size(); i++)
    {
        cout << i << endl;
        if (s[i] == ')')
        {
            for(int j = i; j >= 0; j--)
            {
                if (s[j] == '(')
                {
                    for (int k = j + 1; k <= (i-j)/2+j; k++)
                    {
                        //cout << i-k << endl;
                        swap(s[k], s[i+j-k]);
                        //cout << s[k] << endl;
                    }
                    s.erase(j,1);
                    j = -1;
                }
            }
            s.erase(i-1,1);
            i-=2;
        }
    }

//    for(int i = s.size()-1; i >= 0; i--)
    for(int i = 0; i < s.size(); i++)
    {
        cout << s[i];
    }

    return s;
}
