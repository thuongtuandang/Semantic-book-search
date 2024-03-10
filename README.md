# Semantic book search project

In this project, we will create a vector database from a csv file and perform semantic search with this vector database. It is a full-stack project with react frontend, django backend and qdrant database.

# Results

In the results folder, you will see the results with the following search text:

"fantasy novel with a dark theme"

"romantic novel with forbidden love"

The results are good.

# Create dabase

The database for books is available at:

https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata

We will use qdrant to create a vector database for books based on their descriptions (see details in database/books.ipynb)

Then you can start docker and run qdrant in terminal with the command: 

    docker run -p 6333:6333 qdrant/qdrant

After that, you can take a look at you vector database at this link
http://localhost:6333/dashboard#/collections/books

Note that you must keep it running to perform semantic search.

# Backend

For backend, I use django. Assume that we receive the search text from frontend, and here are steps to do:
1. Use QdrantClient to perform search where the query vector is encoded with SentenceTransformer.
2. Return results with several important fields (authors, description, thumbnail) together with their indices

# Frontend

For frontend, I use React. We use POST method with header 'Content-Type': 'application/json'. After that, we can use map method with key = index to separate the results from backend.