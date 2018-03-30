int shapeArea(int n) {
    int Area = 1;
    for (int i = 2; i <= n; i++) {
        Area += 4*(i-1);
    }
    return Area;
}
