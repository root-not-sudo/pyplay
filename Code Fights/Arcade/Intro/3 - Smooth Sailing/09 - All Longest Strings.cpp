std::vector<std::string> allLongestStrings(std::vector<std::string> inputArray) {
    int size = inputArray.size();
    int longest = inputArray[0].size();
    std::vector<std::string> outputArray;
    for (int i = 1; i < size; i++)
    {
        if (inputArray[i].size() > longest)
        {
            longest = inputArray[i].size();
        }
    }

    for (int i = 0; i < size; i++)
    {
        if (inputArray[i].size() == longest)
        {
//            cout << inputArray[i] << endl;
            outputArray.push_back(inputArray[i]);
        }
    }
    return outputArray;
}
