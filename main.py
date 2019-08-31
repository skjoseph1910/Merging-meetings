def merge_ranges(meetings):

    # Merge meeting ranges
    finallist = []
    checklist= []
    meetings.sort()
    for i in range(len(meetings)):
        list = [] 
        if (meetings[i][0], meetings[i][1]) not in checklist:
            list.append(meetings[i][0])
            list.append(meetings[i][1])
            for j in range(len(meetings)):
                if meetings[j][0] >= min(list) and meetings[j][0] <= max(list):
                    list.append(meetings[j][0])
                    list.append(meetings[j][1])
                    checklist.append((meetings[j][0], meetings[j][1]))
            
            finallist.append((min(list), max(list)))

    return finallist
    
 def main():
    actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
    print(actual)
