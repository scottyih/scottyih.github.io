# Scott Wen-tau Yih's personal website

A Jekyll site hosted on GitHub Pages at https://scottyih.org.

## Updating content

- Homepage and research overview: `_pages/bio.md`.
- Publications: one Markdown record per paper in `_publications/`, with an accompanying BibTeX `.txt` file.
- Public releases: use `code`, `dataset`, `model`, and `project` in publication front matter. Each accepts a URL or a list of URLs; links appear in the archive, individual paper pages, and homepage selections. Confirm the release belongs to the paper rather than a dependency or unrelated benchmark.
- Use `Wen-tau Yih` consistently in publication author lists, and `Yih, Wen-tau` when BibTeX uses surname-first names.
- Accepted papers use the conference name and year in `venue` (for example, `COLM 2026`), with the archive date in that year. Prefer the proceedings link for `paperurl` and retain the arXiv link as `preprint` when available.
- Homepage representative papers: select the seven most-cited papers from Google Scholar. Set `selected: true`, an integer `selected_rank` in descending citation order, and a short `highlight` in publication front matter. Record the dated ranking in `_data/representative_publications.yml` when refreshing the selection. These papers appear first in the combined Selected papers section.
- Award-winning papers: set `award` and a short `highlight` in publication front matter. Additional award-winning papers follow the representative papers in the same homepage list, newest first. Each paper appears once, with award badges also shown on the archive and individual pages.
- Tutorial resources: `_pages/talks.html`. Individual talk records live in `_talks/`.
- Profile and search metadata: `_config.yml`.
- CV publication is deferred while the drafts are being revised. The CV page and all CV downloads are excluded in `_config.yml`, and CV links are omitted from navigation and the homepage.
- Dated conference paper rankings: `_data/publication_rankings.yml`. Verified entries appear beside the paper in the publication archive, detail page, and homepage selections. Each entry includes its source link and the date of the list.
- Dated citation evidence: set `show_citation_count: true` in publication front matter to display the paper's count, entry link, and snapshot date from `_data/representative_publications.yml`. This is enabled for DistMult and appears in the same three views. The count describes citations to the paper; it does not establish a conference rank or measure how often the method is used.

The October 2026 content update used Google Scholar for coverage and publication details, ACL Anthology for conference metadata and BibTeX, and arXiv and publisher pages for primary records. New entries include `source_urls` for provenance. Published versions replace matching preprints; an available preprint is retained as an additional link. Patents and edited proceedings were excluded from this publication update. Dates with only month or year precision use the first day for sorting; the archive displays the year.

The homepage describes multi-agent systems and memory for automated research, with recursive self-improvement as a current research direction. Citation counts are linked through Google Scholar, with dated snapshots shown for papers that have `show_citation_count` enabled.

The [publication release audit](PUBLICATION_RELEASE_AUDIT.md) covers all 179 records as of 23 October 2026. Its source evidence and outcomes are stored in `_data/publication_release_audit.yml`. “No verified release found” is a dated search result, not a claim that no release exists. Announced releases that are unavailable and historical links that could not be reverified are recorded explicitly.

## Conference paper rankings

Record a placement only after reading the original Paper Digest list and confirming the paper, its rank, and the conference year. Preserve the list's own date rather than substituting the retrieval date. Match the list's scope and wording: a ranking across several conferences must name that group, and “Most Influential Papers” should not be relabeled as a citation ranking unless the source states that criterion.

The data schema is:

```yaml
source: Paper Digest
papers:
  /publication/PAPER-PERMALINK:
    - verified: true
      rank: 1
      kind: conference
      conference: CONFERENCE
      conference_year: 2020
      source: Paper Digest
      source_url: https://resources.paperdigest.org/EXACT-LIST-URL/
      list_title: Most Influential CONFERENCE Papers
      list_date: March 2025
      label: OPTIONAL ACCURATE DESCRIPTION OF THE RANKING AND ITS SCOPE
```

This is a schema example. Replace its placeholders and example rank with the verified source details. The October 2026 update uses the user's saved Paper Digest conference lists and the “100 Must-Read” NLP and machine learning lists. The site displays the conference ranking when available; rankings across several conferences are retained as supporting data. Each source record preserves its list version, publication and modification dates, selection criteria, and the saved HTML's hash.

## Theme documentation

A Github Pages template for academic websites. This was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License. See LICENSE.md.

I think I've got things running smoothly and fixed some major bugs, but feel free to file issues or make pull requests if you want to improve the generic template / theme.

# Instructions

1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section
1. (Optional) Use the Jupyter notebooks or python scripts in the `markdown_generator` folder to generate markdown files for publications and talks from a TSV file.

See more info at https://academicpages.github.io/

## To run locally (not on GitHub Pages, to serve on your own computer)
1. Clone the repository and made updates as detailed above
1. Make sure you have ruby-dev, bundler, and nodejs installed: `sudo apt install ruby-dev ruby-bundler nodejs`
1. Run `bundle clean` to clean up the directory (no need to run `--force`)
1. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
1. Run `bundle exec jekyll serve` to generate the HTML and serve it from localhost:4000

# Changelog -- bugfixes and enhancements

There is one logistical issue with a ready-to-fork template theme like academic pages that makes it a little tricky to get bug fixes and updates to the core theme. If you fork this repository, customize it, then pull again, you'll probably get merge conflicts. If you want to save your various .yml configuration files and markdown files, you can delete the repository and fork it again. Or you can manually patch. 

To support this, all changes to the underlying code appear as a closed issue with the tag 'code change' -- get the list [here](https://github.com/academicpages/academicpages.github.io/issues?q=is%3Aclosed%20is%3Aissue%20label%3A%22code%20change%22%20). Each issue thread includes a comment linking to the single commit or a diff across multiple commits, so those with forked repositories can easily identify what they need to patch.
