std::vector<int> sortByHeight(std::vector<int> a) {

    std::vector<int> b = a;
    int n = a.size();
    sort(a.begin(), a.end());
    int i = 0;

    for (int j = 0; j < n; j++)
    {
        while ((a[i] < 0))
        {
            i++;
        }

        if (b[j] >= 0)
        {
            b[j] = a[i];
            i++;
        }
    }

    return b;


}
