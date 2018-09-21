# coding=utf-8

from math import sqrt

import networkx as nx
import random
import numpy as np
import community
import time
import infomap

class cada():
	def __init__(self, graph, algorithm='louvain', resolution=0.1):
		
		# First do community detection
		if algorithm == 'louvain':
			partition = community.best_partition(graph, resolution=resolution)
		else:
			partition = self.run_infomap(graph)
		
		communities = set()
		for node in graph.nodes():
			if node in partition:
				communities.add(partition[node])

		anom_score = {}

		# Compute anomaly score for each node
		for node in graph.nodes():
			comms = {}
			for neighbor in graph.neighbors(node):
				if neighbor != node:
					if partition[neighbor] not in comms:
						comms[partition[neighbor]] = 0

					comms[partition[neighbor]] += 1

			if len(comms) > 0:
				# The number of communities it is connected to. 
				comms = np.array(list(comms.values()))
				# print('nr communities connected', comms)
				max_com = np.max(comms)
				# print('Maxcommunity', max_com)
				comms = comms / max_com
				# print('Communities normalized', comms)
				anom_score[node] = np.sum(comms)		
				# print('Anomaly score., ', anom_score[node])

		self.anomaly_scores = sorted(anom_score.items(), key=lambda x: x[1])[::-1]


	def run_infomap(self, graph):
		"""
		Runs Infomap with infomap package 
		"""
		infomapSimple = infomap.Infomap("--two-level --silent")
		network = infomapSimple.network()
		
		for e in graph.edges():
			network.addLink(e[0], e[1])

		partition = {}
		infomapSimple.run();
		for node in infomapSimple.iterTree():
			if node.isLeaf():
				partition[node.physicalId] = node.moduleIndex()

		return partition

	def get_anomaly_scores(self, nr_anomalies=None):
		"""
		Returns tuple (node, anomaly_score) for either nr_anomalies or all
		"""
		if nr_anomalies:
			return self.anomaly_scores[:nr_anomalies]
		else:
			return self.anomaly_scores 

	def get_top_anomalies(self, nr_anomalies=100):
		"""
		Returns highest scoring anomalies
		"""					
		anomalies = []
		for anomaly in self.anomaly_scores[:nr_anomalies]:
			anomalies.append(anomaly[0])

		return anomalies

	def get_anomalies_threshold(self, threshold):
		"""
		Returns anomalies that are above a certain threshold.
		"""
		anomalies = []

		for anomaly in self.anomaly_scores:
			if anomaly[1] > threshold:
				anomalies.append(anomaly[0])
			else:
				break

		return anomalies


