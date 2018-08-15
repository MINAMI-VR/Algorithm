public class Euclid {
    int x, y;

    public void set(int a, int b) {
        this.x = a;
        this.y = b;
        if (a < b) {
            this.x = b;
            this.y = a;
        }
    }

    public int getGCD() {
        int tmp;
        while ((tmp = this.x % this.y) != 0) {
            this.x = this.y;
            this.y = tmp;
        }
        return y;
    }
}
