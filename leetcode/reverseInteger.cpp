// https://leetcode.com/problems/reverse-integer/

#include <iostream>
#include <algorithm>
#include <string>
#include <math.h>

using namespace std;

class Solution
{
public:
    int reverse(int x)
    {
        bool neg = false;

        if (x == -pow(2, 31))
        {
            return 0;
        }
        else if (x < 0)
        {
            neg = true;
            x *= -1;
        }

        string str = to_string(x);
        string rev_str = "";
        for (int i = str.size() - 1; i >= 0; i--)
        {
            rev_str += str[i];
        }

        cout << rev_str << endl;

        long answer = 0;
        for (int i = 0; i < rev_str.length(); i++)
        {
            answer += pow(10, i) * stoi(rev_str.substr(rev_str.length() - 1 - i, 1));
        }

        if (neg)
        {
            answer = (-1) * answer;
        }

        if (answer > pow(2, 31) - 1 || answer < -pow(2, 31))
        {
            return 0;
        }
        else
        {
            return answer;
        }
    }
};

int main()
{
    Solution sol;
    int v = sol.reverse(-2147483648);
    cout << v << endl;
}