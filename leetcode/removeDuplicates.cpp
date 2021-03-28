// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

#include <vector>
#include <iostream>

using namespace std;

class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        int prev;

        vector<int>::iterator iter;
        for (iter = nums.begin(); iter != nums.end(); iter++)
        {
            if (iter == nums.begin())
            {
                prev = *iter;
            }
            else
            {
                if (*iter == prev)
                {
                    nums.erase(iter);
                    iter--;
                }
                else
                {
                    prev = *iter;
                }
            }
        }

        return nums.size();
    }
};

int main()
{

    Solution s;
    vector<int> v = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    int c = s.removeDuplicates(v);

    cout << c << endl;
};