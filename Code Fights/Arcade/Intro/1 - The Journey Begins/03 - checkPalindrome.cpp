bool checkPalindrome(std::string inputString) {
    string Pal = inputString;
    reverse(inputString.begin(),inputString.end());
    if (Pal == inputString) {
        return 1;
    }

    if (Pal != inputString) {
        return 0;
    }
}
