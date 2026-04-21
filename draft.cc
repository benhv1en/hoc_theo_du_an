#include <bits/stdc++.h>
using namespace std;
bool IsFound(const unordered_set<int>& set, const int& number) {
  return set.find(number) != set.end();
}

vector<int> recoverOrder(vector<int>& order, vector<int>& friends) {
  unordered_set<int> my_set(friends.begin(), friends.end());
  vector<int> answer;
  for (const int& number : order)
    if (my_set.count(number)) answer.push_back(number);
  return answer;
}

vector<int> buildArray(vector<int>& nums) {
  vector<int> middle;
  for (const int& element : nums) middle.push_back(nums[element]);
  return middle;
}

int minimumOperations(vector<int>& nums) {
  int answer;
  for (const int& element : nums)
    if (0 != element % 3) ++answer;
  return answer;
}

int finalValueAfterOperations(vector<string>& operations) {
  int value = 0;
  for (const string& operation : operations)
    value = (operation[1] == '+') ? value + 1 : value - 1;
  return value;
}
int main() {}