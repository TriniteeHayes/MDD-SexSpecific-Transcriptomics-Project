import GEOparse

def download_geo(accession="GSE98793", output="GSE98793"):
    print(f"Downloading {accession}...")
    gse = GEOparse.get_GEO(geo=accession, destdir=output)
    print("Done!")
    return gse

if __name__ == "__main__":
    download_geo()
