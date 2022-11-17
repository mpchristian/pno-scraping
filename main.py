import helpers


def get_articles(main_page_url, amount):
    """It recieves the url of the main page and the max naumber of artiles;
    Uses all helper functions: fetch, scrape_articles, scrape_article,
    get_name_of_article, download and scrape_next_page_link
    to get the articles and download the pdf version available
    """

    current_page_url = main_page_url
    all_articles_data = []
    counter = 1

    while current_page_url and counter <= amount:
        current_page_content = helpers.fetch(current_page_url)
        urls_current_page = helpers.scrape_articles(
          current_page_content,
          ".entry-title.h2 a::attr(href)")

        for url in urls_current_page:
            current_article_content = helpers.fetch(url)
            current_article = helpers.scrape_article(current_article_content)
            filename = helpers.get_name_of_article(
              current_article,
              "/home/christian/Personal-projects/pno-scraping/roteiros"
              )
            helpers.download(current_article['pdf_url'], filename)

            counter += 1
            if counter > amount:
                break

        current_page_url = helpers.scrape_next_page_link(
          current_page_content,
          "a.next.page-numbers::attr(href)")

    return all_articles_data


# Execute
url = 'https://perguntarnaoofende.com/?s=roteiro'

get_articles(url, 3)
