int addTwoDigits(int n) {
    float ones = n % 10;
    float tens = floor(n/10);
    float sum = ones + tens;
    return sum;
}
