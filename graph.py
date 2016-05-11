import excelParser
import Dijkstra
import random
import sys

city_list = ["서울","수원","신탄진", "청평","가평","남춘천","충주" ,"제천" ,
            "단양","영주","안동","태백","신기","동해" ,"정동진" ,"대천" ,
            "논산","군산","익산","전주","정읍","남원" ,"곡성" ,"광주" ,
            "화순","목포","보성","순천","여수","마산" ,"밀양" ,"경주" ,"포항","부산"]



class Graph(object):
    
    
####################초기화###################

    def __init__(self, graph_dict={}):
        #그래프 클래스 초기화
        self.__graph_dict = graph_dict
        

    def vertices(self):
        #꼭지점
        return list(self.__graph_dict.keys())

    def edges(self):
        #엣지
        return self.__generate_edges()

    def __generate_edges(self):
        #엣지 리스트
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges


##############경로찾기#######################

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        #시작점, 끝점이용해서 모든 경로를 찾아주는 함수 >> 너무 방대해서 이용안함;
        graph = self.__graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex,path)
                for p in extended_paths: 
                    paths.append(p)
        return paths


    def find_Nailro_paths(self, ticket_day, start_vertex, vertex_list):
        #ticket_day 7 이면 random 3, 5이면 랜럼2
        #시작점 start_vertex, 추가점 리스트 vertextList
        #입력받은 역을 이용해서, 경로를 반환
        randomNum = 0
        if(ticket_day == 7) :
            randomNum = 3
        elif(ticket_day == 5):
            randomNum = 2
        else:
            return 0
        v = vertex_list
        i=0
        while (i < randomNum):
            tmp = random.choice(city_list)
            if(tmp not in v):
              
                v += [tmp]
                i += 1
        
        result_paths = [start_vertex] #리턴할 경로
        result_time = 0
        start = start_vertex
        
        #시작점과 가장 가까운점 찾기
        while len(v) != 0:
            tmp = self.find_min_dist(start, v)
            next_v = tmp[0][-1]
            result_paths += [next_v]
            result_time += tmp[1]
            del v[v.index(next_v)]
            start = next_v
        
        tmp = self.find_min_dist(start, [start_vertex])
        result_time += tmp[1]
        result_paths += [start_vertex]
        
        
        return result_paths, result_time
        
        
    ####다이제스트라 이용하여 시작점과 가장 가까운 점과의 최단거리, 시간찾기!!!!!!!
    def find_min_dist(self, start, vertex_list):
        #시작점 start, 꼭지점 리스트vertex_list
        graph = self.__graph_dict
        time = {} #꼭지점 : 시간
        for v in vertex_list:
            time[v] = Dijkstra.dijkstra_path_time(self.__graph_dict, start, v)
        path = [start]
        min_time = 10000000
        for vertex, time in time.items():
            if min_time>time:
                min_time = time
                path = Dijkstra.dijkstra_path(self.__graph_dict, start, vertex)
        return path, min_time
        
        
    def cost_of_path(self, path):
        ret = []
        for x in range(0, len(path)-1):
            if excelParser.getPrice(path[x], path[x+1]):
                ret += [excelParser.getPrice(path[x], path[x+1])]
                
            else :
            #직통아닐때
                ret += ["직통없음"]
        return ret
        
        
        
        