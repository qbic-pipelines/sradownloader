#!/usr/bin/env python
from __future__ import print_function
from collections import OrderedDict
import re

# TODO nf-core: Add additional regexes for new tools in process get_software_versions
regexes = {
    'steffenlem/sradownloader': ['v_pipeline.txt', r"(\S+)"],
    'Nextflow': ['v_nextflow.txt', r"(\S+)"],
    'prefetch': ['v_prefetch.txt', r"(\d{1,2}\.\d{1,2}\.\d{1,2})"],
    'pigz': ['v_pigz.txt', r"(\d{1,2}\.\d{1,2})"],
    'fasterq-dump': ['v_fasterq-dump.txt', r"(\d{1,2}\.\d{1,2}\.\d{1,2})"],
    'Click': ['v_click.txt', r"(\d{1,2}\.\d{1,2})"]
}
results = OrderedDict()
results['steffenlem/sradownloader'] = '<span style="color:#999999;\">N/A</span>'
results['Nextflow'] = '<span style="color:#999999;\">N/A</span>'


# Search each file using its regex
for k, v in regexes.items():
    try:
        with open(v[0]) as x:
            versions = x.read()
            match = re.search(v[1], versions)
            if match:
                results[k] = "v{}".format(match.group(1))
    except IOError:
        results[k] = False

# Remove software set to false in results
for k in results:
    if not results[k]:
        del(results[k])

# Dump to YAML
print ('''
id: 'software_versions'
section_name: 'steffenlem/sradownloader Software Versions'
section_href: 'https://github.com/steffenlem/sradownloader'
plot_type: 'html'
description: 'are collected at run time from the software output.'
data: |
    <dl class="dl-horizontal">
''')
for k,v in results.items():
    print("        <dt>{}</dt><dd><samp>{}</samp></dd>".format(k,v))
print ("    </dl>")

# Write out regexes as csv file:
with open('software_versions.csv', 'w') as f:
    for k,v in results.items():
        f.write("{}\t{}\n".format(k,v))
