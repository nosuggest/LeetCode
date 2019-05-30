class Qsort:
    def __init__(self):
        self.data = None
        self.output = None
    #快速排序
    def QuickSort(self,data,start,end):
        #判断low是否小于high,如果为false,直接返回
        self.data = data
        if start < end:
            i,j = start,end
            #设置基准数
            key = self.data[i]
            while i < j:
                #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
                while (i < j) and (self.data[j] >= key):
                    j = j - 1
            
                #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
                self.data[i] = self.data[j]
                
                #同样的方式比较前半区
                while (i < j) and (self.data[i] <= key):
                    i = i + 1
                self.data[j] = self.data[i]
            #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
            self.data[i] = key
            #递归前后半区
            self.QuickSort(self.data, start, i - 1)
            self.QuickSort(self.data, j + 1, end)
        self.output = self.data

    #分桶排序
    def BucketSort(self,data):
        self.data = data
        result = []
        set_res = [0 for i in range(max(set(self.data))-min(set(self.data))+1)]
        for i in data:
            set_res[i-min(self.data)] = set_res[i-min(self.data)] + 1
        for i in range(len(set_res)):
            if set_res[i] != 0:
                result = result + [i+min(self.data)]*set_res[i]
        self.output = result

if __name__ == '__main__':    
    data = [49,38,65,97,76,13,27,49]
    model = Qsort()
    model1 = Qsort()
    model.QuickSort(data,0,len(data)-1)
    print(model.output)
    model1.BucketSort(data)
    print(model1.output)