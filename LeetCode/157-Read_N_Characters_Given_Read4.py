# Runtime: 36 ms, faster than 65.14% of Python3 online submissions for Read N Characters Given Read4.
# Memory Usage: 13.1 MB, less than 6.00% of Python3 online submissions for Read N Characters Given Read4.
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        ret = 4
        rest = n
        tmp = ['']
        while rest > 0 and ret >= 4:
            ret = read4(buf)
            if ret:
                tmp += buf[:min(rest, ret)]
            rest -= ret
        buf[:] = ''.join(tmp)
        return len(buf)