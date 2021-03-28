// https://leetcode.com/problems/palindrome-number/

#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    bool isPalindrome(int x)
    {
        if (x < 0)
        {
            return false;
        }

        string str_x = to_string(x);
        int mid = str_x.size() / 2;
        vector<int> stack;
        bool flag;

        if (str_x.size() % 2 == 0)
        {
            flag = false;
        }
        else
        {
            flag = true;
        }

        for (int i = 0; i < str_x.size(); i++)
        {
            if (i < mid)
            {
                stack.push_back(stoi(str_x.substr(i, 1)));
                cout << "push " << stoi(str_x.substr(i, 1)) << endl;
            }
            else if (i >= mid)
            {

                if (flag && i == mid)
                {
                    continue;
                }

                cout << stack.back() << stoi(str_x.substr(i, 1)) << endl;
                if (stack.back() != stoi(str_x.substr(i, 1)))
                {
                    return false;
                }
                stack.pop_back();
            }
        }

        return true;
    }
};

int main()
{
    Solution s;
    bool a = s.isPalindrome(1221);
    cout << a << endl;
};