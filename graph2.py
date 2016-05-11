import excelParser
import Dijkstra
import sys

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

    def find_Nailro_paths(self, start_vertex, vertex_list):
        #시작점 start_vertex, 추가점 리스트 vertextList
        #입력받은 역을 이용해서, 경로를 반환
        v = vertex_list
        result_paths = [start_vertex] #리턴할 경로
        result_time = 0
        start = start_vertex
        
        #시작점과 가장 가까운점 찾기
        while len(v) != 0:
            tmp = self.find_min_dist(start, v)
            next_v = tmp[0][-1]
            for x in tmp[0][1:]:
                if x not in result_paths:
                   
                    result_paths += [x]
            # result_paths += tmp[0][1:]
            result_time += tmp[1]
            del v[v.index(next_v)]
            start = next_v
        
        tmp = self.find_min_dist(start, [start_vertex])
        result_time += tmp[1]
        for x in tmp[0][1:]:
            
            if x not in result_paths:
                result_paths += [x]
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
    
# 입력 받은값만 나타내기
#   def print_graph2(start, vertex_list, path)
      


if __name__ == "__main__":

#     gr = { "a" : {"d": 1, "c":2}
#           
#         }
    import excelParser
    time_g = excelParser.createTimeGraph()
    # price_g = excelParser.createPriceGraph()
    time_graph = Graph(time_g)
    # price_graph = Graph(price_g)
    # # print (time_graph.find_min_dist("수원", ["부산", "남춘천", "가평"]))
    # # print (time_graph.finㅂd_min_dist("청평", ["수원", "남춘천"]))
    
    print (time_graph.find_Nailro_paths('서울', ['수원', '신탄진', '가평']))
