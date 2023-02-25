            
    sortedZ=[]
    for point in sorted :
        if abs(point.y-midP.y)<minP:
            sortedZ.append(point)
            
    sortedZ.sort(key=lambda p: p.z)
    
    for i in range(len(sortedZ)):
        j=j+1
        while j < len(sortedZ) and sortedZ[j].z-sortedZ[i].z < minP :
            tempMin2=distance(sortedZ[i],sortedZ[j])
            if tempMin2 < minP :
                minP=tempMin2
                cp= [sortedZ[i],sortedZ[j]]
            j+=1