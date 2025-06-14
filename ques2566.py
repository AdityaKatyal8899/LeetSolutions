class Solution:
    def minMaxDifference(self, num: int) -> int:
        str_num = str(num)

        # Maximize: replace first digit that's not 9
        for ch in str_num:
            if ch != '9':
                max_num = str_num.replace(ch, '9')
                break
        else:
            max_num = str_num

        # Minimize: replace first digit that's not 0
        for ch in str_num:
            if ch != '0':
                min_num = str_num.replace(ch, '0')
                break
        else:
            min_num = str_num

        return int(max_num) - int(min_num)
