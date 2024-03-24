"""
**Create Movie, Person, and Country Nodes with Relationships in Neo4j**

This Python script demonstrates creating nodes and relationships in a Neo4j database using the Neo4j Python Driver. Here's what the script does:

1. **Connects to Neo4j:** Establishes a connection to your Neo4j server using the provided URI and credentials (replace placeholders with your actual details).
2. **Defines Data:** Creates dictionaries containing information about a country, a person, and a movie.
3. **Constructs Cypher Query:** Creates a Cypher query that performs the following actions:
    - **Merges Country Node (if not existing):** Uses `MERGE` to create a country node if a node with the specified name doesn't already exist.
    - **Creates Person Node:** Creates a person node with the provided name and family name (optional).
    - **Creates Movie Node:** Creates a movie node with details like title, genre, and release year.
    - **Establishes Relationships:** Creates relationships of type `:ACTED_IN` between the person and movie nodes, and between the country and movie nodes (consider using a more appropriate relationship type for country-movie connections).
    - **Returns Created Nodes:** Returns the details of the newly created country, person, and movie nodes.
4. **Executes Query:** Executes the constructed Cypher query and handles potential errors.
5. **Prints Results (if successful):** If the query execution is successful, prints a message indicating the creation of the nodes.
6. **Closes Connection (always):** Ensures the connection to the Neo4j driver is closed, regardless of success or failure.

**Requirements:**

- Python 3.x
- Neo4j Python Driver (`pip install neo4j`)
- Neo4j database

**Before Running:**

- Install the Neo4j Python Driver.
- Configure the `URI` and `AUTH` variables with your Neo4j server connection details.
- Consider using a more suitable relationship type for the country-movie connection (e.g., `:PRODUCED_IN`).

**Usage:**

1. Run the script to create the nodes and relationships in your Neo4j database.

**Additional Notes:**

- This script assumes a basic understanding of Neo4j and Cypher queries.
- Refer to the Neo4j Manual (https://neo4j.com/docs/) for more details on Cypher syntax and the Neo4j Python Driver documentation (https://neo4j.com/docs/python-manual/current/) for advanced driver usage.
"""

from neo4j import GraphDatabase

URL = "bolt://0.0.0.0:7687"
USERNAME = "neo4j"
PASSWORD = "abc@123!zxy"

try:
    driver = GraphDatabase.driver(URL, auth=(USERNAME, PASSWORD))  # Replace credentials with yours
    print("Neo4j Driver installed successfully!")
    # Function to execute a Cypher query
    def execute_query(query, parameters=None):
        with driver.session() as session:
            # Execute the query with optional parameters
            result = session.run(query, parameters)
            print(result.data())
            # Access results using `data()` method
            return result.data()  # Return a list of dictionaries containing the results
        
    # Movie Country data for the actor
    country_data = {"name": "USA"}

    # Director data for the actor
    person_data = {"name": "name", "family": "family"}
    
    # Movie data with a new field "release_year"
    movie_data = {"title": "The Evil", "genre": "Data Science", "release_year": 2024}

    # Create movie query with dynamic property setting
    create_movie_query = f"""
    MERGE (country:Country {{name: "{country_data['name']}"}}) 
    CREATE (person:Person {{name: "{person_data['name']}"}}) 
    CREATE (m:Movie {{ {', '.join([f'{key}: "{movie_data[key]}"' for key in movie_data.keys()])} }})
    CREATE (person)-[:ACTED_IN]->(m)
    CREATE (country)-[:ACTED_IN]->(m)
    RETURN country, person, m
    """

    result = execute_query(create_movie_query)

    if result:
        print(f"Successfully created movie node: {result[0]}")  # Assuming single result


except Exception as e:
  print("Error:", e)
finally:
  if driver:
    driver.close()
