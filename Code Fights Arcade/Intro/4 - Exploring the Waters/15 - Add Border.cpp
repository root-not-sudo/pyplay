std::vector<std::string> addBorder(std::vector<std::string> picture) {

    int n = picture[0].size() + 2;
    int m = picture.size() + 2;
    std::vector<std::string> b(m);
    b[0] = std::string(n, '*');
    b[m-1] = b[0];
    for (int i = 1; i < m - 1; i++)
    {
        b[i] = "*" + picture[i-1] + "*";
    }
    return b;
}
