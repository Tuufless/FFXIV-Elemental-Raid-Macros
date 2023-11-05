# Run with mdl -s .\.mdl.rb <path>

# Enable all rules by default
all

# Rules found here: https://github.com/updownpress/markdown-lint/tree/master/rules

exclude_rule 'MD001'    # allow headers to skip levels
exclude_rule 'MD033'    # allow in-line HTML
exclude_rule 'MD040'    # fenced code-blocks don't need a language specified (macros)
exclude_rule 'MD041'    # allow files that do not start with a header

# Nested lists should be indented with four spaces.
rule 'MD007', :indent => 2
