#include <iostream>
#include <bits/stdc++.h> 

using namespace std;

class Solution {
    public:

        stack <char> _stack;
        queue <char> _queue;

        void pushCharacter (char ch)
        {
            _stack.push (ch);
        }

        void enqueueCharacter(char ch)
        {
            _queue.push (ch);
        }

        char popCharacter ()
        {
            char top = _stack.top ();
            _stack.pop ();
            //cout << "pop " << top << endl;
            return top;
        }

        char dequeueCharacter()
        {
            char front = _queue.front ();
            //cout << "deque " << front << endl;
            _queue.pop ();
            return front;
        }
};

int main() {
    // read the string s.
    string s;
    getline(cin, s);
    
  	// create the Solution class object p.
    Solution obj;
    
    // push/enqueue all the characters of string s to stack.
    for (int i = 0; i < s.length(); i++) {
        obj.pushCharacter(s[i]);
        obj.enqueueCharacter(s[i]);
    }
    
    bool isPalindrome = true;
    
    // pop the top character from stack.
    // dequeue the first character from queue.
    // compare both the characters.
    for (int i = 0; i < s.length() / 2; i++) {
        if (obj.popCharacter() != obj.dequeueCharacter()) {
            isPalindrome = false;
            
            break;
        }
    }
    
    // finally print whether string s is palindrome or not.
    if (isPalindrome) {
        cout << "The word, " << s << ", is a palindrome.";
    } else {
        cout << "The word, " << s << ", is not a palindrome.";
    }
    
    return 0;
}



