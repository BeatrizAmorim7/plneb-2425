from bs4 import BeautifulSoup
import requests
import json

# Extrair os links das últimas edições da revista a partir da página de archives.
def get_issue_urls(main_url, num_issues=4):  # num_issues é o número de edições a ser extraído
    response = requests.get(main_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    issue_links = {}

    for archive in soup.find_all("a", class_="title")[:num_issues]:
        issue_links[archive.get_text(strip=True)] = archive.get("href")

    return issue_links

# Extrair informações detalhadas do artigo a partir da página do artigo
def extract_article_info(article_url):
    response = requests.get(article_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    abstract = {}
    abstract_div = soup.find("section", class_="item abstract")  # secção do resumo

    if abstract_div:
        for paragraph in abstract_div.find_all("p"):
            strong = paragraph.find("strong")  # verifica se o parágrafo tem algum título (como a introdução, métodos, etc)
            if not strong:
                if not abstract:  # o primeiro parágrafo sem strong é o resumo (é só texto corrido)
                    abstract = paragraph.get_text(strip=True)
                else:
                    if isinstance(abstract, str):  # Concatena se for string
                        abstract += " " + paragraph.get_text(strip=True)
            else:
                section = strong.get_text(strip=True).rstrip(':')  # Obtém o título da secção, como introdução, etc
                strong.extract()  # Remove o <strong> do parágrafo
                abstract[section] = paragraph.get_text(strip=True)  # Associa o título ao conteúdo

    # Keywords
    keywords = []
    keywords_div = soup.find("section", class_="item keywords")
    if keywords_div:
        keywords = [kw.strip() for kw in keywords_div.span.get_text().split(",")]  # Divide e limpa

    # DOI
    doi = ""
    doi_div = soup.find("section", class_="item doi")
    if doi_div and doi_div.find("a"):
        doi = doi_div.find("a")["href"].strip()

    # data de publicação
    publish_date = ""
    date_div = soup.find("div", class_="item published")
    if date_div and date_div.find("div", class_="value"):
        publish_date = date_div.find("div", class_="value").get_text(strip=True)

    # PDF link
    pdf_link = ""
    pdf_section = soup.find("div", class_="item galleys")
    if pdf_section:
        pdf_tag = pdf_section.find("a", class_="obj_galley_link pdf")
        if pdf_tag:
            pdf_link = pdf_tag["href"].strip()

    return abstract, keywords, doi, publish_date, pdf_link

def scrape_articles():
    main_url = "https://revista.spmi.pt/index.php/rpmi/issue/archive"
    issue_urls = get_issue_urls(main_url)
    article_data = []

    for issue_title, issue_url in issue_urls.items():  # Itera por cada edição
        response = requests.get(issue_url)  # Acede à página da edição
        soup = BeautifulSoup(response.text, 'html.parser')

        for article_div in soup.find_all("div", class_="obj_article_summary"):
            title_tag = article_div.find("h3", class_="title").find("a")
            article_url = title_tag["href"]
            if not article_url.startswith("http"):
                article_url = "https://revista.spmi.pt" + article_url

            title = title_tag.get_text(strip=True)
            span_title = title_tag.find("span")
            if span_title:
                title = span_title.get_text(strip=True)

            # Authors
            authors = []
            authors_div = article_div.find("div", class_="authors")
            if authors_div:
                authors = [a.strip() for a in authors_div.get_text().split(",")]

            abstract, keywords, doi, publish_date, pdf_link = extract_article_info(article_url)

            article_data.append([
                title, article_url, authors, issue_title,
                abstract, keywords, doi, publish_date, pdf_link
            ])

    return article_data

# Guardar ficheiro JSON
if __name__ == "__main__":
    raw_data = scrape_articles()
    articles = []

    for data in raw_data:
        title, url, authors, archive, abstract, keywords, doi, publish_date, pdf_link = data
        article = {
            "title": title,
            "url": url,
            "authors": authors,
            "archives": archive,
            "abstract": abstract,
            "keywords": keywords,
            "doi": doi,
            "publish_date": publish_date,
            "pdf_link": pdf_link
        }
        articles.append(article)

    with open("revista.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

    print(f"Successfully scraped {len(articles)} articles")
 