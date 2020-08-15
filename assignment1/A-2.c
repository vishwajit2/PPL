int Z;

void f()
{
        int a, b, c;
        a = Z;
        if (a < 10) {
                b = 5;
                c = 17;
        } else {
                b = 6;
                c = 20;
                if (a == 0) {
                        c = 0;
                }
        }
        Z = b * 10 + c;
}

void fun() {
        int a = 1, b = 2, c = 3, y;
        y = a ? b : c;
        }
