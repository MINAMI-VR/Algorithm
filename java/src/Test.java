import java.util.Random;

public class Test {
    public void euclidTest() {
        Random r = new Random();
        var a = r.nextInt(100) + 1;
        var b = r.nextInt(100) + 1;

        Euclid e = new Euclid();
        e.set(a, b);
        var gcd = e.getGCD();
        System.out.println(a + ", " + b);
        System.out.println("GCD = " + gcd);
        System.out.println();
    }

    public void bubbleSortTest() {
        RandomArray ra = new RandomArray();
        int arr[] = ra.getRandomArray();

        BubbleSort bubble = new BubbleSort();
        ra.printArray(arr);
        bubble.bubbleSort(arr);
        ra.printArray(arr);
        System.out.println();
    }

    public void insertSortTest() {
        RandomArray ra = new RandomArray();
        int arr[] = ra.getRandomArray();

        InsertSort insert = new InsertSort();
        ra.printArray(arr);
        insert.insertSort(arr);
        ra.printArray(arr);
        System.out.println();
    }

    public void selectSortTest() {
        RandomArray ra = new RandomArray();
        int arr[] = ra.getRandomArray();

        SelectSort select = new SelectSort();
        ra.printArray(arr);
        select.selectSort(arr);
        ra.printArray(arr);
        System.out.println();
    }

    /*
        public void quickSortTest() {
            RandomArray ra = new RandomArray();
            int arr[] = ra.getRandomArray();

            QuickSort quick = new QuickSort();
            ra.printArray(arr);
            quick.quickSort(arr);
            ra.printArray(arr);
            System.out.println();
        }
    */

    public void bucketSortTest() {
        RandomArray ra = new RandomArray();
        int arr[] = ra.getRandomArray();

        CountingSort bucket = new CountingSort();
        ra.printArray(arr);
        bucket.countingSort(arr);
        ra.printArray(arr);
        System.out.println();
    }

    public void sequentialSearchTest() {
        RandomArray ra = new RandomArray();
        int arr[] = ra.getRandomArray();

        Random r = new Random();
        var val = arr[r.nextInt(arr.length)];

        SequentialSearch sequential = new SequentialSearch();
        ra.printArray(arr);
        var i = sequential.sequentialSearch(arr, val);
        System.out.println("index = " + i + ", value = " + val);
        System.out.println();
    }
}
