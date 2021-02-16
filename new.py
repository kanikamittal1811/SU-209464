is_tes =True
color = True
new_html= True



if is_tes :
        # get change clf_5 to clf
        with open(path+'/ip/clf.json') as f: # make this path variable
            #parse json
            data = json.load(f)
            # get clips
            for i in data['compos']:
                if i['class']=="Background":
                    continue
                else:
                    clas= i['class']
                    id= i['id']
                    clip_path= path+'/new/'+clas+'/'+str(id)+'.jpg'
                    #add clip path in new json
                    i['clip_path']=clip_path

                    # get path of project directory +"tesseract E:\\smart-ui\\uied\\final\\"  E:\\smart-ui\\uied\\final\\
                    command= 'cmd /c '+"tesseract " +clip_path.replace("/", "\\")+" stdout -l eng > temp.txt"
                    os.system(command) #"E:\\smart-ui\\uied\\final\\
                    a = open("temp.txt", "r")
                    var =a.read()
                    # set var
                    i["ocr"]= var
            # make new json
            with open(path+'/new.json', 'w') as json_file:
                json.dump(data, json_file)
if color:
    
    #print(km.cluster_centers_[0][0])
    with open(path+'/new.json') as f: 
        data = json.load(f)
        for i in data['compos']:
            if i['class']=="REDUNDANT":
                continue
            else:
                clip_path=i['clip_path'] #"E:\\smart-ui\\uied\\final\\"+
                img = cv2.imread(clip_path.replace("/", "\\")) ### set directory path
                #rgb = img[0][0];
                all_pixels = img.reshape((-1,3))
                from sklearn.cluster import KMeans
                k = 2
                km = KMeans(n_clusters=k)
                km.fit(all_pixels)
                rgb= km.cluster_centers_[0]
                rgb=rgb[::-1]
                rgb= rgb.astype(int)
                i["color"]= '#%02x%02x%02x' % tuple(rgb)
        with open(path+'/new.json', 'w') as json_file:
            json.dump(data, json_file)


if new_html:
    htmltext="""<!DOCTYPE html>
    <html>
    <head>
    <title>HTML, CSS and JavaScript demo</title>
    </head>
    <body>"""
    char= ['\n', '\f', '\\','/',']','[', '(', ")" ]
    with open(path+'/new.json') as f: # make this path variable
        #parse json
        data = json.load(f)
        # get clips
        for i in data['compos']:

            # """
            #           'CheckBox': (0, 0, 255), 
            #           'Chronometer': (255, 166, 166),
            #           'ImageButton': (77, 77, 255),  
            #           'ProgressBar': (166, 0, 255),
            #           'RadioButton': (166, 166, 166),
            #           'RatingBar': (0, 166, 255), 
            #           'SeekBar': (0, 166, 10), 'Spinner': (50, 21, 255),
            #           'Switch': (80, 166, 66), 
            #           'ToggleButton': (0, 66, 80), 
            #           'VideoView': (88, 66, 0),
            # 
            #           'EditText': (255, 166, 0),
            #           'ImageView': (255, 0, 166) -
            #           'EditText': (255, 166, 0), -
            #           'Button': (0, 255, 0), -
            #           'TextView': (169, 255, 0), ' -
            #           'NonText': (0,0,255), -
            #           'Compo':(0, 0, 255), -
            #           'Text':(169, 255, 0), -
            #           'Block':(80, 166, 66) -
            # """
            if i['class']=="REDUNDANT":
                continue

            elif(i['class']=="Button"):
                #class editText
                div ='<div style="position: absolute; top:'+str(i["row_min"])+'px; left:'+str(i["column_min"])+'px; border:3px solid black; height:'+str(i["height"])+'px; width:'+str(i["width"])+'px;"><button style="background-color:'+i['color']+';">'+''.join([c for c in i['ocr'] if c not in char])+'</button></div>'
                htmltext=htmltext+div


            elif(i['class']=="EditText"):
                #class button
                #add input and form
                div= 
                div ='<div style="background-color:'+i['color']+'; position: absolute; top:'+str(i["row_min"])+'px; left:'+str(i["column_min"])+'px; border:3px solid black; height:'+str(i["height"])+'px; width:'+str(i["width"])+'px;">'+''.join([c for c in i['ocr'] if c not in char])+'</div>'
                htmltext=htmltext+div


            elif(i['class']=="ImageView"):

                #class image view

                # make if condition if text present or not
                div ='<div style="background-color:'+i['color']+'; position: absolute; top:'+str(i["row_min"])+'px; left:'+str(i["column_min"])+'px; border:3px solid black; height:'+str(i["height"])+'px; width:'+str(i["width"])+'px;">'+''.join([c for c in i['ocr'] if c not in char])+'</div>'
                htmltext=htmltext+div
            
            elif(i['class']=='CheckBox'):
                div='<div style="background-color:'+i['color']+'; position: absolute; top:'+str(i["row_min"])+'px; left:'+str(i["column_min"])+'px; border:3px solid black; height:'+str(i["height"])+'px; width:'+str(i["width"])+'px;">'+'<form action="#"><input type="checkbox" ></form>'+'</div>'
                
                htmltext=htmltext+div

            elif(i['class']=='Chronometer'):
                div='<div style="background-color:'+i['color']+'; position: absolute; top:'+str(i["row_min"])+'px; left:'+str(i["column_min"])+'px; border:3px solid black; height:'+str(i["height"])+'px; width:'+str(i["width"])+'px;">'+'<form action="#"><input type="checkbox" ></form>'+'</div>'
                
                htmltext=htmltext+div

            elif(i['class']=='ImageButton'):
                
                htmltext=htmltext+div

            elif(i['class']=='ProgressBar'):
                
                htmltext=htmltext+div

            elif(i['class']=='RadioButton'):
                
                htmltext=htmltext+div

            elif(i['class']=='RatingBar'):
                
                htmltext=htmltext+div

            elif(i['class']=='SeekBar'):
                htmltext=htmltext+div

            elif(i['class']=='Switch'): 
                htmltext=htmltext+div

            elif(i['class']=='ToggleButton'):
                htmltext=htmltext+div

            elif(i['class']=='VideoView'):
                
                htmltext=htmltext+div






            else:
                #class text view/ Text/ Compo/ block/Nontext/
                div ='<div style="background-color:'+i['color']+'; position: absolute; top:'+str(i["row_min"])+'px; left:'+str(i["column_min"])+'px; border:3px solid black; height:'+str(i["height"])+'px; width:'+str(i["width"])+'px;">'+''.join([c for c in i['ocr'] if c not in char])+'</div>'
                htmltext=htmltext+div
                
        htmltext= htmltext+"</body></html>"
        Html_file= open(path+'/output_new.html',"w")
        Html_file.write(htmltext)
        Html_file.close()
    #print(htmltext)
                