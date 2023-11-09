# Run with mdl -s .\.mdl.rb <path>

# Enable all rules by default
all

# Rules found here: https://github.com/updownpress/markdown-lint/tree/master/rules

exclude_rule 'MD001'    # allow headers to skip levels
exclude_rule 'MD024'    # allow duplicate headers
exclude_rule 'MD033'    # allow in-line HTML
exclude_rule 'MD034'    # allow bare URLs (false positives)
exclude_rule 'MD036'    # allow for standalone bold text (that can look like a header)
exclude_rule 'MD040'    # fenced code-blocks don't need a language specified (macros)
exclude_rule 'MD041'    # allow files that do not start with a header

# Nested lists should be indented with two spaces.
rule 'MD007', :indent => 2

# Ordered lists should increase in numerical order.
rule 'MD029', :style => :ordered
