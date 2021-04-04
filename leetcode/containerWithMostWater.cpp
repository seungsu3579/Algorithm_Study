// https://leetcode.com/problems/container-with-most-water/

#include <vector>
#include <iostream>

using namespace std;

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int i = 0;
        int j = height.size() - 1;
        int max_water = (j - i) * min(height[i], height[j]);

        while (i != j)
        {

            if (height[i] < height[j])
            {
                i++;
            }
            else
            {
                j--;
            }

            if (max_water < (j - i) * min(height[i], height[j]))
            {
                max_water = (j - i) * min(height[i], height[j]);
            }
        }

        return max_water;
    }
};

int main()
{

    Solution s;
    vector<int> v = {4, 3, 2, 1, 4};
    int c = s.maxArea(v);

    cout << c << endl;
};