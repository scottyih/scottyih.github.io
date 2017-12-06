---
title: "Continuous Representations for Natural Language Understanding"
collection: talks
type: "Tutorial"
permalink: /talks/2017-07-19-tutorial-deeplearn2017
venue: "International Summer School on Deep Learning 2017"
date: 2017-07-19
location: "Bilbao, Spain"
---

[Link to Slides](https://github.com/scottyih/Slides/blob/master/DeepLearn2017-Yih%20Deck.pptx)

Understanding human language has been one of the long-standing research goals since the dawn of AI. In this lecture, we will discuss how recently developed methods, mostly deep neural network models, advance the state of the art. The lecture starts from the broad introduction of the research of natural language processing, analyzing why understanding language remains difficult. We will introduce several representative NLP tasks and discuss the role of machine leaning in the data-driven approaches. Historical and modern paradigms of problem formulations and models will also be briefly surveyed in this part.

The rest of lecture focuses on two key natural language understanding tasks: information extraction and question answering. Transforming unstructured text to structured databases, information extraction aims to find the entities and their relationships in text, as well as to make the extracted facts easily accessible programmatically. We will first give an overview on the basic problem setting, such as binary relation extraction as sequence labeling problems. After that, we will emphasize more on the latest distant supervision methods, which model the multi-sentence, n-ary relation settings using structured LSTM models. New approaches for embedding entities and relations in a knowledge base for reasoning for previously unknown facts will also be covered.

Question answering, while often used as the means to demonstrate machine intelligence, is an important application for fulfilling user's information need. In this part, we'll start by introducing the general framework of answering question using unstructured text, such as Wikipedia or the Web, and describe the current state-of-the-art deep learning approaches. We will also discuss how to leverage structured data such as databases or tables to answer questions, with the focus on semantic parsing methods.
QA with knowledge base aims to answer natural language questions using real-world facts stored in an existing, large-scale database. The representative approach for this task is to develop a semantic parser (of questions), which will be the main focus. Other approaches like text matching in the embedding space and those driven by information extraction will also be discussed. 
