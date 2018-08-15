public class CountingSort {
    public void countingSort(int[] arr) {
        int bucket[] = new int[getMax(arr) + 1];
        for (int i = 0; i < arr.length; i++) bucket[arr[i]]++;
        var index = 0;
        for (int i = 0; i < bucket.length; i++) {
            for (int j = 0; j < bucket[i]; j++) {
                arr[index] = i;
                index++;
            }
        }
    }

    private int getMax(int[] arr) {
        var max = 0;
        for (int i = 0; i < arr.length; i++) {
            if (max < arr[i]) max = arr[i];
        }
        return max;
    }
}
