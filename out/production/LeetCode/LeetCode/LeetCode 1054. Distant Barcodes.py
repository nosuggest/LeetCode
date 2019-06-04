class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        length = len(barcodes)
        default_dict = {}
        for i in barcodes:
            if i not in default_dict:
                default_dict[i] = 1
            else:
                default_dict[i] += 1
        
        sortKeys =sorted(default_dict.items(),key=lambda x:x[1],reverse=True)
        
        fill_list = []
        for singleone in sortKeys:
            fill_list+=[singleone[0]]*singleone[1]
        
        
        result_list = [0]*length
        for i in range(0,length,2):
            result_list[i] = fill_list.pop(0)


        for i in range(1,length,2):
            result_list[i] = fill_list.pop(0)
            
            
        return result_list