import java.util.*;

public class ArrayIntersection {
        public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read size of array
        int N = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character
        
        int[] arr1 = new int[N];
        int[] arr2 = new int[N];
        
        // Read first array
        String[] firstArrayInput = scanner.nextLine().split(" ");
        for (int i = 0; i < N; i++) {
            arr1[i] = Integer.parseInt(firstArrayInput[i]);
        }
        
        // Read second array
        String[] secondArrayInput = scanner.nextLine().split(" ");
        for (int i = 0; i < N; i++) {
            arr2[i] = Integer.parseInt(secondArrayInput[i]);
        }
        
        // Find intersection and print result
        List<Integer> intersection = findIntersection(arr1, arr2);
        System.out.println(intersection);
    }
    
    public static List<Integer> findIntersection(int[] arr1, int[] arr2) {
        HashMap<Integer, Integer> map = new HashMap<>();
        List<Integer> intersectionList = new ArrayList<>();
        
        // Store frequency of elements in arr1
        for (int num : arr1) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        
        // Check elements of arr2 in map
        for (int num : arr2) {
            if (map.getOrDefault(num, 0) > 0) {
                intersectionList.add(num);
                map.put(num, map.get(num) - 1); // Decrease count to prevent duplicates
            }
        }
        
        return intersectionList;
    }
}
