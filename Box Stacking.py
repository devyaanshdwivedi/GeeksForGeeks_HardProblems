#User function Template for python3

class Solution:
    def maxHeight(self,height, width, length, n):
        boxes = [[] for i in range(3*n)]
        index = 0
        for i in range(n):
            boxes[index].append(height[i])
            boxes[index].append(min(width[i], length[i]))
            boxes[index].append(max(width[i], length[i]))
            index += 1
            boxes[index].append(width[i])
            boxes[index].append(min(height[i], length[i]))
            boxes[index].append(max(height[i], length[i]))
            index += 1
            boxes[index].append(length[i])
            boxes[index].append(min(width[i], height[i]))
            boxes[index].append(max(width[i], height[i]))
            index += 1
           # print(boxes)
           
        boxes.sort(reverse = True, key = lambda x: x[2]*x[1])
           
           # print(boxes)
        n *= 3
        msh = [0]*n
           
        for i in range(n):
            msh[i] = boxes[i][0]
            for j in range(i):
                if boxes[i][1] < boxes[j][1] and boxes[i][2] < boxes[j][2]:
                    if msh[i] < msh[j] + boxes[i][0]:
                        msh[i] = msh[j] + boxes[i][0]
        return max(msh)
            
        #Code here
