// https://leetcode.com/problems/integer-to-roman/

#include <string>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution
{
public:
    string intToRoman(int num)
    {
        map<int, char> roman = {{1, 'I'}, {5, 'V'}, {10, 'X'}, {50, 'L'}, {100, 'C'}, {500, 'D'}, {1000, 'M'}};

        int num4 = num / 1000;
        int num3 = (num % 1000) / 100;
        int num2 = (num % 100) / 10;
        int num1 = (num % 10);

        cout << num << ":" << num4 << " " << num3 << " " << num2 << " " << num1 << endl;

        string answer = "";
        answer += transform(num4, roman.at(1000), 'x', 'x');
        answer += transform(num3, roman.at(100), roman.at(500), roman.at(1000));
        answer += transform(num2, roman.at(10), roman.at(50), roman.at(100));
        answer += transform(num1, roman.at(1), roman.at(5), roman.at(10));

        return answer;
    }

    string transform(int num, char a, char b, char c)
    {
        string value = "";
        if (num < 4)
        {
            for (int i = 0; i < num; i++)
            {
                value += a;
            }
        }
        else if (num == 4)
        {
            value += a;
            value += b;
        }
        else if (num == 9)
        {
            value += a;
            value += c;
        }
        else if (num >= 5)
        {
            value += b;
            for (int i = 0; i < num - 5; i++)
            {
                value += a;
            }
        }
        cout << value << endl;

        return value;
    }
};

int main()
{
    Solution s;
    string test = s.intToRoman(3);
    cout << test << endl;
}