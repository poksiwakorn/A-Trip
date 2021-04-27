def makeList_Of_DistanceBetweenPointToPoint_From_DictFromGooglemapsAPI(dictFromGooglemapsAPI):
    dataOut = list()
    for i in range(len(dictFromGooglemapsAPI["rows"])):
        counters = 0
        for j in dictFromGooglemapsAPI["rows"][i]["elements"]:
            if i != counters:
                dataOut.append(float(j["distance"]["text"].strip(" km")))
            counters += 1
    #data = [26.3, 19.4, 25.2, 27.5, 19.6, 35.1, 45.7, 12.5, 13.7, 21.5, 18.7, 11.1]
    return dataOut

def makeList_Of_ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint_From_ListOfKeyOfSelectedPlace(listOfKeyOfSelectedPlace):
    data = list()
    for i in listOfKeyOfSelectedPlace:
        for j in listOfKeyOfSelectedPlace:
            listOfKeyOfPointToKeyOfPoint = list()          
            if(j is not i):
                listOfKeyOfPointToKeyOfPoint.append(i)
                listOfKeyOfPointToKeyOfPoint.append(j)
                data.append(listOfKeyOfPointToKeyOfPoint)
    #data = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'A'], ['B', 'C'], ['B', 'D'], ['C', 'A'], ['C', 'B'], ['C', 'D'], ['D', 'A'], ['D', 'B'], ['D', 'C']]
    return data

def makeList_of_ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint_And_DistanceBetweenPointToPoint(ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint, DistanceBetweenPointToPoint):
    data = list()
    for i in range(len(ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint)):
        temp = list()
        temp.append(ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint[i])
        temp.append(DistanceBetweenPointToPoint[i])
        data.append(temp)
    #data = [[['A', 'B'], 26.3], [['A', 'C'], 19.4], [['A', 'D'], 25.2], [['B', 'A'], 27.5], [['B', 'C'], 19.6], [['B', 'D'], 35.1], [['C', 'A'], 45.7], [['C', 'B'], 12.5], [['C', 'D'], 13.7], [['D', 'A'], 21.5], [['D', 'B'], 18.7], [['D', 'C'], 11.1]]
    return data

def makeList_Of_ListOf_AllListOfRoute_ListofDistance_And_SumOfDistance(numberOfSelectedPlace, ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint_And_DistanceBetweenPointToPoint, path, distance, data, currentPoint = None):
    if currentPoint is None:
        for i in ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint_And_DistanceBetweenPointToPoint:
            path.append(i[0][0])
            distance.append(i[1])
            nextPoint = i[0][1]
            makeList_Of_ListOf_AllListOfRoute_ListofDistance_And_SumOfDistance(numberOfSelectedPlace,ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint_And_DistanceBetweenPointToPoint,path, distance, data, nextPoint)
            path.pop()
            distance.pop()
        return data
    else:
        for i in ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint_And_DistanceBetweenPointToPoint:
            if i[0][0] == currentPoint and path.count(i[0][1]) == 0:
                path.append(i[0][0])
                distance.append(i[1])
                nextPoint = i[0][1]
                makeList_Of_ListOf_AllListOfRoute_ListofDistance_And_SumOfDistance(numberOfSelectedPlace,ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint_And_DistanceBetweenPointToPoint,path, distance, data, nextPoint)
                if len(path) == numberOfSelectedPlace-1:
                    listPath = list()
                    listDistance = list()
                    sumOfDistance = 0.
                    path.append(nextPoint)
                    for j in path:
                        listPath.append(j)
                    for j in distance:
                        listDistance.append(j)
                        sumOfDistance += j
                    data.append([listPath,listDistance,round(sumOfDistance,2)])
                    path.pop()
                path.pop()
                distance.pop()


def something(listOfKeyOfSelectedPlace, dictFromGooglemapsAPI):
    return makeList_of_ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint_And_DistanceBetweenPointToPoint(makeList_Of_ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint_From_ListOfKeyOfSelectedPlace(listOfKeyOfSelectedPlace), makeList_Of_DistanceBetweenPointToPoint_From_DictFromGooglemapsAPI(dictFromGooglemapsAPI))
    

a = makeList_Of_ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint_From_ListOfKeyOfSelectedPlace(["A","B","C","D"])
print(a)

test = {'destination_addresses':['Unnamed Road, Khwaeng Sam Wa Tawan Tok, Khet Khlong Sam Wa, Krung Thep Maha Nakhon 10510, Thailand','62 หมู่ที่ 1 ถนน รังสิต - องครักษ์ Tambon Bang Yitho, Amphoe Thanyaburi, Chang Wat Pathum Thani 12130, Thailand','22/44-45 Phahonyothin Rd, Khwaeng Lat Yao, Khet Chatuchak, Krung Thep Maha Nakhon 10900, Thailand'],'origin_addresses':['Unnamed Road, Khwaeng Sam Wa Tawan Tok, Khet Khlong Sam Wa, Krung Thep Maha Nakhon 10510, Thailand','62 หมู่ที่ 1 ถนน รังสิต - องครักษ์ Tambon Bang Yitho, Amphoe Thanyaburi, Chang Wat Pathum Thani 12130, Thailand','22/44-45 Phahonyothin Rd, Khwaeng Lat Yao, Khet Chatuchak, Krung Thep Maha Nakhon 10900, Thailand'],'rows':[{'elements':[{'distance': {'text': '1 m', 'value': 0},'duration': {'text': '1 min', 'value': 0},'status': 'OK'},{'distance': {'text': '26.3 km', 'value': 26338},'duration': {'text': '33 mins', 'value': 1999},'status': 'OK'},{'distance': {'text': '19.4 km', 'value': 19353},'duration': {'text': '32 mins', 'value': 1930},'status': 'OK'}]},{'elements':[{'distance': {'text': '25.2 km', 'value': 25183}, 'duration': {'text': '41 mins', 'value': 2467}, 'status': 'OK'},{'distance': {'text': '1 m', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'},{'distance': {'text': '27.5 km', 'value': 27491}, 'duration': {'text': '31 mins', 'value': 1838}, 'status': 'OK'}]},{'elements':[{'distance': {'text': '19.6 km', 'value': 19570}, 'duration': {'text': '36 mins', 'value': 2162}, 'status': 'OK'},                     {'distance': {'text': '35.1 km', 'value': 35129}, 'duration': {'text': '39 mins', 'value': 2364}, 'status': 'OK'},{'distance': {'text': '1 m', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}]}], 'status': 'OK'}
#b = makeList_Of_DistanceBetweenPointToPoint_From_DictFromGooglemapsAPI(test)
b = [26.3, 19.4, 25.2, 27.5, 19.6, 35.1, 45.7, 12.5, 13.7, 21.5, 18.7, 11.1]
print(b)

c = makeList_of_ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint_And_DistanceBetweenPointToPoint(a,b)
print(c)

print("")
#print(something(["A","B","C"],test))

d = makeList_Of_ListOf_AllListOfRoute_ListofDistance_And_SumOfDistance(4,c,list() ,list(), list())
for i in d:
    print(i)
#print(d)
