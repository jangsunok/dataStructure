from flask import Flask, render_template, request, redirect, url_for
from mongoengine import connect, Document, StringField, IntField, BooleanField
from networkx import Graph
from jinja2 import Template
# from wtforms import Form, TextField, TextAreaField, SubmitField, validators, ValidationError

import os
import manage

import excelParser
import graph



app = Flask(__name__)
app.debug = True

#connect('datastructure')

city_list = ["서울","수원","신탄진", "청평","가평","남춘천","충주" ,"제천" ,
            "단양","영주","안동","태백","신기","동해" ,"정동진" ,"대천" ,
            "논산","군산","익산","전주","정읍","남원" ,"곡성" ,"광주" ,
            "화순","목포","보성","순천","여수","마산" ,"밀양" ,"경주" ,"포항","부산"]


class NailroInput(object):
    ticket_day = 0
    station_start = ""
    station_option1 = ""
    station_option2 = ""
    station_option3 = ""
    option_station_list = []
    
    
    def __init__(self, ticket_day, station_start, station_option1, station_option2, station_option3):
        #클래스 초기화
        self.ticket_day = ticket_day
        self.station_start = station_start
        self.station_option1 = station_option1
        self.station_option2 = station_option2
        self.station_option3 = station_option3
        self.option_station_list = [station_option1, station_option2]
        if(ticket_day == 7):
            self.option_station_list += station_option3



#첫 시작페이지
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():


    if request.method == 'POST':
        
        if "submit1" in request.form:
        
            ticket_day = int(request.form['ticket_day'])
            station_start = request.form['station_start']
            station_option1 = request.form['station_option1']
            station_option2 = request.form['station_option2']
            station_option3 = request.form['station_option3']
            
            nailroform = NailroInput(ticket_day, station_start, station_option1, station_option2, station_option3)
            
            station_list = list(set(nailroform.option_station_list))
    
            time_g = excelParser.createTimeGraph()
            price_g = excelParser.createPriceGraph()
            time_graph = graph.Graph(time_g)
            price_graph = graph.Graph(price_g)
            paths = time_graph.find_Nailro_paths(ticket_day, nailroform.station_start, station_list)
            return render_template('index.html', nailroform=nailroform, paths=paths)

        
        if "submit2" in request.form:
            train_start = request.form['start']
            train_option = []
            for i in range(1, 11):
                tmp = 'option' + str(i)
                if (request.form[tmp] != ""):
                    train_option += [request.form[tmp]]
                    
            time_g = excelParser.createTimeGraph()
            price_g = excelParser.createPriceGraph()
            time_graph = graph.Graph(time_g)
            price_graph = graph.Graph(price_g)
            
            cost = time_graph.cost_of_path([train_start]+train_option)
            print (cost)
        
            return render_template('index.html', start = train_start, train_option=train_option, cost = cost)
       
    else: 
    #request.method == 'GET':
        #render_template를 이용하면, template폴더안에있는 html파일을 오픈해줌
        
        return render_template('index.html')




if __name__ == '__main__':
    port = int(os.getenv('PORT',  8000))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)


