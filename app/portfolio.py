import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path="app/resource/my_portfolio.xlsx"):
        self.file_path = file_path
        self.data = pd.read_excel(file_path)  # Read the Excel file containing project details
        self.chroma_client = chromadb.PersistentClient('vectorstore')  # Initialize ChromaDB PersistentClient
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")  # Create or retrieve a collection

    def load_portfolio(self):
        # Check if collection is empty, then add data from the Excel file
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=[row["TechStack"]],  # TechStack corresponds to the skills used
                    metadatas={"project_name": row["ProjectName"], "url": row["URL"]}, 
                    ids=[str(uuid.uuid4())]  # Generate a unique ID for each entry
                )

    def query_links(self, skills):
        # Query the collection for projects matching the given skills
        if not skills:
            return []  # Return empty list if no skills provided to prevent the error
        
        results = self.collection.query(query_texts=skills, n_results=2)
        
        # Extract metadatas from the results
        metadatas = results.get('metadatas', [])
        
        projects = []
        for metadata in metadatas:
            if isinstance(metadata, list):
                for meta in metadata:
                    if isinstance(meta, dict):
                        projects.append({
                            'project_name': meta.get('project_name', 'Unknown'),
                            'url': meta.get('url', '#')
                        })
            elif isinstance(metadata, dict):
                projects.append({
                    'project_name': metadata.get('project_name', 'Unknown'),
                    'url': metadata.get('url', '#')
                })
        
        return projects

    def get_all_projects(self):
        # Fetch all projects from the loaded Excel file
        projects = []
        for _, row in self.data.iterrows():
            projects.append({
                'project_name': row["ProjectName"],
                'url': row["URL"]
            })
        return projects
