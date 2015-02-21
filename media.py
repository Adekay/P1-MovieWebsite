import random
import urllib


class Movie():
    """ Business object class for holding information related to a movie."""
    
    NUM_RELATED_LINKS = 5

    def __init__(self, title, storyline, poster_url, trailer_url, imdb_url, rt_url):
        self.title = title
        self.storyline = storyline
        self.poster_url = poster_url
        self.trailer_url = trailer_url
        self.imdb_url = imdb_url
        self.rt_url = rt_url
        self.related_links = []


    def build_related_content(self, content_sources):
        random.seed()

        self.related_links = []
        links_created = 0
        while links_created < Movie.NUM_RELATED_LINKS:
            source_pos = random.randint(0, len(content_sources) - 1)
            new_link = content_sources[source_pos].get_random_link(self)
            # Check if the new random link already exists in the list
            if new_link not in self.related_links:
                self.related_links.append(new_link)
                links_created = links_created + 1


    def get_related_content_links(self):
        content = ""

        for link in self.related_links:
            content += link
        return content


class RelatedContentSource():
    """Represents a source from which we can generate related content for the a Movie object."""

    def __init__(self, source_label, source_url, search_keywords):
        self.source_label = source_label
        self.source_url = source_url
        self.search_keywords = search_keywords

    # A single related link template
    related_link_template = '''
    <a href="{link_url}" target="_blank"> Find '{keyword}' on {source}</a></br>
    '''

    def get_random_link(self, movie):
        # Retrieves a random related link for the movie
        keyword_pos = random.randint(0, len(self.search_keywords) - 1)
        keyword_key = self.search_keywords.keys()[keyword_pos]

        return RelatedContentSource.related_link_template.format(
            link_url=self.source_url + urllib.quote_plus(movie.title) + urllib.quote_plus(" " + self.search_keywords[keyword_key]),
            keyword=keyword_key,
            source=self.source_label
        )
