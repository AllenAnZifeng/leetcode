class Solution:
    def insert(self,value,l):
        if value<=l[0]:
            l.insert(0,value)
        if value>=l[-1]:
            l.append(value)
        for i in range(len(l)):
            if value > l[i] and value<l[i+1]:
                l.insert(i+1,value)
                return None

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        median=0
        temp=0
        temp_list=[0]*2 # a box to check if the two temps are equal, meaning that the value of that index is not changing
        length1=len(nums1)
        length2=len(nums2)
        if length1>length2:
            longer_list=nums1
            shorter_list=nums2
        else:
            longer_list=nums2
            shorter_list=nums1
        length_sum=length1+length2


        if length_sum%2==0:    #even num
            median_index=[(length_sum//2)-1,length_sum//2]
        else: #odd num
            median_index=[length_sum//2]   #the median index
        target_index=median_index[-1]
        for i in range(len(shorter_list)):
            self.insert(shorter_list[i],longer_list)
            temp=longer_list[target_index]
            temp_list[0]=temp_list[1]
            temp_list[1] = temp

            print('temp list')
            print(temp_list)
            if temp_list[0]==temp_list[1]:
                break
        print('longer list')
        print(longer_list)
        print('median_index list')
        print(median_index)

        if len(median_index)==1:
            median=longer_list[median_index[0]]
            print(median)
            return median
        elif len(median_index)==2:
            median=(longer_list[median_index[0]]+longer_list[median_index[1]])/2
            print(median)
            return median

a=Solution()
l1=[1,2,2]
l2=[1,2,3]
a.findMedianSortedArrays(l1,l2)