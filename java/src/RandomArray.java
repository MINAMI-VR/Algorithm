import java.util.Arrays;
import java.util.Random;

public class RandomArray {

    public int[] getRandomArray() {
        Random r = new Random();
        var length = r.nextInt(10) + 20;
        int arr[] = new int[length];
        for (int i = 0; i < length; i++) arr[i] = r.nextInt(100);
        return arr;
    }

    public void printArray(int[] arr) {
        System.out.println(Arrays.toString(arr));
    }
}
