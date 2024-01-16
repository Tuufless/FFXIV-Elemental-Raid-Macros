# FFXIV Elemental Raid Macros

Hello! This is the underlying Github repository for the
[FFXIV Elemental Raid Macros](https://tuufless.github.io/FFXIV-Elemental-Raid-Macros/) site.

The website is generated via [Jekyll](https://jekyllrb.com/) using [Just-The-Docs](https://just-the-docs.github.io/just-the-docs/)
as a theme.

## How to contribute

1. Make a fork of the repository.
2. Make your edits in the fork.
3. Create a Pull Request- once approved, your edits will be merged into the
main repository.

## Testing locally

Before pushing, it is often a good idea to build and preview the created site
locally to check if everything is working as expected. This lets you test
changes before committing them, and avoids having to wait for Github Pages.

### Setup

In order to build the site locally, you'll first need to:

1. [Download and install Ruby](https://www.ruby-lang.org/en/downloads/)
2. [Download and install Jekyll](https://jekyllrb.com/docs/installation/#guides)
3. Install the project dependencies using `bundle install`.

### Serving

Once Ruby and Jekyll are installed, you can generate the site via the command:
```
bundle exec jekyll serve
```
This will generate the requisite HTML pages under the `_site` folder (note that `_site` is part of `.gitignore`).

Once the site has been built and running, you can then open it on your browser
by navigating to `http://localhost:4000/`.

## Assets

Image assets should be placed in the `assets` directory- this is done in order
to support future localisation efforts, as relative image paths from the
various pages don't seem to work well.
