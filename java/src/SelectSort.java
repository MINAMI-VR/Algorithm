public class SelectSort {
    public void selectSort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            var min_i = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[min_i] > arr[j]) min_i = j;
            }
            var tmp = arr[min_i];
            for (int j = min_i; i < j; j--) arr[j] = arr[j - 1];
            arr[i] = tmp;
        }
    }
}
