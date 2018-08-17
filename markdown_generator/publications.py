
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes an Excel file of publications with metadata and converts them for use with [academicpages.github.io](academicpages.github.io). 

# ## Data format
# 
# The Excel file should have a sheet called "main", which contains the table of publications.
# The data sheet needs to have the following columns: pub_date, title, venue, author, abstract, bibtex, url_slug, paper_url, slides_poster, video, dataset, code, award, with a header at the top. 
# 
# - `pub_date` must be formatted as YYYY-MM-DD.
# - `url_slug` will be the descriptive part of the .md file and the permalink URL for the page about the paper. 
#   The .md file will be `YYYY-MM-DD-[url_slug].md` and the permalink will be `https://[yourdomain]/publications/YYYY-MM-DD-[url_slug]`


# ## Import pandas
# 
# We are using the very handy pandas library for dataframes.

import pandas as pd

# ## Import Excel
# 
# Pandas makes this easy with the read_excel function. 
# 
publications = pd.read_excel("publications.xls", sheetname='main')


# ## Escape special characters
# 
# YAML is very picky about how it takes a valid string, so we are replacing single and double quotes (and ampersands) with their HTML encoded equivilents. This makes them look not so readable in raw format, but they are parsed and rendered nicely.

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


# ## Creating the markdown files
# 
# This is where the heavy lifting is done. This loops through all the rows in the TSV dataframe, then starts to concatentate a big string (```md```) that contains the markdown for each type. 
# It does the YAML metadata first, then does the description for the individual page. If you don't want something to appear (like the "Recommended citation")

import os
for row, item in publications.iterrows():
    
    md_filename = str(item.pub_date.date()) + "-" + ('%04d' % item.url_slug) + ".md"
    html_filename = str(item.pub_date.date()) + "-" + ('%04d' % item.url_slug)
    year = str(item.pub_date.year)
    
    print("%s\t%s\t%s" % (md_filename, html_filename, year))

    ## YAML variables
    
    md = "---\ntitle: \""   + item.title + '"\n'
    
    md += """collection: publications"""
    
    md += """\npermalink: /publication/""" + html_filename
    
    if len(str(item.abstract)) > 5:
        md += "\nabstract: '" + html_escape(item.abstract) + "'"
    
    md += "\ndate: " + str(item.pub_date.date()) 

    md += "\nauthor: '" + html_escape(item.author) + "'"

    md += "\nvenue: '" + html_escape(item.venue) + "'"
    
    paper_url = str(item.paper_url).strip()
    if paper_url.startswith('http'):
        md += "\npaperurl: '" + paper_url + "'"
    elif len(paper_url) > 5:
        md += "\npaperurl: '../files/" + paper_url + "'"
        paper_url = '../files/' + paper_url

    if len(str(item.bibtex)) > 5:
        bib_filename = str(item.pub_date.date()) + "-" + ('%04d' % item.url_slug) + ".txt"
        md += "\nbiburl: '../publications/" + bib_filename + "'"

    if len(str(item.slides_poster)) > 5:
        md += "\nslides_poster: "+ item.slides_poster 

    if len(str(item.video)) > 5:
        md += "\nvideo: " + item.video 

    if len(str(item.dataset)) > 5:
        md += "\ndataset: " + item.dataset

    if len(str(item.code)) > 5:
        md += "\ncode: " + item.code

    if len(str(item.award)) > 5:
        md += "\naward: " + html_escape(item.award) 
    
    md += "\n---"
    
    ## Markdown description for individual page
    
    if len(str(item.paper_url)) > 5:
        md += "\n\n<a href='" + paper_url + "'>Download paper here</a>\n" 
        
    if len(str(item.abstract)) > 5:
        md += "\n" + html_escape(item.abstract) + "\n"
        
    #md += "\nRecommended citation: " + item.citation
    
    md_filename = os.path.basename(md_filename)

    with open("../_publications/" + md_filename, 'w') as f:
        f.write(md)

    if len(str(item.bibtex)) > 5:
        with open("../_publications/" + bib_filename, 'w') as f:
            f.write(item.bibtex)
