bool isLucky(int n) {

    string sup = to_string(n);
    int front;
    int back;

    if (n >= 10 && n < 100)
    {
        front = u_int(sup[0]);
        back = u_int(sup[1]);
    }

    if (n >= 1000 && n < 10000)
    {
        front = u_int(sup[0]) + u_int(sup[1]);
        back = u_int(sup[2]) + u_int(sup[3]);

    }

    if (n >= 100000 && n < 1000000)
    {
        front = u_int(sup[0]) + u_int(sup[1]) + u_int(sup[2]);
        back = u_int(sup[3]) + u_int(sup[4]) + u_int(sup[5]);
    }

    if (front == back)
    {
        return true;
    }
    else
    {
        return false;
    }
}
