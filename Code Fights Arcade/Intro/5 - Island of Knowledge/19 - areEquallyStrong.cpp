bool areEquallyStrong(int yL, int yR, int fL, int fR) {
    return (max(yL, yR) == max(fL, fR) && min(yL, yR) == min(fL, fR));
}
