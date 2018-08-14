public class SequentialSearch {
    public int sequentialSearch(int[] arr, int val) {

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == val) return i;
        }
        return -1;
    }
}
