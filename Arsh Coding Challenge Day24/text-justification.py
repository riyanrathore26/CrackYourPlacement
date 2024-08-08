from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify_line(line, maxWidth, is_last_line=False):
            if len(line) == 1:
                # If there's only one word in the line
                return line[0].ljust(maxWidth)
            
            if is_last_line:
                # Left justify for the last line
                return ' '.join(line).ljust(maxWidth)

            total_chars = sum(len(word) for word in line)
            total_spaces = maxWidth - total_chars
            gaps = len(line) - 1
            even_spaces, extra_spaces = divvy_up_spaces(total_spaces, gaps)

            result = ''
            for i in range(len(line) - 1):
                result += line[i] + ' ' * (even_spaces + (1 if i < extra_spaces else 0))
            result += line[-1]
            return result

        def divvy_up_spaces(total_spaces, gaps):
            # Even spaces between words and extra spaces to distribute
            even_spaces = total_spaces // gaps
            extra_spaces = total_spaces % gaps
            return even_spaces, extra_spaces

        result = []
        line = []
        line_len = 0

        for word in words:
            if line_len + len(word) + len(line) > maxWidth:
                result.append(justify_line(line, maxWidth))
                line = []
                line_len = 0
            
            line.append(word)
            line_len += len(word)
        
        result.append(justify_line(line, maxWidth, is_last_line=True))
        return result