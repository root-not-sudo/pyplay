bool areSimilar(std::vector<int> a, std::vector<int> b) {

    if (a == b)
    {
        return true;
    }
    else
    {
        int s = 0, ai = -1, aj = -1;
        int n = a.size();
        for (int i = 0; i < n; i++)
        {
            if (a[i] != b[i])
            {
                s++;
                if (aj == ai)
                {
                    aj = i;
                }
                if (ai == -1)
                {
                    ai = i;
                }
            }
            if (s > 2)
            {
                i = n;
                return false;
                break;
            }
        }
        if (s == 2)
        {
            swap(a[ai], a[aj]);
            if (a == b)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

    }
}
