# ArtefactAuthenticationSystematicReview

This repository contains the research data from a Systematic Review conducted into existing techniques for authenticating digital artefacts encountered as part of a digital forensics investigation.

The files contained within are:

1. SCOPUS Export 04Dec2021.rtf -> the results of the original search conducted via SCOPUS
2. Data extraction.xlsx -> the data extracted from the papers selected in the primary dataset upon which the review was based

If accepted for publication, this README will be updtaed with relevant details. Currently, the review paper is in draft so no further information is available at this stage.

NOTE:
During the submission process, some duplicate IDs were discovered to have been assigned to multiple papers. This did not affect the results of the research in any way, but some ID did need to be manually re-assigned. This is now reflected in the SCOPUS Export 04Dec2021.rtf document, however the papers are kept in the original order returned by SCOPUS, therefore some of the IDs appear our of order.

In order to provide further assurance, an analysis.py python script has been provided alongside this. This script checks for the number of IDs expected vs. assigned and ensures that there are no duplicates. In order to prevent accidental modifications to the original SCOPUS export, this script expects an input file named 'input.txt'.
To runt eh script copy it to a local directory along with the SCOPUS export RTF file. Rename the RTF to 'input.txt' and run 'python analysis.py' (using Python 2). The output shows the number of duplicates. Example output is shown below:

$ python analysis.py
Counter final value: 1257
Number of duplicates found: 0
Length of results: 1257
Length of expected ID values NOT used (should be 0): 0

