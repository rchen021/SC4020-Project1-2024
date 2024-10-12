import urllib.request
import io
import zipfile
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import time
import networkx as nx
import os
from networkx.algorithms.community.quality import modularity

def load_dolphin_network():
    """Load Dolphin Social Network Dataset"""
    file_path = 'dataset/dolphins.gml'
    if os.path.exists(file_path):
        G = nx.read_gml(file_path)
        print(f"Dolphin network loaded with {len(G.nodes())} nodes and {len(G.edges())} edges.")
    else:
        print("Dolphin dataset file not found. Please check the file path.")
    return G

def load_football_network():
    """Load American Football Network Dataset"""
    url = "http://www-personal.umich.edu/~mejn/netdata/football.zip"
    
    try:
        sock = urllib.request.urlopen(url)  # open URL
        s = io.BytesIO(sock.read())  # read into BytesIO "file"
        sock.close()

        zf = zipfile.ZipFile(s)  # zipfile object
        gml = zf.read("football.gml").decode()  # read gml data
        gml = gml.split("\n")[1:]  # remove first line
        G = nx.parse_gml(gml)  # parse gml data
        print(f"American Football network loaded with {len(G.nodes())} nodes and {len(G.edges())} edges.")
    except Exception as e:
        print("Error loading American Football dataset:", e)
    return G

def load_amazon_network():
    """Load Amazon Co-Purchasing Network Dataset"""
    file_path = 'dataset/com-amazon.ungraph.txt'
    if os.path.exists(file_path):
        G = nx.read_edgelist(file_path)
        print(f"Amazon co-purchasing network loaded with {len(G.nodes())} nodes and {len(G.edges())} edges.")
    else:
        print("Amazon dataset file not found. Please check the file path.")
    return G

def load_book_network():
    """Load American Kreb's book network Dataset"""
    file_path = 'dataset/polbooks.gml'
    if os.path.exists(file_path):
        G = nx.read_gml(file_path)
        print(f"American Kreb's book network loaded with {len(G.nodes())} nodes and {len(G.edges())} edges.")
    else:
        print("American Kreb's book dataset file not found. Please check the file path.")
    return G

def load_power_grid_network():
    """Load American Kreb's book network Dataset"""
    file_path = 'dataset/polbooks.gml'
    if os.path.exists(file_path):
        G = nx.read_gml(file_path)
        print(f"American Kreb's book network loaded with {len(G.nodes())} nodes and {len(G.edges())} edges.")
    else:
        print("American Kreb's book dataset file not found. Please check the file path.")
    return G

def main():
    print("Choose a dataset to load:")
    print("1. Dolphin Social Network")
    print("2. American Football Network")
    print("3. Amazon Co-Purchasing Network")
    print("4. American Kreb's book Network")

    choice = input("Enter the number of your choice: ")
    print()

    if choice == '1':
        G = load_dolphin_network()
        x = 'Dolphin Social Network'
    elif choice == '2':
        G = load_football_network()
        x = 'American Football Network'
    elif choice == '3':
        G = load_amazon_network()
        x = 'Amazon Co-Purchasing Network'
    elif choice == '4':
        G = load_book_network()    
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return

    print()
    if G:
        s = 0
        total_time = 0
        for i in range(3):  # Looping 3 times
            # Start timer
            start_time = time.time()

            # Get the community partition using the Louvain method
            communities = nx.community.louvain_communities(G, resolution=1, seed = 123)

            # Calculate the modularity of the partition
            modularity_score = modularity(G, communities)
            print(f"Modularity (Run {i+1}):", modularity_score)

            s += modularity_score

            # End timer and calculate running time
            end_time = time.time()
            run_time = end_time - start_time
            total_time += run_time
            print(f"Run {i+1} time: {run_time:.4f} seconds")

        # Print mean modularity and mean running time
        print(f'\nMean modularity: {s/3:.4f}')
        print(f'Average running time: {total_time/3:.4f} seconds')

if __name__ == "__main__":
    main()
