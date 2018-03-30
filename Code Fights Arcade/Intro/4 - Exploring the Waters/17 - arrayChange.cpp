int arrayChange(std::vector<int> inputArray) {

    int n = inputArray.size();
    int count = 0;
    for (int i = 1; i < n; i++)
    {
        if (inputArray[i-1] >= inputArray[i])
        {
            count += inputArray[i-1] - inputArray[i] + 1;
            inputArray[i] = inputArray[i-1] + 1;
        }
    }
    return count;
}
