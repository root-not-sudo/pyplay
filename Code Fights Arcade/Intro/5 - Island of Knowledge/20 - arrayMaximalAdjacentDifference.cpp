int arrayMaximalAdjacentDifference(std::vector<int> A) {
    int max = 0;
    for (int i = 0; i < A.size() - 1; i++)
    {
        if (abs(A[i] - A[i+1]) > max)
        {
            max = abs(A[i] - A[i+1]);
        }
    }
    return max;
}
