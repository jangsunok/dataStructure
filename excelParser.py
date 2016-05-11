import xlrd

#엑셀파일의 데이터를 가져옴
path = 'nailro.xlsx'

workbook = xlrd.open_workbook(path)

    
city_id = {"서울" : 1,"수원" : 2,"신탄진" : 3,"청평" : 4,"가평" : 5,"남춘천" : 6,"충주" : 7,"제천" : 8,
            "단양" : 9,"영주" : 10,"안동" : 11,"태백" : 12,"신기" : 13,"동해" : 14,"정동진" : 15,"대천" : 16,
            "논산" : 17,"군산" : 18,"익산" : 19,"전주" : 20,"정읍" : 21,"남원" : 22,"곡성" : 23,"광주" : 24,
            "화순" : 25,"목포" : 26,"보성" : 27,"순천" : 28,"여수" : 29,"마산" : 30,"밀양" : 31,"경주" : 32,
            "포항" : 33,"부산" : 34}


def getTime(city_name1, city_name2):
    #city1에서 city2로가는 시간 (단위:분, 실수형)
    if city_id[city_name1]==KeyError:
        return None
    if city_id[city_name2]==KeyError:
        return None
    
    min_id = min(city_id[city_name1], city_id[city_name2])
    max_id = max(city_id[city_name1], city_id[city_name2])
    
    
    worksheet = workbook.sheet_by_index(0)

    offset = 1
    
    rows = []
    for i, row in enumerate(range(worksheet.nrows)):
        # if i <= offset:  # (Optionally) skip headers
        #     continue
        r = []
        for j, col in enumerate(range(worksheet.ncols)):
            r.append(worksheet.cell_value(i, j))
        rows.append(r)
    
    return (rows[min_id][max_id])
    
    
    
def getPrice(city_name1, city_name2):
    #city1에서 city2로가는 가격 (단위:원, 실수형)
    
    if city_id[city_name1]==KeyError:
        return None
    if city_id[city_name2]==KeyError:
        return None
    
    min_id = min(city_id[city_name1], city_id[city_name2])
    max_id = max(city_id[city_name1], city_id[city_name2])
    
    worksheet = workbook.sheet_by_index(1)

    offset = 1
    
    rows = []
    for i, row in enumerate(range(worksheet.nrows)):
        # if i <= offset:  # (Optionally) skip headers
        #     continue
        r = []
        for j, col in enumerate(range(worksheet.ncols)):
            r.append(worksheet.cell_value(i, j))
        rows.append(r)
        
    
    return (rows[min_id][max_id])


def createTimeGraph():
    graph = {}

    for city1 in city_id.keys():
        tmp = {}
        for city2 in city_id.keys():
            if city1 != city2:
                if getTime(city1, city2) !="":
                    tmp[city2] = getTime(city1, city2)
        graph[city1] = tmp
    return graph
    
def createPriceGraph():
    graph = {}

    for city1 in city_id.keys():
        tmp = {}
        for city2 in city_id.keys():
            if city1 != city2:
                if getPrice(city1, city2) !="":
                    tmp[city2] = getPrice(city1, city2)
        graph[city1] = tmp
    return graph
    
    

