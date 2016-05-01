import json
from pymongo import MongoClient

client = MongoClient()
db=client["project"]
collection=db["graph"]

cnt=0
with open('./data/Hindu.json') as data_file:    
    data = json.load(data_file)
    for i in range(len(data["articles"])):
    	url=data["articles"][i]["URL"]
    	articleId = data["articles"][i]["articleId"]
    	title = data["articles"][i]["title"]
    	source=data["articles"][i]["source"]
    	relations = data["articles"][i]["content"]["relations"]
    	sentimentMap=dict()
    	for relation in relations:
    		se=list()
    		oe=list()
    		score=0.0
    		if 'subject' in relation:
    			if 'entities' in relation['subject']:
    				for sub in relation['subject']['entities']:
    					se.append(sub['text'])

    		if 'object' in relation:
    			if 'entities' in relation['object']:
    				for sub in relation['object']['entities']:
    					oe.append(sub['text'])

	    		if 'sentimentFromSubject' in relation['object']:
	    			score=float(relation['object']['sentimentFromSubject']['score'])
	    			#print score

	    	if len(se)>0 and len(oe)>0:		
	    		for s in se:
	    			for o in oe:
	    				if (s,o) in sentimentMap:
	    					sc = sentimentMap[(s,o)]
	    					sentimentMap[(s,o)]=sc+score
	    				else:
	    					sentimentMap[(s,o)]=score

    	for key in sentimentMap:
    		record=dict()
    		record["articleId"]=articleId
    		record["title"]=title
    		record["URL"]=url
    		record["source"]=source
    		record["subjectEntity"]=key[0]
    		record["objectEntity"]=key[1]
    		record["polarity"]=sentimentMap[key]
    		#print sentimentMap[key]
    		collection.insert(record)
    		cnt+=1

    print "Inserted ",cnt, "records"
