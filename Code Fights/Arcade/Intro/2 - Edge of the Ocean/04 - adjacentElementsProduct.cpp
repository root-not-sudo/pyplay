int adjacentElementsProduct(std::vector<int> inputArray) {
    float max = inputArray[0] * inputArray[1];
    for (int i = 0; i < inputArray.size()-1; i++) {
        if (max < inputArray[i] * inputArray[i+1]) {
            max = inputArray[i] * inputArray[i+1];
        }
    }
    return max;
}
