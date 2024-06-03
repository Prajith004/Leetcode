class Solution {
    public int[] frequencySort(int[] nums) {

        int[] arr = new int[nums.length];

        List<Integer> list = new ArrayList<>();

        for (int val : nums) {

            list.add(val);
        }

        for (int i = 0; i < list.size(); ++i) {

            arr[i] = Collections.frequency(list, list.get(i));
        }

        for (int i = 0; i < arr.length; ++i) {

            for (int j = i + 1; j < arr.length; ++j) {

                if (arr[i] > arr[j]) {

                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;

                    int temp1 = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp1;

                } else if (arr[i] == arr[j]) {

                    if (nums[i] < nums[j]) {

                        int temp = nums[i];
                        nums[i] = nums[j];
                        nums[j] = temp;
                    }

                }
            }
        }

        return nums;
    }
}