import media
import fresh_tomatoes
import xml.etree.ElementTree as ET
import json


def load_movie(movieElement):
    # Creates a Movie object from an XML element
    movie = media.Movie(movieElement.find("Title").text,
                        movieElement.find("Description").text,
                        movieElement.find("PosterURL").text,
                        movieElement.find("TrailerURL").text,
                        movieElement.find("IMDB").text,
                        movieElement.find("RT").text)
    return movie


def load_related_sources():
    sources_file = open("sources.dat")
    sources_data = json.load(sources_file)

    # Load the list of keywords from the JSON encoded file
    keywords_file = open("keywords.dat")
    search_keywords = json.load(keywords_file)
    keywords_file.close()

    related_sources = []
    for source in sources_data.keys():
        content_source = media.RelatedContentSource(source, sources_data[source], search_keywords)
        related_sources.append(content_source)
    
    return related_sources


def load_data():
    # Load the list of source for related link material
    related_sources = load_related_sources()

    # Load the XML file containing movie details
    tree = ET.parse("movielist.xml")
    root = tree.getroot()

    # Build the list of Movie objects, generating the related links as we go
    movies = []
    for child in root:
        movie = load_movie(child)
        movie.build_related_content(related_sources)
        movies.append(movie)
    return movies


def start_website():
    fresh_tomatoes.open_movies_page(load_data())

start_website()
