#!/usr/bin/python

from __future__ import print_function
from alchemyapi import AlchemyAPI
import json
import xml.sax
from sets import Set
import pprint


#read from file
body = []
title = []
alchemyapi = AlchemyAPI()

def remove_non_ascii(text):
	return ''.join(i for i in text if ord(i)<128)

class ArticleHandler(xml.sax.ContentHandler):
	def __init__(self):
		xml.sax.ContentHandler.__init__(self)
		self.isTitle = False
		self.isBody =False
		self.content = ''
  
	def startElement(self, name, attrs):
		#print("startElement '" + name + "'")
		if name == "title":
			self.isTitle = True
			self.isBody = False
			self.content = ''
		elif name == 'body':
			self.isTitle = False
			self.isBody = True
			self.content = ''
  
	def endElement(self, name):
		#print("endElement '" + name + "'")
		if name == 'title':
			title.append(self.content)
			self.isTitle = False
			self.content = ''
		elif name == 'body':
			body.append(self.content)
			self.isBody = False
			self.content = ''
 
	def characters(self, content):
		self.content+=content


def extract_entities(content):
	response = alchemyapi.entities('text', content,{'sentiment':1,'keywords':1,'entities':1,'requireEntities':1})
	entity_list = []
	if response['status'] == 'OK':
		#print('## Entities ##')
		for entity in response['entities']:
			word=entity['text'].encode('utf-8')
			#print('text: ', entity['text'].encode('utf-8'))
			if word not in entity_list:
				entity_list.append(word)
			#print('type: ', entity['type'])
			#print('relevance: ', entity['relevance'])
			#print('sentiment: ', entity['sentiment']['type'])
			#if 'score' in entity['sentiment']:
			#	print('sentiment score: ' + entity['sentiment']['score'])
			#	print('')
		return entity_list 

def extract_relations(content):
	response = alchemyapi.relations('text', content,{'sentiment':1,'keywords':1,'entities':1,'requireEntities':1})
	if response['status'] == 'OK':
		#print('## Object ##')
		#print(json.dumps(response, indent=4))
		##Steps###
		#1. Extract Subject, Object, Action from JSON
		#2. Store it in a file as Adjecency List
		#3. Plot simple Graph on that adjecency List
		#print('## Relations ##')
		subject_entities = []
		object_entities = []
		topic_entity_map = {}
		for relation in response['relations']:
			if 'action' in relation:
				topic = relation['action']['verb']['text'].encode('utf-8')
				if topic not in topic_entity_map:
					topic_entity_map[topic] = {'subject':[],'object':[]}
			if 'subject' in relation:
				if 'entities' in relation['subject']:
					for keyword in relation['subject']['entities']:
						if keyword['text'].encode('utf-8') not in subject_entities:
							subject_entities.append(keyword['text'].encode('utf-8'))
							if 'action' in relation:
								topic_entity_map[topic]['subject'].append(keyword['text'].encode('utf-8'))

			if 'object' in relation:
				if 'entities' in relation['object']:
					for keyword in relation['object']['entities']:
						if keyword['text'].encode('utf-8') not in object_entities:
							object_entities.append(keyword['text'].encode('utf-8'))	
							if 'action' in relation:
								topic_entity_map[topic]['object'].append(keyword['text'].encode('utf-8'))

		for item in topic_entity_map:
			if len(topic_entity_map[item]['subject']) >0 or len(topic_entity_map[item]['object']) >0:
				pprint.pprint(topic_entity_map[item])		 
					
		#print(subject_entities)	
		#print(object_entities)	
		#pprint.pprint(topic_entity_map)
	 #    	    print('Subject: ', relation['subject']['text'].encode('utf-8'))

	 #    	if 'action' in relation:
	 #    	    print('Action: ', relation['action']['text'].encode('utf-8'))

	 #    	if 'object' in relation:
	 #    	    print('Object: ', relation['object']['text'].encode('utf-8'))

	 #    	print('')			       


def main(sourceFileName):
	global title
	source = open(sourceFileName)
	xml.sax.parse(source, ArticleHandler())
	i=0

	for content in body:
		titleClean = remove_non_ascii(title[i])
		#print("****************************************************")
		#print(titleClean)
		i+=1
		contentClean = remove_non_ascii(content)
		entities=extract_entities(contentClean)
		for item in entities:
			print(item+",",end="")
		print(end="\n")	
		#extract_relations(contentClean)
		
		
		
if __name__ == "__main__":
	main("articles.xml")
