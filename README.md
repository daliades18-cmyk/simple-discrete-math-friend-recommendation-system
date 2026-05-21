# Social Network Friend Recommendation System

## Project Description

The Social Network Friend Recommendation System is a Python-based project that suggests new friends to users based on mutual connections in a social network.

The system models the social network using graph concepts where:
- Users are represented as nodes
- Friendships are represented as edges

The recommendation mechanism identifies mutual friends and suggests users who are not already connected.

---

## Objectives

- To implement a social network model
- To apply Discrete Mathematics concepts in a real-world application
- To recommend friends using mutual connections
- To understand graph-based relationships

---

## Concepts Used

- Graph Theory
- Relations
- Sets
- Vertices and Edges
- Mutual Connections

---

## Features

- Add users
- Create friendships
- Display social network connections
- Recommend friends based on mutual friends

---

## Technologies Used

- Python
- Dictionaries
- Lists

---

## Working Principle

1. Users are added to the social network
2. Friendships are created between users
3. The system checks friends of friends
4. Existing friends are ignored
5. Users with mutual connections are recommended

---

## Sample Input

A -> B, C  
B -> A, D  
C -> A, D  
D -> B, C

---

## Sample Output

Friend Recommendations for A:

D (Mutual Friends: 2)

---

## How to Run

1. Install Python
2. Save the program as `social_network.py`
3. Open terminal or command prompt
4. Run the command:

```bash
python social_network.py
