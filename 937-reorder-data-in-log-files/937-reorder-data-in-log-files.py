class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        letter_logs = collections.defaultdict(list)
        digit_logs = []
        
        for log in logs:
            words = log.split(' ')
            if words[1].isnumeric():
                digit_logs.append(log)
                
            else:
                letter_logs[' '.join(words[1:])].append(words[0])
                
        final_logs = []
        for k in sorted(letter_logs.keys()):
            for idf in sorted(letter_logs[k]):
                log = idf + ' ' + k
                final_logs.append(log)
                
                
        final_logs += digit_logs
        
        return final_logs
                
                
            
        